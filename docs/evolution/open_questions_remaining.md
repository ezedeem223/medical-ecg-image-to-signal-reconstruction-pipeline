# Remaining Open Questions

Only refactor-relevant unresolved questions are listed here. These are not a dump of all Phase 1 ambiguities.

## 1. Did the full notebook (42) ensemble path ever become the intended final runtime, or did it mainly serve as a checkpoint-generation and benchmarking branch?

- Why it matters: This determines whether ensemble logic belongs in the Phase 3 core design or only in archival experiment modules.
- Affected notebooks or checkpoints: ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb; best_model_deeplab_ph10.pth; best_model_efficientnet_ph10.pth
- Current best interpretation: The ensemble branch appears strategically important for generating and comparing competitor checkpoints, but the final likely deployment path narrows back toward detector plus one primary segmentation checkpoint with fallback.
- Confidence: `medium`

## 2. In the final compact notebooks, is EfficientNet-B3 always the intended primary segmentation model, or is model selection meant to remain dynamic between EffB3 and phase-10 weights?

- Why it matters: Refactor planning needs a default inference contract and a clear story for fallback behavior.
- Affected notebooks or checkpoints: ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (51).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb; best_model_effb3_phase9_ddp (2).pth; best_model_phase10.pth
- Current best interpretation: EffB3 looks like the preferred late-stage primary model, while phase-10 remains a trusted fallback or comparison branch.
- Confidence: `medium`

## 3. How direct is the handoff from the large research notebooks into the first compact deployment notebook?

- Why it matters: This affects whether a future repository should preserve an explicit training-to-deployment export stage or infer it from notebook history.
- Affected notebooks or checkpoints: ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb; best_model_phase10.pth; best.pt
- Current best interpretation: The handoff is conceptually clear but historically implicit: the compact notebook family packages the phase-10 and detector lineage rather than documenting a separate export notebook.
- Confidence: `medium`

## 4. Should the renderer and late diagnostic cells be preserved as operational tools or moved into a debug-only package during refactor?

- Why it matters: This changes the shape of the final repository and whether visualization lives on the main inference path.
- Affected notebooks or checkpoints: ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb; ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb
- Current best interpretation: They should survive, but as opt-in debug and validation utilities rather than as mandatory runtime stages.
- Confidence: `high`

## 5. What should be done with temporary competitor bootstrap checkpoints such as `temp_deeplab_base.pt` and `temp_effnet_base.pt`?

- Why it matters: They affect archive scope and whether competitor training provenance is reproducible enough for a cleaned repository.
- Affected notebooks or checkpoints: ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb; temp_deeplab_base.pt; temp_effnet_base.pt
- Current best interpretation: These artifacts look like branch-specific training initializers that belong in archive or provenance notes rather than the core runtime layout.
- Confidence: `medium`
