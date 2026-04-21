from __future__ import annotations

import numpy as np
from scipy.signal import butter, filtfilt, resample, savgol_filter


def apply_high_pass(signal: np.ndarray, *, cutoff: float, fs: float, order: int = 3) -> np.ndarray:
    try:
        if len(signal) < order * 3:
            return signal
        nyquist = 0.5 * fs
        if nyquist <= 0:
            return signal
        normalized = cutoff / nyquist
        if not (0 < normalized < 1):
            return signal
        b, a = butter(order, normalized, btype="high")
        return filtfilt(b, a, signal)
    except Exception:
        return signal


def normalize_signal(raw_trace_px: np.ndarray, *, pixels_per_mv: float, fs: float, high_pass_cutoff_hz: float) -> np.ndarray:
    signal_mv = (raw_trace_px - np.median(raw_trace_px)) / pixels_per_mv
    signal_mv = np.nan_to_num(signal_mv, nan=0.0, posinf=0.0, neginf=0.0)
    if len(signal_mv) >= 11:
        signal_mv = savgol_filter(signal_mv, 11, 3)
    if len(signal_mv) >= 30:
        signal_mv = apply_high_pass(signal_mv, cutoff=high_pass_cutoff_hz, fs=fs, order=3)
    return np.clip(signal_mv, -7.0, 7.0)


def resample_signal(signal: np.ndarray, *, target_len: int) -> np.ndarray:
    if len(signal) == 0:
        return np.zeros(target_len, dtype=np.float32)
    return resample(signal, target_len).astype(np.float32)


def smart_einthoven_fix(leads: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    try:
        if "I" in leads and "II" in leads and "III" in leads:
            length = min(len(leads["I"]), len(leads["II"]), len(leads["III"]))
            lead_i = leads["I"][:length]
            lead_ii = leads["II"][:length]
            lead_iii = leads["III"][:length]
            residual = (lead_i + lead_iii) - lead_ii
            leads["II"][:length] += residual / 3.0
            leads["I"][:length] -= residual / 3.0
            leads["III"][:length] -= residual / 3.0
    except Exception:
        return leads
    return leads
