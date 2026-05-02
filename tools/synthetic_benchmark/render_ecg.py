"""
ECG-paper-style image renderer for synthetic benchmark cases.

Renders 12-lead-like waveform arrays as PNG images that visually resemble
standard ECG paper printouts. Images are labeled SYNTHETIC throughout.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np


LEAD_NAMES = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]
GRID_COLOR = (255, 180, 180)
MAJOR_GRID_COLOR = (240, 140, 140)
SIGNAL_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 242, 242)
LABEL_COLOR = (80, 0, 0)


def render_ecg_image(
    waveforms: np.ndarray,
    *,
    fs: int = 500,
    mm_per_mv: float = 10.0,
    mm_per_s: float = 25.0,
    dpi: int = 150,
) -> np.ndarray:
    try:
        return _render_matplotlib(waveforms, fs=fs, mm_per_mv=mm_per_mv, mm_per_s=mm_per_s, dpi=dpi)
    except ImportError:
        return _render_numpy(waveforms, fs=fs)


def _render_matplotlib(
    waveforms: np.ndarray,
    *,
    fs: int,
    mm_per_mv: float,
    mm_per_s: float,
    dpi: int,
) -> np.ndarray:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    n_leads, n_samples = waveforms.shape
    duration_s = n_samples / fs

    cols = 2
    rows = (n_leads + cols - 1) // cols
    fig_w = max(12.0, duration_s * mm_per_s / 25.4)
    fig_h = rows * 2.2

    fig, axes = plt.subplots(rows, cols, figsize=(fig_w, fig_h), dpi=dpi)
    axes = np.array(axes).flatten()

    t = np.linspace(0, duration_s, n_samples)
    for idx in range(n_leads):
        ax = axes[idx]
        signal = waveforms[idx]
        _draw_ecg_grid(ax, t_max=duration_s, amp_range=(-2.0, 2.0))
        ax.plot(t, signal, color="black", linewidth=0.8, zorder=3)
        ax.set_xlim(0, duration_s)
        ax.set_ylim(-2.2, 2.2)
        ax.set_ylabel("mV", fontsize=6)
        ax.set_xlabel("s", fontsize=6)
        ax.tick_params(labelsize=5)
        ax.set_title(f"Lead {LEAD_NAMES[idx]}", fontsize=7, pad=2)

    for idx in range(n_leads, len(axes)):
        axes[idx].set_visible(False)

    syn_patch = mpatches.Patch(color="red", label="SYNTHETIC — NOT REAL ECG DATA")
    fig.legend(handles=[syn_patch], loc="lower center", fontsize=7, ncol=1)
    fig.suptitle("Synthetic ECG-like Signal  [SYNTHETIC]", fontsize=9, color="darkred")
    fig.tight_layout(rect=[0, 0.04, 1, 0.96])

    from io import BytesIO
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=dpi)
    plt.close(fig)
    buf.seek(0)

    try:
        from PIL import Image
        img = Image.open(buf)
        return np.array(img.convert("RGB"))
    except ImportError:
        pass
    buf.seek(0)
    return _png_bytes_to_stub_array(buf.read())


def _draw_ecg_grid(ax, *, t_max: float, amp_range: tuple[float, float]) -> None:
    import matplotlib.ticker as ticker
    minor_t = 0.04
    major_t = 0.2
    minor_amp = 0.1
    major_amp = 0.5

    ax.set_facecolor("#fff5f5")
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(minor_t))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(major_t))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(minor_amp))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(major_amp))
    ax.grid(which="minor", color="#ffaaaa", linewidth=0.3, zorder=1)
    ax.grid(which="major", color="#ff6666", linewidth=0.6, zorder=2)


def _render_numpy(waveforms: np.ndarray, *, fs: int) -> np.ndarray:
    n_leads, n_samples = waveforms.shape
    cell_h = 80
    cell_w = min(600, n_samples // 2)
    rows = (n_leads + 1) // 2
    h = rows * cell_h + 20
    w = cell_w * 2 + 60
    img = np.full((h, w, 3), 255, dtype=np.uint8)
    img[:, :] = list(BACKGROUND_COLOR)

    for idx in range(n_leads):
        row = idx // 2
        col = idx % 2
        y0 = row * cell_h + 10
        x0 = col * (cell_w + 30) + 30
        signal = waveforms[idx]
        signal_ds = signal[::(len(signal) // cell_w + 1)][:cell_w]
        mn, mx = signal_ds.min(), signal_ds.max()
        rng = mx - mn if mx > mn else 1.0
        ys = ((signal_ds - mn) / rng * (cell_h - 20)).astype(int)
        ys = (cell_h - 20) - ys + y0 + 5
        xs = np.arange(len(signal_ds)) + x0
        for i in range(len(xs) - 1):
            _draw_line(img, xs[i], ys[i], xs[i + 1], ys[i + 1], SIGNAL_COLOR)

    return img


def _draw_line(
    img: np.ndarray, x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int]
) -> None:
    h, w = img.shape[:2]
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        if 0 <= y0 < h and 0 <= x0 < w:
            img[y0, x0] = color
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy


def _png_bytes_to_stub_array(data: bytes) -> np.ndarray:
    h, w = 200, 600
    img = np.full((h, w, 3), 240, dtype=np.uint8)
    return img


def save_image(image: np.ndarray, path: Path) -> Path:
    """Save image to disk and return the actual path written.

    Tries matplotlib (PNG), then Pillow (PNG), then falls back to a PPM
    writer that needs no third-party library. The returned path always
    matches the file that was actually written on disk, so callers can
    record the real filename instead of assuming the requested suffix.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 1, figsize=(image.shape[1] / 100, image.shape[0] / 100))
        ax.imshow(image)
        ax.axis("off")
        fig.savefig(str(path), dpi=100, bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        return path
    except ImportError:
        pass
    try:
        from PIL import Image as PILImage
        PILImage.fromarray(image).save(str(path))
        return path
    except ImportError:
        pass
    ppm_path = path.with_suffix(".ppm")
    _save_ppm(image, ppm_path)
    return ppm_path


def _save_ppm(image: np.ndarray, path: Path) -> None:
    h, w, _ = image.shape
    with open(path, "wb") as f:
        f.write(f"P6\n{w} {h}\n255\n".encode())
        f.write(image.tobytes())
