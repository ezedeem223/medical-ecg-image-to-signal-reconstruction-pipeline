# File Audit: `checkpoint_effb3_phase9_ddp (1) (1).pt`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 63 |
| Original path | checkpoint_effb3_phase9_ddp (1) (1).pt |
| Report path | docs/file-audit/models/checkpoint_effb3_phase9_ddp-1-1.md |
| SHA-256 | 081a24f80b7e7e326c0884b2e221a4c794709283d706b76308818a7c177305bc |
| Size (bytes) | 208,388,883 |
| Modified (UTC) | 2026-04-18T21:20:16.184249+00:00 |

## Archive Layout

**Archive summary**

- is_zip_archive=True
- entry_count=2567
- sample entry: checkpoint_effb3_phase9_ddp/data.pkl
- sample entry: checkpoint_effb3_phase9_ddp/byteorder
- sample entry: checkpoint_effb3_phase9_ddp/data/0
- sample entry: checkpoint_effb3_phase9_ddp/data/1
- sample entry: checkpoint_effb3_phase9_ddp/data/10
- sample entry: checkpoint_effb3_phase9_ddp/data/100
- sample entry: checkpoint_effb3_phase9_ddp/data/1000
- sample entry: checkpoint_effb3_phase9_ddp/data/1001
- sample entry: checkpoint_effb3_phase9_ddp/data/1002
- sample entry: checkpoint_effb3_phase9_ddp/data/1003
- sample entry: checkpoint_effb3_phase9_ddp/data/1004
- sample entry: checkpoint_effb3_phase9_ddp/data/1005
- sample entry: checkpoint_effb3_phase9_ddp/data/1006
- sample entry: checkpoint_effb3_phase9_ddp/data/1007
- sample entry: checkpoint_effb3_phase9_ddp/data/1008
- sample entry: checkpoint_effb3_phase9_ddp/data/1009
- sample entry: checkpoint_effb3_phase9_ddp/data/101
- sample entry: checkpoint_effb3_phase9_ddp/data/1010
- sample entry: checkpoint_effb3_phase9_ddp/data/1011
- sample entry: checkpoint_effb3_phase9_ddp/data/1012

## Referencing Notebooks

**Notebook references**

- None

## Safe Load Strategy

**Strategy**

- torch.load(map_location='cpu', weights_only=True)

## Manual Interpretation

**Analyst notes**

- This is the only full resumable training checkpoint in the bundle: it stores epoch, optimizer, scheduler, AMP scaler, best_val, and EMA in addition to model weights.
- The presence of both training-state metadata and EMA weights makes it the authoritative provenance artifact for the phase-9 EfficientNet-B3 DDP training run.

**Load status**

- loaded

**Python type**

- dict

**Top-level keys**

- epoch
- model
- optimizer
- scheduler
- scaler
- best_val
- ema

**Top-level value summary**

- epoch: {"python_type": "int", "value": 176}
- model: {"python_type": "OrderedDict", "state_dict": {"key_count": 694, "tensor_count": 694, "parameter_count": 13312063, "families": {"encoder._conv_stem": {"count": 1, "sample_keys": ["encoder._conv_stem.weight"], "sample_tensors": [{"key": "encoder._conv_stem.weight", "shape": [40, 3, 3, 3], "dtype": "torch.float32"}]}, "encoder._bn0": {"count": 5, "sample_keys": ["encoder._bn0.weight", "encoder._bn0.bias", "encoder._bn0.running_mean"], "sample_tensors": [{"key": "encoder._bn0.weight", "shape": [40], "dtype": "torch.float32"}, {"key": "encoder._bn0.bias", "shape": [40], "dtype": "torch.float32"}]}, "encoder._blocks": {"count": 560, "sample_keys": ["encoder._blocks.0._depthwise_conv.weight", "encoder._blocks.0._bn1.weight", "encoder._blocks.0._bn1.bias"], "sample_tensors": [{"key": "encoder._blocks.0._depthwise_conv.weight", "shape": [40, 1, 3, 3], "dtype": "torch.float32"}, {"key": "encoder._blocks.0._bn1.weight", "shape": [40], "dtype": "torch.float32"}]}, "encoder._conv_head": {"count": 1, "sample_keys": ["encoder._conv_head.weight"], "sample_tensors": [{"key": "encoder._conv_head.weight", "shape": [1536, 384, 1, 1], "dtype": "torch.float32"}]}, "encoder._bn1": {"count": 5, "sample_keys": ["encoder._bn1.weight", "encoder._bn1.bias", "encoder._bn1.running_mean"], "sample_tensors": [{"key": "encoder._bn1.weight", "shape": [1536], "dtype": "torch.float32"}, {"key": "encoder._bn1.bias", "shape": [1536], "dtype": "torch.float32"}]}, "decoder.blocks": {"count": 120, "sample_keys": ["decoder.blocks.0.conv1.0.weight", "decoder.blocks.0.conv1.1.weight", "decoder.blocks.0.conv1.1.bias"], "sample_tensors": [{"key": "decoder.blocks.0.conv1.0.weight", "shape": [256, 520, 3, 3], "dtype": "torch.float32"}, {"key": "decoder.blocks.0.conv1.1.weight", "shape": [256], "dtype": "torch.float32"}]}, "segmentation_head": {"count": 2, "sample_keys": ["segmentation_head.0.weight", "segmentation_head.0.bias"], "sample_tensors": [{"key": "segmentation_head.0.weight", "shape": [1, 16, 3, 3], "dtype": "torch.float32"}, {"key": "segmentation_head.0.bias", "shape": [1], "dtype": "torch.float32"}]}}}}
- optimizer: {"python_type": "dict", "keys": ["state", "param_groups"], "state_entries": 421, "param_group_count": 1}
- scheduler: {"python_type": "dict", "keys": ["T_0", "T_i", "T_mult", "eta_min", "T_cur", "base_lrs", "last_epoch", "verbose", "_step_count", "_get_lr_called_within_step", "_last_lr", "T_max", "factor", "default_min_lr", "min_lrs", "patience", "cooldown", "cooldown_counter", "mode", "threshold", "threshold_mode", "eps", "mode_worse", "best", "num_bad_epochs"]}
- scaler: {"python_type": "dict", "keys": ["scale", "growth_factor", "backoff_factor", "growth_interval", "_growth_tracker"]}
- best_val: {"python_type": "float", "value": 0.007812690135324374}
- ema: {"python_type": "dict", "state_dict": {"key_count": 606, "tensor_count": 606, "parameter_count": 13311975, "families": {"encoder._conv_stem": {"count": 1, "sample_keys": ["encoder._conv_stem.weight"], "sample_tensors": [{"key": "encoder._conv_stem.weight", "shape": [40, 3, 3, 3], "dtype": "torch.float32"}]}, "encoder._bn0": {"count": 4, "sample_keys": ["encoder._bn0.weight", "encoder._bn0.bias", "encoder._bn0.running_mean"], "sample_tensors": [{"key": "encoder._bn0.weight", "shape": [40], "dtype": "torch.float32"}, {"key": "encoder._bn0.bias", "shape": [40], "dtype": "torch.float32"}]}, "encoder._blocks": {"count": 484, "sample_keys": ["encoder._blocks.0._depthwise_conv.weight", "encoder._blocks.0._bn1.weight", "encoder._blocks.0._bn1.bias"], "sample_tensors": [{"key": "encoder._blocks.0._depthwise_conv.weight", "shape": [40, 1, 3, 3], "dtype": "torch.float32"}, {"key": "encoder._blocks.0._bn1.weight", "shape": [40], "dtype": "torch.float32"}]}, "encoder._conv_head": {"count": 1, "sample_keys": ["encoder._conv_head.weight"], "sample_tensors": [{"key": "encoder._conv_head.weight", "shape": [1536, 384, 1, 1], "dtype": "torch.float32"}]}, "encoder._bn1": {"count": 4, "sample_keys": ["encoder._bn1.weight", "encoder._bn1.bias", "encoder._bn1.running_mean"], "sample_tensors": [{"key": "encoder._bn1.weight", "shape": [1536], "dtype": "torch.float32"}, {"key": "encoder._bn1.bias", "shape": [1536], "dtype": "torch.float32"}]}, "decoder.blocks": {"count": 110, "sample_keys": ["decoder.blocks.0.conv1.0.weight", "decoder.blocks.0.conv1.1.weight", "decoder.blocks.0.conv1.1.bias"], "sample_tensors": [{"key": "decoder.blocks.0.conv1.0.weight", "shape": [256, 520, 3, 3], "dtype": "torch.float32"}, {"key": "decoder.blocks.0.conv1.1.weight", "shape": [256], "dtype": "torch.float32"}]}, "segmentation_head": {"count": 2, "sample_keys": ["segmentation_head.0.weight", "segmentation_head.0.bias"], "sample_tensors": [{"key": "segmentation_head.0.weight", "shape": [1, 16, 3, 3], "dtype": "torch.float32"}, {"key": "segmentation_head.0.bias", "shape": [1], "dtype": "torch.float32"}]}}}}

## Inspection Limits And Risks

**Notes**

- Because the checkpoint includes executable Python pickled objects, it should be inspected or restored only in a trusted environment.
