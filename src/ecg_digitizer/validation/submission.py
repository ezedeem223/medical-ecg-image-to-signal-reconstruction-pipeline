from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from ecg_digitizer.config.schema import AppConfig
from ecg_digitizer.io import load_template_ids


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    row_count: int
    submission_path: Path


def validate_submission(config: AppConfig, submission_path: Path | None = None) -> ValidationResult:
    path = Path(submission_path or config.output.submission_path)
    if not path.exists():
        raise FileNotFoundError(f"Submission file not found: {path}")

    template_ids = np.array(load_template_ids(config.paths.sample_submission))
    submission = pd.read_csv(path)

    if list(submission.columns) != ["id", "value"]:
        raise AssertionError(f"Columns mismatch: {list(submission.columns)}")
    if len(submission) != len(template_ids):
        raise AssertionError(f"Row count mismatch: {len(submission)} != {len(template_ids)}")
    if submission["id"].isna().any():
        raise AssertionError("Found NaN in id column.")
    if submission["value"].isna().any():
        raise AssertionError("Found NaN in value column.")

    values = pd.to_numeric(submission["value"], errors="coerce").to_numpy()
    if not np.isfinite(values).all():
        raise AssertionError("Found non-finite values in submission.")

    submission_ids = submission["id"].astype(str).to_numpy()
    if not np.array_equal(submission_ids, template_ids):
        raise AssertionError("Submission IDs do not match the template order exactly.")

    return ValidationResult(valid=True, row_count=len(submission), submission_path=path)
