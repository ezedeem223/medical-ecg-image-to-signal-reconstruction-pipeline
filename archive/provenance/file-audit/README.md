# File Audit Index

This directory contains a deterministic file-by-file audit for every notebook and every checkpoint found in the project root at generation time.

## Audit Scope

- Notebook files: 57
- Model files: 6
- Total audited files: 63
- Inspection mode: static notebook JSON analysis + stored output inspection + read-only checkpoint inspection.
- Extracted notebook image outputs: 48
- Notebooks with full cell review: 57/57
- Image/HTML outputs with manual translations: 54
- Models with manual interpretation: 6/6
- Notebooks with unresolved open questions: 12/57
- Interpretation confidence split: high=45, medium=12, low=0
- Manifest: [manifest.csv](manifest.csv)
- Extracted image artifacts: [image-outputs/](image-outputs/)
- Checkpoint companion summary: [checkpoint-companion-summary.md](checkpoint-companion-summary.md)
- Phase 2 synthesis seed: [../final_synthesis_outline.md](../final_synthesis_outline.md)

## Phase 1 Closure Standard

- A notebook is Phase-1 complete only when a notebook summary exists, every source cell has exactly one editorial note, output translations remain preserved, delta notes exist, open questions are tracked, a confidence level is assigned, and the manifest marks the notebook as editorially complete.
- Observed facts remain in the structural sections of each report; the manual layer is reserved for editorial interpretation, historical framing, and unresolved questions.

## Completion Table

| Review order | Source file | Type | Report | Status | Editorial | Confidence | Complete |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh.md) | completed | cell-reviewed | medium | yes |
| 2 | `ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-1.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-1.md) | completed | cell-reviewed | high | yes |
| 3 | `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-2.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-2.md) | completed | cell-reviewed | medium | yes |
| 4 | `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-3.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-3.md) | completed | cell-reviewed | medium | yes |
| 5 | `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-4.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-4.md) | completed | cell-reviewed | medium | yes |
| 6 | `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-5.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-5.md) | completed | cell-reviewed | medium | yes |
| 7 | `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-6.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-6.md) | completed | cell-reviewed | medium | yes |
| 8 | `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-7.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-7.md) | completed | cell-reviewed | medium | yes |
| 9 | `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-8.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-8.md) | completed | cell-reviewed | medium | yes |
| 10 | `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-9.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-9.md) | completed | cell-reviewed | medium | yes |
| 11 | `ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-10.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-10.md) | completed | cell-reviewed | high | yes |
| 12 | `ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-11.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-11.md) | completed | cell-reviewed | high | yes |
| 13 | `ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-12.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-12.md) | completed | cell-reviewed | high | yes |
| 14 | `ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-13.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-13.md) | completed | cell-reviewed | high | yes |
| 15 | `ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-14.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-14.md) | completed | cell-reviewed | high | yes |
| 16 | `ecg-sim2real-datagenerator-mohamad-sabbagh (15).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-15.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-15.md) | completed | cell-reviewed | high | yes |
| 17 | `ecg-sim2real-datagenerator-mohamad-sabbagh (16).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-16.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-16.md) | completed | cell-reviewed | high | yes |
| 18 | `ecg-sim2real-datagenerator-mohamad-sabbagh (17).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-17.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-17.md) | completed | cell-reviewed | high | yes |
| 19 | `ecg-sim2real-datagenerator-mohamad-sabbagh (18).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-18.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-18.md) | completed | cell-reviewed | high | yes |
| 20 | `ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-19.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-19.md) | completed | cell-reviewed | high | yes |
| 21 | `ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-20.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-20.md) | completed | cell-reviewed | high | yes |
| 22 | `ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-21.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-21.md) | completed | cell-reviewed | high | yes |
| 23 | `ecg-sim2real-datagenerator-mohamad-sabbagh (22).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-22.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-22.md) | completed | cell-reviewed | high | yes |
| 24 | `ecg-sim2real-datagenerator-mohamad-sabbagh (23).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-23.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-23.md) | completed | cell-reviewed | high | yes |
| 25 | `ecg-sim2real-datagenerator-mohamad-sabbagh (24).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-24.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-24.md) | completed | cell-reviewed | high | yes |
| 26 | `ecg-sim2real-datagenerator-mohamad-sabbagh (25).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-25.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-25.md) | completed | cell-reviewed | high | yes |
| 27 | `ecg-sim2real-datagenerator-mohamad-sabbagh (26).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-26.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-26.md) | completed | cell-reviewed | high | yes |
| 28 | `ecg-sim2real-datagenerator-mohamad-sabbagh (27).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-27.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-27.md) | completed | cell-reviewed | high | yes |
| 29 | `ecg-sim2real-datagenerator-mohamad-sabbagh (28).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-28.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-28.md) | completed | cell-reviewed | high | yes |
| 30 | `ecg-sim2real-datagenerator-mohamad-sabbagh (29).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-29.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-29.md) | completed | cell-reviewed | high | yes |
| 31 | `ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-30.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-30.md) | completed | cell-reviewed | high | yes |
| 32 | `ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-31.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-31.md) | completed | cell-reviewed | medium | yes |
| 33 | `ecg-sim2real-datagenerator-mohamad-sabbagh (32).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-32.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-32.md) | completed | cell-reviewed | high | yes |
| 34 | `ecg-sim2real-datagenerator-mohamad-sabbagh (33).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-33.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-33.md) | completed | cell-reviewed | high | yes |
| 35 | `ecg-sim2real-datagenerator-mohamad-sabbagh (34).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-34.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-34.md) | completed | cell-reviewed | high | yes |
| 36 | `ecg-sim2real-datagenerator-mohamad-sabbagh (35).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-35.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-35.md) | completed | cell-reviewed | high | yes |
| 37 | `ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-36.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-36.md) | completed | cell-reviewed | high | yes |
| 38 | `ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-37.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-37.md) | completed | cell-reviewed | high | yes |
| 39 | `ecg-sim2real-datagenerator-mohamad-sabbagh (38).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-38.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-38.md) | completed | cell-reviewed | high | yes |
| 40 | `ecg-sim2real-datagenerator-mohamad-sabbagh (39).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-39.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-39.md) | completed | cell-reviewed | high | yes |
| 41 | `ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-40.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-40.md) | completed | cell-reviewed | high | yes |
| 42 | `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-41.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-41.md) | completed | cell-reviewed | high | yes |
| 43 | `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-42.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-42.md) | completed | cell-reviewed | medium | yes |
| 44 | `ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-43.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-43.md) | completed | cell-reviewed | high | yes |
| 45 | `ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-44.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-44.md) | completed | cell-reviewed | high | yes |
| 46 | `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-45.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-45.md) | completed | cell-reviewed | high | yes |
| 47 | `ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-46.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-46.md) | completed | cell-reviewed | high | yes |
| 48 | `ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-47.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-47.md) | completed | cell-reviewed | high | yes |
| 49 | `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-48.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-48.md) | completed | cell-reviewed | high | yes |
| 50 | `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-49.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-49.md) | completed | cell-reviewed | high | yes |
| 51 | `ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-50.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-50.md) | completed | cell-reviewed | high | yes |
| 52 | `ecg-sim2real-datagenerator-mohamad-sabbagh (51).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-51.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-51.md) | completed | cell-reviewed | high | yes |
| 53 | `ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-52.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-52.md) | completed | cell-reviewed | high | yes |
| 54 | `ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-53.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-53.md) | completed | cell-reviewed | high | yes |
| 55 | `ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-54.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-54.md) | completed | cell-reviewed | high | yes |
| 56 | `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-55.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-55.md) | completed | cell-reviewed | high | yes |
| 57 | `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb` | notebook | [notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-56.md](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-56.md) | completed | cell-reviewed | medium | yes |
| 58 | `best.pt` | model | [models/best.md](models/best.md) | completed | model-reviewed | n/a | yes |
| 59 | `best_model_deeplab_ph10.pth` | model | [models/best_model_deeplab_ph10.md](models/best_model_deeplab_ph10.md) | completed | model-reviewed | n/a | yes |
| 60 | `best_model_effb3_phase9_ddp (2).pth` | model | [models/best_model_effb3_phase9_ddp-2.md](models/best_model_effb3_phase9_ddp-2.md) | completed | model-reviewed | n/a | yes |
| 61 | `best_model_efficientnet_ph10.pth` | model | [models/best_model_efficientnet_ph10.md](models/best_model_efficientnet_ph10.md) | completed | model-reviewed | n/a | yes |
| 62 | `best_model_phase10.pth` | model | [models/best_model_phase10.md](models/best_model_phase10.md) | completed | model-reviewed | n/a | yes |
| 63 | `checkpoint_effb3_phase9_ddp (1) (1).pt` | model | [models/checkpoint_effb3_phase9_ddp-1-1.md](models/checkpoint_effb3_phase9_ddp-1-1.md) | completed | model-reviewed | n/a | yes |

## Notebook Families

### Offline Kaggle inference pipeline variant with packaged dependencies.

- [ecg-sim2real-datagenerator-mohamad-sabbagh (15).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-15.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (16).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-16.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (17).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-17.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (18).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-18.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-19.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-20.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-21.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (22).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-22.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (23).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-23.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (24).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-24.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (25).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-25.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (26).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-26.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (27).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-27.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (28).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-28.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (29).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-29.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-30.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-31.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (32).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-32.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (33).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-33.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (34).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-34.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (35).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-35.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-36.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-37.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (38).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-38.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (39).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-39.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-40.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-41.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-43.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-44.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-45.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-46.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-47.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-48.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-49.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-50.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (51).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-51.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-52.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-53.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-54.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-55.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-56.md)

### Kaggle ECG digitization inference notebook combining YOLO and segmentation.

- [ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-7.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-8.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-10.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-11.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-12.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-13.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-14.md)

### End-to-end synthetic data generation and training notebook.

- [ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-2.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-3.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-4.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-5.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-6.md)

### Phase 10 real-world fine-tuning notebook.

- [ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-9.md)
- [ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-42.md)

### Prototype notebook with custom dataset / model helper definitions.

- [ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb](notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-1.md)

## Model Reports

- [best.pt](models/best.md)
- [best_model_deeplab_ph10.pth](models/best_model_deeplab_ph10.md)
- [best_model_effb3_phase9_ddp (2).pth](models/best_model_effb3_phase9_ddp-2.md)
- [best_model_efficientnet_ph10.pth](models/best_model_efficientnet_ph10.md)
- [best_model_phase10.pth](models/best_model_phase10.md)
- [checkpoint_effb3_phase9_ddp (1) (1).pt](models/checkpoint_effb3_phase9_ddp-1-1.md)

## Short Evolution Timeline

- `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb` (1 notebook(s)): End-to-end synthetic data generation and training notebook.
- `ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb` (1 notebook(s)): Prototype notebook with custom dataset / model helper definitions.
- `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb` (5 notebook(s)): End-to-end synthetic data generation and training notebook.
- `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb` (2 notebook(s)): Kaggle ECG digitization inference notebook combining YOLO and segmentation.
- `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb` (1 notebook(s)): Phase 10 real-world fine-tuning notebook.
- `ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb` (5 notebook(s)): Kaggle ECG digitization inference notebook combining YOLO and segmentation.
- `ecg-sim2real-datagenerator-mohamad-sabbagh (15).ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb` (27 notebook(s)): Offline Kaggle inference pipeline variant with packaged dependencies.
- `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb` (1 notebook(s)): Phase 10 real-world fine-tuning notebook.
- `ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb` (14 notebook(s)): Offline Kaggle inference pipeline variant with packaged dependencies.

## Snapshot Characteristics

- Almost every notebook is code-only; markdown documentation is effectively absent.
- Kaggle-specific paths and dependency bootstrap steps recur throughout the notebook series.
- Later notebooks increasingly consolidate around YOLO + segmentation inference pipelines and checkpoint loading.
- Image-bearing notebooks now include explicit prose translations tied to extracted PNG artifacts instead of only figure-size placeholders.
- The audit reports intentionally preserve per-file detail even when multiple notebook revisions are near-duplicates.
