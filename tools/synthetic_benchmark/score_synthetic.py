"""
Synthetic-only waveform fidelity scoring utility.

Computes MAE, RMSE, and an SNR-proxy score between ground-truth and prediction
CSV files. This utility is strictly for synthetic benchmark evaluation.

IMPORTANT LIMITATIONS:
  - Scores are computed on parametrically generated synthetic waveforms only.
  - These scores do NOT constitute clinical accuracy measurements.
  - Do NOT compare these scores to published ECG reconstruction benchmarks.
  - Do NOT use these scores to support diagnostic claims.

Expected CSV format (ground-truth and prediction):
  Row 0: header  ->  lead_name, 0, 1, 2, ..., N-1
  Rows 1-12:          I, <float>, <float>, ...

Usage:
    python tools/synthetic_benchmark/score_synthetic.py \\
        --ground-truth benchmark_cases/seed/waveforms/case_000.csv \\
        --prediction path/to/prediction.csv \\
        --output reports/synthetic_score.json
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np

SYNTHETIC_DISCLAIMER = (
    "SYNTHETIC BENCHMARK ONLY. Scores measure fidelity on parametrically generated "
    "waveforms. These results do not represent clinical accuracy and must not be used "
    "for diagnostic or regulatory purposes."
)
LEAD_NAMES = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]


def load_waveform_csv(path: Path) -> dict[str, np.ndarray]:
    leads: dict[str, np.ndarray] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            raise ValueError(f"Empty CSV: {path}")
        for row in reader:
            if not row:
                continue
            lead_name = row[0].strip()
            try:
                values = np.array([float(v) for v in row[1:]], dtype=np.float32)
            except ValueError as exc:
                raise ValueError(f"Non-numeric value in row for lead {lead_name!r}: {exc}") from exc
            leads[lead_name] = values
    return leads


def _align_length(a: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    min_len = min(len(a), len(b))
    return a[:min_len], b[:min_len]


def compute_mae(gt: np.ndarray, pred: np.ndarray) -> float:
    gt, pred = _align_length(gt, pred)
    return float(np.mean(np.abs(gt - pred)))


def compute_rmse(gt: np.ndarray, pred: np.ndarray) -> float:
    gt, pred = _align_length(gt, pred)
    return float(np.sqrt(np.mean((gt - pred) ** 2)))


def compute_snr_proxy(gt: np.ndarray, pred: np.ndarray) -> float | None:
    gt, pred = _align_length(gt, pred)
    signal_power = float(np.mean(gt ** 2))
    if signal_power < 1e-10:
        return None
    noise_power = float(np.mean((gt - pred) ** 2))
    if noise_power < 1e-12:
        return float("inf")
    return float(10.0 * np.log10(signal_power / noise_power))


def score_waveforms(
    ground_truth: dict[str, np.ndarray],
    prediction: dict[str, np.ndarray],
) -> dict:
    common_leads = sorted(set(ground_truth) & set(prediction))
    missing_in_pred = sorted(set(ground_truth) - set(prediction))
    missing_in_gt = sorted(set(prediction) - set(ground_truth))

    per_lead: dict[str, dict] = {}
    all_mae: list[float] = []
    all_rmse: list[float] = []
    all_snr: list[float] = []

    for lead in common_leads:
        gt_sig = ground_truth[lead]
        pred_sig = prediction[lead]
        gt_a, pred_a = _align_length(gt_sig, pred_sig)
        length_match = len(gt_sig) == len(pred_sig)

        mae = compute_mae(gt_a, pred_a)
        rmse = compute_rmse(gt_a, pred_a)
        snr = compute_snr_proxy(gt_a, pred_a)

        per_lead[lead] = {
            "mae": round(mae, 6),
            "rmse": round(rmse, 6),
            "snr_proxy_db": round(snr, 3) if snr is not None and np.isfinite(snr) else None,
            "gt_length": int(len(gt_sig)),
            "pred_length": int(len(pred_sig)),
            "aligned_length": int(len(gt_a)),
            "length_match": length_match,
        }
        all_mae.append(mae)
        all_rmse.append(rmse)
        if snr is not None and np.isfinite(snr):
            all_snr.append(snr)

    aggregate = {
        "mean_mae": round(float(np.mean(all_mae)), 6) if all_mae else None,
        "mean_rmse": round(float(np.mean(all_rmse)), 6) if all_rmse else None,
        "mean_snr_proxy_db": round(float(np.mean(all_snr)), 3) if all_snr else None,
        "num_leads_scored": len(common_leads),
    }

    return {
        "synthetic": True,
        "disclaimer": SYNTHETIC_DISCLAIMER,
        "aggregate": aggregate,
        "per_lead": per_lead,
        "missing_leads": {
            "in_prediction": missing_in_pred,
            "in_ground_truth": missing_in_gt,
        },
        "common_leads": common_leads,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score synthetic waveform predictions against ground-truth CSVs."
    )
    parser.add_argument("--ground-truth", required=True, help="Path to ground-truth waveform CSV.")
    parser.add_argument("--prediction", required=True, help="Path to prediction waveform CSV.")
    parser.add_argument(
        "--output",
        default="reports/synthetic_score.json",
        help="Output JSON path for scoring results.",
    )
    args = parser.parse_args(argv)

    gt_path = Path(args.ground_truth)
    pred_path = Path(args.prediction)
    out_path = Path(args.output)

    if not gt_path.exists():
        print(f"ERROR: Ground-truth file not found: {gt_path}", file=sys.stderr)
        return 1
    if not pred_path.exists():
        print(f"ERROR: Prediction file not found: {pred_path}", file=sys.stderr)
        return 1

    print(f"[score_synthetic] Ground truth : {gt_path}")
    print(f"[score_synthetic] Prediction   : {pred_path}")
    print("[score_synthetic] SYNTHETIC benchmark scoring only.")

    gt_data = load_waveform_csv(gt_path)
    pred_data = load_waveform_csv(pred_path)

    result = score_waveforms(gt_data, pred_data)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    agg = result["aggregate"]
    print(f"\n[score_synthetic] Aggregate results ({agg['num_leads_scored']} leads):")
    print(f"  Mean MAE   : {agg['mean_mae']}")
    print(f"  Mean RMSE  : {agg['mean_rmse']}")
    print(f"  Mean SNR   : {agg['mean_snr_proxy_db']} dB (proxy, synthetic only)")
    print(f"\n  Output     : {out_path}")
    print(f"\n  DISCLAIMER : {SYNTHETIC_DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
