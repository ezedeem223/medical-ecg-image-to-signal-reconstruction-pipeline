from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_submission_rows(rows: list[tuple[str, str]], destination: Path, *, overwrite: bool) -> Path:
    if destination.exists() and not overwrite:
        raise FileExistsError(f"Submission already exists and overwrite is disabled: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows, columns=["id", "value"])
    frame.to_csv(destination, index=False)
    return destination
