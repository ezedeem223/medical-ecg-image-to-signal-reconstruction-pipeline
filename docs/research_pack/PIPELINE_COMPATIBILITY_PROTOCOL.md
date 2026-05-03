# ECG Pipeline Compatibility Protocol

**Label:** `SYNTHETIC_COMPATIBILITY_ONLY`
**Status:** Engineering reference — not a clinical protocol.

---

## Purpose

This document defines the protocol for testing whether the existing
ECG image-to-signal runtime pipeline can accept synthetic benchmark
fixtures, which assets are required, what skip semantics apply when
assets are absent, and what claims are permitted and forbidden.

This is an engineering compatibility and research tooling pass.
It is not clinical validation, diagnostic evaluation, or model benchmarking
against published real-world ECG datasets.

---

## What Synthetic Compatibility Testing Can Check

- Whether required config files, model checkpoints, and data directories exist.
- Whether the synthetic fixture directory structure conforms to the runtime input contract.
- Whether the runtime pipeline can be invoked without crashing on synthetic inputs.
- Whether a submission CSV is produced when the runtime executes.
- Whether submission IDs can be mapped back to per-lead waveform CSVs.
- Whether synthetic scoring can be computed between predicted and ground-truth waveforms.
- Whether engineering QC checks pass on predicted waveform CSVs.

---

## What Synthetic Compatibility Testing Cannot Check

- Real ECG reconstruction accuracy.
- Clinical diagnostic performance.
- Generalisation to real patient populations.
- Model robustness to acquisition conditions not represented in synthetic data.
- Compliance with FDA, CE, or any other regulatory framework.
- Comparison with published ECG digitization benchmarks.
- Ground-truth fidelity of the YOLO detector on real paper ECG images.
- Lead segmentation accuracy on real printed ECG grids.

---

## Required Assets for Full Pipeline Execution

| Asset | Kind | Role |
|-------|------|------|
| `configs/runtime.default.yaml` | file | Runtime configuration |
| `configs/models.yaml` | file | Model registry (checkpoint paths and roles) |
| `models/best.pt` | file | YOLO lead detector checkpoint |
| `models/best_model_effb3_phase9_ddp (2).pth` | file | Primary EfficientNet-B3 segmentation checkpoint |
| `models/best_model_phase10.pth` | file | Fallback ResNet50 segmentation checkpoint |
| `data/images/` | directory | Input ECG page images |
| `data/test.csv` | file | Test manifest (`id`, optional `fs` columns) |
| `data/sample_submission.parquet` | file | Submission template (`id` column, expected row order) |

If any of these assets is absent, `can_run_full_pipeline` is set to `false` and
all reasons are listed explicitly in the asset readiness report.

---

## Required Input Contract

The runtime submission template (`sample_submission.parquet`) must contain one row
per expected output signal sample, with IDs in the format:

```
{patient_id}_{point_index}_{lead_name}
```

For synthetic fixtures the patient ID corresponds to the case ID (e.g. `case_000`).

The synthetic adapter generates submission IDs in this format but limits
`point_index` to a configurable number of samples (default: 100) to keep
fixture size manageable. Real competition submissions use the full signal length.

---

## Skip Semantics

When required assets are absent:

1. The smoke test **does not attempt** pipeline execution.
2. A report is written with status `SKIPPED_ASSETS_MISSING`.
3. All missing files are listed explicitly.
4. The tool exits with code 0 — skip is not an error.

When the input contract cannot be met (e.g. parquet unavailable):

1. Status is set to `SKIPPED_INPUT_CONTRACT_UNAVAILABLE`.
2. The exact reason (missing dependency, format mismatch) is recorded.
3. The tool exits with code 0.

When assets are present but runtime execution fails:

1. Status is set to `RUNTIME_EXECUTION_FAILED`.
2. stdout and stderr summaries are recorded.
3. This may be expected for synthetic inputs due to domain mismatch.
4. It does not indicate a bug in the pipeline itself.

---

## Why Missing Assets Are Reported Rather Than Hidden

The compatibility layer is designed for transparent engineering review.
Hiding missing assets would create a false impression of readiness.
Explicit reporting allows:

- Identifying exactly what must be provided before real execution.
- Separating engineering completeness from model availability.
- Ensuring portfolio reviewers understand the actual runtime state.

---

## Distinction Between Test Modes

| Mode | What It Does | What It Proves |
|------|-------------|----------------|
| Generation-only benchmark | Generates synthetic ECG waveforms and images | That the generator works deterministically |
| Pipeline smoke test | Runs the full runtime on synthetic fixtures | That the runtime can be invoked; not that output is accurate |
| Synthetic scoring | Computes MAE/RMSE between synthetic ground truth and predictions | That the scoring utility works; scores are on synthetic data only |
| Engineering QC | Checks waveform CSVs for structural validity | That output format conforms to the expected schema |
| Real ECG validation | Runs on real patient ECG recordings | Would establish actual reconstruction accuracy |
| Clinical validation | Follows a regulated validation protocol | Would establish diagnostic utility |

This toolset implements only the first four modes.

---

## Allowed Wording

- "Synthetic compatibility testing"
- "Engineering readiness check"
- "Smoke test on synthetic fixtures"
- "SYNTHETIC_COMPATIBILITY_ONLY"
- "Pipeline input contract compatibility"
- "Scores on synthetic benchmark waveforms"

---

## Forbidden Wording

- "Clinical validation"
- "Diagnostic performance"
- "FDA/medical approval" or "CE marking"
- "Real ECG accuracy"
- "Published benchmark performance"
- "Validated on patients"
- "Reconstruction accuracy" (without synthetic qualifier)
- "Performance on competition data"

---

## Case Profiles (Benchmark Expansion Reference)

The synthetic benchmark supports the following named distortion profiles.
All profiles generate parametric waveforms only; they do not represent
real clinical ECG abnormalities.

| Profile | Generator Parameter | Notes |
|---------|--------------------|-|
| normal-like | `hr=75`, low distortion | Baseline normal sinus rate |
| tachycardia-like | `hr > 100` | Elevated synthetic heart rate only |
| bradycardia-like | `hr < 60` | Reduced synthetic heart rate only |
| low amplitude | `amplitude_scale < 0.5` | Reduced signal amplitude |
| baseline wander | `wander_hz`, `wander_amp` | Low-frequency drift |
| grid weakness | `grid_alpha < 0.3` | Faint background grid |
| partial crop | `crop_frac > 0` | Simulated image cropping |
| noise-heavy | `noise_sigma` high | High additive Gaussian noise |
| rotation-heavy | `rotation_deg` high | Image rotation distortion |
| low-contrast | `contrast_scale < 0.5` | Reduced image contrast |

These profiles are documented for future benchmark expansion.
Adding them to the generator must maintain deterministic seeds and must
not destabilise existing tests.
