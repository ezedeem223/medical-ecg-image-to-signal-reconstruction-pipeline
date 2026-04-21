from __future__ import annotations

import pytest

from ecg_digitizer import load_config
from ecg_digitizer.models.registry import load_model_registry
from ecg_digitizer.models.selector import build_model_selection
from ecg_digitizer.runtime.bootstrap import validate_environment


def test_model_registry_and_selection(repo_fixture) -> None:
    config = load_config(repo_fixture["config"])
    registry = load_model_registry(config.paths.models_registry, project_root=config.paths.project_root)
    selection = build_model_selection(config, registry)

    assert selection.detector.model_id == "yolo_best"
    assert selection.primary_segmenter.model_id == "effb3_primary"
    assert selection.fallback_segmenter.model_id == "phase10_fallback"
    assert selection.primary_segmenter.path.name == "best_model_effb3_phase9_ddp (2).pth"


def test_validate_environment_allows_explicit_failover(repo_fixture) -> None:
    config = load_config(repo_fixture["config"])
    registry = load_model_registry(config.paths.models_registry, project_root=config.paths.project_root)
    selection = build_model_selection(config, registry)

    selection.primary_segmenter.path.unlink()
    validate_environment(config, selection)


def test_validate_environment_fails_without_available_checkpoints(repo_fixture) -> None:
    config = load_config(repo_fixture["config"])
    registry = load_model_registry(config.paths.models_registry, project_root=config.paths.project_root)
    selection = build_model_selection(config, registry)

    selection.primary_segmenter.path.unlink()
    selection.fallback_segmenter.path.unlink()

    with pytest.raises(FileNotFoundError):
        validate_environment(config, selection)
