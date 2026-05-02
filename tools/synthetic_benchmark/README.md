# Synthetic ECG Benchmark Seed

This directory contains tools to generate and evaluate a small synthetic ECG-like benchmark
dataset. All cases are **parametric and clearly labeled synthetic** — no real ECG data is
used or required.

## Purpose

The synthetic benchmark provides a controlled test bed for:
- Verifying that waveform extraction tools produce structured output
- Measuring reconstruction fidelity on known ground-truth signals
- Exploring how distortions (blur, noise, rotation, contrast) degrade pipeline outputs
- Establishing a reproducible baseline for future research iterations

## What It Is Not

- Not a clinical validation dataset
- Not a substitute for real ECG evaluation
- Not derived from PhysioNet, PTB-XL, or any patient data
- Not intended to support diagnostic claims

## Files

| File | Purpose |
|------|---------|
| `generate_cases.py` | Parametric waveform generation + image rendering + metadata |
| `render_ecg.py` | ECG-paper-style image renderer |
| `distortions.py` | Controlled image distortion functions |
| `metadata.py` | Per-case metadata JSON builder |
| `score_synthetic.py` | Waveform fidelity scoring (MAE, RMSE, SNR-proxy) |

## Quick Start

```bash
# Generate 5 synthetic cases (default)
python tools/synthetic_benchmark/generate_cases.py \
    --output benchmark_cases/seed \
    --num-cases 5

# Score a prediction against ground truth
python tools/synthetic_benchmark/score_synthetic.py \
    --ground-truth benchmark_cases/seed/waveforms/case_000.csv \
    --prediction path/to/prediction.csv \
    --output reports/synthetic_score.json
```

## Output Layout

```
benchmark_cases/seed/
├── README.md
├── synthetic_manifest.json
├── images/
│   ├── case_000_clean.png
│   ├── case_000_blur.png
│   └── ...
├── waveforms/
│   └── case_000.csv   (12-lead ground-truth, shape: 12 x T)
└── metadata/
    └── case_000.json
```

## Distortion Variants

Each case is rendered under multiple distortion conditions:

| Variant | Description |
|---------|-------------|
| `clean` | No distortion |
| `blur` | Gaussian blur |
| `noise` | Additive Gaussian noise |
| `low_contrast` | Reduced contrast + brightness offset |
| `rotation` | Small random rotation |
| `cropped` | Random margin crop |
