"""
Pipeline Compatibility Report Generator — ECG Pipeline Compatibility Layer

Generates a consolidated Markdown report from:
- asset readiness JSON
- synthetic runtime input manifest
- smoke test summary JSON
- optional synthetic score JSON
- optional QC report

SYNTHETIC COMPATIBILITY ONLY.

Usage:
    python tools/pipeline_compat/generate_pipeline_compat_report.py \\
        --asset-readiness reports/pipeline_compat/asset_readiness_report.json \\
        --fixture-manifest data/synthetic_runtime_compat/synthetic_runtime_input_manifest.json \\
        --smoke-summary reports/pipeline_compat/synthetic_pipeline_compat_summary.json \\
        --output reports/pipeline_compat/PIPELINE_COMPATIBILITY_REPORT.md
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.pipeline_compat.schemas import COMPAT_DISCLAIMER, SYNTHETIC_LABEL  # noqa: E402

_FORBIDDEN_PHRASES = [
    "clinical validation",
    "clinical accuracy",
    "diagnostic performance",
    "fda",
    "ce mark",
    "approved",
    "real ecg accuracy",
    "published benchmark",
]


def _load_json_safe(path: Path | None) -> dict | None:
    if path is None or not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def generate(
    asset_readiness: dict | None,
    fixture_manifest: dict | None,
    smoke_summary: dict | None,
    synthetic_score: dict | None,
    output_path: Path,
) -> str:
    now = datetime.now(timezone.utc).isoformat()

    lines = [
        "# ECG Pipeline Compatibility Report",
        "",
        f"**Generated:** {now}",
        f"**Label:** `{SYNTHETIC_LABEL}`",
        "",
        "> **Disclaimer:** This is a synthetic compatibility and engineering "
        "smoke-test report only. It does not establish clinical validity, "
        "real ECG reconstruction accuracy, or diagnostic performance.",
        "",
        "---",
        "",
    ]

    lines += ["## 1. Asset Readiness", ""]
    if asset_readiness:
        can_run = asset_readiness.get("can_run_full_pipeline", False)
        lines.append(f"**Can run full pipeline:** {'✅ YES' if can_run else '❌ NO'}")
        skip_reasons = asset_readiness.get("skip_reasons", [])
        if skip_reasons:
            lines += ["", "**Missing assets:**"]
            for r in skip_reasons:
                lines.append(f"- {r}")
        warnings = asset_readiness.get("warnings", [])
        if warnings:
            lines += ["", "**Warnings:**"]
            for w in warnings:
                lines.append(f"- ⚠️  {w}")
    else:
        lines.append("_Asset readiness report not available. Run inspect_asset_readiness.py._")
    lines.append("")

    lines += ["## 2. Input Compatibility", ""]
    if fixture_manifest:
        n_cases = fixture_manifest.get("num_cases", 0)
        fmt = fixture_manifest.get("submission_format", "unknown")
        parquet_note = fixture_manifest.get("parquet_note", "")
        lines += [
            f"- Synthetic fixture cases prepared: **{n_cases}**",
            f"- Submission template format: **{fmt}**",
        ]
        if parquet_note and fmt != "parquet":
            lines.append(f"- ⚠️  {parquet_note}")
    else:
        lines.append(
            "_Fixture manifest not available. Run prepare_synthetic_runtime_inputs.py._"
        )
    lines.append("")

    lines += ["## 3. Runtime Execution", ""]
    if smoke_summary:
        status = smoke_summary.get("status", "UNKNOWN")
        lines.append(f"**Smoke test status:** `{status}`")
        cmd = smoke_summary.get("command_attempted")
        if cmd:
            lines += ["", "**Command attempted:**", f"```\n{cmd}\n```"]
        for reason in smoke_summary.get("skip_reasons", []):
            lines.append(f"- ⏭️  {reason}")
        for lim in smoke_summary.get("limitations", []):
            lines.append(f"- ℹ️  {lim}")
    else:
        lines.append("_Smoke test summary not available. Run run_synthetic_pipeline_smoke.py._")
    lines.append("")

    lines += ["## 4. Output Validation", ""]
    if smoke_summary:
        out_files = smoke_summary.get("output_files", [])
        if out_files:
            lines.append("**Output files generated:**")
            for f in out_files:
                lines.append(f"- `{f}`")
        else:
            lines.append("No output files generated.")
    else:
        lines.append("_Not available._")
    lines.append("")

    lines += ["## 5. Synthetic Scoring", ""]
    if synthetic_score:
        agg = synthetic_score.get("aggregate", {})
        lines += [
            f"- Mean MAE: `{agg.get('mean_mae', 'N/A')}`",
            f"- Mean RMSE: `{agg.get('mean_rmse', 'N/A')}`",
            f"- Leads scored: `{agg.get('num_leads_scored', 'N/A')}`",
            "",
            "> Scores are on **synthetic benchmark waveforms only** — not real ECG data.",
        ]
    else:
        lines.append(
            "_Synthetic score not available. Run score_synthetic.py on any predicted waveforms._"
        )
    lines.append("")

    lines += ["## 6. QC Inspection", ""]
    lines.append(
        "_Run `tools/quality/generate_quality_report.py` on waveform CSVs for QC results._"
    )
    lines.append("")

    lines += ["## 7. Limitations", ""]
    base_limitations = [
        "All results are based on parametric synthetic waveforms — not real ECG recordings.",
        "Synthetic images may not match the spatial layout expected by the YOLO detector.",
        "Submission ID format must align exactly with the runtime template parser.",
        "Even a passing smoke test does not validate clinical or reconstruction accuracy.",
        "No published benchmark performance is claimed or implied.",
    ]
    for lim in base_limitations:
        lines.append(f"- {lim}")
    lines.append("")

    lines += ["## 8. Next Steps", ""]
    next_steps = [
        "If assets are missing: obtain model checkpoints and real input data before retesting.",
        "If fixture format is incompatible: install pandas + pyarrow for parquet support.",
        "If smoke test fails: review `stderr_summary` in the smoke summary JSON.",
        "If smoke test passes: run `convert_submission_to_waveforms.py` then `score_synthetic.py`.",
        "Do not merge this branch to main until the full compatibility pass is reviewed.",
    ]
    for step in next_steps:
        lines.append(f"- {step}")
    lines.append("")

    lines += [
        "---",
        "",
        f"> **Full disclaimer:** {COMPAT_DISCLAIMER}",
        "",
    ]

    report = "\n".join(lines)

    for phrase in _FORBIDDEN_PHRASES:
        if phrase.lower() in report.lower():
            report += f"\n\n<!-- WARNING: Report may contain restricted phrase: {phrase} -->\n"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate consolidated pipeline compatibility report."
    )
    parser.add_argument(
        "--asset-readiness",
        default="reports/pipeline_compat/asset_readiness_report.json",
    )
    parser.add_argument(
        "--fixture-manifest",
        default="data/synthetic_runtime_compat/synthetic_runtime_input_manifest.json",
    )
    parser.add_argument(
        "--smoke-summary",
        default="reports/pipeline_compat/synthetic_pipeline_compat_summary.json",
    )
    parser.add_argument("--synthetic-score", default=None)
    parser.add_argument(
        "--output",
        default="reports/pipeline_compat/PIPELINE_COMPATIBILITY_REPORT.md",
    )
    args = parser.parse_args(argv)

    asset_readiness = _load_json_safe(ROOT / args.asset_readiness)
    fixture_manifest = _load_json_safe(ROOT / args.fixture_manifest)
    smoke_summary = _load_json_safe(ROOT / args.smoke_summary)
    synthetic_score = _load_json_safe(ROOT / args.synthetic_score) if args.synthetic_score else None
    output_path = (ROOT / args.output).resolve()

    print(f"[compat_report] Asset readiness loaded : {asset_readiness is not None}")
    print(f"[compat_report] Fixture manifest loaded : {fixture_manifest is not None}")
    print(f"[compat_report] Smoke summary loaded    : {smoke_summary is not None}")

    generate(asset_readiness, fixture_manifest, smoke_summary, synthetic_score, output_path)

    print(f"[compat_report] Report → {output_path}")
    print(f"\n  DISCLAIMER: {COMPAT_DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
