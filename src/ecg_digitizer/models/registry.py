from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ModelArtifact:
    model_id: str
    kind: str
    role: str
    path: Path
    encoder_name: str | None = None
    decoder_attention_type: str | None = None


@dataclass(frozen=True)
class ModelRegistry:
    models: dict[str, ModelArtifact]

    def get(self, model_id: str) -> ModelArtifact:
        try:
            return self.models[model_id]
        except KeyError as exc:
            raise KeyError(f"Unknown model id: {model_id}") from exc


def load_model_registry(path: Path, *, project_root: Path) -> ModelRegistry:
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw_models: dict[str, dict[str, Any]] = raw.get("models", {})
    models: dict[str, ModelArtifact] = {}
    for model_id, payload in raw_models.items():
        filename = payload["filename"]
        model_path = Path(filename)
        if not model_path.is_absolute():
            model_path = (project_root / "models" / model_path).resolve()
        models[model_id] = ModelArtifact(
            model_id=model_id,
            kind=str(payload["kind"]),
            role=str(payload["role"]),
            path=model_path,
            encoder_name=payload.get("encoder_name"),
            decoder_attention_type=payload.get("decoder_attention_type"),
        )
    return ModelRegistry(models=models)
