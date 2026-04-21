# File Audit: `best_model_deeplab_ph10.pth`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 59 |
| Original path | best_model_deeplab_ph10.pth |
| Report path | docs/file-audit/models/best_model_deeplab_ph10.md |
| SHA-256 | c2225d216ea341169b51a728528deb2a05d85a73a027533890ed8ba02560b5a1 |
| Size (bytes) | 107,076,140 |
| Modified (UTC) | 2026-04-18T21:21:17.189049+00:00 |

## Archive Layout

**Archive summary**

- is_zip_archive=True
- entry_count=383
- sample entry: best_model_deeplab_ph10/data.pkl
- sample entry: best_model_deeplab_ph10/byteorder
- sample entry: best_model_deeplab_ph10/data/0
- sample entry: best_model_deeplab_ph10/data/1
- sample entry: best_model_deeplab_ph10/data/10
- sample entry: best_model_deeplab_ph10/data/100
- sample entry: best_model_deeplab_ph10/data/101
- sample entry: best_model_deeplab_ph10/data/102
- sample entry: best_model_deeplab_ph10/data/103
- sample entry: best_model_deeplab_ph10/data/104
- sample entry: best_model_deeplab_ph10/data/105
- sample entry: best_model_deeplab_ph10/data/106
- sample entry: best_model_deeplab_ph10/data/107
- sample entry: best_model_deeplab_ph10/data/108
- sample entry: best_model_deeplab_ph10/data/109
- sample entry: best_model_deeplab_ph10/data/11
- sample entry: best_model_deeplab_ph10/data/110
- sample entry: best_model_deeplab_ph10/data/111
- sample entry: best_model_deeplab_ph10/data/112
- sample entry: best_model_deeplab_ph10/data/113

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

- Pure weights-only state_dict for a binary segmentation model with a DeepLabV3+-style decoder.aspp branch and a ResNet-family encoder layout.
- The 1-channel segmentation head indicates that the checkpoint predicts a foreground trace mask rather than multi-class lead labels.

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
| Key count | 379 |
| Tensor count | 379 |
| Parameter count | 26,734,959 |

### Prefix Families

#### `decoder.aspp`

- Key count: 46
- Sample keys: `decoder.aspp.0.convs.0.0.weight`, `decoder.aspp.0.convs.0.1.weight`, `decoder.aspp.0.convs.0.1.bias`
- Sample tensor: `decoder.aspp.0.convs.0.0.weight` shape=[256, 2048, 1, 1] dtype=torch.float32
- Sample tensor: `decoder.aspp.0.convs.0.1.weight` shape=[256] dtype=torch.float32

#### `decoder.block1`

- Key count: 6
- Sample keys: `decoder.block1.0.weight`, `decoder.block1.1.weight`, `decoder.block1.1.bias`
- Sample tensor: `decoder.block1.0.weight` shape=[48, 256, 1, 1] dtype=torch.float32
- Sample tensor: `decoder.block1.1.weight` shape=[48] dtype=torch.float32

#### `decoder.block2`

- Key count: 7
- Sample keys: `decoder.block2.0.0.weight`, `decoder.block2.0.1.weight`, `decoder.block2.1.weight`
- Sample tensor: `decoder.block2.0.0.weight` shape=[304, 1, 3, 3] dtype=torch.float32
- Sample tensor: `decoder.block2.0.1.weight` shape=[256, 304, 1, 1] dtype=torch.float32

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
- Sample tensor: `segmentation_head.0.weight` shape=[1, 256, 1, 1] dtype=torch.float32
- Sample tensor: `segmentation_head.0.bias` shape=[1] dtype=torch.float32

## Inspection Limits And Risks

**Notes**

- This artifact does not include optimizer or scheduler state, so it supports inference or fine-tuning initialization rather than exact training resumption.
