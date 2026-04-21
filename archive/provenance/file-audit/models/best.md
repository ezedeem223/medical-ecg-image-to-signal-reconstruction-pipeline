# File Audit: `best.pt`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 58 |
| Original path | best.pt |
| Report path | docs/file-audit/models/best.md |
| SHA-256 | 3e4e1a5cbb07e848947964b0ccf0abcb0f367807139437dbd4c3861210e2c090 |
| Size (bytes) | 136,715,059 |
| Modified (UTC) | 2026-04-18T21:18:23.753160+00:00 |

## Archive Layout

**Archive summary**

- is_zip_archive=True
- entry_count=603
- sample entry: best/data.pkl
- sample entry: best/byteorder
- sample entry: best/data/0
- sample entry: best/data/1
- sample entry: best/data/10
- sample entry: best/data/100
- sample entry: best/data/101
- sample entry: best/data/102
- sample entry: best/data/103
- sample entry: best/data/104
- sample entry: best/data/105
- sample entry: best/data/106
- sample entry: best/data/107
- sample entry: best/data/108
- sample entry: best/data/109
- sample entry: best/data/11
- sample entry: best/data/110
- sample entry: best/data/111
- sample entry: best/data/112
- sample entry: best/data/113

## Referencing Notebooks

**Notebook references**

- ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (15).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (16).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (17).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (18).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (22).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (23).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (24).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (25).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (26).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (27).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (28).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (29).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (32).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (33).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (34).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (35).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (38).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (39).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (51).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb

## Safe Load Strategy

**Strategy**

- Temporary trusted venv created with --system-site-packages; installed ultralytics==8.3.241; attempted ultralytics.YOLO plus torch.load with allowlisted ultralytics task models.

## Manual Interpretation

**Analyst notes**

- The successful inspection path is ultralytics.YOLO, not bare torch.load(weights_only=True). This file is a full Ultralytics detector artifact tied to a 12-class lead-localization task.
- The class map resolves to the standard lead names I, II, III, aVR, aVL, aVF, and V1 through V6, which matches how later notebooks use YOLO to localize ECG lead regions before segmentation or strip extraction.

**Load status**

- loaded

**Python type**

- DetectionModel

## State Dict Summary

| Field | Value |
| --- | --- |
| Key count | 595 |
| Tensor count | 595 |
| Parameter count | 68,222,341 |

### Prefix Families

#### `model.bn`

- Key count: 35
- Sample keys: `model.0.bn.weight`, `model.0.bn.bias`, `model.0.bn.running_mean`
- Sample tensor: `model.0.bn.weight` shape=[80] dtype=torch.float32
- Sample tensor: `model.0.bn.bias` shape=[80] dtype=torch.float32

#### `model.conv`

- Key count: 7
- Sample keys: `model.0.conv.weight`, `model.1.conv.weight`, `model.3.conv.weight`
- Sample tensor: `model.0.conv.weight` shape=[80, 3, 3, 3] dtype=torch.float32
- Sample tensor: `model.1.conv.weight` shape=[160, 80, 3, 3] dtype=torch.float32

#### `model.cv1`

- Key count: 54
- Sample keys: `model.2.cv1.conv.weight`, `model.2.cv1.bn.weight`, `model.2.cv1.bn.bias`
- Sample tensor: `model.2.cv1.conv.weight` shape=[160, 160, 1, 1] dtype=torch.float32
- Sample tensor: `model.2.cv1.bn.weight` shape=[160] dtype=torch.float32

#### `model.cv2`

- Key count: 96
- Sample keys: `model.2.cv2.conv.weight`, `model.2.cv2.bn.weight`, `model.2.cv2.bn.bias`
- Sample tensor: `model.2.cv2.conv.weight` shape=[160, 400, 1, 1] dtype=torch.float32
- Sample tensor: `model.2.cv2.bn.weight` shape=[160] dtype=torch.float32

#### `model.cv3`

- Key count: 42
- Sample keys: `model.22.cv3.0.0.conv.weight`, `model.22.cv3.0.0.bn.weight`, `model.22.cv3.0.0.bn.bias`
- Sample tensor: `model.22.cv3.0.0.conv.weight` shape=[320, 320, 3, 3] dtype=torch.float32
- Sample tensor: `model.22.cv3.0.0.bn.weight` shape=[320] dtype=torch.float32

#### `model.dfl`

- Key count: 1
- Sample keys: `model.22.dfl.conv.weight`
- Sample tensor: `model.22.dfl.conv.weight` shape=[1, 16, 1, 1] dtype=torch.float32

#### `model.m`

- Key count: 360
- Sample keys: `model.2.m.0.cv1.conv.weight`, `model.2.m.0.cv1.bn.weight`, `model.2.m.0.cv1.bn.bias`
- Sample tensor: `model.2.m.0.cv1.conv.weight` shape=[80, 80, 3, 3] dtype=torch.float32
- Sample tensor: `model.2.m.0.cv1.bn.weight` shape=[80] dtype=torch.float32

## Loader Attempt Log

**Attempt records**

- {"python_type": "DetectionModel", "state_dict": {"key_count": 595, "tensor_count": 595, "parameter_count": 68222341, "families": {"model.conv": {"count": 7, "sample_keys": ["model.0.conv.weight", "model.1.conv.weight", "model.3.conv.weight"], "sample_tensors": [{"key": "model.0.conv.weight", "shape": [80, 3, 3, 3], "dtype": "torch.float32"}, {"key": "model.1.conv.weight", "shape": [160, 80, 3, 3], "dtype": "torch.float32"}]}, "model.bn": {"count": 35, "sample_keys": ["model.0.bn.weight", "model.0.bn.bias", "model.0.bn.running_mean"], "sample_tensors": [{"key": "model.0.bn.weight", "shape": [80], "dtype": "torch.float32"}, {"key": "model.0.bn.bias", "shape": [80], "dtype": "torch.float32"}]}, "model.cv1": {"count": 54, "sample_keys": ["model.2.cv1.conv.weight", "model.2.cv1.bn.weight", "model.2.cv1.bn.bias"], "sample_tensors": [{"key": "model.2.cv1.conv.weight", "shape": [160, 160, 1, 1], "dtype": "torch.float32"}, {"key": "model.2.cv1.bn.weight", "shape": [160], "dtype": "torch.float32"}]}, "model.cv2": {"count": 96, "sample_keys": ["model.2.cv2.conv.weight", "model.2.cv2.bn.weight", "model.2.cv2.bn.bias"], "sample_tensors": [{"key": "model.2.cv2.conv.weight", "shape": [160, 400, 1, 1], "dtype": "torch.float32"}, {"key": "model.2.cv2.bn.weight", "shape": [160], "dtype": "torch.float32"}]}, "model.m": {"count": 360, "sample_keys": ["model.2.m.0.cv1.conv.weight", "model.2.m.0.cv1.bn.weight", "model.2.m.0.cv1.bn.bias"], "sample_tensors": [{"key": "model.2.m.0.cv1.conv.weight", "shape": [80, 80, 3, 3], "dtype": "torch.float32"}, {"key": "model.2.m.0.cv1.bn.weight", "shape": [80], "dtype": "torch.float32"}]}, "model.cv3": {"count": 42, "sample_keys": ["model.22.cv3.0.0.conv.weight", "model.22.cv3.0.0.bn.weight", "model.22.cv3.0.0.bn.bias"], "sample_tensors": [{"key": "model.22.cv3.0.0.conv.weight", "shape": [320, 320, 3, 3], "dtype": "torch.float32"}, {"key": "model.22.cv3.0.0.bn.weight", "shape": [320], "dtype": "torch.float32"}]}, "model.dfl": {"count": 1, "sample_keys": ["model.22.dfl.conv.weight"], "sample_tensors": [{"key": "model.22.dfl.conv.weight", "shape": [1, 16, 1, 1], "dtype": "torch.float32"}]}}}, "yaml_keys": ["nc", "depth_multiple", "width_multiple", "backbone", "head", "ch", "channels"], "loader": "ultralytics.YOLO", "task": "detect", "class_names": {"0": "I", "1": "II", "2": "III", "3": "aVR", "4": "aVL", "5": "aVF", "6": "V1", "7": "V2", "8": "V3", "9": "V4", "10": "V5", "11": "V6"}}
- {"loader": "torch.load(weights_only=True)", "error": "Weights only load failed. This file can still be loaded, to do so you have two options, \u001b[1mdo those steps only if you trust the source of the checkpoint\u001b[0m. \n\t(1) In PyTorch 2.6, we changed the default value of the `weights_only` argument in `torch.load` from `False` to `True`. Re-running `torch.load` with `weights_only` set to `False` will likely succeed, but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.\n\t(2) Alternatively, to load with `weights_only=True` please check the recommended steps in the following error message.\n\tWeightsUnpickler error: Unsupported global: GLOBAL torch.nn.modules.container.Sequential was not an allowed global by default. Please use `torch.serialization.add_safe_globals([torch.nn.modules.container.Sequential])` or the `torch.serialization.safe_globals([torch.nn.modules.container.Sequential])` context manager to allowlist this global if you trust this class/function.\n\nCheck the documentation of torch.load to learn more about types accepted by default with weights_only https://pytorch.org/docs/stable/generated/torch.load.html."}
- {"python_type": "dict", "top_level_keys": ["date", "version", "license", "docs", "epoch", "best_fitness", "model", "ema", "updates", "optimizer", "scaler", "train_args", "train_metrics", "train_results", "git"], "loader": "torch.load(weights_only=False)"}

## Inspection Limits And Risks

**Notes**

- Direct torch.load(weights_only=True) still fails unless additional globals are allowlisted; future reinspection depends on a compatible ultralytics runtime.
