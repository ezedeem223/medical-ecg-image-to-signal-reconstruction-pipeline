from __future__ import annotations

import numpy as np

from ecg_digitizer.models.interfaces import LeadDetectorProtocol, SegmenterProtocol


class MockDetector:
    def detect_lead_crops(self, image_rgb: np.ndarray) -> dict[int, np.ndarray]:
        return {0: image_rgb}


class MockSegmenter:
    def predict_probmap(
        self,
        crop_rgb: np.ndarray,
        *,
        target_height: int,
        max_width: int,
        hflip: bool = True,
    ) -> tuple[np.ndarray, float]:
        output = np.ones((target_height, min(max_width, crop_rgb.shape[1])), dtype=np.float32)
        return output, 1.0


def test_detector_protocol_contract() -> None:
    assert isinstance(MockDetector(), LeadDetectorProtocol)


def test_segmenter_protocol_contract() -> None:
    assert isinstance(MockSegmenter(), SegmenterProtocol)
