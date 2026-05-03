# Pipeline Compatibility Tools

**Label:** `SYNTHETIC_COMPATIBILITY_ONLY`

This directory contains engineering tools for the ECG Pipeline Compatibility Max Pass.
They bridge the synthetic benchmark with the full runtime pipeline to test input
contract compatibility — **not** to validate ECG reconstruction accuracy.

---

## Tools

| Script | Purpose |
|--------|---------|
| `inspect_asset_readiness.py` | Check whether all required configs, checkpoints, and data files exist |
| `prepare_synthetic_runtime_inputs.py` | Build a minimal runtime-compatible fixture from synthetic benchmark cases |
| `run_synthetic_pipeline_smoke.py` | Attempt a limited smoke test; skip honestly if assets are missing |
| `convert_submission_to_waveforms.py` | Convert runtime submission CSV to per-lead waveform CSVs for synthetic scoring |
| `generate_pipeline_compat_report.py` | Generate a consolidated compatibility report from all tool outputs |
| `schemas.py` | Shared constants and asset definitions |

---

## Quick Start

```bash
# Step 1 — generate synthetic cases
python tools/synthetic_benchmark/generate_cases.py \
    --output benchmark_cases/seed --num-cases 5

# Step 2 — inspect assets
python tools/pipeline_compat/inspect_asset_readiness.py \
    --config configs/runtime.default.yaml \
    --output-json reports/pipeline_compat/asset_readiness_report.json \
    --output-md  reports/pipeline_compat/asset_readiness_report.md

# Step 3 — prepare synthetic fixture
python tools/pipeline_compat/prepare_synthetic_runtime_inputs.py \
    --synthetic-root benchmark_cases/seed \
    --output-root data/synthetic_runtime_compat \
    --max-cases 3

# Step 4 — optional smoke test (skips safely if assets missing)
python tools/pipeline_compat/run_synthetic_pipeline_smoke.py \
    --synthetic-root benchmark_cases/seed \
    --fixture-root data/synthetic_runtime_compat \
    --config configs/runtime.default.yaml \
    --report reports/pipeline_compat/synthetic_pipeline_smoke_report.md \
    --summary-json reports/pipeline_compat/synthetic_pipeline_compat_summary.json

# Step 5 — generate consolidated report
python tools/pipeline_compat/generate_pipeline_compat_report.py \
    --asset-readiness reports/pipeline_compat/asset_readiness_report.json \
    --fixture-manifest data/synthetic_runtime_compat/synthetic_runtime_input_manifest.json \
    --smoke-summary reports/pipeline_compat/synthetic_pipeline_compat_summary.json \
    --output reports/pipeline_compat/PIPELINE_COMPATIBILITY_REPORT.md
```

See `docs/research_pack/ECG_PIPELINE_COMPATIBILITY_RUNBOOK.md` for the full step-by-step runbook.

---

## What This Is

- Engineering readiness check
- Synthetic fixture preparation
- Optional smoke test with honest skip semantics
- Compatibility report generation

## What This Is Not

- Clinical validation
- Real ECG reconstruction accuracy assessment
- Diagnostic performance evaluation
- Published benchmark comparison

---

> **Disclaimer:** All synthetic outputs are labeled `SYNTHETIC_COMPATIBILITY_ONLY`.
> This toolset does not validate ECG reconstruction performance, clinical utility,
> or diagnostic correctness.
