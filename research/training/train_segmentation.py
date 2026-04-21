from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Optional research-only segmentation training scaffold.")
    parser.add_argument(
        "--config",
        default="research/training/configs/segmentation.reference.yaml",
        help="Research training config path.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate the configuration and print the resolved plan without starting a training loop.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config_path = Path(args.config).resolve()
    raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}

    experiment = raw.get("experiment", {})
    model = raw.get("model", {})
    data = raw.get("data", {})

    print(f"config={config_path}")
    print(f"experiment_name={experiment.get('name', 'unnamed')}")
    print(f"encoder={model.get('encoder_name', 'resnet50')}")
    print(f"checkpoint_init={model.get('init_checkpoint', '')}")
    print(f"train_images={data.get('train_images', '')}")
    print(f"train_masks={data.get('train_masks', '')}")
    print("scope=research-only")

    if args.dry_run:
        print("mode=dry-run")
        return 0

    raise NotImplementedError(
        "Phase 4 preserves training as optional research scaffolding only. "
        "Use this entrypoint for future extraction, not as part of the maintained runtime."
    )


if __name__ == "__main__":
    raise SystemExit(main())
