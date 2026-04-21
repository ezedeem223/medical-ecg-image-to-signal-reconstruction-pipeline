from __future__ import annotations

import argparse
from pathlib import Path

from ecg_digitizer.config import load_config
from ecg_digitizer.models.detector import YOLOLeadDetector
from ecg_digitizer.models.registry import load_model_registry
from ecg_digitizer.models.selector import build_model_selection
from ecg_digitizer.preprocessing import read_image_rgb


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect detector crops for a single ECG page.")
    parser.add_argument("--config", default="configs/runtime.default.yaml")
    parser.add_argument("--image", required=True, help="Image path to inspect.")
    parser.add_argument("--device", default="cpu")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_config(args.config)
    registry = load_model_registry(config.paths.models_registry, project_root=config.paths.project_root)
    selection = build_model_selection(config, registry)
    detector = YOLOLeadDetector(
        artifact=selection.detector,
        device=args.device,
        conf=config.runtime.yolo_conf,
        iou=config.runtime.yolo_iou,
    )

    image_path = Path(args.image).resolve()
    image_rgb = read_image_rgb(image_path)
    if image_rgb is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    crops = detector.detect_lead_crops(image_rgb)
    print(f"image={image_path}")
    print(f"detected_leads={len(crops)}")
    for lead_idx, crop in sorted(crops.items()):
        print(f"lead_index={lead_idx} crop_shape={crop.shape}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
