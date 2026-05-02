"""
Controlled image distortions for synthetic ECG benchmark cases.

Each function takes a uint8 numpy array (H x W x 3) and returns a distorted
copy. All functions are deterministic given an integer seed.
"""
from __future__ import annotations

import math

import numpy as np


def apply_clean(image: np.ndarray) -> np.ndarray:
    return image.copy()


def apply_blur(image: np.ndarray, *, sigma: float = 2.0) -> np.ndarray:
    try:
        from scipy.ndimage import gaussian_filter
        blurred = gaussian_filter(image.astype(np.float32), sigma=[sigma, sigma, 0])
        return np.clip(blurred, 0, 255).astype(np.uint8)
    except ImportError:
        pass
    radius = max(1, int(math.ceil(sigma * 3)) | 1)
    kernel = _gaussian_kernel_1d(radius, sigma)
    out = image.astype(np.float32)
    for c in range(out.shape[2]):
        for ax in (0, 1):
            out[:, :, c] = np.apply_along_axis(
                lambda row: np.convolve(row, kernel, mode="same"), ax, out[:, :, c]
            )
    return np.clip(out, 0, 255).astype(np.uint8)


def apply_noise(image: np.ndarray, *, std: float = 20.0, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, std, size=image.shape).astype(np.float32)
    return np.clip(image.astype(np.float32) + noise, 0, 255).astype(np.uint8)


def apply_low_contrast(
    image: np.ndarray, *, alpha: float = 0.5, beta: float = 40.0
) -> np.ndarray:
    out = image.astype(np.float32) * alpha + beta
    return np.clip(out, 0, 255).astype(np.uint8)


def apply_rotation(image: np.ndarray, *, angle_deg: float = 5.0) -> np.ndarray:
    try:
        from scipy.ndimage import rotate as nd_rotate
        rotated = nd_rotate(image, angle_deg, axes=(0, 1), reshape=False, cval=255)
        return np.clip(rotated, 0, 255).astype(np.uint8)
    except ImportError:
        pass
    angle_rad = math.radians(angle_deg)
    h, w = image.shape[:2]
    cy, cx = h / 2.0, w / 2.0
    cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
    out = np.full_like(image, 255)
    ys, xs = np.mgrid[0:h, 0:w]
    ys_c = ys - cy
    xs_c = xs - cx
    src_y = (cos_a * ys_c - sin_a * xs_c + cy).astype(int)
    src_x = (sin_a * ys_c + cos_a * xs_c + cx).astype(int)
    valid = (src_y >= 0) & (src_y < h) & (src_x >= 0) & (src_x < w)
    out[valid] = image[src_y[valid], src_x[valid]]
    return out


def apply_cropped(
    image: np.ndarray, *, margin_frac: float = 0.08, seed: int = 0
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    h, w = image.shape[:2]
    top = int(rng.integers(0, max(1, int(h * margin_frac))))
    bottom = h - int(rng.integers(0, max(1, int(h * margin_frac))))
    left = int(rng.integers(0, max(1, int(w * margin_frac))))
    right = w - int(rng.integers(0, max(1, int(w * margin_frac))))
    top = max(0, top)
    bottom = min(h, max(top + 1, bottom))
    left = max(0, left)
    right = min(w, max(left + 1, right))
    return image[top:bottom, left:right].copy()


DISTORTION_REGISTRY: dict[str, object] = {
    "clean": apply_clean,
    "blur": apply_blur,
    "noise": apply_noise,
    "low_contrast": apply_low_contrast,
    "rotation": apply_rotation,
    "cropped": apply_cropped,
}


def apply_distortion(name: str, image: np.ndarray, *, seed: int = 0) -> np.ndarray:
    fn = DISTORTION_REGISTRY.get(name)
    if fn is None:
        raise ValueError(f"Unknown distortion: {name!r}. Valid: {sorted(DISTORTION_REGISTRY)}")
    if name in ("noise", "cropped"):
        return fn(image, seed=seed)  # type: ignore[call-arg]
    return fn(image)  # type: ignore[call-arg]


def _gaussian_kernel_1d(radius: int, sigma: float) -> np.ndarray:
    xs = np.arange(-radius, radius + 1, dtype=np.float64)
    kernel = np.exp(-(xs ** 2) / (2.0 * sigma ** 2))
    return (kernel / kernel.sum()).astype(np.float32)
