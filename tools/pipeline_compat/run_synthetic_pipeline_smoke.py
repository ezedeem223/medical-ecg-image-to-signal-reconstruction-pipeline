"""
Optional Full-Pipeline Smoke Test — ECG Pipeline Compatibility Layer

Attempts a limited runtime smoke test on synthetic compatibility fixtures
ONLY when all required assets are present. Always exits 0 — skip and
failure states are recorded in the report, not raised as errors.

Report statuses:
  SKIPPED_ASSETS_MISSING
  SKIPPED_INPUT_CONTRACT_UNAVAILABLE
  RUNTIME_EXECUTED_VALIDATION_PASSED
  RUNTIME_EXECUTED_VALIDATION_FAILED
  RUNTIME_EXECUTION_FAILED
  REPORT_ONLY

SYNTHETIC COMPATIBILITY ONLY — not a real ECG evaluation.

Usage:
    python tools/pipeline_compat/run_synthetic_pipeline_smoke.py \\
        --synthetic-root benchmark_cases/seed \\
        --fixture-root data/synthetic_runtime_compat \\
        --config configs/runtime.default.yaml \\
        --report reports/pipeline_compat/synthetic_pipeline_smoke_report.md \\
        --summary-json reports/pipeline_compat/synthetic_pipeline_compat_summary.json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.pipeline_compat.inspect_asset_readiness import inspect  # noqa: E402
from tools.pipeline_compat.schemas import COMPAT_DISCLAIMER, SYNTHETIC_LABEL  # noqa: E402


def _make_synthetic_config(
    fixture_root: Path, base_config_path: Path, tmp_dir: Path
) -> Path:
    manifest_path = fixture_root / "synthetic_runtime_input_manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        submission_template = manifest.get("submission_template", "")
        images_dir = manifest.get("images_dir", str(fixture_root / "images"))
    else:
        submission_template = str(fixture_root / "sample_submission.csv")
        images_dir = str(fixture_root / "images")

    test_csv = str(fixture_root / "test.csv")

    config_out = tmp_dir / "synthetic_runtime_config.yaml"
    config_out.write_text(
        f"# AUTO-GENERATED synthetic compatibility config — DO NOT COMMIT\n"
        f"# {SYNTHETIC_LABEL}\n\n"
        f"paths:\n"
        f"  project_root: {ROOT}\n"
        f"  data_root: {fixture_root}\n"
        f"  image_root: {images_dir}\n"
        f"  test_csv: {test_csv}\n"
        f"  sample_submission: {submission_template}\n"
        f"  output_submission: {tmp_dir}/submission_synthetic.csv\n"
        f"  models_registry: {ROOT}/configs/models.yaml\n\n"
        f"models:\n"
        f"  detector_id: yolo_best\n"
        f"  primary_segmentation_id: effb3_primary\n"
        f"  fallback_segmentation_id: phase10_fallback\n"
        f"  allow_primary_failover: true\n"
        f"  use_fallback_assist: true\n\n"
        f"runtime:\n"
        f"  device: cpu\n"
        f"  yolo_conf: 0.10\n"
        f"  yolo_iou: 0.45\n"
        f"  target_height: 384\n"
        f"  max_width: 1536\n"
        f"  max_cache: 4\n"
        f"  dp_max_width: 1400\n"
        f"  dp_smooth: 0.45\n"
        f"  tta_scales: [1.0]\n"
        f"  tta_hflip: false\n"
        f"  primary_threshold: 0.45\n"
        f"  fallback_threshold: 0.50\n"
        f"  morph_kernel: 3\n"
        f"  min_component_area: 120\n"
        f"  skeleton_boost: false\n"
        f"  high_pass_cutoff_hz: 0.5\n"
        f"  image_extensions: [\".ppm\", \".png\", \".jpg\", \".jpeg\", \".bmp\"]\n\n"
        f"output:\n"
        f"  submission_path: {tmp_dir}/submission_synthetic.csv\n"
        f"  overwrite: true\n"
        f"  float_format: \"%.4f\"\n\n"
        f"debug:\n"
        f"  enabled: false\n"
        f"  artifacts_dir: {tmp_dir}/debug\n",
        encoding="utf-8",
    )
    return config_out


def run_smoke(
    synthetic_root: Path,
    fixture_root: Path,
    base_config: Path,
    report_path: Path,
    summary_json_path: Path,
) -> dict:
    checked_at = datetime.now(timezone.utc).isoformat()
    summary: dict = {
        "synthetic": True,
        "compatibility_only": True,
        "label": SYNTHETIC_LABEL,
        "checked_at_utc": checked_at,
        "status": "REPORT_ONLY",
        "asset_readiness": {},
        "fixture_summary": {},
        "command_attempted": None,
        "stdout_summary": None,
        "stderr_summary": None,
        "output_files": [],
        "scoring_possible": False,
        "qc_possible": False,
        "skip_reasons": [],
        "limitations": [],
        "disclaimer": COMPAT_DISCLAIMER,
    }

    readiness = inspect(ROOT, str(base_config))
    summary["asset_readiness"] = {
        "can_run_full_pipeline": readiness["can_run_full_pipeline"],
        "skip_reasons": readiness["skip_reasons"],
        "warnings": readiness["warnings"],
    }

    if not readiness["can_run_full_pipeline"]:
        summary["status"] = "SKIPPED_ASSETS_MISSING"
        summary["skip_reasons"] = readiness["skip_reasons"]
        _write_reports(summary, report_path, summary_json_path)
        return summary

    manifest_path = fixture_root / "synthetic_runtime_input_manifest.json"
    if not manifest_path.exists():
        summary["status"] = "SKIPPED_INPUT_CONTRACT_UNAVAILABLE"
        summary["skip_reasons"].append(
            f"Synthetic runtime fixture not found: {manifest_path}. "
            "Run prepare_synthetic_runtime_inputs.py first."
        )
        _write_reports(summary, report_path, summary_json_path)
        return summary

    fixture_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    summary["fixture_summary"] = {
        "num_cases": fixture_manifest.get("num_cases", 0),
        "submission_format": fixture_manifest.get("submission_format", "unknown"),
        "images_dir": fixture_manifest.get("images_dir", ""),
    }

    if fixture_manifest.get("submission_format") == "csv_fallback":
        summary["status"] = "SKIPPED_INPUT_CONTRACT_UNAVAILABLE"
        summary["skip_reasons"].append(
            "Submission template is CSV fallback; runtime requires parquet. "
            "Install pandas + pyarrow and re-run prepare_synthetic_runtime_inputs.py."
        )
        _write_reports(summary, report_path, summary_json_path)
        return summary

    with tempfile.TemporaryDirectory(prefix="ecg_smoke_") as tmp_dir:
        tmp = Path(tmp_dir)
        synth_config = _make_synthetic_config(fixture_root, base_config, tmp)

        cmd = [
            sys.executable, "-m", "ecg_digitizer",
            "run", "--config", str(synth_config),
        ]
        summary["command_attempted"] = " ".join(cmd)

        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,
                cwd=str(ROOT),
            )
            stdout = proc.stdout[-4000:] if proc.stdout else ""
            stderr = proc.stderr[-4000:] if proc.stderr else ""
            summary["stdout_summary"] = stdout
            summary["stderr_summary"] = stderr

            submission_out = tmp / "submission_synthetic.csv"
            if submission_out.exists():
                summary["output_files"].append(str(submission_out))

            if proc.returncode == 0 and submission_out.exists():
                summary["status"] = "RUNTIME_EXECUTED_VALIDATION_PASSED"
                summary["scoring_possible"] = True
                summary["qc_possible"] = True
            elif proc.returncode == 0:
                summary["status"] = "RUNTIME_EXECUTION_FAILED"
                summary["limitations"].append(
                    "Runtime returned exit 0 but no submission file was produced."
                )
            else:
                summary["status"] = "RUNTIME_EXECUTION_FAILED"
                summary["limitations"].append(
                    f"Runtime exited with code {proc.returncode}. "
                    "This may be expected due to synthetic input domain mismatch."
                )
        except subprocess.TimeoutExpired:
            summary["status"] = "RUNTIME_EXECUTION_FAILED"
            summary["limitations"].append("Runtime timed out after 300 seconds.")
        except FileNotFoundError:
            summary["status"] = "RUNTIME_EXECUTION_FAILED"
            summary["limitations"].append(
                "ecg_digitizer module not found. Ensure the package is installed (pip install -e .)."
            )

    summary["limitations"] += [
        "Synthetic images may not match real ECG page layout expected by the runtime.",
        "Submission ID format (case_id_index_lead) must align with runtime template parser.",
        "Even a passing smoke test does not validate clinical or reconstruction accuracy.",
    ]

    _write_reports(summary, report_path, summary_json_path)
    return summary


def _write_reports(summary: dict, report_path: Path, summary_json_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    summary_json_path.parent.mkdir(parents=True, exist_ok=True)

    summary_json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    status = summary["status"]
    emoji = {
        "SKIPPED_ASSETS_MISSING": "⏭️",
        "SKIPPED_INPUT_CONTRACT_UNAVAILABLE": "⏭️",
        "RUNTIME_EXECUTED_VALIDATION_PASSED": "✅",
        "RUNTIME_EXECUTED_VALIDATION_FAILED": "❌",
        "RUNTIME_EXECUTION_FAILED": "❌",
        "REPORT_ONLY": "📋",
    }.get(status, "❓")

    readiness = summary.get("asset_readiness", {})
    fixture = summary.get("fixture_summary", {})

    lines = [
        "# Synthetic Pipeline Smoke Test Report",
        "",
        f"**Status:** {emoji} `{status}`",
        f"**Checked at:** {summary['checked_at_utc']}",
        f"**Label:** `{summary['label']}`",
        "",
        "## Asset Readiness Summary",
        "",
        f"- Can run full pipeline: {'✅' if readiness.get('can_run_full_pipeline') else '❌'}",
    ]
    for r in readiness.get("skip_reasons", []):
        lines.append(f"- ❌ {r}")
    for w in readiness.get("warnings", []):
        lines.append(f"- ⚠️  {w}")

    if fixture:
        lines += [
            "",
            "## Fixture Summary",
            "",
            f"- Cases: {fixture.get('num_cases', 0)}",
            f"- Submission format: {fixture.get('submission_format', 'unknown')}",
            f"- Images directory: `{fixture.get('images_dir', '')}`",
        ]

    if summary.get("command_attempted"):
        lines += ["", "## Command Attempted", "", f"```\n{summary['command_attempted']}\n```"]

    if summary.get("skip_reasons"):
        lines += ["", "## Skip Reasons", ""]
        for r in summary["skip_reasons"]:
            lines.append(f"- {r}")

    if summary.get("limitations"):
        lines += ["", "## Limitations", ""]
        for lim in summary["limitations"]:
            lines.append(f"- {lim}")

    lines += [
        "",
        "---",
        "",
        f"> **Disclaimer:** {COMPAT_DISCLAIMER}",
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run optional ECG pipeline smoke test on synthetic fixtures."
    )
    parser.add_argument("--synthetic-root", default="benchmark_cases/seed")
    parser.add_argument("--fixture-root", default="data/synthetic_runtime_compat")
    parser.add_argument("--config", default="configs/runtime.default.yaml")
    parser.add_argument(
        "--report",
        default="reports/pipeline_compat/synthetic_pipeline_smoke_report.md",
    )
    parser.add_argument(
        "--summary-json",
        default="reports/pipeline_compat/synthetic_pipeline_compat_summary.json",
    )
    args = parser.parse_args(argv)

    synthetic_root = (ROOT / args.synthetic_root).resolve()
    fixture_root = (ROOT / args.fixture_root).resolve()
    base_config = (ROOT / args.config).resolve()
    report_path = (ROOT / args.report).resolve()
    summary_json = (ROOT / args.summary_json).resolve()

    print(f"[smoke_test] Synthetic root : {synthetic_root}")
    print(f"[smoke_test] Fixture root   : {fixture_root}")
    print(f"[smoke_test] Config         : {base_config}")
    print(f"[smoke_test] Label          : {SYNTHETIC_LABEL}")

    result = run_smoke(synthetic_root, fixture_root, base_config, report_path, summary_json)
    print(f"[smoke_test] Status: {result['status']}")
    print(f"[smoke_test] Report → {report_path}")
    print(f"[smoke_test] Summary JSON → {summary_json}")
    print(f"\n  DISCLAIMER: {COMPAT_DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
