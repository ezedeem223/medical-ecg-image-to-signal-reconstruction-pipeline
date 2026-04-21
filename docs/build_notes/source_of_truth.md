# Phase 4 Source Of Truth

This file freezes the final repository decisions used during the Phase 4 build.

## Anchor Freeze

- Structural anchor: version `57` / `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`
- Primary performance anchor: version `50` / `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`
- Secondary performance reference: version `46` / `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`

## Why The Anchors Differ

The structural anchor is the best source for module boundaries, execution flow, helper separation, and validation/export structure. It is not the best runtime anchor because the preserved score history marks the modular endpoint as an exception regression rather than a peak-scoring path.

The performance anchor and its secondary score reference preserve the best-known runtime lineage. They supply the final runtime behavior for:

- YOLO-first lead localization
- EfficientNet-B3 primary segmentation
- phase-10 fallback behavior
- calibration, trace extraction, and timing normalization
- strict `id,value` export behavior

## What Phase 4 Borrows From Each Lineage

From the structural anchor:

- modular package boundaries
- config/bootstrap separation
- model registry/selection boundaries
- validation/export separation
- debug hooks kept outside the hot path

From the primary performance anchor:

- runtime ordering
- EffB3-first segmentation behavior
- practical fallback assistance from phase-10
- robust calibration and extraction behavior

From the secondary performance reference:

- score-proven ResNet50/phase-10 fallback expectations
- behavioral cross-checks when the late EffB3 branch diverges

## What Phase 4 Does Not Copy Directly

The final repository intentionally does not copy these notebook-era behaviors into core runtime:

- checkpoint auto-discovery
- glob-based runtime path guessing
- notebook wheel-install repair logic
- ensemble execution from notebook `(42)`
- interactive debug cells as required runtime stages

## Final Runtime Policy

- Primary segmentation model = `best_model_effb3_phase9_ddp (2).pth`
- Fallback segmentation model = `best_model_phase10.pth`
- Model selection is explicit and config-driven
- Core runtime auto-discovery is forbidden
