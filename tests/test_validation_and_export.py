from __future__ import annotations

import pandas as pd
import pytest

from ecg_digitizer import load_config
from ecg_digitizer.submission_export import write_submission_rows
from ecg_digitizer.validation import validate_submission


def test_write_and_validate_submission(repo_fixture) -> None:
    config = load_config(repo_fixture["config"])
    rows = [
        ("patientA_0_I", "0.0000"),
        ("patientA_1_I", "0.1000"),
        ("patientA_0_II", "0.2000"),
        ("patientA_1_II", "0.3000"),
    ]
    destination = write_submission_rows(rows, repo_fixture["output"], overwrite=True)
    result = validate_submission(config, destination)

    assert result.valid is True
    assert result.row_count == 4


def test_validate_submission_rejects_wrong_order(repo_fixture) -> None:
    config = load_config(repo_fixture["config"])
    frame = pd.DataFrame(
        {
            "id": ["patientA_1_I", "patientA_0_I", "patientA_0_II", "patientA_1_II"],
            "value": [0.1, 0.0, 0.2, 0.3],
        }
    )
    frame.to_csv(repo_fixture["output"], index=False)

    with pytest.raises(AssertionError):
        validate_submission(config, repo_fixture["output"])
