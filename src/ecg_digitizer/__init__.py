from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from ecg_digitizer.config import load_config as _load_config

if TYPE_CHECKING:
    from pathlib import Path as PathLikePath

    from ecg_digitizer.config.schema import AppConfig

__all__ = ["load_config", "run_inference", "validate_submission", "PACKAGE_ROOT"]

PACKAGE_ROOT = Path(__file__).resolve().parent


def load_config(path: str | "PathLikePath") -> "AppConfig":
    return _load_config(path)


def run_inference(config, **kwargs):
    from ecg_digitizer.runtime import run_inference as _run_inference

    return _run_inference(config, **kwargs)


def validate_submission(config, submission_path=None):
    from ecg_digitizer.validation import validate_submission as _validate_submission

    return _validate_submission(config, submission_path)
