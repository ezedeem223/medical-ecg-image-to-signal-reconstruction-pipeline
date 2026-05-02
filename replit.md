# Medical ECG Image-to-Signal Reconstruction Pipeline

## Project Overview

A production-oriented Python CLI library for converting scanned or photographed 12-lead ECG sheets into structured digital waveforms. This is a pure Python package with no web frontend.

## Architecture

- **Language**: Python 3.11
- **Package manager**: pip (editable install via `pyproject.toml`)
- **Entry point**: `ecg-digitizer` CLI (`src/ecg_digitizer/cli.py`)
- **Test framework**: pytest

## Package Structure

```
src/ecg_digitizer/
  calibration/    - Grid-spacing estimation and amplitude calibration
  config/         - Typed runtime configuration and path resolution
  extraction/     - Viterbi-based trace extraction
  io/             - Image indexing and file utilities
  models/         - Model registry, YOLO detector, segmentation loaders
  postprocessing/ - Filtering, resampling, waveform consistency
  preprocessing/  - Image loading and grid-light suppression
  runtime/        - Inference orchestration and bootstrap validation
  submission_export/ - Deterministic CSV export
  validation/     - Strict submission validation
  cli.py          - CLI entry point
```

## Key Configuration

- Runtime config: `configs/runtime.default.yaml`
- Model registry: `configs/models.yaml`
- Models directory: `models/` (contains `best.pt`, `best_model_effb3_phase9_ddp (2).pth`, `best_model_phase10.pth`)
- Data directory: `data/` (images, test.csv, sample_submission.parquet)
- Output: `results/submission.csv`

## CLI Commands

```bash
# Run ECG digitization inference
ecg-digitizer run --config configs/runtime.default.yaml

# Validate a generated submission
ecg-digitizer validate --config configs/runtime.default.yaml --submission results/submission.csv
```

## Python API

```python
from ecg_digitizer import load_config, run_inference

config = load_config("configs/runtime.default.yaml")
submission_path = run_inference(config)
```

## Environment Variables

- `ECG_DIGITIZER_CONFIG` - Override default config file path
- `ECG_DIGITIZER_DATA_ROOT` - Override data root directory
- `ECG_DIGITIZER_OUTPUT` - Override output submission path

## Installation

```bash
# Runtime install
pip install -e .
pip install -r requirements.txt

# Dev install (includes pytest, ruff)
pip install -e ".[dev]"
```

## Model Policy

- Detector: `models/best.pt` (YOLO)
- Primary segmentation: `models/best_model_effb3_phase9_ddp (2).pth` (EfficientNet-B3 U-Net)
- Fallback segmentation: `models/best_model_phase10.pth` (ResNet50 U-Net)
- Model selection is explicit and config-driven
