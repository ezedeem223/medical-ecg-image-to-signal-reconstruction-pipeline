from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from ecg_digitizer.config import load_config
from ecg_digitizer.io import infer_patient_lengths, load_template_ids, parse_template_id


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plot digitized waveforms for one patient from a submission file.")
    parser.add_argument("--config", default="configs/runtime.default.yaml")
    parser.add_argument("--submission", default="results/submission.csv")
    parser.add_argument("--patient-id", required=True)
    parser.add_argument("--output", default="")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_config(args.config)
    submission = pd.read_csv(Path(args.submission))
    template_ids = load_template_ids(config.paths.sample_submission)
    patient_lengths = infer_patient_lengths(template_ids)

    length = patient_lengths.get(args.patient_id)
    if not length:
        raise KeyError(f"Unknown patient id in template: {args.patient_id}")

    grouped: dict[str, list[float]] = {}
    for record_id, value in zip(submission["id"].astype(str), submission["value"].astype(float)):
        pid, _point_index, lead = parse_template_id(record_id)
        if pid == args.patient_id and lead is not None:
            grouped.setdefault(lead, []).append(value)

    figure, axes = plt.subplots(len(grouped), 1, figsize=(12, max(4, len(grouped) * 2)), sharex=True)
    if len(grouped) == 1:
        axes = [axes]
    for axis, (lead, values) in zip(axes, grouped.items()):
        axis.plot(values, linewidth=1.0)
        axis.set_title(lead)
        axis.grid(True, alpha=0.3)
    figure.suptitle(f"Digitized waveforms for {args.patient_id}")
    figure.tight_layout()

    if args.output:
        destination = Path(args.output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(destination, dpi=150)
        print(f"saved={destination}")
    else:
        plt.show()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
