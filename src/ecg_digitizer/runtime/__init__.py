from __future__ import annotations

from typing import Any

__all__ = ["run_inference"]


def __getattr__(name: str) -> Any:
    if name == "run_inference":
        from ecg_digitizer.runtime.pipeline import run_inference

        return run_inference
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
