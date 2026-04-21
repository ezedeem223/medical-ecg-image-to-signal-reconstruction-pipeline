# File Audit: `best_model_phase10.pth`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 62 |
| Original path | best_model_phase10.pth |
| Report path | docs/file-audit/models/best_model_phase10.md |
| SHA-256 | 311a6f91961c61ec8d0e7fff4affafd59af9f00a97cdc4c08986ad2a44f5be79 |
| Size (bytes) | 135,647,702 |
| Modified (UTC) | 2026-04-18T21:21:28.114735+00:00 |

## Archive Layout

**Archive summary**

- is_zip_archive=True
- entry_count=444
- sample entry: best_model_phase10/data.pkl
- sample entry: best_model_phase10/byteorder
- sample entry: best_model_phase10/data/0
- sample entry: best_model_phase10/data/1
- sample entry: best_model_phase10/data/10
- sample entry: best_model_phase10/data/100
- sample entry: best_model_phase10/data/101
- sample entry: best_model_phase10/data/102
- sample entry: best_model_phase10/data/103
- sample entry: best_model_phase10/data/104
- sample entry: best_model_phase10/data/105
- sample entry: best_model_phase10/data/106
- sample entry: best_model_phase10/data/107
- sample entry: best_model_phase10/data/108
- sample entry: best_model_phase10/data/109
- sample entry: best_model_phase10/data/11
- sample entry: best_model_phase10/data/110
- sample entry: best_model_phase10/data/111
- sample entry: best_model_phase10/data/112
- sample entry: best_model_phase10/data/113

## Referencing Notebooks

**Notebook references**

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

- torch.load(map_location='cpu', weights_only=True)

## Manual Interpretation

**Analyst notes**

- Binary segmentation checkpoint with a ResNet-style encoder and decoder.blocks layout consistent with a U-Net style decoder rather than the DeepLab ASPP branch.
- This file is referenced across a wide span of later notebooks, which makes it the primary reusable phase-10 segmentation weight in the notebook series.

**Load status**

- loaded

**Python type**

- OrderedDict

**Top-level keys**

- encoder.conv1.weight
- encoder.bn1.weight
- encoder.bn1.bias
- encoder.bn1.running_mean
- encoder.bn1.running_var
- encoder.bn1.num_batches_tracked
- encoder.layer1.0.conv1.weight
- encoder.layer1.0.bn1.weight
- encoder.layer1.0.bn1.bias
- encoder.layer1.0.bn1.running_mean
- encoder.layer1.0.bn1.running_var
- encoder.layer1.0.bn1.num_batches_tracked
- encoder.layer1.0.conv2.weight
- encoder.layer1.0.bn2.weight
- encoder.layer1.0.bn2.bias
- encoder.layer1.0.bn2.running_mean
- encoder.layer1.0.bn2.running_var
- encoder.layer1.0.bn2.num_batches_tracked
- encoder.layer1.0.conv3.weight
- encoder.layer1.0.bn3.weight
- encoder.layer1.0.bn3.bias
- encoder.layer1.0.bn3.running_mean
- encoder.layer1.0.bn3.running_var
- encoder.layer1.0.bn3.num_batches_tracked
- encoder.layer1.0.downsample.0.weight
- encoder.layer1.0.downsample.1.weight
- encoder.layer1.0.downsample.1.bias
- encoder.layer1.0.downsample.1.running_mean
- encoder.layer1.0.downsample.1.running_var
- encoder.layer1.0.downsample.1.num_batches_tracked
- encoder.layer1.1.conv1.weight
- encoder.layer1.1.bn1.weight
- encoder.layer1.1.bn1.bias
- encoder.layer1.1.bn1.running_mean
- encoder.layer1.1.bn1.running_var
- encoder.layer1.1.bn1.num_batches_tracked
- encoder.layer1.1.conv2.weight
- encoder.layer1.1.bn2.weight
- encoder.layer1.1.bn2.bias
- encoder.layer1.1.bn2.running_mean
- encoder.layer1.1.bn2.running_var
- encoder.layer1.1.bn2.num_batches_tracked
- encoder.layer1.1.conv3.weight
- encoder.layer1.1.bn3.weight
- encoder.layer1.1.bn3.bias
- encoder.layer1.1.bn3.running_mean
- encoder.layer1.1.bn3.running_var
- encoder.layer1.1.bn3.num_batches_tracked
- encoder.layer1.2.conv1.weight
- encoder.layer1.2.bn1.weight

## State Dict Summary

| Field | Value |
| --- | --- |
| Key count | 440 |
| Tensor count | 440 |
| Parameter count | 33,871,243 |

### Prefix Families

#### `decoder.blocks`

- Key count: 120
- Sample keys: `decoder.blocks.0.conv1.0.weight`, `decoder.blocks.0.conv1.1.weight`, `decoder.blocks.0.conv1.1.bias`
- Sample tensor: `decoder.blocks.0.conv1.0.weight` shape=[256, 3072, 3, 3] dtype=torch.float32
- Sample tensor: `decoder.blocks.0.conv1.1.weight` shape=[256] dtype=torch.float32

#### `encoder.bn1`

- Key count: 5
- Sample keys: `encoder.bn1.weight`, `encoder.bn1.bias`, `encoder.bn1.running_mean`
- Sample tensor: `encoder.bn1.weight` shape=[64] dtype=torch.float32
- Sample tensor: `encoder.bn1.bias` shape=[64] dtype=torch.float32

#### `encoder.conv1`

- Key count: 1
- Sample keys: `encoder.conv1.weight`
- Sample tensor: `encoder.conv1.weight` shape=[64, 3, 7, 7] dtype=torch.float32

#### `encoder.layer1`

- Key count: 60
- Sample keys: `encoder.layer1.0.conv1.weight`, `encoder.layer1.0.bn1.weight`, `encoder.layer1.0.bn1.bias`
- Sample tensor: `encoder.layer1.0.conv1.weight` shape=[64, 64, 1, 1] dtype=torch.float32
- Sample tensor: `encoder.layer1.0.bn1.weight` shape=[64] dtype=torch.float32

#### `encoder.layer2`

- Key count: 78
- Sample keys: `encoder.layer2.0.conv1.weight`, `encoder.layer2.0.bn1.weight`, `encoder.layer2.0.bn1.bias`
- Sample tensor: `encoder.layer2.0.conv1.weight` shape=[128, 256, 1, 1] dtype=torch.float32
- Sample tensor: `encoder.layer2.0.bn1.weight` shape=[128] dtype=torch.float32

#### `encoder.layer3`

- Key count: 114
- Sample keys: `encoder.layer3.0.conv1.weight`, `encoder.layer3.0.bn1.weight`, `encoder.layer3.0.bn1.bias`
- Sample tensor: `encoder.layer3.0.conv1.weight` shape=[256, 512, 1, 1] dtype=torch.float32
- Sample tensor: `encoder.layer3.0.bn1.weight` shape=[256] dtype=torch.float32

#### `encoder.layer4`

- Key count: 60
- Sample keys: `encoder.layer4.0.conv1.weight`, `encoder.layer4.0.bn1.weight`, `encoder.layer4.0.bn1.bias`
- Sample tensor: `encoder.layer4.0.conv1.weight` shape=[512, 1024, 1, 1] dtype=torch.float32
- Sample tensor: `encoder.layer4.0.bn1.weight` shape=[512] dtype=torch.float32

#### `segmentation_head`

- Key count: 2
- Sample keys: `segmentation_head.0.weight`, `segmentation_head.0.bias`
- Sample tensor: `segmentation_head.0.weight` shape=[1, 16, 3, 3] dtype=torch.float32
- Sample tensor: `segmentation_head.0.bias` shape=[1] dtype=torch.float32

## Inspection Limits And Risks

**Notes**

- Because the artifact is a pure state_dict, the exact training configuration must be reconstructed from notebooks rather than from the file itself.
