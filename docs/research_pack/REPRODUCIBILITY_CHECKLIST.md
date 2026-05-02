# Reproducibility Checklist

**Purpose:** Step-by-step guide to reproduce all research workbench outputs
from a clean clone of this repository.

**Branch:** `agent-lab/ecg-research-workbench-seed`
**Scope:** Synthetic benchmark, scoring, QC reports, and research documentation.
           Full pipeline inference requires additional assets (see Section 6).

---

## 1. Environment

### 1.1 Python Version
```
Python >= 3.11
```

### 1.2 Install Core Dependencies
```bash
pip install -e .
pip install -r requirements.txt
```

### 1.3 Install Dev Dependencies (for tests and linting)
```bash
pip install -r requirements-dev.txt
```

### 1.4 Verify Installation
```bash
python -c "import numpy, pandas, yaml; print('Core deps OK')"
ecg-digitizer --help
```

Expected: help text for `ecg-digitizer run` and `ecg-digitizer validate`.

### 1.5 Optional Dependencies for Image Rendering
The synthetic benchmark renderer uses `matplotlib` for ECG-paper-style output.
If matplotlib is unavailable, a fallback NumPy-based renderer is used (reduced
visual quality). To enable full rendering:

```bash
pip install matplotlib
pip install Pillow  # optional, improves PNG export
```

---

## 2. Configs

### 2.1 Runtime Config
Default config: `configs/runtime.default.yaml`

Review and adjust paths if your data root differs:
```yaml
paths:
  project_root: ..
  data_root: data
  image_root: data/images
  test_csv: data/test.csv
  sample_submission: data/sample_submission.parquet
  models_registry: configs/models.yaml
```

### 2.2 Model Registry
`configs/models.yaml` defines the three required checkpoints:
- `yolo_best` — `models/best.pt`
- `effb3_primary` — `models/best_model_effb3_phase9_ddp (2).pth`
- `phase10_fallback` — `models/best_model_phase10.pth`

---

## 3. Checkpoints

The repository tracks three model checkpoints under `models/`:

| File | Role | Required for |
|------|------|-------------|
| `best.pt` | YOLO lead detector | Full pipeline inference only |
| `best_model_effb3_phase9_ddp (2).pth` | Primary segmenter | Full pipeline inference only |
| `best_model_phase10.pth` | Fallback segmenter | Full pipeline inference only |

**The synthetic benchmark, scoring utility, and QC tools do NOT require these
checkpoints.**

---

## 4. Synthetic Benchmark Generation

```bash
python tools/synthetic_benchmark/generate_cases.py \
    --output benchmark_cases/seed \
    --num-cases 5 \
    --seed 42
```

**Expected outputs:**
```
benchmark_cases/seed/
├── README.md
├── synthetic_manifest.json
├── images/
│   ├── case_000_clean.png
│   ├── case_000_blur.png
│   ├── case_000_noise.png
│   ├── case_000_low_contrast.png
│   ├── case_000_rotation.png
│   ├── case_000_cropped.png
│   └── case_001_*.png  ...
├── waveforms/
│   ├── case_000.csv
│   └── case_001.csv  ...
└── metadata/
    ├── case_000.json
    └── case_001.json  ...
```

**Verify:** `benchmark_cases/seed/synthetic_manifest.json` must contain
`"synthetic": true` and `"num_cases": 5`.

---

## 5. Scoring

Score a prediction against the generated ground truth:

```bash
python tools/synthetic_benchmark/score_synthetic.py \
    --ground-truth benchmark_cases/seed/waveforms/case_000.csv \
    --prediction benchmark_cases/seed/waveforms/case_000.csv \
    --output reports/synthetic_score_selftest.json
```

**Self-test mode:** Scoring a file against itself produces MAE=0, RMSE=0.
This confirms the scoring tool is working correctly.

**Expected output fields in `reports/synthetic_score_selftest.json`:**
```json
{
  "synthetic": true,
  "aggregate": { "mean_mae": 0.0, "mean_rmse": 0.0, "num_leads_scored": 12 },
  ...
}
```

---

## 6. QC Reports

```bash
python tools/quality/generate_quality_report.py \
    --input benchmark_cases/seed/waveforms/case_000.csv \
    --output reports/quality_report.md
```

**Expected result:** `reports/quality_report.md` with overall status `OK`.

---

## 7. Tests

```bash
python -m pytest tests/ -v
```

**Targeted new tests (no model weights or real data required):**
```bash
python -m pytest tests/test_synthetic_benchmark.py \
                 tests/test_synthetic_scoring.py \
                 tests/test_quality_checks.py \
                 tests/test_research_pack_exists.py -v
```

**Expected:** All new tests pass. Existing project tests (13 original) should
also continue to pass.

---

## 8. Linting

```bash
python -m ruff check .
```

**Expected:** No errors. Warnings from archive/ directory are excluded per
`pyproject.toml` configuration.

---

## 9. Expected Outputs Summary

| Output | Path | Requires weights? |
|--------|------|-------------------|
| Synthetic cases (5) | `benchmark_cases/seed/` | No |
| Synthetic manifest | `benchmark_cases/seed/synthetic_manifest.json` | No |
| Scoring report | `reports/synthetic_score.json` | No |
| QC report | `reports/quality_report.md` | No |
| Full pipeline submission | `results/submission.csv` | Yes |

---

## 10. Limitations

- Synthetic benchmark outputs are fully reproducible given a fixed `--seed`.
  Changing the seed produces different waveforms.

- Full pipeline inference (`ecg-digitizer run`) additionally requires:
  - Real ECG images in `data/images/`
  - `data/test.csv` and `data/sample_submission.parquet`
  - All three model checkpoint files (correct versions, not placeholders)

- The QC report interprets amplitude in signal units. If pipeline output
  is in a different unit convention, amplitude range thresholds may need
  adjustment.

- Image rendering quality depends on whether matplotlib is installed.
  Without matplotlib, a minimal fallback renderer is used.
