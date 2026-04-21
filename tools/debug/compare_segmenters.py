from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from ecg_digitizer.config import load_config
from ecg_digitizer.models.registry import load_model_registry
from ecg_digitizer.models.segmentation import SMPUnetBinarySegmenter
from ecg_digitizer.models.selector import build_model_selection
from ecg_digitizer.preprocessing import preprocess_remove_grid_rgb, read_image_rgb


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare primary and fallback segmenters on one crop or page.")
    parser.add_argument("--config", default="configs/runtime.default.yaml")
    parser.add_argument("--image", required=True, help="Input image or crop.")
    parser.add_argument("--device", default="cpu")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_config(args.config)
    registry = load_model_registry(config.paths.models_registry, project_root=config.paths.project_root)
    selection = build_model_selection(config, registry)

    image_path = Path(args.image).resolve()
    image_rgb = read_image_rgb(image_path)
    if image_rgb is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    crop_rgb = preprocess_remove_grid_rgb(image_rgb)
    primary = SMPUnetBinarySegmenter(selection.primary_segmenter, device=args.device)
    fallback = SMPUnetBinarySegmenter(selection.fallback_segmenter, device=args.device)

    primary_prob, _ = primary.predict_probmap(
        crop_rgb,
        target_height=config.runtime.target_height,
        max_width=config.runtime.max_width,
        hflip=config.runtime.tta_hflip,
    )
    fallback_prob, _ = fallback.predict_probmap(
        crop_rgb,
        target_height=config.runtime.target_height,
        max_width=config.runtime.max_width,
        hflip=config.runtime.tta_hflip,
    )

    diff = np.abs(primary_prob - fallback_prob)
    print(f"image={image_path}")
    print(f"primary_mean={float(primary_prob.mean()):.6f}")
    print(f"fallback_mean={float(fallback_prob.mean()):.6f}")
    print(f"mean_abs_diff={float(diff.mean()):.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
