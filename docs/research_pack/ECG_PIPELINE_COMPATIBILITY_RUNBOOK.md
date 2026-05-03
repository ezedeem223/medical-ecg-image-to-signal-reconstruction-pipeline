# ECG Pipeline Compatibility Runbook

**Label:** `SYNTHETIC_COMPATIBILITY_ONLY`
**Status:** Engineering runbook — not a clinical protocol.

This runbook walks through the full compatibility pass in order.
All steps use synthetic data only. No real ECG data is required.

---

## Prerequisites

```bash
# Ensure the package is installed in development mode
pip install -e ".[dev]"

# Confirm ruff and pytest are available
python -m ruff --version
python -m pytest --version
```

---

## Step 1 — Generate Synthetic Cases

Generate the synthetic benchmark. This produces waveform CSVs, metadata JSON,
and rendered ECG images under `benchmark_cases/seed/`.

```bash
python tools/synthetic_benchmark/generate_cases.py \
    --output benchmark_cases/seed \
    --num-cases 5
```

Expected output:

```
[synthetic_benchmark] Generating 5 SYNTHETIC cases
  Output: benchmark_cases/seed
  FS=500 Hz  duration=10s  seed=42
  WARNING: All output is SYNTHETIC — not real ECG data.
  ...
[synthetic_benchmark] Done. Generated 5 cases.
  Manifest: benchmark_cases/seed/synthetic_manifest.json
```

---

## Step 2 — Inspect Assets

Check whether all required runtime files exist (configs, model checkpoints, data).

```bash
python tools/pipeline_compat/inspect_asset_readiness.py \
    --config configs/runtime.default.yaml \
    --output-json reports/pipeline_compat/asset_readiness_report.json \
    --output-md  reports/pipeline_compat/asset_readiness_report.md
```

Review the output:

- `can_run_full_pipeline: true` — all assets present.
- `can_run_full_pipeline: false` — list of missing assets shown. Step 4 will be skipped automatically.

The report is safe to run in CI. It always exits 0.

---

## Step 3 — Prepare Synthetic Runtime Fixture

Build a minimal runtime-compatible fixture from synthetic benchmark cases.
This creates an isolated directory under `data/synthetic_runtime_compat/`.
It does **not** touch `data/images/` or any real data.

```bash
python tools/pipeline_compat/prepare_synthetic_runtime_inputs.py \
    --synthetic-root benchmark_cases/seed \
    --output-root data/synthetic_runtime_compat \
    --max-cases 3
```

Outputs:

```
data/synthetic_runtime_compat/
  README.md
  images/                         ← copied synthetic images
  test.csv                        ← id, fs columns
  sample_submission.parquet       ← or sample_submission.csv if parquet unavailable
  synthetic_runtime_input_manifest.json
  ground_truth_waveforms/
  metadata/
```

If parquet support is unavailable, a CSV fallback is generated and the smoke
test will be skipped with `SKIPPED_INPUT_CONTRACT_UNAVAILABLE`.

---

## Step 4 — Run Optional Smoke Test

Attempt a limited full-runtime execution on the synthetic fixture.
The tool checks asset readiness first and skips safely if anything is missing.

```bash
python tools/pipeline_compat/run_synthetic_pipeline_smoke.py \
    --synthetic-root benchmark_cases/seed \
    --fixture-root data/synthetic_runtime_compat \
    --config configs/runtime.default.yaml \
    --report reports/pipeline_compat/synthetic_pipeline_smoke_report.md \
    --summary-json reports/pipeline_compat/synthetic_pipeline_compat_summary.json
```

Possible statuses:

| Status | Meaning |
|--------|---------|
| `SKIPPED_ASSETS_MISSING` | Model checkpoints or data files absent |
| `SKIPPED_INPUT_CONTRACT_UNAVAILABLE` | Parquet unavailable or fixture incomplete |
| `RUNTIME_EXECUTED_VALIDATION_PASSED` | Runtime ran and produced valid submission |
| `RUNTIME_EXECUTED_VALIDATION_FAILED` | Runtime ran but submission invalid |
| `RUNTIME_EXECUTION_FAILED` | Runtime crashed; may be expected for synthetic inputs |

Always exits 0. Check the Markdown report and summary JSON for details.

---

## Step 5 — Convert Submission If Possible

If the smoke test produced `results/submission.csv`, convert it to per-lead
waveform CSVs for synthetic scoring.

```bash
python tools/pipeline_compat/convert_submission_to_waveforms.py \
    --submission results/submission.csv \
    --manifest data/synthetic_runtime_compat/synthetic_runtime_input_manifest.json \
    --output-dir reports/pipeline_compat/predicted_waveforms \
    --report reports/pipeline_compat/submission_conversion_report.md
```

If the submission file does not exist or IDs cannot be parsed, the tool
skips and reports why. It never fabricates lead waveforms.

---

## Step 6 — Score Synthetic-Only If Possible

If predicted waveforms were produced, score them against synthetic ground truth.

```bash
python tools/synthetic_benchmark/score_synthetic.py \
    --predicted reports/pipeline_compat/predicted_waveforms \
    --ground-truth benchmark_cases/seed/waveforms \
    --manifest benchmark_cases/seed/synthetic_manifest.json \
    --output reports/synthetic_score.json
```

Scores are on synthetic waveforms only. They do not represent real ECG
reconstruction accuracy.

---

## Step 7 — Generate QC and Consolidated Report

Run the quality check on any predicted waveforms:

```bash
python tools/quality/generate_quality_report.py \
    --waveform-dir reports/pipeline_compat/predicted_waveforms \
    --output reports/quality_report.md
```

Generate the consolidated compatibility report:

```bash
python tools/pipeline_compat/generate_pipeline_compat_report.py \
    --asset-readiness reports/pipeline_compat/asset_readiness_report.json \
    --fixture-manifest data/synthetic_runtime_compat/synthetic_runtime_input_manifest.json \
    --smoke-summary reports/pipeline_compat/synthetic_pipeline_compat_summary.json \
    --output reports/pipeline_compat/PIPELINE_COMPATIBILITY_REPORT.md
```

---

## Step 8 — Decide Whether to Merge

Before merging to main, confirm:

- [ ] `python -m ruff check .` passes with no errors.
- [ ] `python -m pytest` passes all tests.
- [ ] Asset readiness report accurately reflects the current state.
- [ ] No forbidden phrases appear in any committed report.
- [ ] No synthetic outputs are committed that could be mistaken for real data.
- [ ] All committed report files are clearly labeled `SYNTHETIC_COMPATIBILITY_ONLY`.

Do not merge if the smoke test `RUNTIME_EXECUTION_FAILED` — investigate first.
Do not merge if tests fail.

---

## Troubleshooting

**`can_run_full_pipeline: false`**
→ Check which assets are missing. Model checkpoints must be present in `models/`.

**`SKIPPED_INPUT_CONTRACT_UNAVAILABLE`**
→ Install pyarrow: `pip install pyarrow` then re-run Step 3.

**`RUNTIME_EXECUTION_FAILED`**
→ Check `stderr_summary` in the smoke summary JSON. May be expected for synthetic inputs.

**`ModuleNotFoundError: ecg_digitizer`**
→ Run `pip install -e .` from the repository root.

**Parquet write fails silently**
→ Confirm both `pandas` and `pyarrow` are installed.

---

> **Disclaimer:** This runbook covers synthetic compatibility and engineering
> smoke testing only. No clinical validation, diagnostic performance evaluation,
> or real ECG accuracy claim is made or implied.
> All synthetic outputs are labeled `SYNTHETIC_COMPATIBILITY_ONLY`.
