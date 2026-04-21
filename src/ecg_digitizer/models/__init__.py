from __future__ import annotations

from typing import Any

__all__ = [
    "LeadDetectorProtocol",
    "ModelArtifact",
    "ModelRegistry",
    "ModelSelection",
    "SMPUnetBinarySegmenter",
    "SegmenterProtocol",
    "YOLOLeadDetector",
    "build_model_selection",
    "load_model_registry",
]


def __getattr__(name: str) -> Any:
    if name in {"LeadDetectorProtocol", "SegmenterProtocol"}:
        from ecg_digitizer.models.interfaces import LeadDetectorProtocol, SegmenterProtocol

        return {"LeadDetectorProtocol": LeadDetectorProtocol, "SegmenterProtocol": SegmenterProtocol}[name]
    if name in {"ModelArtifact", "ModelRegistry", "load_model_registry"}:
        from ecg_digitizer.models.registry import ModelArtifact, ModelRegistry, load_model_registry

        return {
            "ModelArtifact": ModelArtifact,
            "ModelRegistry": ModelRegistry,
            "load_model_registry": load_model_registry,
        }[name]
    if name in {"ModelSelection", "build_model_selection"}:
        from ecg_digitizer.models.selector import ModelSelection, build_model_selection

        return {"ModelSelection": ModelSelection, "build_model_selection": build_model_selection}[name]
    if name == "YOLOLeadDetector":
        from ecg_digitizer.models.detector import YOLOLeadDetector

        return YOLOLeadDetector
    if name == "SMPUnetBinarySegmenter":
        from ecg_digitizer.models.segmentation import SMPUnetBinarySegmenter

        return SMPUnetBinarySegmenter
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
