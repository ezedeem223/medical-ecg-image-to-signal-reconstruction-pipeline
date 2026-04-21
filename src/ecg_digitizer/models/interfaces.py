from __future__ import annotations

from typing import Protocol, runtime_checkable

import numpy as np


@runtime_checkable
class LeadDetectorProtocol(Protocol):
    def detect_lead_crops(self, image_rgb: np.ndarray) -> dict[int, np.ndarray]:
        ...


@runtime_checkable
class SegmenterProtocol(Protocol):
    def predict_probmap(
        self,
        crop_rgb: np.ndarray,
        *,
        target_height: int,
        max_width: int,
        hflip: bool = True,
    ) -> tuple[np.ndarray, float]:
        ...
