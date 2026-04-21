from __future__ import annotations

import argparse
import os
from pathlib import Path

from ecg_digitizer import load_config, run_inference
from ecg_digitizer.validation import validate_submission


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Medical ECG image digitization runtime.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run ECG digitization inference.")
    run_parser.add_argument(
        "--config",
        default=os.getenv("ECG_DIGITIZER_CONFIG", "configs/runtime.default.yaml"),
        help="Path to the runtime config.",
    )

    validate_parser = subparsers.add_parser("validate", help="Validate a generated submission.")
    validate_parser.add_argument(
        "--config",
        default=os.getenv("ECG_DIGITIZER_CONFIG", "configs/runtime.default.yaml"),
        help="Path to the runtime config.",
    )
    validate_parser.add_argument(
        "--submission",
        default=os.getenv("ECG_DIGITIZER_OUTPUT", "results/submission.csv"),
        help="Submission CSV to validate.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        config = load_config(args.config)
        output_path = run_inference(config)
        print(f"submission_path={output_path}")
        return 0

    if args.command == "validate":
        config = load_config(args.config)
        result = validate_submission(config, Path(args.submission))
        print(f"validated={result.valid} rows={result.row_count}")
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
