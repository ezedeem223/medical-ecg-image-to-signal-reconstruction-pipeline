from __future__ import annotations

from ecg_digitizer.config.schema import AppConfig
from ecg_digitizer.models.selector import ModelSelection


def validate_environment(config: AppConfig, selection: ModelSelection) -> None:
    if not config.paths.sample_submission.exists():
        raise FileNotFoundError(f"Template file not found: {config.paths.sample_submission}")
    if not config.paths.image_root.exists():
        raise FileNotFoundError(f"Image root not found: {config.paths.image_root}")
    if not selection.detector.path.exists():
        raise FileNotFoundError(f"Detector checkpoint not found: {selection.detector.path}")

    primary_exists = selection.primary_segmenter.path.exists()
    fallback_exists = selection.fallback_segmenter.path.exists()

    if primary_exists and fallback_exists:
        return

    if primary_exists and not fallback_exists:
        raise FileNotFoundError(
            f"Fallback segmentation checkpoint not found: {selection.fallback_segmenter.path}"
        )

    if not primary_exists and selection.allow_primary_failover and fallback_exists:
        return

    if not primary_exists:
        raise FileNotFoundError(
            f"Primary segmentation checkpoint not found: {selection.primary_segmenter.path}"
        )

    raise FileNotFoundError(
        f"Fallback segmentation checkpoint not found: {selection.fallback_segmenter.path}"
    )
