from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class PathSettings:
    project_root: Path
    data_root: Path
    image_root: Path
    test_csv: Path | None
    sample_submission: Path
    output_submission: Path
    models_registry: Path


@dataclass(frozen=True)
class ModelSelectionSettings:
    detector_id: str
    primary_segmentation_id: str
    fallback_segmentation_id: str
    allow_primary_failover: bool = True
    use_fallback_assist: bool = True


@dataclass(frozen=True)
class RuntimeSettings:
    device: str = "auto"
    yolo_conf: float = 0.10
    yolo_iou: float = 0.45
    target_height: int = 384
    max_width: int = 1536
    max_cache: int = 12
    dp_max_width: int = 1400
    dp_smooth: float = 0.45
    tta_scales: tuple[float, ...] = (0.95, 1.0, 1.15)
    tta_hflip: bool = True
    primary_threshold: float = 0.45
    fallback_threshold: float = 0.50
    morph_kernel: int = 3
    min_component_area: int = 120
    skeleton_boost: bool = True
    high_pass_cutoff_hz: float = 0.5
    image_extensions: tuple[str, ...] = (".png", ".jpg", ".jpeg", ".bmp")


@dataclass(frozen=True)
class OutputSettings:
    submission_path: Path
    overwrite: bool = True
    float_format: str = "%.4f"


@dataclass(frozen=True)
class DebugSettings:
    enabled: bool = False
    artifacts_dir: Path | None = None


@dataclass(frozen=True)
class AppConfig:
    config_path: Path
    paths: PathSettings
    models: ModelSelectionSettings
    runtime: RuntimeSettings
    output: OutputSettings
    debug: DebugSettings
    metadata: dict[str, str] = field(default_factory=dict)
