# Architecture Vs Performance Decision

## Structural anchor

- Selected notebook: version 57 / `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`
- Reason:
  - Notebook (56) is the clearest refactor origin because it separates bootstrap, path resolution, model loading, inference helpers, formatting, validation, and diagnostic cells into a modular late-stage execution flow.
Limitations:
- It depends on runtime path discovery more than a future repository should.
- Its observed notebook run ended in an import exception, so it is not the best direct runtime anchor.

## Performance anchor

- Primary runtime reference: version 50 / `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`
- Secondary runtime reference: version 46 / `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`
- Reason:
  - Version 50 sits on the late EfficientNet-B3 deployment line while still looking like a successful compact Kaggle runner, making it the strongest available runtime anchor that also aligns with the late architectural direction.
  - Version 46 is an earlier score-proven compact runtime reference that keeps the detector plus phase-10 lineage intact and serves as a fallback design check when late EffB3 behavior diverges.

## Shared stable components

- YOLO detector with `best.pt`: Present across the mature compact eras and still referenced by the modular late notebooks.
- Compact offline Kaggle bootstrap shell: Both anchors assume a self-contained runner that can load local wheels and ship `submission.csv`.
- Calibration, trace extraction, and submission formatting core: These remain non-negotiable survivors across the score-proven and structurally mature lineages.
- Explicit schema and submission validation: Late compact notebooks and the modular rewrite both preserve validation as part of runtime correctness.

## Divergent components

### Segmentation default
- Structural anchor view: Late modular notebooks promote EffB3-aware loading and dual-path logic.
- Performance anchor view: Score-proven behavior peaks before the final modular rewrite and still keeps phase-10 as an active companion.
- Adopted decision: Hybrid: EffB3 primary, phase-10 explicit fallback.
### Bootstrap and model path resolution
- Structural anchor view: Generalized discovery and modular helpers.
- Performance anchor view: Compact hard-coded Kaggle paths that were already score-proven.
- Adopted decision: Structural anchor for module design, but with explicit config instead of notebook-style auto-discovery.
### Diagnostics and debug cells
- Structural anchor view: Late notebooks surface diagnostics more clearly.
- Performance anchor view: Best-known score lineages do not require them on the hot path.
- Adopted decision: Keep as opt-in tooling only.
### Ensemble/competitor logic from notebook (42)
- Structural anchor view: Useful provenance but not central to the modular final engine.
- Performance anchor view: No preserved evidence that full ensemble execution beat the compact single-primary runtime line.
- Adopted decision: Research/archive, not core runtime.

## Decision matrix

| Subsystem | Adopted follow rule | Anchor bias | Final planning policy | Scope |
| --- | --- | --- | --- | --- |
| detector | hybrid adoption | shared stable component | Keep the project-specific YOLO detector as a core runtime module, exposed through the structural anchor layout. | core runtime |
| segmentation | hybrid adoption | performance anchor for behavior, structural anchor for loading shape | Use EffB3 as the default runtime segmentation path and preserve the phase-10 branch as an explicit fallback. | core runtime |
| fallback selection | hybrid adoption | hybrid | Replace implicit notebook branching with an explicit selector that can choose primary or fallback checkpoints deterministically. | core runtime |
| calibration | hybrid adoption | performance anchor behavior inside structural modules | Preserve the score-proven calibration behavior while expressing it as a dedicated module. | core runtime |
| extraction | hybrid adoption | performance anchor behavior inside structural modules | Keep Viterbi/adaptive extraction logic as a first-class runtime subsystem. | core runtime |
| filtering | hybrid adoption | performance anchor | Retain only the filtering steps that were clearly part of the score-proven late compact behavior; treat extra signal polishing as optional. | core runtime |
| validation | structural anchor | structural anchor | Promote validation/export into a clean module that always runs before submission emission. | core runtime |
| bootstrap | structural anchor | structural anchor | Use the modular late-lineage bootstrap shape, but freeze model paths and wheel handling behind config rather than ad hoc notebook discovery. | core runtime |
| debug utilities | optional only | structural anchor | Retain renderer, visual diagnostics, and notebook-style checks as tooling outside the default inference path. | optional research/debug |

## Final adopted planning policy

- Evidence:
  - `best.pt` remains active across the mature lineages.
  - `best_model_effb3_phase9_ddp (2).pth` is the late active primary candidate.
  - `best_model_phase10.pth` remains the trusted fallback-active checkpoint.
- Planning inference:
  - Final repository structure should follow the modular late notebook line.
  - Final runtime defaults should follow the best-known scoring compact line.
- Adopted policy:
  - Use a dual-anchor design.
  - Borrow structure from version 57.
  - Borrow runtime-critical behavior from version 50, with version 46 as a secondary score-proven reference.
  - Keep ensemble logic, renderer-heavy exploration, and temporary bootstrap artifacts out of the default runtime.
