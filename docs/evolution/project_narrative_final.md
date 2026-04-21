# Final Project Narrative

This project is a full ECG image-to-signal reconstruction program built through a long notebook lineage. Its goal is to recover calibrated multi-lead waveforms from ECG page images and export them in competition-ready long format.

## Why it matters

The work matters because it tackles the hard boundary between image understanding and signal recovery. It is not enough to segment traces visually; the pipeline must also preserve timing, amplitude, lead ordering, and submission integrity.

## Major breakthroughs

- Turning the original monolithic experiment into a staged synthetic-to-real research pipeline.
- Promoting YOLO lead localization into a durable front-end component.
- Moving from synthetic-only segmentation to phase-10 real-image pseudo-label fine-tuning.
- Hardening the project into compact no-internet Kaggle runners with strong validation and path logic.
- Using notebook (42) to open a competitor branch and then promoting EffB3 into the late deployment mainline.
- Ending with a modular final notebook that exposes the future repository boundaries directly.

## Mature pipeline direction

The mature direction is a detector-plus-segmentation inference pipeline with strong calibration, adaptive extraction, timing normalization, and schema validation. EfficientNet-B3 appears to be the late preferred segmentation branch, while the phase-10 model remains the clearest fallback lineage.

## Preserve in the final repository

- YOLO lead detector integration and fallback cropping logic.
- Phase-10 and EffB3 checkpoint integration with explicit model-selection behavior.
- Calibration, geometry repair, and adaptive DP/Viterbi extraction.
- Submission formatting, validation, and diagnostics.
- Renderer-backed debugging utilities.
- The modular responsibility split embodied by notebook (56).

## Archive-only candidates

- Repeated brute-force offline install retries that do not change the runtime design.
- Benchmark-only ensemble descendants that do not survive into the final likely architecture.
- Temporary base checkpoints and training bootstrap details from the competitor branch.
- Near-duplicate compact runners whose only change is environment recovery rather than algorithmic behavior.
