from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

from ecg_digitizer.config.schema import (
    AppConfig,
    DebugSettings,
    ModelSelectionSettings,
    OutputSettings,
    PathSettings,
    RuntimeSettings,
)


def _resolve_path(value: str | None, *, config_dir: Path, project_root: Path) -> Path | None:
    if value is None:
        return None
    path = Path(value)
    if path.is_absolute():
        return path
    if value.startswith("."):
        return (config_dir / path).resolve()
    return (project_root / path).resolve()


def _infer_project_root(config_path: Path, raw_paths: dict[str, Any]) -> Path:
    explicit = raw_paths.get("project_root")
    if explicit:
        return _resolve_path(str(explicit), config_dir=config_path.parent, project_root=config_path.parent) or config_path.parent
    if config_path.parent.name == "configs":
        return config_path.parent.parent.resolve()
    return config_path.parent.resolve()


def load_config(path: str | os.PathLike[str]) -> AppConfig:
    config_path = Path(path).resolve()
    raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    raw_paths = raw.get("paths", {})
    project_root = _infer_project_root(config_path, raw_paths)
    config_dir = config_path.parent

    data_root_override = os.getenv("ECG_DIGITIZER_DATA_ROOT")
    output_override = os.getenv("ECG_DIGITIZER_OUTPUT")

    data_root = _resolve_path(data_root_override or raw_paths.get("data_root", "data"), config_dir=config_dir, project_root=project_root)
    image_root = _resolve_path(raw_paths.get("image_root", "data/images"), config_dir=config_dir, project_root=project_root)
    test_csv = _resolve_path(raw_paths.get("test_csv"), config_dir=config_dir, project_root=project_root)
    sample_submission = _resolve_path(raw_paths.get("sample_submission", "data/sample_submission.parquet"), config_dir=config_dir, project_root=project_root)
    output_submission = _resolve_path(output_override or raw_paths.get("output_submission", "results/submission.csv"), config_dir=config_dir, project_root=project_root)
    models_registry = _resolve_path(raw_paths.get("models_registry", "configs/models.yaml"), config_dir=config_dir, project_root=project_root)

    path_settings = PathSettings(
        project_root=project_root,
        data_root=data_root or project_root / "data",
        image_root=image_root or project_root / "data" / "images",
        test_csv=test_csv,
        sample_submission=sample_submission or project_root / "data" / "sample_submission.parquet",
        output_submission=output_submission or project_root / "results" / "submission.csv",
        models_registry=models_registry or project_root / "configs" / "models.yaml",
    )

    raw_models = raw.get("models", {})
    model_settings = ModelSelectionSettings(
        detector_id=raw_models.get("detector_id", "yolo_best"),
        primary_segmentation_id=raw_models.get("primary_segmentation_id", "effb3_primary"),
        fallback_segmentation_id=raw_models.get("fallback_segmentation_id", "phase10_fallback"),
        allow_primary_failover=bool(raw_models.get("allow_primary_failover", True)),
        use_fallback_assist=bool(raw_models.get("use_fallback_assist", True)),
    )

    raw_runtime = raw.get("runtime", {})
    runtime_settings = RuntimeSettings(
        device=str(raw_runtime.get("device", "auto")),
        yolo_conf=float(raw_runtime.get("yolo_conf", 0.10)),
        yolo_iou=float(raw_runtime.get("yolo_iou", 0.45)),
        target_height=int(raw_runtime.get("target_height", 384)),
        max_width=int(raw_runtime.get("max_width", 1536)),
        max_cache=int(raw_runtime.get("max_cache", 12)),
        dp_max_width=int(raw_runtime.get("dp_max_width", 1400)),
        dp_smooth=float(raw_runtime.get("dp_smooth", 0.45)),
        tta_scales=tuple(float(v) for v in raw_runtime.get("tta_scales", [0.95, 1.0, 1.15])),
        tta_hflip=bool(raw_runtime.get("tta_hflip", True)),
        primary_threshold=float(raw_runtime.get("primary_threshold", 0.45)),
        fallback_threshold=float(raw_runtime.get("fallback_threshold", 0.50)),
        morph_kernel=int(raw_runtime.get("morph_kernel", 3)),
        min_component_area=int(raw_runtime.get("min_component_area", 120)),
        skeleton_boost=bool(raw_runtime.get("skeleton_boost", True)),
        high_pass_cutoff_hz=float(raw_runtime.get("high_pass_cutoff_hz", 0.5)),
        image_extensions=tuple(str(v) for v in raw_runtime.get("image_extensions", [".png", ".jpg", ".jpeg", ".bmp"])),
    )

    raw_output = raw.get("output", {})
    output_settings = OutputSettings(
        submission_path=output_submission or project_root / "results" / "submission.csv",
        overwrite=bool(raw_output.get("overwrite", True)),
        float_format=str(raw_output.get("float_format", "%.4f")),
    )

    raw_debug = raw.get("debug", {})
    debug_settings = DebugSettings(
        enabled=bool(raw_debug.get("enabled", False)),
        artifacts_dir=_resolve_path(raw_debug.get("artifacts_dir"), config_dir=config_dir, project_root=project_root),
    )

    return AppConfig(
        config_path=config_path,
        paths=path_settings,
        models=model_settings,
        runtime=runtime_settings,
        output=output_settings,
        debug=debug_settings,
        metadata={
            "structural_anchor_version": "57",
            "performance_anchor_version": "50",
            "secondary_performance_reference": "46",
        },
    )
