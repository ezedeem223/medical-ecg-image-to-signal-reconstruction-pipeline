from __future__ import annotations

from dataclasses import dataclass

import cv2
import numpy as np

from ecg_digitizer.io.indexing import LEAD_TO_IDX, normalize_lead_name
from ecg_digitizer.models.registry import ModelArtifact


@dataclass
class YOLOLeadDetector:
    artifact: ModelArtifact
    device: str
    conf: float
    iou: float
    max_side: int = 1280

    def __post_init__(self) -> None:
        from ultralytics import YOLO

        self._model = YOLO(str(self.artifact.path))
        self._class_to_lead = self._build_class_mapping()

    def _build_class_mapping(self) -> dict[int, int]:
        names = getattr(self._model, "names", None)
        items: list[tuple[int, str]]
        if isinstance(names, dict):
            items = [(int(key), str(value)) for key, value in names.items()]
        elif isinstance(names, list):
            items = list(enumerate(str(item) for item in names))
        else:
            items = []

        mapping: dict[int, int] = {}
        for class_id, class_name in items:
            lead_name = normalize_lead_name(class_name)
            if lead_name in LEAD_TO_IDX:
                mapping[class_id] = LEAD_TO_IDX[lead_name]
        if len(mapping) < 8:
            for index in range(12):
                mapping.setdefault(index, index)
        return mapping

    def detect_lead_crops(self, image_rgb: np.ndarray) -> dict[int, np.ndarray]:
        height, width = image_rgb.shape[:2]
        if height < 20 or width < 20:
            return {}

        scale = self.max_side / float(max(height, width))
        if scale < 1.0:
            resized = cv2.resize(image_rgb, (max(32, int(width * scale)), max(32, int(height * scale))))
        else:
            resized = image_rgb
            scale = 1.0

        best: dict[int, tuple[float, tuple[int, int, int, int]]] = {}
        results = self._model.predict(resized, conf=self.conf, iou=self.iou, verbose=False, device=self.device)
        if not results or results[0].boxes is None:
            return {}

        boxes = results[0].boxes.data.detach().cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2, confidence, class_id = box[:6]
            mapped = self._class_to_lead.get(int(class_id), int(class_id))
            if not 0 <= mapped < 12:
                continue
            x1o, y1o, x2o, y2o = x1 / scale, y1 / scale, x2 / scale, y2 / scale
            x1i, y1i = max(0, int(x1o)), max(0, int(y1o))
            x2i, y2i = min(width, int(x2o)), min(height, int(y2o))
            if x2i <= x1i + 10 or y2i <= y1i + 10:
                continue
            previous = best.get(mapped)
            if previous is None or float(confidence) > previous[0]:
                best[mapped] = (float(confidence), (x1i, y1i, x2i, y2i))

        crops: dict[int, np.ndarray] = {}
        for lead_index, (_confidence, (x1, y1, x2, y2)) in best.items():
            crops[lead_index] = image_rgb[y1:y2, x1:x2].copy()
        return crops
