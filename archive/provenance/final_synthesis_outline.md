# Phase 2 Synthesis Seed

This file is a scaffold for Phase 2 synthesis only. It is not the final narrative and should not be treated as a completed cross-notebook analysis.

## Project Timeline Headings

- Early monolithic exploration: main notebook.
- Compact proof-of-concept consolidation: notebook (1).
- Synthetic-to-real staged research pipeline: notebooks (2) through (6).
- Architecture hardening and combat-detector era: notebooks (7) through (9).
- Compact deployment and robustness iteration: notebooks (10) through (41).
- Ensemble and competitor checkpoint branch: notebook (42) and its compact descendants (43) through (48).
- EfficientNet-B3 integration and modular finalization: notebooks (49) through (56).

## Renderer Evolution

- Track how the renderer moves from synthetic data generation into a persistent qualitative debugging surface in compact deployment notebooks.
- Record when the renderer stops being a training dependency and becomes primarily an interpretation and quality-control tool.

## Model Evolution

- Baseline synthetic segmentation branch.
- Real-data and pseudo-label fine-tuning branch.
- Phase-7 and phase-8 architecture and optimization experiments.
- Phase-10 dominant checkpoint reuse.
- EfficientNet-B3 and DeepLabV3+ competitor branch from notebook (42).
- EfficientNet-B3 deployment integration in notebooks (49) through (56).

## Inference Evolution

- Viterbi and dynamic-programming signal extraction prototypes.
- Geometry and calibration-aware reconstruction.
- YOLO-assisted lead localization.
- Compact no-internet deployment shells.
- Ensemble and checkpoint-routing inference variants.
- Modular final execution flow in notebook (56).

## Checkpoint Map

- Primary cross-reference: [file-audit/checkpoint-companion-summary.md](file-audit/checkpoint-companion-summary.md)
- Confirm which checkpoints are bundled artifacts versus notebook-only references before writing Phase 2 lineage claims.

## Terminology Glossary Seed

| Term | Working definition for synthesis |
| --- | --- |
| notebook | One saved `.ipynb` revision in the ordered development chain. |
| revision | A notebook that changes the immediately prior workflow in the sequence. |
| phase | The project-local stage label used in checkpoint or cell naming, such as phase 2, phase 7, phase 8, phase 9, or phase 10. |
| experiment | A bounded branch of notebook work that tests a new model, loss, calibration strategy, or inference policy. |
| checkpoint | A saved `.pt` or `.pth` artifact used for detector or segmentation reuse. |
| renderer | The code path that rasterizes synthetic ECG signals or provides visual debugging views of masks and recovered traces. |
| teacher | A model or prior pipeline whose outputs are used to guide another stage, often through pseudo-label generation. |
| student | The model trained or fine-tuned using synthetic labels, pseudo-labels, or inherited checkpoint knowledge. |
| pseudo-labeling | Generating approximate supervision from existing models or heuristic pipelines on real images. |
| lead detector | The YOLO-based localization model that finds ECG lead regions on a page before segmentation. |
| segmentation | Predicting a foreground trace mask from an ECG crop or lead image. |
| trace extraction | Turning a predicted mask or probability map into a one-dimensional ECG waveform. |
| post-processing | Any path-cleaning, smoothing, gating, calibration, or formatting step applied after raw model output. |
| calibration | Estimating paper grid spacing, scale, and orientation so extracted signals can be mapped back to plausible physical units. |
| inference pipeline | The end-to-end chain that loads inputs, localizes leads, segments traces, extracts waveforms, and writes submission output. |

## Phase 2 Preparation Notes

- Use notebook-level open questions and confidence levels as synthesis risk markers instead of assuming every revision is equally certain.
- Treat the structural sections in the audit reports as observed facts and the manual interpretation sections as higher-level inference.
- Reconcile checkpoint lineage with the companion summary before writing any final timeline claims.
