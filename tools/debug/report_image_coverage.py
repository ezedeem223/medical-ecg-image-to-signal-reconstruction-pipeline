from __future__ import annotations

import argparse

from ecg_digitizer.config import load_config
from ecg_digitizer.io import build_image_index, infer_patient_lengths, load_template_ids


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Report template-to-image coverage for inference inputs.")
    parser.add_argument("--config", default="configs/runtime.default.yaml")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_config(args.config)
    template_ids = load_template_ids(config.paths.sample_submission)
    patient_lengths = infer_patient_lengths(template_ids)
    image_index = build_image_index(config.paths.image_root, config.runtime.image_extensions)

    matched = sum(1 for pid in patient_lengths if pid in image_index or pid.rstrip(".0") in image_index)
    total = len(patient_lengths)
    print(f"patients={total}")
    print(f"images_indexed={len(image_index)}")
    print(f"matched_patients={matched}")
    print(f"unmatched_patients={max(0, total - matched)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
