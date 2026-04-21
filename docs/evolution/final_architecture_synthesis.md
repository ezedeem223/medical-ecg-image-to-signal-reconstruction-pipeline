# Final Architecture Synthesis

This synthesis uses Phase 1 structural facts and Phase 2 curated interpretation. The bullets under **Observed evidence** are factual summaries; the paragraph under **Synthesis** is the project-level inference.

## 1. Project objective

**Observed evidence**
- The notebook family repeatedly targets competition-ready reconstruction from ECG images into long-format submission files.
- From the earliest notebook onward, segmentation output is treated as an intermediate representation that must be converted into 1D waveforms.

**Synthesis**

The project solves ECG image-to-signal reconstruction for the PhysioNet digitization competition. Its stable objective is not generic image segmentation, but recovering calibrated multi-lead waveforms from scanned or rendered ECG pages and writing competition-safe outputs.

## 2. Evolution timeline

**Observed evidence**
- The ordered notebook chain moves from monolithic research, to staged synthetic/real research, to compact deployment, to an ensemble competitor branch, and finally to EffB3 integration plus modular finalization.
- Milestone notebooks include the main notebook, notebook (1), notebook (9), notebook (10), notebook (42), notebook (49), and notebook (56).

**Synthesis**

The project evolved in discrete eras rather than as one smooth line. Each era answers a different question: can segmentation recover traces at all, can the pipeline survive real pages, can it run reliably on Kaggle, does a broader checkpoint family help, and which late-stage path should anchor a future refactor.

## 3. Renderer evolution

**Observed evidence**
- The renderer starts as a synthetic data factory in the earliest notebooks.
- Compact notebooks keep renderer cells even after training disappears, usually as a visual debugging or sanity-check surface.

**Synthesis**

The renderer survives because it does double duty. Early on it manufactures supervision; later it provides an interpretable surface for checking detector crops, predicted masks, and reconstructed traces. A refactor should preserve the renderer as a debug and evaluation utility even if synthetic training becomes a separate submodule.

## 4. Dataset and input evolution

**Observed evidence**
- Synthetic rendered images and masks dominate the earliest notebooks.
- PhysioNet competition files appear early and then remain present through the final modular notebook.
- PTB-XL loading appears explicitly in later research and compact notebooks as a waveform source.

**Synthesis**

The data strategy becomes progressively layered: synthetic data establishes the segmentation thesis, real competition pages expose domain gaps, and PTB-XL acts as a reusable waveform source that keeps the renderer grounded in realistic rhythms. By the end, the operational runtime depends on competition pages plus metadata, while synthetic and PTB-XL assets mainly support training and debugging.

## 5. Model evolution

**Observed evidence**
- Early notebooks train a baseline segmentation branch directly on synthetic assets.
- Notebook (7) upgrades the segmentation architecture and detector hardening together.
- Notebook (9) creates the dominant phase-10 checkpoint, while notebook (42) creates DeepLabV3+ and EfficientNet competitor branches.
- Notebooks (49) through (56) promote the EffB3 branch into active deployment decisions.

**Synthesis**

Model evolution follows a clear pattern: baseline synthetic segmentation, stronger architecture plus detector hardening, phase-10 real-image fine-tuning, competitor expansion, then EffB3-centered deployment. The final likely architecture is not a generic ensemble; it is a detector plus segmentation system where EffB3 appears primary and phase-10 remains a trusted fallback.

## 6. Checkpoint evolution

**Observed evidence**
- Checkpoint names progress from baseline and real-data variants to numbered phase checkpoints, then to competitor-specific names and EffB3 DDP artifacts.
- The companion summary shows `best.pt` and `best_model_phase10` as especially durable lineages, with later EffB3 artifacts becoming increasingly prominent.

**Synthesis**

Checkpoint naming mirrors project maturity. Early checkpoints encode experimentation, phase-10 marks the mature single-model branch, notebook (42) expands the candidate set, and EffB3 artifacts signal the late transition from research comparison to deployment selection.

## 7. Detection and cropping evolution

**Observed evidence**
- Detector preparation appears in early staged research notebooks.
- Notebook (7) makes combat detector training explicit, and compact notebooks thereafter assume a detector-backed lead localization stage.
- Late notebooks keep fallback split logic when YOLO or exact localization is unavailable.

**Synthesis**

Lead detection evolves from an auxiliary branch into a non-negotiable front end. The mature pipeline expects YOLO-backed crops first and only falls back to geometric splitting when the detector or page structure fails.

## 8. Segmentation evolution

**Observed evidence**
- Segmentation is present from the baseline notebook onward.
- The project later distinguishes between the phase-10 ResNet family, DeepLabV3+, and EfficientNet-B3 competitors.

**Synthesis**

Segmentation remains the central waveform-recovery mechanism, but the project learns that model-family choice matters. The final synthesis should treat segmentation as a pluggable stage with at least one primary model and one fallback-capable alternate lineage.

## 9. Trace extraction evolution

**Observed evidence**
- Viterbi-style extraction is already present in the earliest notebook.
- Later notebooks introduce adaptive and quality-gated variants rather than abandoning the DP family.

**Synthesis**

Trace extraction is one of the strongest long-lived technical through-lines. The project never replaces Viterbi-style decoding outright; it progressively wraps it in calibration, adaptive weighting, and fallback logic.

## 10. Calibration and post-processing evolution

**Observed evidence**
- Calibration helpers appear in the earliest notebooks and become more explicit in the geometry-heavy research branch.
- Notebook (9) adds signal-domain cleanup such as high-pass filtering and smarter post-processing.
- Late compact notebooks emphasize deskewing, trimming, gating, and per-lead timing normalization.

**Synthesis**

Post-processing grows from helper code into a major subsystem. The late notebooks show that segmentation alone is not sufficient; calibration, deskewing, gating, and sometimes filtering are necessary to produce competition-safe waveforms.

## 11. Submission pipeline evolution

**Observed evidence**
- Submission writers exist from the earliest notebook.
- Compact notebooks repeatedly refine schema checks, row-count validation, ID formatting, and metadata-driven timing.

**Synthesis**

Submission generation becomes a serious engineering concern rather than a final line of code. By the compact era, the project treats export correctness as a first-class stage that deserves dedicated logic and diagnostics.

## 12. Final likely architecture

**Observed evidence**
- Notebook (56) is the final modular rewrite.
- Notebooks (49) through (56) make EffB3 a first-class deployed checkpoint while preserving the older phase-10 path.
- The final compact notebooks still rely on YOLO detection, calibration-aware decoding, and submission validation.

**Synthesis**

The most likely final architecture is: offline Kaggle bootstrap and path resolution -> competition image indexing and diagnostics -> YOLO lead detection (`best.pt`) with fallback crop splitting -> primary EffB3 segmentation with phase-10 fallback or selector -> calibration, cleanup, and adaptive DP/Viterbi trace extraction -> per-lead timing normalization -> validated submission export. The renderer survives as an optional debug surface, not as the main runtime dependency.

## 13. Remaining ambiguities

**Observed evidence**
- Notebook (42) and its descendants do not make the long-term fate of the full ensemble branch fully explicit.
- Notebook (56) auto-discovers model paths and still includes a debug cell whose operational status is not fully resolved.

**Synthesis**

There are no major blind spots about the broad architecture, but there are still tactical ambiguities around default checkpoint selection, the archival status of the ensemble branch, and whether some diagnostic blocks should survive as operational components.

## 14. Refactor implications

**Observed evidence**
- Notebook (56) already splits the runtime into coherent blocks.
- The compact era stabilizes around detector, segmentation, extraction, formatting, and validation as durable responsibilities.

**Synthesis**

Phase 3 refactor planning should treat the final repository as a composition of durable modules: environment/bootstrap, data indexing, detector, segmentation model registry, geometry and calibration, trace extraction, output formatting, and validation. Archive candidates are duplicate bootstrap retries, isolated benchmark notebooks, and training-only checkpoint initialization details that do not survive into the final runtime.
