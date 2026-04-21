# Performance Lineage

## Evidence scope

- Observed facts:
  - The preserved score-history context identifies versions `46` and `50` as the best-known scoring tier.
  - Versions `56` and `57` are treated as exception regressions.
  - The structural endpoint is version `57` / `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`.
  - The scored versions represented in this phase are: v33, v34, v35, v36, v38, v40, v41, v42, v44, v45, v46, v47, v48, v49, v50, v51, v52, v53, v54, v55, v56, v57.
- Interpretation:
  - Peak score happened before the modular endpoint.
  - The best scoring lineage and the best structural lineage are related, but not identical.

## Best-scoring lineage

- Primary performance anchor: version 50 / `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`
  - Why: Version 50 sits on the late EfficientNet-B3 deployment line while still looking like a successful compact Kaggle runner, making it the strongest available runtime anchor that also aligns with the late architectural direction.
- Secondary performance reference: version 46 / `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`
  - Why: Version 46 is an earlier score-proven compact runtime reference that keeps the detector plus phase-10 lineage intact and serves as a fallback design check when late EffB3 behavior diverges.

## What the score history implies

- Observed facts:
  - Version 50 belongs to the `effb3-integration-modular-finalization` era.
  - Version 46 belongs to the `ensemble-competitor-branch` era.
  - Structural improvements continued into the final modular notebook, but the latest two tracked versions are exception rows: v56 (ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb), v57 (ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb).
- Interpretation:
  - The project's best-known runtime behavior lives in the compact late deployment family, not in the final modular notebook run itself.
  - Later work improved maintainability, checkpoint management, and module separation, but did not preserve guaranteed peak runtime behavior automatically.

## Era-level interpretation

- Score-improving eras:
  - Late compact ensemble-to-EffB3 transition around versions 46 and 50.
  - Compact deployment hardening before full modularization.
- Maintainability-oriented eras:
  - The modular finalization notebooks culminating in version 57.
  - Late diagnostic and path-hardening revisions where clarity improved more than preserved score evidence.

## Final Phase 3 reading

- Structural anchor and performance anchor are intentionally separated.
- Performance decisions should borrow the runtime-critical behavior from version 50 first, version 46 second.
- Repository architecture decisions should still borrow from version 57.
- Confidence: `medium`
