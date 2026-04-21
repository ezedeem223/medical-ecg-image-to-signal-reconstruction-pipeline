# Final Runtime Scope

## Core runtime

- YOLO detection via `best.pt`.
- EffB3 segmentation as the primary path.
- Phase-10 segmentation as the explicit fallback path.
- Checkpoint selector, calibration, trace extraction, timing normalization, and submission validation/export.
- Config-driven bootstrap and deterministic path resolution.

## Optional research/debug module

- Synthetic renderer as a debug/inspection tool.
- Visual diagnostics, coverage checks, and notebook-style sanity plots.
- Model comparison helpers and controlled fallback benchmarking.

## Archive only

- Full ensemble execution logic from notebook (42) and its compact packaging branch.
- Temporary competitor bootstrap checkpoints such as `temp_deeplab_base.pt` and `temp_effnet_base.pt`.
- Historical environment-repair retries that existed only to keep Kaggle notebooks alive.

## Subsystem callouts

- YOLO detection: `core runtime`
- EffB3 segmentation: `core runtime`
- Phase-10 segmentation fallback: `core runtime`
- Notebook (42) ensemble logic: `archive only` by default
- Renderer: `optional research/debug`
- Diagnostics: `optional research/debug`
- Bootstrap/environment logic: `core runtime`, but rewritten in modular form
- Training-only artifacts: `archive only` or `optional research`
- Temporary competitor checkpoints: `archive only`
- Validation/export logic: `core runtime`
