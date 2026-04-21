# Models

This directory contains the three tracked core runtime checkpoints:

- `best.pt`: YOLO lead detector
- `best_model_effb3_phase9_ddp (2).pth`: primary EfficientNet-B3 segmentation model
- `best_model_phase10.pth`: explicit phase-10 fallback segmentation model

Non-core and historical checkpoints live under `archive/checkpoints/`.
