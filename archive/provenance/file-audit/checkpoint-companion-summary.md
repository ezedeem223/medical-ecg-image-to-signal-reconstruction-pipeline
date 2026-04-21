# Checkpoint Companion Summary

This is the Phase 1 closure cross-reference for checkpoints mentioned across the notebook series. It is intentionally lighter than the full model reports and is meant to support later synthesis work.

## `best.pt`

- Audited artifact in bundle: yes
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (15).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (16).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (17).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (18).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (22).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (23).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (24).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (25).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (26).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (27).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (28).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (29).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (32).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (33).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (34).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (35).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (38).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (39).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Interpreted role: The successful inspection path is ultralytics.YOLO, not bare torch.load(weights_only=True). This file is a full Ultralytics detector artifact tied to a 12-class lead-localization task.
- Development phase: Lead detector deployment branch
- Interpretation confidence: high
- Model report: [models/best.md](models/best.md)

## `best_model.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low

## `best_model_deeplab_ph10.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low

## `best_model_deeplab_ph10.pth`

- Audited artifact in bundle: yes
- Referencing notebooks: None
- Interpreted role: Pure weights-only state_dict for a binary segmentation model with a DeepLabV3+-style decoder.aspp branch and a ResNet-family encoder layout.
- Development phase: Bundled checkpoint artifact
- Interpretation confidence: high
- Model report: [models/best_model_deeplab_ph10.md](models/best_model_deeplab_ph10.md)

## `best_model_effb3_phase9_ddp (2).pth`

- Audited artifact in bundle: yes
- Referencing notebooks: None
- Interpreted role: Binary segmentation checkpoint with an EfficientNet-B3 style encoder and a decoder.blocks family, consistent with the phase-9 DDP experiments referenced by the filename.
- Development phase: Phase 9 EfficientNet-B3 DDP era
- Interpretation confidence: medium
- Model report: [models/best_model_effb3_phase9_ddp-2.md](models/best_model_effb3_phase9_ddp-2.md)

## `best_model_effb3_phase9_ddp.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (51).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`
- Interpreted role: Inference-oriented EfficientNet-B3 export from the phase-9 DDP branch.
- Development phase: Phase 9 EfficientNet-B3 DDP era
- Interpretation confidence: medium

## `best_model_efficientnet_ph10.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low

## `best_model_efficientnet_ph10.pth`

- Audited artifact in bundle: yes
- Referencing notebooks: None
- Interpreted role: Binary segmentation checkpoint with an EfficientNet-style encoder (_conv_stem, _blocks, squeeze-excitation sublayers) and a compact segmentation head.
- Development phase: Bundled checkpoint artifact
- Interpretation confidence: high
- Model report: [models/best_model_efficientnet_ph10.md](models/best_model_efficientnet_ph10.md)

## `best_model_phase10.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (15).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (16).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (17).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (18).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (22).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (23).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (24).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (25).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (26).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (27).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (28).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (29).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (32).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (33).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (34).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (35).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (38).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (39).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Interpreted role: Primary phase-10 segmentation checkpoint reused across many later notebooks.
- Development phase: Phase 10 pseudo-label / real-image fine-tuning era
- Interpretation confidence: medium

## `best_model_phase10.pth`

- Audited artifact in bundle: yes
- Referencing notebooks: None
- Interpreted role: Binary segmentation checkpoint with a ResNet-style encoder and decoder.blocks layout consistent with a U-Net style decoder rather than the DeepLab ASPP branch.
- Development phase: Phase 10 pseudo-label / real-image fine-tuning era
- Interpretation confidence: high
- Model report: [models/best_model_phase10.md](models/best_model_phase10.md)

## `best_model_phase2.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Interpreted role: Intermediate hardening-phase segmentation checkpoint referenced by the geometry and quality-boost notebooks.
- Development phase: Phase 2 hardening era
- Interpretation confidence: medium

## `best_model_phase7.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low

## `best_model_phase8.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low

## `best_model_phase9.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Phase 9 EfficientNet-B3 DDP era
- Interpretation confidence: medium

## `best_model_real_data.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Interpreted role: Real-data fine-tuning checkpoint from the early synthetic-to-real adaptation branch.
- Development phase: Early real-data adaptation branch
- Interpretation confidence: medium

## `checkpoint_effb3_phase9_ddp (1) (1).pt`

- Audited artifact in bundle: yes
- Referencing notebooks: None
- Interpreted role: This is the only full resumable training checkpoint in the bundle: it stores epoch, optimizer, scheduler, AMP scaler, best_val, and EMA in addition to model weights.
- Development phase: Phase 9 EfficientNet-B3 DDP era
- Interpretation confidence: high
- Model report: [models/checkpoint_effb3_phase9_ddp-1-1.md](models/checkpoint_effb3_phase9_ddp-1-1.md)

## `temp_deeplab_base.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`
- Interpreted role: Bootstrap DeepLab base weights used as an initializer before the explicit phase-10 competitor training begins.
- Development phase: Ensemble bootstrap initialization
- Interpretation confidence: low

## `temp_effnet_base.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`
- Interpreted role: Bootstrap EfficientNet base weights used as an initializer before the explicit phase-10 competitor training begins.
- Development phase: Ensemble bootstrap initialization
- Interpretation confidence: low

## `yolov8l.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low

## `yolov8m.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low

## `yolov8n.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (22).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (23).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (24).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (25).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (26).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (27).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (28).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (29).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low

## `yolov8x.pt`

- Audited artifact in bundle: no
- Referencing notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Interpreted role: Checkpoint referenced by notebooks, but its exact historical role remains partly implicit in code rather than in explicit prose.
- Development phase: Unclassified experimental reference
- Interpretation confidence: low
