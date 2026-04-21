# File Audit: `best_model_efficientnet_ph10.pth`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 61 |
| Original path | best_model_efficientnet_ph10.pth |
| Report path | docs/file-audit/models/best_model_efficientnet_ph10.md |
| SHA-256 | 4004052bddf4d6c95c7e49af0135f82f1e5b6fee0e1ebc9276bf3d413f607545 |
| Size (bytes) | 53,516,936 |
| Modified (UTC) | 2026-04-18T21:21:19.852487+00:00 |

## Archive Layout

**Archive summary**

- is_zip_archive=True
- entry_count=698
- sample entry: best_model_efficientnet_ph10/data.pkl
- sample entry: best_model_efficientnet_ph10/byteorder
- sample entry: best_model_efficientnet_ph10/data/0
- sample entry: best_model_efficientnet_ph10/data/1
- sample entry: best_model_efficientnet_ph10/data/10
- sample entry: best_model_efficientnet_ph10/data/100
- sample entry: best_model_efficientnet_ph10/data/101
- sample entry: best_model_efficientnet_ph10/data/102
- sample entry: best_model_efficientnet_ph10/data/103
- sample entry: best_model_efficientnet_ph10/data/104
- sample entry: best_model_efficientnet_ph10/data/105
- sample entry: best_model_efficientnet_ph10/data/106
- sample entry: best_model_efficientnet_ph10/data/107
- sample entry: best_model_efficientnet_ph10/data/108
- sample entry: best_model_efficientnet_ph10/data/109
- sample entry: best_model_efficientnet_ph10/data/11
- sample entry: best_model_efficientnet_ph10/data/110
- sample entry: best_model_efficientnet_ph10/data/111
- sample entry: best_model_efficientnet_ph10/data/112
- sample entry: best_model_efficientnet_ph10/data/113

## Referencing Notebooks

**Notebook references**

- ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb
- ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb

## Safe Load Strategy

**Strategy**

- torch.load(map_location='cpu', weights_only=True)

## Manual Interpretation

**Analyst notes**

- Binary segmentation checkpoint with an EfficientNet-style encoder (_conv_stem, _blocks, squeeze-excitation sublayers) and a compact segmentation head.
- This appears to be a lighter alternative to the ResNet/DeepLab family used for the same phase-10 trace-mask objective.

**Load status**

- loaded

**Python type**

- OrderedDict

**Top-level keys**

- encoder._conv_stem.weight
- encoder._bn0.weight
- encoder._bn0.bias
- encoder._bn0.running_mean
- encoder._bn0.running_var
- encoder._bn0.num_batches_tracked
- encoder._blocks.0._depthwise_conv.weight
- encoder._blocks.0._bn1.weight
- encoder._blocks.0._bn1.bias
- encoder._blocks.0._bn1.running_mean
- encoder._blocks.0._bn1.running_var
- encoder._blocks.0._bn1.num_batches_tracked
- encoder._blocks.0._se_reduce.weight
- encoder._blocks.0._se_reduce.bias
- encoder._blocks.0._se_expand.weight
- encoder._blocks.0._se_expand.bias
- encoder._blocks.0._project_conv.weight
- encoder._blocks.0._bn2.weight
- encoder._blocks.0._bn2.bias
- encoder._blocks.0._bn2.running_mean
- encoder._blocks.0._bn2.running_var
- encoder._blocks.0._bn2.num_batches_tracked
- encoder._blocks.1._depthwise_conv.weight
- encoder._blocks.1._bn1.weight
- encoder._blocks.1._bn1.bias
- encoder._blocks.1._bn1.running_mean
- encoder._blocks.1._bn1.running_var
- encoder._blocks.1._bn1.num_batches_tracked
- encoder._blocks.1._se_reduce.weight
- encoder._blocks.1._se_reduce.bias
- encoder._blocks.1._se_expand.weight
- encoder._blocks.1._se_expand.bias
- encoder._blocks.1._project_conv.weight
- encoder._blocks.1._bn2.weight
- encoder._blocks.1._bn2.bias
- encoder._blocks.1._bn2.running_mean
- encoder._blocks.1._bn2.running_var
- encoder._blocks.1._bn2.num_batches_tracked
- encoder._blocks.2._expand_conv.weight
- encoder._blocks.2._bn0.weight
- encoder._blocks.2._bn0.bias
- encoder._blocks.2._bn0.running_mean
- encoder._blocks.2._bn0.running_var
- encoder._blocks.2._bn0.num_batches_tracked
- encoder._blocks.2._depthwise_conv.weight
- encoder._blocks.2._bn1.weight
- encoder._blocks.2._bn1.bias
- encoder._blocks.2._bn1.running_mean
- encoder._blocks.2._bn1.running_var
- encoder._blocks.2._bn1.num_batches_tracked

## State Dict Summary

| Field | Value |
| --- | --- |
| Key count | 694 |
| Tensor count | 694 |
| Parameter count | 13,312,063 |

### Prefix Families

#### `decoder.blocks`

- Key count: 120
- Sample keys: `decoder.blocks.0.conv1.0.weight`, `decoder.blocks.0.conv1.1.weight`, `decoder.blocks.0.conv1.1.bias`
- Sample tensor: `decoder.blocks.0.conv1.0.weight` shape=[256, 520, 3, 3] dtype=torch.float32
- Sample tensor: `decoder.blocks.0.conv1.1.weight` shape=[256] dtype=torch.float32

#### `encoder._blocks`

- Key count: 560
- Sample keys: `encoder._blocks.0._depthwise_conv.weight`, `encoder._blocks.0._bn1.weight`, `encoder._blocks.0._bn1.bias`
- Sample tensor: `encoder._blocks.0._depthwise_conv.weight` shape=[40, 1, 3, 3] dtype=torch.float32
- Sample tensor: `encoder._blocks.0._bn1.weight` shape=[40] dtype=torch.float32

#### `encoder._bn0`

- Key count: 5
- Sample keys: `encoder._bn0.weight`, `encoder._bn0.bias`, `encoder._bn0.running_mean`
- Sample tensor: `encoder._bn0.weight` shape=[40] dtype=torch.float32
- Sample tensor: `encoder._bn0.bias` shape=[40] dtype=torch.float32

#### `encoder._bn1`

- Key count: 5
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

- The file is weights only, so training provenance such as optimizer state, scaler state, and epoch is not recoverable from this artifact.
