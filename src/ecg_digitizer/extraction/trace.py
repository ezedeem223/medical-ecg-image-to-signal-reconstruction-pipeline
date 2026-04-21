from __future__ import annotations

import cv2
import numpy as np
from scipy.signal import savgol_filter


def build_probmap_mask(probmap: np.ndarray, *, threshold: float, morph_kernel: int, min_component_area: int) -> np.ndarray:
    mask = (probmap >= threshold).astype(np.uint8) * 255
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (morph_kernel, morph_kernel))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    num_labels, labels, stats, _centroids = cv2.connectedComponentsWithStats((mask > 0).astype(np.uint8), connectivity=8)
    filtered = np.zeros_like(mask)
    for label in range(1, num_labels):
        if stats[label, cv2.CC_STAT_AREA] >= min_component_area:
            filtered[labels == label] = 255
    return filtered


def _skeletonize_mask(mask: np.ndarray) -> np.ndarray | None:
    try:
        from skimage.morphology import skeletonize
    except Exception:
        return None
    return skeletonize((mask > 0).astype(np.uint8)).astype(np.uint8) * 255


def boost_probmap_with_skeleton(probmap: np.ndarray, mask: np.ndarray, *, enabled: bool) -> np.ndarray:
    if not enabled:
        return probmap
    skeleton = _skeletonize_mask(mask)
    if skeleton is None:
        return probmap
    boosted = probmap.copy()
    boosted[skeleton > 0] = np.maximum(boosted[skeleton > 0], 0.85)
    return boosted


def _viterbi_dp(probmap: np.ndarray, *, smooth: float) -> np.ndarray:
    height, width = probmap.shape
    cost = -np.log(probmap + 1e-6).astype(np.float32)
    dp = np.zeros_like(cost, dtype=np.float32)
    parent = np.zeros((height, width), dtype=np.int16)

    dp[:, 0] = cost[:, 0]
    parent[:, 0] = np.arange(height, dtype=np.int16)

    for column in range(1, width):
        previous = dp[:, column - 1]
        minus = np.roll(previous, 1)
        minus[0] = 1e9
        zero = previous
        plus = np.roll(previous, -1)
        plus[-1] = 1e9
        stacked = np.stack([minus + smooth, zero, plus + smooth], axis=0)
        which = np.argmin(stacked, axis=0).astype(np.int16)
        best_previous = stacked[which, np.arange(height)]
        dp[:, column] = cost[:, column] + best_previous
        parent[:, column] = np.clip(np.arange(height, dtype=np.int16) + (which - 1), 0, height - 1)

    path = np.zeros(width, dtype=np.int32)
    path[-1] = int(np.argmin(dp[:, -1]))
    for column in range(width - 2, -1, -1):
        path[column] = int(parent[path[column + 1], column + 1])
    return (height - path).astype(np.float32)


def viterbi_adaptive(probmap: np.ndarray, *, dp_max_width: int, dp_smooth: float) -> np.ndarray:
    height, width = probmap.shape
    if width <= 20 or height <= 5:
        path = np.argmax(probmap, axis=0)
        return (height - path).astype(np.float32)
    if width <= dp_max_width:
        return _viterbi_dp(probmap, smooth=dp_smooth)
    path = np.argmax(probmap, axis=0).astype(np.float32)
    window = 21 if width >= 21 else (width if width % 2 == 1 else width - 1)
    if window >= 5:
        path = savgol_filter(path, window, 2)
    return (height - path).astype(np.float32)


def build_trace_signal(probmap: np.ndarray, *, threshold: float, morph_kernel: int, min_component_area: int, dp_max_width: int, dp_smooth: float, skeleton_boost: bool) -> np.ndarray:
    mask = build_probmap_mask(probmap, threshold=threshold, morph_kernel=morph_kernel, min_component_area=min_component_area)
    boosted = boost_probmap_with_skeleton(probmap, mask, enabled=skeleton_boost)
    return viterbi_adaptive(boosted, dp_max_width=dp_max_width, dp_smooth=dp_smooth)
