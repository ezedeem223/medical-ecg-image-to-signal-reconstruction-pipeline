from __future__ import annotations

from pathlib import Path

from ecg_digitizer.cli import main
from ecg_digitizer.validation import ValidationResult


def test_cli_run_command(monkeypatch, repo_fixture) -> None:
    monkeypatch.setattr("ecg_digitizer.cli.load_config", lambda path: object())
    monkeypatch.setattr(
        "ecg_digitizer.cli.run_inference",
        lambda config: Path(repo_fixture["project_root"]) / "results" / "submission.csv",
    )

    assert main(["run", "--config", str(repo_fixture["config"])]) == 0


def test_cli_validate_command(monkeypatch, repo_fixture) -> None:
    monkeypatch.setattr("ecg_digitizer.cli.load_config", lambda path: object())
    monkeypatch.setattr(
        "ecg_digitizer.cli.validate_submission",
        lambda config, submission: ValidationResult(True, 4, Path(submission)),
    )

    assert main(["validate", "--config", str(repo_fixture["config"]), "--submission", "out.csv"]) == 0
