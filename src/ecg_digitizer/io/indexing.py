from __future__ import annotations

from pathlib import Path

import pandas as pd

LEAD_NAMES = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]
LEAD_TO_IDX = {name: index for index, name in enumerate(LEAD_NAMES)}


def clean_pid(pid: str) -> str:
    value = str(pid).strip()
    return value[:-2] if value.endswith(".0") else value


def normalize_lead_name(name: str) -> str:
    value = str(name).strip()
    value = value.replace("Lead", "").replace("lead", "")
    value = value.replace("_", "").replace("-", "").replace(" ", "")
    value = value.replace("AVR", "aVR").replace("AVL", "aVL").replace("AVF", "aVF")
    value = value.replace("AVr", "aVR").replace("AVl", "aVL").replace("AVf", "aVF")
    return value


def parse_template_id(record_id: str) -> tuple[str | None, int | None, str | None]:
    parts = str(record_id).split("_")
    if len(parts) < 3:
        return None, None, None

    lead = normalize_lead_name(parts[-1])
    if lead in LEAD_TO_IDX:
        try:
            return clean_pid("_".join(parts[:-2])), int(parts[-2]), lead
        except ValueError:
            pass

    lead = normalize_lead_name(parts[-2])
    if lead in LEAD_TO_IDX:
        try:
            return clean_pid("_".join(parts[:-2])), int(parts[-1]), lead
        except ValueError:
            pass

    found_lead: str | None = None
    found_index: int | None = None
    for idx in range(len(parts) - 1, -1, -1):
        candidate = normalize_lead_name(parts[idx])
        if candidate in LEAD_TO_IDX:
            found_lead = candidate
            found_index = idx
            break
    if found_lead is None or found_index is None:
        return None, None, None

    for idx in (found_index - 1, found_index + 1):
        if 0 <= idx < len(parts):
            try:
                point_index = int(parts[idx])
            except ValueError:
                continue
            pid = "_".join(parts[pos] for pos in range(len(parts)) if pos not in (found_index, idx))
            return clean_pid(pid), point_index, found_lead

    return None, None, None


def load_template_ids(path: Path) -> list[str]:
    if path.suffix.lower() == ".parquet":
        frame = pd.read_parquet(path, columns=["id"])
    else:
        frame = pd.read_csv(path, usecols=["id"])
    return frame["id"].astype(str).tolist()


def infer_patient_lengths(template_ids: list[str]) -> dict[str, int]:
    lengths: dict[str, int] = {}
    for record_id in template_ids:
        pid, point_index, _lead = parse_template_id(record_id)
        if pid is None or point_index is None:
            continue
        lengths[pid] = max(lengths.get(pid, 0), point_index + 1)
    return lengths


def build_image_index(image_root: Path, extensions: tuple[str, ...]) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for file_path in image_root.rglob("*"):
        if not file_path.is_file():
            continue
        if file_path.suffix.lower() not in {ext.lower() for ext in extensions}:
            continue
        index.setdefault(file_path.stem, file_path)
    return index


def resolve_image_path(patient_id: str, image_index: dict[str, Path]) -> Path | None:
    pid = clean_pid(patient_id)
    if pid in image_index:
        return image_index[pid]
    try:
        as_int = str(int(float(pid)))
    except ValueError:
        return None
    return image_index.get(as_int)


def load_fs_map(test_csv: Path | None) -> dict[str, float]:
    if test_csv is None or not test_csv.exists():
        return {}
    frame = pd.read_csv(test_csv, dtype=str)
    columns_lower = {column.lower(): column for column in frame.columns}
    id_column = columns_lower.get("id") or next((value for key, value in columns_lower.items() if "id" in key), None)
    fs_column = columns_lower.get("fs") or next((value for key, value in columns_lower.items() if "fs" in key), None)
    if id_column is None or fs_column is None:
        return {}
    return {
        clean_pid(record_id): float(fs)
        for record_id, fs in zip(frame[id_column].astype(str), frame[fs_column].astype(str))
        if str(fs).strip()
    }
