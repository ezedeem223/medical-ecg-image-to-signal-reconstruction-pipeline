from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np


def read_image_rgb(path: Path) -> np.ndarray | None:
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        return None
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def preprocess_remove_grid_rgb(image_rgb: np.ndarray) -> np.ndarray:
    try:
        hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
        mask = (
            cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
            | cv2.inRange(hsv, (170, 50, 50), (180, 255, 255))
        )
        output = image_rgb.copy()
        output[mask > 0] = (255, 255, 255)
        return output
    except Exception:
        return image_rgb
