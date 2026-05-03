# Asset Readiness Report

**Checked at:** 2026-05-03T05:45:51.441682+00:00
**Repository root:** `/home/runner/workspace`

**Can run full pipeline:** ❌ NO

## Skip Reasons

- Missing directory: data/images (input ECG page images)
- Missing file: data/test.csv (test manifest (id column, optional fs column))
- Missing file: data/sample_submission.parquet (submission template (id column, expected row order))

## Asset Inventory

| Asset | Kind | Exists | Size / Files | Role |
|-------|------|--------|--------------|------|
| `configs/runtime.default.yaml` | file | ✅ | 963 bytes | runtime configuration |
| `configs/models.yaml` | file | ✅ | 412 bytes | model registry (checkpoint paths and roles) |
| `models/best.pt` | file | ✅ | 136,715,059 bytes | YOLO lead detector checkpoint |
| `models/best_model_effb3_phase9_ddp (2).pth` | file | ✅ | 53,454,686 bytes | primary EfficientNet-B3 segmentation checkpoint |
| `models/best_model_phase10.pth` | file | ✅ | 135,647,702 bytes | fallback ResNet50 segmentation checkpoint |
| `data/images` | directory | ❌ | — | input ECG page images |
| `data/test.csv` | file | ❌ | — | test manifest (id column, optional fs column) |
| `data/sample_submission.parquet` | file | ❌ | — | submission template (id column, expected row order) |

---

> **Disclaimer:** This report only checks engineering readiness for running the existing pipeline. It does not validate ECG reconstruction performance, clinical utility, or diagnostic correctness.
