"""
Submission-to-Waveform Converter — ECG Pipeline Compatibility Layer

Converts a runtime submission CSV (id, value) to per-lead waveform CSV files
compatible with the synthetic scoring utility (score_synthetic.py).

Expected submission ID format (from synthetic fixture):
    {case_id}_{point_index}_{lead_name}
    e.g.: case_000_0_I, case_000_1_I, ..., case_000_99_II, ...

Expected waveform output format:
    lead_name, 0, 1, 2, ..., N-1
    I, <float>, <float>, ...
    II, <float>, ...

Behavior:
- If the submission file does not exist, skip and report.
- If the ID format cannot be parsed, skip and report. Never fabricate leads.
- If mapping is ambiguous, refuse and document why.

SYNTHETIC COMPATIBILITY ONLY.

Usage:
    python tools/pipeline_compat/convert_submission_to_waveforms.py \\
        --submission results/submission.csv \\
        --manifest data/synthetic_runtime_compat/synthetic_runtime_input_manifest.json \\
        --output-dir reports/pipeline_compat/predicted_waveforms \\
        --report reports/pipeline_compat/submission_conversion_report.md
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.pipeline_compat.schemas import COMPAT_DISCLAIMER, LEAD_NAMES, SYNTHETIC_LABEL  # noqa: E402


def _parse_synthetic_id(record_id: str) -> tuple[str | None, int | None, str | None]:
    parts = record_id.split("_")
    if len(parts) < 3:
        return None, None, None

    candidate_lead = parts[-1]
    if candidate_lead in LEAD_NAMES:
        try:
            return "_".join(parts[:-2]), int(parts[-2]), candidate_lead
        except ValueError:
            pass

    candidate_lead = parts[-2]
    if candidate_lead in LEAD_NAMES:
        try:
            return "_".join(parts[:-2]), int(parts[-1]), candidate_lead
        except ValueError:
            pass

    return None, None, None


def convert(
    submission_path: Path,
    manifest_path: Path | None,
    output_dir: Path,
    report_path: Path,
) -> dict:
    result: dict = {
        "synthetic": True,
        "compatibility_only": True,
        "label": SYNTHETIC_LABEL,
        "status": "SKIPPED",
        "skip_reason": None,
        "converted_cases": [],
        "failed_cases": [],
        "output_dir": str(output_dir),
        "disclaimer": COMPAT_DISCLAIMER,
    }

    if not submission_path.exists():
        result["skip_reason"] = f"Submission file not found: {submission_path}"
        _write_report(result, report_path)
        return result

    if manifest_path is not None and not manifest_path.exists():
        result["skip_reason"] = f"Fixture manifest not found: {manifest_path}"
        _write_report(result, report_path)
        return result

    with open(submission_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        result["skip_reason"] = "Submission file is empty."
        _write_report(result, report_path)
        return result

    if "id" not in rows[0] or "value" not in rows[0]:
        result["skip_reason"] = (
            f"Submission must have 'id' and 'value' columns. "
            f"Found: {list(rows[0].keys())}"
        )
        _write_report(result, report_path)
        return result

    by_case: dict[str, dict[str, dict[int, float]]] = defaultdict(lambda: defaultdict(dict))
    unparseable = 0
    for row in rows:
        rid = row["id"]
        try:
            val = float(row["value"])
        except (ValueError, TypeError):
            unparseable += 1
            continue
        case_id, idx, lead = _parse_synthetic_id(rid)
        if case_id is None or idx is None or lead is None:
            unparseable += 1
            continue
        by_case[case_id][lead][idx] = val

    if not by_case:
        result["skip_reason"] = (
            f"Could not parse any submission IDs into (case_id, point_index, lead) tuples. "
            f"{unparseable} rows had unrecognised format. "
            f"Expected format: {{case_id}}_{{index}}_{{lead}}, e.g. case_000_0_I. "
            f"Conversion refused — never fabricate lead waveforms."
        )
        _write_report(result, report_path)
        return result

    output_dir.mkdir(parents=True, exist_ok=True)

    for case_id, lead_data in by_case.items():
        n_samples = max(
            (max(indices.keys()) + 1 for indices in lead_data.values() if indices),
            default=0,
        )
        if n_samples == 0:
            result["failed_cases"].append({"case_id": case_id, "reason": "No valid samples."})
            continue

        missing_leads = [lead for lead in LEAD_NAMES if lead not in lead_data]
        if missing_leads:
            result["failed_cases"].append({
                "case_id": case_id,
                "reason": (
                    f"Missing leads in submission: {missing_leads}. "
                    "Conversion skipped — never fabricate missing leads."
                ),
            })
            continue

        out_path = output_dir / f"{case_id}_predicted.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["lead_name"] + [str(i) for i in range(n_samples)])
            for lead in LEAD_NAMES:
                row = [lead] + [
                    f"{lead_data[lead].get(i, 0.0):.6f}" for i in range(n_samples)
                ]
                writer.writerow(row)

        result["converted_cases"].append({
            "case_id": case_id,
            "output_path": str(out_path),
            "n_samples": n_samples,
            "leads": LEAD_NAMES,
        })

    result["status"] = (
        "CONVERTED" if result["converted_cases"] else "SKIPPED_NO_VALID_CASES"
    )
    if unparseable:
        result["unparseable_rows"] = unparseable

    _write_report(result, report_path)
    return result


def _write_report(result: dict, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Submission-to-Waveform Conversion Report",
        "",
        f"**Status:** `{result['status']}`",
        f"**Label:** `{result['label']}`",
        "",
    ]
    if result.get("skip_reason"):
        lines += ["## Skip Reason", "", result["skip_reason"], ""]

    if result.get("converted_cases"):
        lines += ["## Converted Cases", ""]
        for c in result["converted_cases"]:
            lines.append(
                f"- `{c['case_id']}` → `{c['output_path']}` "
                f"({c['n_samples']} samples × 12 leads)"
            )
        lines.append("")

    if result.get("failed_cases"):
        lines += ["## Failed / Skipped Cases", ""]
        for c in result["failed_cases"]:
            lines.append(f"- `{c['case_id']}`: {c['reason']}")
        lines.append("")

    lines += [
        "---",
        "",
        f"> **Disclaimer:** {COMPAT_DISCLAIMER}",
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert submission CSV to per-lead waveform CSVs for synthetic scoring."
    )
    parser.add_argument("--submission", default="results/submission.csv")
    parser.add_argument(
        "--manifest",
        default="data/synthetic_runtime_compat/synthetic_runtime_input_manifest.json",
    )
    parser.add_argument(
        "--output-dir",
        default="reports/pipeline_compat/predicted_waveforms",
    )
    parser.add_argument(
        "--report",
        default="reports/pipeline_compat/submission_conversion_report.md",
    )
    args = parser.parse_args(argv)

    submission_path = (ROOT / args.submission).resolve()
    manifest_path = (ROOT / args.manifest).resolve() if args.manifest else None
    output_dir = (ROOT / args.output_dir).resolve()
    report_path = (ROOT / args.report).resolve()

    print(f"[convert_submission] Submission : {submission_path}")
    print(f"[convert_submission] Manifest   : {manifest_path}")
    print(f"[convert_submission] Output dir : {output_dir}")

    result = convert(submission_path, manifest_path, output_dir, report_path)
    print(f"[convert_submission] Status: {result['status']}")
    if result.get("skip_reason"):
        print(f"[convert_submission] Skip reason: {result['skip_reason']}")
    print(f"[convert_submission] Report → {report_path}")
    print(f"\n  DISCLAIMER: {COMPAT_DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
