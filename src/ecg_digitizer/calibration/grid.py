from __future__ import annotations

import cv2
import numpy as np
from scipy.signal import find_peaks


def estimate_grid_spacing_px(image_rgb: np.ndarray) -> float | None:
    try:
        gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
        if gray.size == 0 or np.std(gray) < 3:
            return None
        edges_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        edges_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        projection_x = np.sum(np.abs(edges_x), axis=0)
        projection_y = np.sum(np.abs(edges_y), axis=1)
        peaks_x, _ = find_peaks(projection_x, distance=10, prominence=np.percentile(projection_x, 75))
        peaks_y, _ = find_peaks(projection_y, distance=10, prominence=np.percentile(projection_y, 75))

        diffs: list[float] = []
        if len(peaks_x) > 5:
            delta_x = np.diff(peaks_x)
            diffs.extend(delta_x[(delta_x > 8) & (delta_x < 120)])
        if len(peaks_y) > 5:
            delta_y = np.diff(peaks_y)
            diffs.extend(delta_y[(delta_y > 8) & (delta_y < 120)])
        if len(diffs) < 6:
            return None
        return float(np.median(np.array(diffs)))
    except Exception:
        return None


def choose_ppmv(local_grid_px: float | None, resize_scale: float, raw_trace_px: np.ndarray) -> float:
    if local_grid_px is None or not np.isfinite(local_grid_px) or local_grid_px < 5:
        return 250.0

    ppmv_small_box = local_grid_px * 10.0 * resize_scale
    ppmv_big_box = local_grid_px * 2.0 * resize_scale

    def score_candidate(ppmv: float) -> float:
        if ppmv <= 0:
            return 1e9
        signal = (raw_trace_px - np.median(raw_trace_px)) / ppmv
        signal = np.nan_to_num(signal)
        peak_to_peak = float(np.percentile(signal, 99) - np.percentile(signal, 1))
        if peak_to_peak <= 0:
            return 1e9
        if peak_to_peak < 0.2:
            return 1000.0 + (0.2 - peak_to_peak) * 1000.0
        if peak_to_peak > 8.0:
            return 1000.0 + (peak_to_peak - 8.0) * 300.0
        return abs(peak_to_peak - 2.5)

    score_small = score_candidate(ppmv_small_box)
    score_big = score_candidate(ppmv_big_box)
    candidate = ppmv_small_box if score_small <= score_big else ppmv_big_box
    if not np.isfinite(candidate) or candidate < 10:
        return 250.0
    return float(candidate)
