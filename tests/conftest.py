from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


@pytest.fixture()
def repo_fixture(tmp_path: Path) -> dict[str, Path]:
    project_root = tmp_path
    (project_root / "configs").mkdir()
    (project_root / "data" / "images").mkdir(parents=True)
    (project_root / "models").mkdir()
    (project_root / "results").mkdir()

    template = pd.DataFrame({"id": ["patientA_0_I", "patientA_1_I", "patientA_0_II", "patientA_1_II"]})
    template_path = project_root / "data" / "sample_submission.csv"
    template.to_csv(template_path, index=False)

    test_csv = pd.DataFrame({"id": ["patientA"], "fs": [500]})
    test_csv_path = project_root / "data" / "test.csv"
    test_csv.to_csv(test_csv_path, index=False)

    for filename in ("best.pt", "best_model_effb3_phase9_ddp (2).pth", "best_model_phase10.pth"):
        (project_root / "models" / filename).write_bytes(b"placeholder")

    models_yaml = """models:
  yolo_best:
    kind: yolo
    role: detector
    filename: best.pt
  effb3_primary:
    kind: smp_unet
    role: segmentation
    filename: best_model_effb3_phase9_ddp (2).pth
    encoder_name: efficientnet-b3
    decoder_attention_type: scse
  phase10_fallback:
    kind: smp_unet
    role: segmentation
    filename: best_model_phase10.pth
    encoder_name: resnet50
    decoder_attention_type: scse
"""
    models_registry = project_root / "configs" / "models.yaml"
    models_registry.write_text(models_yaml, encoding="utf-8")

    config_yaml = """paths:
  project_root: ..
  data_root: data
  image_root: data/images
  test_csv: data/test.csv
  sample_submission: data/sample_submission.csv
  output_submission: results/submission.csv
  models_registry: configs/models.yaml

models:
  detector_id: yolo_best
  primary_segmentation_id: effb3_primary
  fallback_segmentation_id: phase10_fallback
  allow_primary_failover: true
  use_fallback_assist: true

runtime:
  device: cpu
  tta_scales: [1.0]
  image_extensions: [".png", ".jpg"]

output:
  submission_path: results/submission.csv
  overwrite: true
  float_format: "%.4f"
"""
    config_path = project_root / "configs" / "runtime.test.yaml"
    config_path.write_text(config_yaml, encoding="utf-8")

    return {
        "project_root": project_root,
        "config": config_path,
        "template": template_path,
        "test_csv": test_csv_path,
        "models_registry": models_registry,
        "image_root": project_root / "data" / "images",
        "output": project_root / "results" / "submission.csv",
    }
