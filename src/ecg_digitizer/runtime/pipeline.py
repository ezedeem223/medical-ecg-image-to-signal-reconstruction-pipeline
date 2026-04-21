from __future__ import annotations

from collections import OrderedDict
import logging
from pathlib import Path

import numpy as np

from ecg_digitizer.calibration import choose_ppmv, estimate_grid_spacing_px
from ecg_digitizer.config import AppConfig, load_config
from ecg_digitizer.extraction import build_probmap_mask, build_trace_signal
from ecg_digitizer.io import (
    LEAD_NAMES,
    LEAD_TO_IDX,
    build_image_index,
    clean_pid,
    infer_patient_lengths,
    load_fs_map,
    load_template_ids,
    parse_template_id,
    resolve_image_path,
)
from ecg_digitizer.models import (
    LeadDetectorProtocol,
    SMPUnetBinarySegmenter,
    SegmenterProtocol,
    YOLOLeadDetector,
    build_model_selection,
    load_model_registry,
)
from ecg_digitizer.postprocessing import normalize_signal, resample_signal, smart_einthoven_fix
from ecg_digitizer.preprocessing import preprocess_remove_grid_rgb, read_image_rgb
from ecg_digitizer.runtime.bootstrap import validate_environment
from ecg_digitizer.submission_export import write_submission_rows

LOGGER = logging.getLogger(__name__)


def _resolve_device(requested: str) -> str:
    if requested != "auto":
        return requested
    try:
        import torch
    except Exception:
        return "cpu"
    return "cuda" if torch.cuda.is_available() else "cpu"


def _ensure_config(config: AppConfig | str | Path) -> AppConfig:
    if isinstance(config, AppConfig):
        return config
    return load_config(config)


def _build_segmenter(
    segmenter: SegmenterProtocol | None,
    artifact,
    *,
    device: str,
) -> SegmenterProtocol:
    return segmenter or SMPUnetBinarySegmenter(artifact=artifact, device=device)


def _aggregate_probmap(
    segmenter: SegmenterProtocol,
    crop_rgb: np.ndarray,
    *,
    target_height: int,
    max_width: int,
    scales: tuple[float, ...],
    hflip: bool,
) -> tuple[np.ndarray, float]:
    accumulated: list[np.ndarray] = []
    resize_scales: list[float] = []
    for scale in scales:
        scaled_height = int(round(target_height * scale))
        scaled_height = int(np.ceil(scaled_height / 32.0) * 32)
        probmap, resize_scale = segmenter.predict_probmap(
            crop_rgb,
            target_height=scaled_height,
            max_width=max_width,
            hflip=hflip,
        )
        if probmap.shape[0] != target_height:
            import cv2

            probmap = cv2.resize(probmap, (probmap.shape[1], target_height), interpolation=cv2.INTER_LINEAR)
        accumulated.append(probmap)
        resize_scales.append(resize_scale)
    return np.mean(np.stack(accumulated, axis=0), axis=0).astype(np.float32), float(np.mean(resize_scales))


def _compute_patient_matrix(
    pid: str,
    target_len: int,
    *,
    image_index: dict[str, Path],
    detector: LeadDetectorProtocol,
    primary_segmenter: SegmenterProtocol,
    fallback_segmenter: SegmenterProtocol | None,
    config: AppConfig,
    fs_map: dict[str, float],
) -> np.ndarray:
    output = np.zeros((12, target_len), dtype=np.float32)
    image_path = resolve_image_path(pid, image_index)
    if image_path is None:
        return output

    image_rgb = read_image_rgb(image_path)
    if image_rgb is None:
        return output

    fs = float(fs_map.get(clean_pid(pid), 500.0))
    crops = detector.detect_lead_crops(image_rgb)
    detected = [(lead_idx, crop) for lead_idx, crop in sorted(crops.items()) if crop is not None and crop.size > 200]
    if not detected:
        return output

    global_grid = estimate_grid_spacing_px(image_rgb)
    leads: dict[str, np.ndarray] = {}

    for lead_idx, crop in detected:
        prepared_crop = preprocess_remove_grid_rgb(crop)
        primary_probmap, resize_scale = _aggregate_probmap(
            primary_segmenter,
            prepared_crop,
            target_height=config.runtime.target_height,
            max_width=config.runtime.max_width,
            scales=config.runtime.tta_scales,
            hflip=config.runtime.tta_hflip,
        )

        fallback_probmap = None
        if fallback_segmenter is not None and config.models.use_fallback_assist:
            fallback_probmap, _ = _aggregate_probmap(
                fallback_segmenter,
                prepared_crop,
                target_height=config.runtime.target_height,
                max_width=config.runtime.max_width,
                scales=config.runtime.tta_scales,
                hflip=config.runtime.tta_hflip,
            )

        primary_mask = build_probmap_mask(
            primary_probmap,
            threshold=config.runtime.primary_threshold,
            morph_kernel=config.runtime.morph_kernel,
            min_component_area=config.runtime.min_component_area,
        )

        probmap_for_trace = primary_probmap
        mask_for_trace = primary_mask
        if fallback_probmap is not None:
            fallback_mask = build_probmap_mask(
                fallback_probmap,
                threshold=config.runtime.fallback_threshold,
                morph_kernel=config.runtime.morph_kernel,
                min_component_area=config.runtime.min_component_area,
            )
            weak = (primary_probmap > 0.25) & (primary_probmap < config.runtime.primary_threshold)
            mask_for_trace = primary_mask.copy()
            mask_for_trace[weak & (fallback_mask > 0)] = 255
            probmap_for_trace = (0.75 * primary_probmap + 0.25 * fallback_probmap).astype(np.float32)

        raw_trace = build_trace_signal(
            probmap_for_trace,
            threshold=config.runtime.primary_threshold,
            morph_kernel=config.runtime.morph_kernel,
            min_component_area=config.runtime.min_component_area,
            dp_max_width=config.runtime.dp_max_width,
            dp_smooth=config.runtime.dp_smooth,
            skeleton_boost=config.runtime.skeleton_boost,
        )

        local_grid = estimate_grid_spacing_px(crop) or global_grid
        pixels_per_mv = choose_ppmv(local_grid, resize_scale, raw_trace)
        signal = normalize_signal(
            raw_trace,
            pixels_per_mv=pixels_per_mv,
            fs=fs,
            high_pass_cutoff_hz=config.runtime.high_pass_cutoff_hz,
        )
        leads[LEAD_NAMES[lead_idx]] = resample_signal(signal, target_len=target_len)

    leads = smart_einthoven_fix(leads)
    for idx, lead_name in enumerate(LEAD_NAMES):
        if lead_name in leads:
            output[idx] = np.nan_to_num(leads[lead_name], nan=0.0)
    return output


def run_inference(
    config: AppConfig | str | Path,
    *,
    detector: LeadDetectorProtocol | None = None,
    primary_segmenter: SegmenterProtocol | None = None,
    fallback_segmenter: SegmenterProtocol | None = None,
) -> Path:
    app_config = _ensure_config(config)
    registry = load_model_registry(app_config.paths.models_registry, project_root=app_config.paths.project_root)
    selection = build_model_selection(app_config, registry)
    validate_environment(app_config, selection)

    device = _resolve_device(app_config.runtime.device)
    detector_impl = detector or YOLOLeadDetector(
        artifact=selection.detector,
        device=device,
        conf=app_config.runtime.yolo_conf,
        iou=app_config.runtime.yolo_iou,
    )

    primary_artifact = selection.primary_segmenter
    primary_injected = primary_segmenter
    using_fallback_as_primary = False
    if not selection.primary_segmenter.path.exists():
        primary_artifact = selection.fallback_segmenter
        if primary_injected is None:
            primary_injected = fallback_segmenter
        using_fallback_as_primary = True
        LOGGER.warning(
            "Primary segmentation checkpoint missing; switching to explicit fallback: %s",
            primary_artifact.path,
        )

    primary_impl = _build_segmenter(primary_injected, primary_artifact, device=device)
    fallback_impl = None
    if selection.allow_primary_failover and not using_fallback_as_primary:
        fallback_impl = _build_segmenter(fallback_segmenter, selection.fallback_segmenter, device=device)

    template_ids = load_template_ids(app_config.paths.sample_submission)
    patient_lengths = infer_patient_lengths(template_ids)
    fs_map = load_fs_map(app_config.paths.test_csv)
    image_index = build_image_index(app_config.paths.image_root, app_config.runtime.image_extensions)

    cache: OrderedDict[str, np.ndarray] = OrderedDict()
    rows: list[tuple[str, str]] = []

    for record_id in template_ids:
        pid, point_index, lead_name = parse_template_id(record_id)
        if pid is None or point_index is None or lead_name is None:
            rows.append((record_id, app_config.output.float_format % 0.0))
            continue

        target_len = patient_lengths.get(pid, 5000)
        if target_len <= 0 or target_len > 10000:
            target_len = 5000

        if pid in cache:
            matrix = cache[pid]
            cache.move_to_end(pid)
        else:
            matrix = _compute_patient_matrix(
                pid,
                target_len,
                image_index=image_index,
                detector=detector_impl,
                primary_segmenter=primary_impl,
                fallback_segmenter=(
                    fallback_impl if (fallback_impl is not None and app_config.models.use_fallback_assist) else None
                ),
                config=app_config,
                fs_map=fs_map,
            )
            cache[pid] = matrix
            if len(cache) > app_config.runtime.max_cache:
                cache.popitem(last=False)

        lead_idx = LEAD_TO_IDX.get(lead_name, 0)
        value = 0.0
        if 0 <= point_index < matrix.shape[1]:
            candidate = float(matrix[lead_idx][point_index])
            if np.isfinite(candidate):
                value = candidate
        rows.append((record_id, app_config.output.float_format % value))

    return write_submission_rows(rows, app_config.output.submission_path, overwrite=app_config.output.overwrite)
