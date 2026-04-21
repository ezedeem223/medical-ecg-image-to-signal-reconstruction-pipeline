# File Audit: `best_model_effb3_phase9_ddp (2).pth`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 60 |
| Original path | best_model_effb3_phase9_ddp (2).pth |
| Report path | docs/file-audit/models/best_model_effb3_phase9_ddp-2.md |
| SHA-256 | d6fa2100fe8e8eaa0489710b05bd2c4d36269223bb7450a78c2d4977ab94471b |
| Size (bytes) | 53,454,686 |
| Modified (UTC) | 2026-04-18T21:19:14.292729+00:00 |

## Archive Layout

**Archive summary**

- is_zip_archive=True
- entry_count=610
- sample entry: best_model_effb3_phase9_ddp/data.pkl
- sample entry: best_model_effb3_phase9_ddp/byteorder
- sample entry: best_model_effb3_phase9_ddp/data/0
- sample entry: best_model_effb3_phase9_ddp/data/1
- sample entry: best_model_effb3_phase9_ddp/data/10
- sample entry: best_model_effb3_phase9_ddp/data/100
- sample entry: best_model_effb3_phase9_ddp/data/101
- sample entry: best_model_effb3_phase9_ddp/data/102
- sample entry: best_model_effb3_phase9_ddp/data/103
- sample entry: best_model_effb3_phase9_ddp/data/104
- sample entry: best_model_effb3_phase9_ddp/data/105
- sample entry: best_model_effb3_phase9_ddp/data/106
- sample entry: best_model_effb3_phase9_ddp/data/107
- sample entry: best_model_effb3_phase9_ddp/data/108
- sample entry: best_model_effb3_phase9_ddp/data/109
- sample entry: best_model_effb3_phase9_ddp/data/11
- sample entry: best_model_effb3_phase9_ddp/data/110
- sample entry: best_model_effb3_phase9_ddp/data/111
- sample entry: best_model_effb3_phase9_ddp/data/112
- sample entry: best_model_effb3_phase9_ddp/data/113

## Referencing Notebooks

**Notebook references**

- None

## Safe Load Strategy

**Strategy**

- torch.load(map_location='cpu', weights_only=True)

## Manual Interpretation

**Analyst notes**

- Binary segmentation checkpoint with an EfficientNet-B3 style encoder and a decoder.blocks family, consistent with the phase-9 DDP experiments referenced by the filename.
- The tensor families match the EMA/model weights stored in the resumable checkpoint, but this file is the inference-oriented weights export rather than the full training snapshot.

**Load status**

- loaded

**Python type**

- dict

**Top-level keys**

- encoder._conv_stem.weight
- encoder._bn0.weight
- encoder._bn0.bias
- encoder._bn0.running_mean
- encoder._bn0.running_var
- encoder._blocks.0._depthwise_conv.weight
- encoder._blocks.0._bn1.weight
- encoder._blocks.0._bn1.bias
- encoder._blocks.0._bn1.running_mean
- encoder._blocks.0._bn1.running_var
- encoder._blocks.0._se_reduce.weight
- encoder._blocks.0._se_reduce.bias
- encoder._blocks.0._se_expand.weight
- encoder._blocks.0._se_expand.bias
- encoder._blocks.0._project_conv.weight
- encoder._blocks.0._bn2.weight
- encoder._blocks.0._bn2.bias
- encoder._blocks.0._bn2.running_mean
- encoder._blocks.0._bn2.running_var
- encoder._blocks.1._depthwise_conv.weight
- encoder._blocks.1._bn1.weight
- encoder._blocks.1._bn1.bias
- encoder._blocks.1._bn1.running_mean
- encoder._blocks.1._bn1.running_var
- encoder._blocks.1._se_reduce.weight
- encoder._blocks.1._se_reduce.bias
- encoder._blocks.1._se_expand.weight
- encoder._blocks.1._se_expand.bias
- encoder._blocks.1._project_conv.weight
- encoder._blocks.1._bn2.weight
- encoder._blocks.1._bn2.bias
- encoder._blocks.1._bn2.running_mean
- encoder._blocks.1._bn2.running_var
- encoder._blocks.2._expand_conv.weight
- encoder._blocks.2._bn0.weight
- encoder._blocks.2._bn0.bias
- encoder._blocks.2._bn0.running_mean
- encoder._blocks.2._bn0.running_var
- encoder._blocks.2._depthwise_conv.weight
- encoder._blocks.2._bn1.weight
- encoder._blocks.2._bn1.bias
- encoder._blocks.2._bn1.running_mean
- encoder._blocks.2._bn1.running_var
- encoder._blocks.2._se_reduce.weight
- encoder._blocks.2._se_reduce.bias
- encoder._blocks.2._se_expand.weight
- encoder._blocks.2._se_expand.bias
- encoder._blocks.2._project_conv.weight
- encoder._blocks.2._bn2.weight
- encoder._blocks.2._bn2.bias

## State Dict Summary

| Field | Value |
| --- | --- |
| Key count | 606 |
| Tensor count | 606 |
| Parameter count | 13,311,975 |

### Prefix Families

#### `decoder.blocks`

- Key count: 110
- Sample keys: `decoder.blocks.0.conv1.0.weight`, `decoder.blocks.0.conv1.1.weight`, `decoder.blocks.0.conv1.1.bias`
- Sample tensor: `decoder.blocks.0.conv1.0.weight` shape=[256, 520, 3, 3] dtype=torch.float32
- Sample tensor: `decoder.blocks.0.conv1.1.weight` shape=[256] dtype=torch.float32

#### `encoder._blocks`

- Key count: 484
- Sample keys: `encoder._blocks.0._depthwise_conv.weight`, `encoder._blocks.0._bn1.weight`, `encoder._blocks.0._bn1.bias`
- Sample tensor: `encoder._blocks.0._depthwise_conv.weight` shape=[40, 1, 3, 3] dtype=torch.float32
- Sample tensor: `encoder._blocks.0._bn1.weight` shape=[40] dtype=torch.float32

#### `encoder._bn0`

- Key count: 4
- Sample keys: `encoder._bn0.weight`, `encoder._bn0.bias`, `encoder._bn0.running_mean`
- Sample tensor: `encoder._bn0.weight` shape=[40] dtype=torch.float32
- Sample tensor: `encoder._bn0.bias` shape=[40] dtype=torch.float32

#### `encoder._bn1`

- Key count: 4
- Sample keys: `encoder._bn1.weight`, `encoder._bn1.bias`, `encoder._bn1.running_mean`
- Sample tensor: `encoder._bn1.weight` shape=[1536] dtype=torch.float32
- Sample tensor: `encoder._bn1.bias` shape=[1536] dtype=torch.float32

#### `encoder._conv_head`

- Key count: 1
- Sample keys: `encoder._conv_head.weight`
- Sample tensor: `encoder._conv_head.weight` shape=[1536, 384, 1, 1] dtype=torch.float32

#### `encoder._conv_stem`

- Key count: 1
- Sample keys: `encoder._conv_stem.weight`
- Sample tensor: `encoder._conv_stem.weight` shape=[40, 3, 3, 3] dtype=torch.float32

#### `segmentation_head`

- Key count: 2
- Sample keys: `segmentation_head.0.weight`, `segmentation_head.0.bias`
- Sample tensor: `segmentation_head.0.weight` shape=[1, 16, 3, 3] dtype=torch.float32
- Sample tensor: `segmentation_head.0.bias` shape=[1] dtype=torch.float32

## Inspection Limits And Risks

**Notes**

- The filename suggests it is a duplicate or copied export; notebook context is required to determine whether it supersedes other phase-9 EfficientNet-B3 checkpoints.
