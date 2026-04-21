from __future__ import annotations

from pathlib import Path

from ecg_digitizer import load_config


def test_load_config_resolves_project_paths(repo_fixture, monkeypatch) -> None:
    override_root = repo_fixture["project_root"] / "data_override"
    override_output = repo_fixture["project_root"] / "results" / "override.csv"
    monkeypatch.setenv("ECG_DIGITIZER_DATA_ROOT", str(override_root))
    monkeypatch.setenv("ECG_DIGITIZER_OUTPUT", str(override_output))

    config = load_config(repo_fixture["config"])

    assert config.paths.project_root == repo_fixture["project_root"]
    assert config.paths.data_root == override_root
    assert config.paths.models_registry == repo_fixture["models_registry"]
    assert config.output.submission_path == override_output
    assert config.metadata["performance_anchor_version"] == "50"
    assert config.metadata["secondary_performance_reference"] == "46"


def test_load_config_accepts_string_path(repo_fixture) -> None:
    config = load_config(str(repo_fixture["config"]))
    assert config.config_path == Path(repo_fixture["config"]).resolve()
