from __future__ import annotations

from dataclasses import dataclass

from ecg_digitizer.config.schema import AppConfig
from ecg_digitizer.models.registry import ModelArtifact, ModelRegistry


@dataclass(frozen=True)
class ModelSelection:
    detector: ModelArtifact
    primary_segmenter: ModelArtifact
    fallback_segmenter: ModelArtifact
    allow_primary_failover: bool
    use_fallback_assist: bool


def build_model_selection(config: AppConfig, registry: ModelRegistry) -> ModelSelection:
    return ModelSelection(
        detector=registry.get(config.models.detector_id),
        primary_segmenter=registry.get(config.models.primary_segmentation_id),
        fallback_segmenter=registry.get(config.models.fallback_segmentation_id),
        allow_primary_failover=config.models.allow_primary_failover,
        use_fallback_assist=config.models.use_fallback_assist,
    )
