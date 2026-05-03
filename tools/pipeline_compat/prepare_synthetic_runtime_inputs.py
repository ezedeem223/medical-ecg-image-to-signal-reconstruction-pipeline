"""
Synthetic-to-Runtime Input Adapter — ECG Pipeline Compatibility Layer

Takes generated synthetic benchmark cases and prepares a minimal
runtime-compatible synthetic fixture directory.

IMPORTANT:
- Does NOT overwrite real data.
- Does NOT write into data/images/ by default.
- Keeps all fixtures under data/synthetic_runtime_compat/ (or --output-root).
- Every file and manifest clearly labels SYNTHETIC_COMPATIBILITY_ONLY.
- If parquet support is unavailable, generates CSV fallback.

Usage:
    python tools/pipeline_compat/prepare_synthetic_runtime_inputs.py \\
        --synthetic-root benchmark_cases/seed \\
        --output-root data/synthetic_runtime_compat \\
        --max-cases 3
"""
from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.pipeline_compat.schemas import COMPAT_DISCLAIMER, LEAD_NAMES, SYNTHETIC_LABEL  # noqa: E402

_SUBMISSION_SAMPLES = 100


def _build_submission_ids(case_id: str, n_samples: int = _SUBMISSION_SAMPLES) -> list[str]:
    ids = []
    for lead in LEAD_NAMES:
        for i in range(n_samples):
            ids.append(f"{case_id}_{i}_{lead}")
    return ids


def _write_test_csv(output_dir: Path, case_ids: list[str], n_samples: int) -> Path:
    path = output_dir / "test.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "fs"])
        for cid in case_ids:
            writer.writerow([cid, "500.0"])
    return path


def _write_submission_template(
    output_dir: Path, case_ids: list[str], n_samples: int
) -> tuple[Path, str]:
    ids = []
    for cid in case_ids:
        ids.extend(_build_submission_ids(cid, n_samples))

    try:
        import pandas as pd
        parquet_path = output_dir / "sample_submission.parquet"
        pd.DataFrame({"id": ids, "value": 0.0}).to_parquet(parquet_path, index=False)
        return parquet_path, "parquet"
    except ImportError:
        pass

    csv_path = output_dir / "sample_submission.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "value"])
        for row_id in ids:
            writer.writerow([row_id, "0.0"])
    return csv_path, "csv_fallback"


def _copy_images(
    synthetic_root: Path, images_out: Path, case_id: str, distortions: list[str]
) -> list[str]:
    copied: list[str] = []
    src_dir = synthetic_root / "images"
    images_out.mkdir(parents=True, exist_ok=True)
    for dist in distortions:
        for ext in (".ppm", ".png", ".jpg"):
            src = src_dir / f"{case_id}_{dist}{ext}"
            if src.exists():
                dst = images_out / f"{case_id}{ext}"
                shutil.copy2(src, dst)
                copied.append(str(dst.relative_to(images_out.parent)))
                break
    return copied


def prepare(
    synthetic_root: Path,
    output_root: Path,
    max_cases: int = 3,
    n_samples: int = _SUBMISSION_SAMPLES,
) -> dict:
    manifest_path = synthetic_root / "synthetic_manifest.json"
    if not manifest_path.exists():
        return {
            "success": False,
            "error": f"Manifest not found: {manifest_path}. Run generate_cases.py first.",
            "synthetic": True,
            "compatibility_only": True,
        }

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cases = manifest.get("cases", [])[:max_cases]

    output_root.mkdir(parents=True, exist_ok=True)
    images_out = output_root / "images"
    gt_out = output_root / "ground_truth_waveforms"
    meta_out = output_root / "metadata"
    gt_out.mkdir(parents=True, exist_ok=True)
    meta_out.mkdir(parents=True, exist_ok=True)

    case_ids = [c["case_id"] for c in cases]

    test_csv_path = _write_test_csv(output_root, case_ids, n_samples)
    submission_path, submission_format = _write_submission_template(
        output_root, case_ids, n_samples
    )

    fixture_cases = []
    for case in cases:
        cid = case["case_id"]
        wf_src = synthetic_root / case.get("waveform_csv", f"waveforms/{cid}.csv")
        meta_src = synthetic_root / case.get("metadata_json", f"metadata/{cid}.json")

        wf_dst = gt_out / f"{cid}.csv"
        meta_dst = meta_out / f"{cid}.json"

        if wf_src.exists():
            shutil.copy2(wf_src, wf_dst)
        if meta_src.exists():
            shutil.copy2(meta_src, meta_dst)

        images = _copy_images(synthetic_root, images_out, cid, case.get("images", [cid + "_clean"]))

        fixture_cases.append({
            "case_id": cid,
            "image_source": str(wf_src.parent.parent / "images"),
            "runtime_image_path": str(images_out / f"{cid}.ppm") if not images else images[0],
            "waveform_ground_truth_path": str(wf_dst),
            "metadata_path": str(meta_dst),
            "distortion_type": "clean",
            "synthetic": True,
            "compatibility_only": True,
            "notes": (
                f"Synthetic fixture for runtime compatibility testing only. "
                f"Submission template uses {n_samples} samples per lead × 12 leads = "
                f"{n_samples * 12} rows per case. "
                f"SYNTHETIC_COMPATIBILITY_ONLY."
            ),
        })

    input_manifest = {
        "synthetic": True,
        "compatibility_only": True,
        "label": SYNTHETIC_LABEL,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_manifest": str(manifest_path),
        "fixture_root": str(output_root),
        "images_dir": str(images_out),
        "test_csv": str(test_csv_path),
        "submission_template": str(submission_path),
        "submission_format": submission_format,
        "n_samples_per_lead": n_samples,
        "num_cases": len(fixture_cases),
        "cases": fixture_cases,
        "disclaimer": COMPAT_DISCLAIMER,
        "parquet_note": (
            "parquet" if submission_format == "parquet"
            else (
                "Parquet support unavailable (pandas/pyarrow not installed). "
                "CSV fallback generated. Full pipeline smoke test cannot run until "
                "parquet support exists or the runtime config is adapted."
            )
        ),
    }

    manifest_out = output_root / "synthetic_runtime_input_manifest.json"
    manifest_out.write_text(json.dumps(input_manifest, indent=2), encoding="utf-8")

    readme = output_root / "README.md"
    readme.write_text(
        f"# Synthetic Runtime Compatibility Fixture\n\n"
        f"**Label:** `{SYNTHETIC_LABEL}`\n\n"
        f"This directory contains synthetic fixtures prepared for engineering "
        f"compatibility testing of the ECG image-to-signal runtime pipeline. "
        f"It does **not** contain real ECG data, real patient data, or competition "
        f"data. All files are generated from the parametric synthetic benchmark.\n\n"
        f"**Do not use this fixture as real runtime input without updating configs.**\n\n"
        f"Generated: {datetime.now(timezone.utc).isoformat()}\n\n"
        f"> {COMPAT_DISCLAIMER}\n",
        encoding="utf-8",
    )

    return input_manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Prepare synthetic runtime fixture for ECG pipeline compatibility testing."
    )
    parser.add_argument("--synthetic-root", default="benchmark_cases/seed")
    parser.add_argument("--output-root", default="data/synthetic_runtime_compat")
    parser.add_argument("--max-cases", type=int, default=3)
    parser.add_argument(
        "--n-samples", type=int, default=_SUBMISSION_SAMPLES,
        help="Samples per lead in submission template (default: 100).",
    )
    args = parser.parse_args(argv)

    synthetic_root = (ROOT / args.synthetic_root).resolve()
    output_root = (ROOT / args.output_root).resolve()

    print(f"[prepare_synthetic_inputs] Source : {synthetic_root}")
    print(f"[prepare_synthetic_inputs] Output : {output_root}")
    print(f"[prepare_synthetic_inputs] Max cases: {args.max_cases}")
    print(f"[prepare_synthetic_inputs] Label: {SYNTHETIC_LABEL}")

    result = prepare(synthetic_root, output_root, args.max_cases, args.n_samples)

    if not result.get("success", True) and "error" in result:
        print(f"[prepare_synthetic_inputs] ERROR: {result['error']}", file=sys.stderr)
        return 1

    print(f"[prepare_synthetic_inputs] Cases prepared: {result.get('num_cases', 0)}")
    print(f"[prepare_synthetic_inputs] Submission format: {result.get('submission_format', 'unknown')}")
    print(f"[prepare_synthetic_inputs] Manifest → {result.get('fixture_root', output_root)}/synthetic_runtime_input_manifest.json")
    if result.get("submission_format") == "csv_fallback":
        print("[prepare_synthetic_inputs] WARNING: parquet unavailable — CSV fallback used.")
    print(f"\n  DISCLAIMER: {COMPAT_DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
