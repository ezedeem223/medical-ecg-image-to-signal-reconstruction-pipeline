# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 56 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-55.md |
| SHA-256 | 931552a9c9fdaaad6bedd34dcaf6e4703a2aa63be1d1dc3d1302a2af273be6f0 |
| Size (bytes) | 122,206 |
| Modified (UTC) | 2026-04-18T21:17:35.750664+00:00 |
| Inferred role | Offline Kaggle inference pipeline variant with packaged dependencies. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 5 |
| Cell count | 7 |
| Code cells | 7 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 0 |
| Editorial cell notes | 7 |
| Editorial output notes | 0 |
| Interpretation confidence | high |
| Open questions | 0 |
| Editorial complete | yes |
| Kernel | {"display_name": "Python 3", "language": "python", "name": "python3"} |
| Language info | {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.11.13"} |

## Dependencies

**Imports**

- collections
- csv
- cv2
- gc
- glob
- importlib
- math
- numpy
- os
- pandas
- pyarrow
- re
- scipy.signal
- segmentation_models_pytorch
- shutil
- site
- subprocess
- sys
- torch
- tqdm
- ultralytics

**Packages requested via pip/install commands**

- None

## Hard-Coded Paths And External Environment Markers

**Environment markers**

- Kaggle input mount
- subprocess usage
- YOLO loader
- segmentation_models_pytorch
- torch.load

**Literal paths / artifacts**

- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {IMAGE_DIR}/sample_submission.parquet

## Symbols Defined

**Functions**

- _normalize_lead_name
- apply_high_pass
- build_unet_resnet50
- clean_pid
- compute_patient_leads
- ensure_pkg
- estimate_skew_angle
- first_int
- get_crops_yolo_mapped
- get_image_path
- get_path
- ok_whl
- parse_rid
- predict_probmaps
- prepare_unet_batch
- preprocess_remove_grid_rgb
- prob_to_signal_mv
- quality_score
- rotate_keep_white
- safe_read_rgb
- trim_prob_map
- viterbi_adaptive_y
- viterbi_dp_y

**Classes**

- None

**Constants / assigned names**

- CLASS_TO_LEAD_IDX
- DEVICE
- DP_MAX_W
- DP_SMOOTH
- FORBIDDEN
- IMAGE_DIR
- LEAD_NAMES
- LEAD_TO_IDX
- M
- MAX_CACHE
- MAX_W
- NEEDED_HINTS
- NEW_BEST_DST
- NEW_BEST_SRC
- NEW_UNET_PATH
- OLD_UNET_PATH
- SAMPLE_PARQUET_PATH
- SUBMISSION_FILE
- TARGET_H
- TEST_CSV_PATH
- YOLO_CONF
- YOLO_INF_MAX
- YOLO_PATH
- hits
- ok
- ppmv
- scale
- t_len
- val

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: submission.csv
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet

**File writes**

- open: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install subscript[0] --no-deps --ignore-installed --quiet
- subprocess.check_call: sys.executable -m pip install whl --no-deps --ignore-installed --quiet

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth

## Stored Output Inventory

**Output types**

- stream: 8
- error: 1

**MIME types**

- None

**Exceptions captured in outputs**

- RuntimeError: Error(s) in loading state_dict for Unet:
	Missing key(s) in state_dict: "encoder.conv1.weight", "encoder.bn1.weight", "encoder.bn1.bias", "encoder.bn1.running_mean", "encoder.bn1.running_var", "encoder.layer1.0.conv1.weight", "encoder.layer1.0.bn1.weight", "encoder.layer1.0.bn1.bias", "encoder.layer1.0.bn1.running_mean", "encoder.layer1.0.bn1.running_var", "encoder.layer1.0.conv2.weight", "encoder.layer1.0.bn2.weight", "encoder.layer1.0.bn2.bias", "encoder.layer1.0.bn2.running_mean", "encoder.layer1.0.bn2.running_var", "encoder.layer1.0.conv3.weight", "encoder.layer1.0.bn3.weight", "encoder.layer1.0.bn3.bias", "encoder.layer1.0.bn3.running_mean", "encoder.layer1.0.bn3.running_var", "encoder.layer1.0.downsample.0.weight", "encoder.layer1.0.downsample.1.weight", "encoder.layer1.0.downsample.1.bias", "encoder.layer1.0.downsample.1.running_mean", "encoder.layer1.0.downsample.1.running_var", "encoder.layer1.1.conv1.weight", "encoder.layer1.1.bn1.weight", "encoder.layer1.1.bn1.bias", "encoder.layer1.1.bn1.running_mean", "encoder.layer1.1.bn1.running_var", "encoder.layer1.1.conv2.weight", "encoder.layer1.1.bn2.weight", "encoder.layer1.1.bn2.bias", "encoder.layer1.1.bn2.running_mean", "encoder.layer1.1.bn2.running_var", "encoder.layer1.1.conv3.weight", "encoder.layer1.1.bn3.weight", "encoder.layer1.1.bn3.bias", "encoder.layer1.1.bn3.running_mean", "encoder.layer1.1.bn3.running_var", "encoder.layer1.2.conv1.weight", "encoder.layer1.2.bn1.weight", "encoder.layer1.2.bn1.bias", "encoder.layer1.2.bn1.running_mean", "encoder.layer1.2.bn1.running_var", "encoder.layer1.2.conv2.weight", "encoder.layer1.2.bn2.weight", "encoder.layer1.2.bn2.bias", "encoder.layer1.2.bn2.running_mean", "encoder.layer1.2.bn2.running_var", "encoder.layer1.2.conv3.weight", "encoder.layer1.2.bn3.weight", "encoder.layer1.2.bn3.bias", "encoder.layer1.2.bn3.running_mean", "encoder.layer1.2.bn3.running_var", "encoder.layer2.0.conv1.weight", "encoder.layer2.0.bn1.weight", "encoder.layer2.0.bn1.bias", "encoder.layer2.0.bn1.running_mean", "encoder.layer2.0.bn1.running_var", "encoder.layer2.0.conv2.weight", "encoder.layer2.0.bn2.weight", "encoder.layer2.0.bn2.bias", "encoder.layer2.0.bn2.running_mean", "encoder.layer2.0.bn2.running_var", "encoder.layer2.0.conv3.weight", "encoder.layer2.0.bn3.weight", "encoder.layer2.0.bn3.bias", "encoder.layer2.0.bn3.running_mean", "encoder.layer2.0.bn3.running_var", "encoder.layer2.0.downsample.0.weight", "encoder.layer2.0.downsample.1.weight", "encoder.layer2.0.downsample.1.bias", "encoder.layer2.0.downsample.1.running_mean", "encoder.layer2.0.downsample.1.running_var", "encoder.layer2.1.conv1.weight", "encoder.layer2.1.bn1.weight", "encoder.layer2.1.bn1.bias", "encoder.layer2.1.bn1.running_mean", "encoder.layer2.1.bn1.running_var", "encoder.layer2.1.conv2.weight", "encoder.layer2.1.bn2.weight", "encoder.layer2.1.bn2.bias", "encoder.layer2.1.bn2.running_mean", "encoder.layer2.1.bn2.running_var", "encoder.layer2.1.conv3.weight", "encoder.layer2.1.bn3.weight", "encoder.layer2.1.bn3.bias", "encoder.layer2.1.bn3.running_mean", "encoder.layer2.1.bn3.running_var", "encoder.layer2.2.conv1.weight", "encoder.layer2.2.bn1.weight", "encoder.layer2.2.bn1.bias", "encoder.layer2.2.bn1.running_mean", "encoder.layer2.2.bn1.running_var", "encoder.layer2.2.conv2.weight", "encoder.layer2.2.bn2.weight", "encoder.layer2.2.bn2.bias", "encoder.layer2.2.bn2.running_mean", "encoder.layer2.2.bn2.running_var", "encoder.layer2.2.conv3.weight", "encoder.layer2.2.bn3.weight", "encoder.layer2.2.bn3.bias", "encoder.layer2.2.bn3.running_mean", "encoder.layer2.2.bn3.running_var", "encoder.layer2.3.conv1.weight", "encoder.layer2.3.bn1.weight", "encoder.layer2.3.bn1.bias", "encoder.layer2.3.bn1.running_mean", "encoder.layer2.3.bn1.running_var", "encoder.layer2.3.conv2.weight", "encoder.layer2.3.bn2.weight", "encoder.layer2.3.bn2.bias", "encoder.layer2.3.bn2.running_mean", "encoder.layer2.3.bn2.running_var", "encoder.layer2.3.conv3.weight", "encoder.layer2.3.bn3.weight", "encoder.layer2.3.bn3.bias", "encoder.layer2.3.bn3.running_mean", "encoder.layer2.3.bn3.running_var", "encoder.layer3.0.conv1.weight", "encoder.layer3.0.bn1.weight", "encoder.layer3.0.bn1.bias", "encoder.layer3.0.bn1.running_mean", "encoder.layer3.0.bn1.running_var", "encoder.layer3.0.conv2.weight", "encoder.layer3.0.bn2.weight", "encoder.layer3.0.bn2.bias", "encoder.layer3.0.bn2.running_mean", "encoder.layer3.0.bn2.running_var", "encoder.layer3.0.conv3.weight", "encoder.layer3.0.bn3.weight", "encoder.layer3.0.bn3.bias", "encoder.layer3.0.bn3.running_mean", "encoder.layer3.0.bn3.running_var", "encoder.layer3.0.downsample.0.weight", "encoder.layer3.0.downsample.1.weight", "encoder.layer3.0.downsample.1.bias", "encoder.layer3.0.downsample.1.running_mean", "encoder.layer3.0.downsample.1.running_var", "encoder.layer3.1.conv1.weight", "encoder.layer3.1.bn1.weight", "encoder.layer3.1.bn1.bias", "encoder.layer3.1.bn1.running_mean", "encoder.layer3.1.bn1.running_var", "encoder.layer3.1.conv2.weight", "encoder.layer3.1.bn2.weight", "encoder.layer3.1.bn2.bias", "encoder.layer3.1.bn2.running_mean", "encoder.layer3.1.bn2.running_var", "encoder.layer3.1.conv3.weight", "encoder.layer3.1.bn3.weight", "encoder.layer3.1.bn3.bias", "encoder.layer3.1.bn3.running_mean", "encoder.layer3.1.bn3.running_var", "encoder.layer3.2.conv1.weight", "encoder.layer3.2.bn1.weight", "encoder.layer3.2.bn1.bias", "encoder.layer3.2.bn1.running_mean", "encoder.layer3.2.bn1.running_var", "encoder.layer3.2.conv2.weight", "encoder.layer3.2.bn2.weight", "encoder.layer3.2.bn2.bias", "encoder.layer3.2.bn2.running_mean", "encoder.layer3.2.bn2.running_var", "encoder.layer3.2.conv3.weight", "encoder.layer3.2.bn3.weight", "encoder.layer3.2.bn3.bias", "encoder.layer3.2.bn3.running_mean", "encoder.layer3.2.bn3.running_var", "encoder.layer3.3.conv1.weight", "encoder.layer3.3.bn1.weight", "encoder.layer3.3.bn1.bias", "encoder.layer3.3.bn1.running_mean", "encoder.layer3.3.bn1.running_var", "encoder.layer3.3.conv2.weight", "encoder.layer3.3.bn2.weight", "encoder.layer3.3.bn2.bias", "encoder.layer3.3.bn2.running_mean", "encoder.layer3.3.bn2.running_var", "encoder.layer3.3.conv3.weight", "encoder.layer3.3.bn3.weight", "encoder.layer3.3.bn3.bias", "encoder.layer3.3.bn3.running_mean", "encoder.layer3.3.bn3.running_var", "encoder.layer3.4.conv1.weight", "encoder.layer3.4.bn1.weight", "encoder.layer3.4.bn1.bias", "encoder.layer3.4.bn1.running_mean", "encoder.layer3.4.bn1.running_var", "encoder.layer3.4.conv2.weight", "encoder.layer3.4.bn2.weight", "encoder.layer3.4.bn2.bias", "encoder.layer3.4.bn2.running_mean", "encoder.layer3.4.bn2.running_var", "encoder.layer3.4.conv3.weight", "encoder.layer3.4.bn3.weight", "encoder.layer3.4.bn3.bias", "encoder.layer3.4.bn3.running_mean", "encoder.layer3.4.bn3.running_var", "encoder.layer3.5.conv1.weight", "encoder.layer3.5.bn1.weight", "encoder.layer3.5.bn1.bias", "encoder.layer3.5.bn1.running_mean", "encoder.layer3.5.bn1.running_var", "encoder.layer3.5.conv2.weight", "encoder.layer3.5.bn2.weight", "encoder.layer3.5.bn2.bias", "encoder.layer3.5.bn2.running_mean", "encoder.layer3.5.bn2.running_var", "encoder.layer3.5.conv3.weight", "encoder.layer3.5.bn3.weight", "encoder.layer3.5.bn3.bias", "encoder.layer3.5.bn3.running_mean", "encoder.layer3.5.bn3.running_var", "encoder.layer4.0.conv1.weight", "encoder.layer4.0.bn1.weight", "encoder.layer4.0.bn1.bias", "encoder.layer4.0.bn1.running_mean", "encoder.layer4.0.bn1.running_var", "encoder.layer4.0.conv2.weight", "encoder.layer4.0.bn2.weight", "encoder.layer4.0.bn2.bias", "encoder.layer4.0.bn2.running_mean", "encoder.layer4.0.bn2.running_var", "encoder.layer4.0.conv3.weight", "encoder.layer4.0.bn3.weight", "encoder.layer4.0.bn3.bias", "encoder.layer4.0.bn3.running_mean", "encoder.layer4.0.bn3.running_var", "encoder.layer4.0.downsample.0.weight", "encoder.layer4.0.downsample.1.weight", "encoder.layer4.0.downsample.1.bias", "encoder.layer4.0.downsample.1.running_mean", "encoder.layer4.0.downsample.1.running_var", "encoder.layer4.1.conv1.weight", "encoder.layer4.1.bn1.weight", "encoder.layer4.1.bn1.bias", "encoder.layer4.1.bn1.running_mean", "encoder.layer4.1.bn1.running_var", "encoder.layer4.1.conv2.weight", "encoder.layer4.1.bn2.weight", "encoder.layer4.1.bn2.bias", "encoder.layer4.1.bn2.running_mean", "encoder.layer4.1.bn2.running_var", "encoder.layer4.1.conv3.weight", "encoder.layer4.1.bn3.weight", "encoder.layer4.1.bn3.bias", "encoder.layer4.1.bn3.running_mean", "encoder.layer4.1.bn3.running_var", "encoder.layer4.2.conv1.weight", "encoder.layer4.2.bn1.weight", "encoder.layer4.2.bn1.bias", "encoder.layer4.2.bn1.running_mean", "encoder.layer4.2.bn1.running_var", "encoder.layer4.2.conv2.weight", "encoder.layer4.2.bn2.weight", "encoder.layer4.2.bn2.bias", "encoder.layer4.2.bn2.running_mean", "encoder.layer4.2.bn2.running_var", "encoder.layer4.2.conv3.weight", "encoder.layer4.2.bn3.weight", "encoder.layer4.2.bn3.bias", "encoder.layer4.2.bn3.running_mean", "encoder.layer4.2.bn3.running_var". 
	Unexpected key(s) in state_dict: "encoder._conv_stem.weight", "encoder._bn0.weight", "encoder._bn0.bias", "encoder._bn0.running_mean", "encoder._bn0.running_var", "encoder._blocks.0._depthwise_conv.weight", "encoder._blocks.0._bn1.weight", "encoder._blocks.0._bn1.bias", "encoder._blocks.0._bn1.running_mean", "encoder._blocks.0._bn1.running_var", "encoder._blocks.0._se_reduce.weight", "encoder._blocks.0._se_reduce.bias", "encoder._blocks.0._se_expand.weight", "encoder._blocks.0._se_expand.bias", "encoder._blocks.0._project_conv.weight", "encoder._blocks.0._bn2.weight", "encoder._blocks.0._bn2.bias", "encoder._blocks.0._bn2.running_mean", "encoder._blocks.0._bn2.running_var", "encoder._blocks.1._depthwise_conv.weight", "encoder._blocks.1._bn1.weight", "encoder._blocks.1._bn1.bias", "encoder._blocks.1._bn1.running_mean", "encoder._blocks.1._bn1.running_var", "encoder._blocks.1._se_reduce.weight", "encoder._blocks.1._se_reduce.bias", "encoder._blocks.1._se_expand.weight", "encoder._blocks.1._se_expand.bias", "encoder._blocks.1._project_conv.weight", "encoder._blocks.1._bn2.weight", "encoder._blocks.1._bn2.bias", "encoder._blocks.1._bn2.running_mean", "encoder._blocks.1._bn2.running_var", "encoder._blocks.2._expand_conv.weight", "encoder._blocks.2._bn0.weight", "encoder._blocks.2._bn0.bias", "encoder._blocks.2._bn0.running_mean", "encoder._blocks.2._bn0.running_var", "encoder._blocks.2._depthwise_conv.weight", "encoder._blocks.2._bn1.weight", "encoder._blocks.2._bn1.bias", "encoder._blocks.2._bn1.running_mean", "encoder._blocks.2._bn1.running_var", "encoder._blocks.2._se_reduce.weight", "encoder._blocks.2._se_reduce.bias", "encoder._blocks.2._se_expand.weight", "encoder._blocks.2._se_expand.bias", "encoder._blocks.2._project_conv.weight", "encoder._blocks.2._bn2.weight", "encoder._blocks.2._bn2.bias", "encoder._blocks.2._bn2.running_mean", "encoder._blocks.2._bn2.running_var", "encoder._blocks.3._expand_conv.weight", "encoder._blocks.3._bn0.weight", "encoder._blocks.3._bn0.bias", "encoder._blocks.3._bn0.running_mean", "encoder._blocks.3._bn0.running_var", "encoder._blocks.3._depthwise_conv.weight", "encoder._blocks.3._bn1.weight", "encoder._blocks.3._bn1.bias", "encoder._blocks.3._bn1.running_mean", "encoder._blocks.3._bn1.running_var", "encoder._blocks.3._se_reduce.weight", "encoder._blocks.3._se_reduce.bias", "encoder._blocks.3._se_expand.weight", "encoder._blocks.3._se_expand.bias", "encoder._blocks.3._project_conv.weight", "encoder._blocks.3._bn2.weight", "encoder._blocks.3._bn2.bias", "encoder._blocks.3._bn2.running_mean", "encoder._blocks.3._bn2.running_var", "encoder._blocks.4._expand_conv.weight", "encoder._blocks.4._bn0.weight", "encoder._blocks.4._bn0.bias", "encoder._blocks.4._bn0.running_mean", "encoder._blocks.4._bn0.running_var", "encoder._blocks.4._depthwise_conv.weight", "encoder._blocks.4._bn1.weight", "encoder._blocks.4._bn1.bias", "encoder._blocks.4._bn1.running_mean", "encoder._blocks.4._bn1.running_var", "encoder._blocks.4._se_reduce.weight", "encoder._blocks.4._se_reduce.bias", "encoder._blocks.4._se_expand.weight", "encoder._blocks.4._se_expand.bias", "encoder._blocks.4._project_conv.weight", "encoder._blocks.4._bn2.weight", "encoder._blocks.4._bn2.bias", "encoder._blocks.4._bn2.running_mean", "encoder._blocks.4._bn2.running_var", "encoder._blocks.5._expand_conv.weight", "encoder._blocks.5._bn0.weight", "encoder._blocks.5._bn0.bias", "encoder._blocks.5._bn0.running_mean", "encoder._blocks.5._bn0.running_var", "encoder._blocks.5._depthwise_conv.weight", "encoder._blocks.5._bn1.weight", "encoder._blocks.5._bn1.bias", "encoder._blocks.5._bn1.running_mean", "encoder._blocks.5._bn1.running_var", "encoder._blocks.5._se_reduce.weight", "encoder._blocks.5._se_reduce.bias", "encoder._blocks.5._se_expand.weight", "encoder._blocks.5._se_expand.bias", "encoder._blocks.5._project_conv.weight", "encoder._blocks.5._bn2.weight", "encoder._blocks.5._bn2.bias", "encoder._blocks.5._bn2.running_mean", "encoder._blocks.5._bn2.running_var", "encoder._blocks.6._expand_conv.weight", "encoder._blocks.6._bn0.weight", "encoder._blocks.6._bn0.bias", "encoder._blocks.6._bn0.running_mean", "encoder._blocks.6._bn0.running_var", "encoder._blocks.6._depthwise_conv.weight", "encoder._blocks.6._bn1.weight", "encoder._blocks.6._bn1.bias", "encoder._blocks.6._bn1.running_mean", "encoder._blocks.6._bn1.running_var", "encoder._blocks.6._se_reduce.weight", "encoder._blocks.6._se_reduce.bias", "encoder._blocks.6._se_expand.weight", "encoder._blocks.6._se_expand.bias", "encoder._blocks.6._project_conv.weight", "encoder._blocks.6._bn2.weight", "encoder._blocks.6._bn2.bias", "encoder._blocks.6._bn2.running_mean", "encoder._blocks.6._bn2.running_var", "encoder._blocks.7._expand_conv.weight", "encoder._blocks.7._bn0.weight", "encoder._blocks.7._bn0.bias", "encoder._blocks.7._bn0.running_mean", "encoder._blocks.7._bn0.running_var", "encoder._blocks.7._depthwise_conv.weight", "encoder._blocks.7._bn1.weight", "encoder._blocks.7._bn1.bias", "encoder._blocks.7._bn1.running_mean", "encoder._blocks.7._bn1.running_var", "encoder._blocks.7._se_reduce.weight", "encoder._blocks.7._se_reduce.bias", "encoder._blocks.7._se_expand.weight", "encoder._blocks.7._se_expand.bias", "encoder._blocks.7._project_conv.weight", "encoder._blocks.7._bn2.weight", "encoder._blocks.7._bn2.bias", "encoder._blocks.7._bn2.running_mean", "encoder._blocks.7._bn2.running_var", "encoder._blocks.8._expand_conv.weight", "encoder._blocks.8._bn0.weight", "encoder._blocks.8._bn0.bias", "encoder._blocks.8._bn0.running_mean", "encoder._blocks.8._bn0.running_var", "encoder._blocks.8._depthwise_conv.weight", "encoder._blocks.8._bn1.weight", "encoder._blocks.8._bn1.bias", "encoder._blocks.8._bn1.running_mean", "encoder._blocks.8._bn1.running_var", "encoder._blocks.8._se_reduce.weight", "encoder._blocks.8._se_reduce.bias", "encoder._blocks.8._se_expand.weight", "encoder._blocks.8._se_expand.bias", "encoder._blocks.8._project_conv.weight", "encoder._blocks.8._bn2.weight", "encoder._blocks.8._bn2.bias", "encoder._blocks.8._bn2.running_mean", "encoder._blocks.8._bn2.running_var", "encoder._blocks.9._expand_conv.weight", "encoder._blocks.9._bn0.weight", "encoder._blocks.9._bn0.bias", "encoder._blocks.9._bn0.running_mean", "encoder._blocks.9._bn0.running_var", "encoder._blocks.9._depthwise_conv.weight", "encoder._blocks.9._bn1.weight", "encoder._blocks.9._bn1.bias", "encoder._blocks.9._bn1.running_mean", "encoder._blocks.9._bn1.running_var", "encoder._blocks.9._se_reduce.weight", "encoder._blocks.9._se_reduce.bias", "encoder._blocks.9._se_expand.weight", "encoder._blocks.9._se_expand.bias", "encoder._blocks.9._project_conv.weight", "encoder._blocks.9._bn2.weight", "encoder._blocks.9._bn2.bias", "encoder._blocks.9._bn2.running_mean", "encoder._blocks.9._bn2.running_var", "encoder._blocks.10._expand_conv.weight", "encoder._blocks.10._bn0.weight", "encoder._blocks.10._bn0.bias", "encoder._blocks.10._bn0.running_mean", "encoder._blocks.10._bn0.running_var", "encoder._blocks.10._depthwise_conv.weight", "encoder._blocks.10._bn1.weight", "encoder._blocks.10._bn1.bias", "encoder._blocks.10._bn1.running_mean", "encoder._blocks.10._bn1.running_var", "encoder._blocks.10._se_reduce.weight", "encoder._blocks.10._se_reduce.bias", "encoder._blocks.10._se_expand.weight", "encoder._blocks.10._se_expand.bias", "encoder._blocks.10._project_conv.weight", "encoder._blocks.10._bn2.weight", "encoder._blocks.10._bn2.bias", "encoder._blocks.10._bn2.running_mean", "encoder._blocks.10._bn2.running_var", "encoder._blocks.11._expand_conv.weight", "encoder._blocks.11._bn0.weight", "encoder._blocks.11._bn0.bias", "encoder._blocks.11._bn0.running_mean", "encoder._blocks.11._bn0.running_var", "encoder._blocks.11._depthwise_conv.weight", "encoder._blocks.11._bn1.weight", "encoder._blocks.11._bn1.bias", "encoder._blocks.11._bn1.running_mean", "encoder._blocks.11._bn1.running_var", "encoder._blocks.11._se_reduce.weight", "encoder._blocks.11._se_reduce.bias", "encoder._blocks.11._se_expand.weight", "encoder._blocks.11._se_expand.bias", "encoder._blocks.11._project_conv.weight", "encoder._blocks.11._bn2.weight", "encoder._blocks.11._bn2.bias", "encoder._blocks.11._bn2.running_mean", "encoder._blocks.11._bn2.running_var", "encoder._blocks.12._expand_conv.weight", "encoder._blocks.12._bn0.weight", "encoder._blocks.12._bn0.bias", "encoder._blocks.12._bn0.running_mean", "encoder._blocks.12._bn0.running_var", "encoder._blocks.12._depthwise_conv.weight", "encoder._blocks.12._bn1.weight", "encoder._blocks.12._bn1.bias", "encoder._blocks.12._bn1.running_mean", "encoder._blocks.12._bn1.running_var", "encoder._blocks.12._se_reduce.weight", "encoder._blocks.12._se_reduce.bias", "encoder._blocks.12._se_expand.weight", "encoder._blocks.12._se_expand.bias", "encoder._blocks.12._project_conv.weight", "encoder._blocks.12._bn2.weight", "encoder._blocks.12._bn2.bias", "encoder._blocks.12._bn2.running_mean", "encoder._blocks.12._bn2.running_var", "encoder._blocks.13._expand_conv.weight", "encoder._blocks.13._bn0.weight", "encoder._blocks.13._bn0.bias", "encoder._blocks.13._bn0.running_mean", "encoder._blocks.13._bn0.running_var", "encoder._blocks.13._depthwise_conv.weight", "encoder._blocks.13._bn1.weight", "encoder._blocks.13._bn1.bias", "encoder._blocks.13._bn1.running_mean", "encoder._blocks.13._bn1.running_var", "encoder._blocks.13._se_reduce.weight", "encoder._blocks.13._se_reduce.bias", "encoder._blocks.13._se_expand.weight", "encoder._blocks.13._se_expand.bias", "encoder._blocks.13._project_conv.weight", "encoder._blocks.13._bn2.weight", "encoder._blocks.13._bn2.bias", "encoder._blocks.13._bn2.running_mean", "encoder._blocks.13._bn2.running_var", "encoder._blocks.14._expand_conv.weight", "encoder._blocks.14._bn0.weight", "encoder._blocks.14._bn0.bias", "encoder._blocks.14._bn0.running_mean", "encoder._blocks.14._bn0.running_var", "encoder._blocks.14._depthwise_conv.weight", "encoder._blocks.14._bn1.weight", "encoder._blocks.14._bn1.bias", "encoder._blocks.14._bn1.running_mean", "encoder._blocks.14._bn1.running_var", "encoder._blocks.14._se_reduce.weight", "encoder._blocks.14._se_reduce.bias", "encoder._blocks.14._se_expand.weight", "encoder._blocks.14._se_expand.bias", "encoder._blocks.14._project_conv.weight", "encoder._blocks.14._bn2.weight", "encoder._blocks.14._bn2.bias", "encoder._blocks.14._bn2.running_mean", "encoder._blocks.14._bn2.running_var", "encoder._blocks.15._expand_conv.weight", "encoder._blocks.15._bn0.weight", "encoder._blocks.15._bn0.bias", "encoder._blocks.15._bn0.running_mean", "encoder._blocks.15._bn0.running_var", "encoder._blocks.15._depthwise_conv.weight", "encoder._blocks.15._bn1.weight", "encoder._blocks.15._bn1.bias", "encoder._blocks.15._bn1.running_mean", "encoder._blocks.15._bn1.running_var", "encoder._blocks.15._se_reduce.weight", "encoder._blocks.15._se_reduce.bias", "encoder._blocks.15._se_expand.weight", "encoder._blocks.15._se_expand.bias", "encoder._blocks.15._project_conv.weight", "encoder._blocks.15._bn2.weight", "encoder._blocks.15._bn2.bias", "encoder._blocks.15._bn2.running_mean", "encoder._blocks.15._bn2.running_var", "encoder._blocks.16._expand_conv.weight", "encoder._blocks.16._bn0.weight", "encoder._blocks.16._bn0.bias", "encoder._blocks.16._bn0.running_mean", "encoder._blocks.16._bn0.running_var", "encoder._blocks.16._depthwise_conv.weight", "encoder._blocks.16._bn1.weight", "encoder._blocks.16._bn1.bias", "encoder._blocks.16._bn1.running_mean", "encoder._blocks.16._bn1.running_var", "encoder._blocks.16._se_reduce.weight", "encoder._blocks.16._se_reduce.bias", "encoder._blocks.16._se_expand.weight", "encoder._blocks.16._se_expand.bias", "encoder._blocks.16._project_conv.weight", "encoder._blocks.16._bn2.weight", "encoder._blocks.16._bn2.bias", "encoder._blocks.16._bn2.running_mean", "encoder._blocks.16._bn2.running_var", "encoder._blocks.17._expand_conv.weight", "encoder._blocks.17._bn0.weight", "encoder._blocks.17._bn0.bias", "encoder._blocks.17._bn0.running_mean", "encoder._blocks.17._bn0.running_var", "encoder._blocks.17._depthwise_conv.weight", "encoder._blocks.17._bn1.weight", "encoder._blocks.17._bn1.bias", "encoder._blocks.17._bn1.running_mean", "encoder._blocks.17._bn1.running_var", "encoder._blocks.17._se_reduce.weight", "encoder._blocks.17._se_reduce.bias", "encoder._blocks.17._se_expand.weight", "encoder._blocks.17._se_expand.bias", "encoder._blocks.17._project_conv.weight", "encoder._blocks.17._bn2.weight", "encoder._blocks.17._bn2.bias", "encoder._blocks.17._bn2.running_mean", "encoder._blocks.17._bn2.running_var", "encoder._blocks.18._expand_conv.weight", "encoder._blocks.18._bn0.weight", "encoder._blocks.18._bn0.bias", "encoder._blocks.18._bn0.running_mean", "encoder._blocks.18._bn0.running_var", "encoder._blocks.18._depthwise_conv.weight", "encoder._blocks.18._bn1.weight", "encoder._blocks.18._bn1.bias", "encoder._blocks.18._bn1.running_mean", "encoder._blocks.18._bn1.running_var", "encoder._blocks.18._se_reduce.weight", "encoder._blocks.18._se_reduce.bias", "encoder._blocks.18._se_expand.weight", "encoder._blocks.18._se_expand.bias", "encoder._blocks.18._project_conv.weight", "encoder._blocks.18._bn2.weight", "encoder._blocks.18._bn2.bias", "encoder._blocks.18._bn2.running_mean", "encoder._blocks.18._bn2.running_var", "encoder._blocks.19._expand_conv.weight", "encoder._blocks.19._bn0.weight", "encoder._blocks.19._bn0.bias", "encoder._blocks.19._bn0.running_mean", "encoder._blocks.19._bn0.running_var", "encoder._blocks.19._depthwise_conv.weight", "encoder._blocks.19._bn1.weight", "encoder._blocks.19._bn1.bias", "encoder._blocks.19._bn1.running_mean", "encoder._blocks.19._bn1.running_var", "encoder._blocks.19._se_reduce.weight", "encoder._blocks.19._se_reduce.bias", "encoder._blocks.19._se_expand.weight", "encoder._blocks.19._se_expand.bias", "encoder._blocks.19._project_conv.weight", "encoder._blocks.19._bn2.weight", "encoder._blocks.19._bn2.bias", "encoder._blocks.19._bn2.running_mean", "encoder._blocks.19._bn2.running_var", "encoder._blocks.20._expand_conv.weight", "encoder._blocks.20._bn0.weight", "encoder._blocks.20._bn0.bias", "encoder._blocks.20._bn0.running_mean", "encoder._blocks.20._bn0.running_var", "encoder._blocks.20._depthwise_conv.weight", "encoder._blocks.20._bn1.weight", "encoder._blocks.20._bn1.bias", "encoder._blocks.20._bn1.running_mean", "encoder._blocks.20._bn1.running_var", "encoder._blocks.20._se_reduce.weight", "encoder._blocks.20._se_reduce.bias", "encoder._blocks.20._se_expand.weight", "encoder._blocks.20._se_expand.bias", "encoder._blocks.20._project_conv.weight", "encoder._blocks.20._bn2.weight", "encoder._blocks.20._bn2.bias", "encoder._blocks.20._bn2.running_mean", "encoder._blocks.20._bn2.running_var", "encoder._blocks.21._expand_conv.weight", "encoder._blocks.21._bn0.weight", "encoder._blocks.21._bn0.bias", "encoder._blocks.21._bn0.running_mean", "encoder._blocks.21._bn0.running_var", "encoder._blocks.21._depthwise_conv.weight", "encoder._blocks.21._bn1.weight", "encoder._blocks.21._bn1.bias", "encoder._blocks.21._bn1.running_mean", "encoder._blocks.21._bn1.running_var", "encoder._blocks.21._se_reduce.weight", "encoder._blocks.21._se_reduce.bias", "encoder._blocks.21._se_expand.weight", "encoder._blocks.21._se_expand.bias", "encoder._blocks.21._project_conv.weight", "encoder._blocks.21._bn2.weight", "encoder._blocks.21._bn2.bias", "encoder._blocks.21._bn2.running_mean", "encoder._blocks.21._bn2.running_var", "encoder._blocks.22._expand_conv.weight", "encoder._blocks.22._bn0.weight", "encoder._blocks.22._bn0.bias", "encoder._blocks.22._bn0.running_mean", "encoder._blocks.22._bn0.running_var", "encoder._blocks.22._depthwise_conv.weight", "encoder._blocks.22._bn1.weight", "encoder._blocks.22._bn1.bias", "encoder._blocks.22._bn1.running_mean", "encoder._blocks.22._bn1.running_var", "encoder._blocks.22._se_reduce.weight", "encoder._blocks.22._se_reduce.bias", "encoder._blocks.22._se_expand.weight", "encoder._blocks.22._se_expand.bias", "encoder._blocks.22._project_conv.weight", "encoder._blocks.22._bn2.weight", "encoder._blocks.22._bn2.bias", "encoder._blocks.22._bn2.running_mean", "encoder._blocks.22._bn2.running_var", "encoder._blocks.23._expand_conv.weight", "encoder._blocks.23._bn0.weight", "encoder._blocks.23._bn0.bias", "encoder._blocks.23._bn0.running_mean", "encoder._blocks.23._bn0.running_var", "encoder._blocks.23._depthwise_conv.weight", "encoder._blocks.23._bn1.weight", "encoder._blocks.23._bn1.bias", "encoder._blocks.23._bn1.running_mean", "encoder._blocks.23._bn1.running_var", "encoder._blocks.23._se_reduce.weight", "encoder._blocks.23._se_reduce.bias", "encoder._blocks.23._se_expand.weight", "encoder._blocks.23._se_expand.bias", "encoder._blocks.23._project_conv.weight", "encoder._blocks.23._bn2.weight", "encoder._blocks.23._bn2.bias", "encoder._blocks.23._bn2.running_mean", "encoder._blocks.23._bn2.running_var", "encoder._blocks.24._expand_conv.weight", "encoder._blocks.24._bn0.weight", "encoder._blocks.24._bn0.bias", "encoder._blocks.24._bn0.running_mean", "encoder._blocks.24._bn0.running_var", "encoder._blocks.24._depthwise_conv.weight", "encoder._blocks.24._bn1.weight", "encoder._blocks.24._bn1.bias", "encoder._blocks.24._bn1.running_mean", "encoder._blocks.24._bn1.running_var", "encoder._blocks.24._se_reduce.weight", "encoder._blocks.24._se_reduce.bias", "encoder._blocks.24._se_expand.weight", "encoder._blocks.24._se_expand.bias", "encoder._blocks.24._project_conv.weight", "encoder._blocks.24._bn2.weight", "encoder._blocks.24._bn2.bias", "encoder._blocks.24._bn2.running_mean", "encoder._blocks.24._bn2.running_var", "encoder._blocks.25._expand_conv.weight", "encoder._blocks.25._bn0.weight", "encoder._blocks.25._bn0.bias", "encoder._blocks.25._bn0.running_mean", "encoder._blocks.25._bn0.running_var", "encoder._blocks.25._depthwise_conv.weight", "encoder._blocks.25._bn1.weight", "encoder._blocks.25._bn1.bias", "encoder._blocks.25._bn1.running_mean", "encoder._blocks.25._bn1.running_var", "encoder._blocks.25._se_reduce.weight", "encoder._blocks.25._se_reduce.bias", "encoder._blocks.25._se_expand.weight", "encoder._blocks.25._se_expand.bias", "encoder._blocks.25._project_conv.weight", "encoder._blocks.25._bn2.weight", "encoder._blocks.25._bn2.bias", "encoder._blocks.25._bn2.running_mean", "encoder._blocks.25._bn2.running_var", "encoder._conv_head.weight", "encoder._bn1.weight", "encoder._bn1.bias", "encoder._bn1.running_mean", "encoder._bn1.running_var". 
	size mismatch for decoder.blocks.0.conv1.0.weight: copying a param with shape torch.Size([256, 520, 3, 3]) from checkpoint, the shape in current model is torch.Size([256, 3072, 3, 3]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([32, 520, 1, 1]) from checkpoint, the shape in current model is torch.Size([192, 3072, 1, 1]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([32]) from checkpoint, the shape in current model is torch.Size([192]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([520, 32, 1, 1]) from checkpoint, the shape in current model is torch.Size([3072, 192, 1, 1]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([520]) from checkpoint, the shape in current model is torch.Size([3072]).
	size mismatch for decoder.blocks.0.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 520, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 3072, 1, 1]).
	size mismatch for decoder.blocks.1.conv1.0.weight: copying a param with shape torch.Size([128, 304, 3, 3]) from checkpoint, the shape in current model is torch.Size([128, 768, 3, 3]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([19, 304, 1, 1]) from checkpoint, the shape in current model is torch.Size([48, 768, 1, 1]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([19]) from checkpoint, the shape in current model is torch.Size([48]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([304, 19, 1, 1]) from checkpoint, the shape in current model is torch.Size([768, 48, 1, 1]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([304]) from checkpoint, the shape in current model is torch.Size([768]).
	size mismatch for decoder.blocks.1.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 304, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 768, 1, 1]).
	size mismatch for decoder.blocks.2.conv1.0.weight: copying a param with shape torch.Size([64, 160, 3, 3]) from checkpoint, the shape in current model is torch.Size([64, 384, 3, 3]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([10, 160, 1, 1]) from checkpoint, the shape in current model is torch.Size([24, 384, 1, 1]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([10]) from checkpoint, the shape in current model is torch.Size([24]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([160, 10, 1, 1]) from checkpoint, the shape in current model is torch.Size([384, 24, 1, 1]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([160]) from checkpoint, the shape in current model is torch.Size([384]).
	size mismatch for decoder.blocks.2.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 160, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 384, 1, 1]).
	size mismatch for decoder.blocks.3.conv1.0.weight: copying a param with shape torch.Size([32, 104, 3, 3]) from checkpoint, the shape in current model is torch.Size([32, 128, 3, 3]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([6, 104, 1, 1]) from checkpoint, the shape in current model is torch.Size([8, 128, 1, 1]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([6]) from checkpoint, the shape in current model is torch.Size([8]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([104, 6, 1, 1]) from checkpoint, the shape in current model is torch.Size([128, 8, 1, 1]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([104]) from checkpoint, the shape in current model is torch.Size([128]).
	size mismatch for decoder.blocks.3.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 104, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 128, 1, 1]).

**Warnings / warning-like lines**

- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Field()` function, which has no effect in 
- warnings.warn(
- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'frozen' attribute with value True was provided to the `Field()` function, which has no effect in
- [1;32m    137[0m                 [0mwarnings[0m[0;34m.[0m[0mwarn[0m[0;34m([0m[0mtext[0m[0;34m,[0m [0mstacklevel[0m[0;34m=[0m[0;34m-[0m[0;36m1[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

## Observed Dependency Summary

**Referenced checkpoints**

- best_model_effb3_phase9_ddp.pt
- best.pt
- best_model_phase10.pt

**Referenced datasets**

- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet

**External files**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- open[w]: submission.csv

**Required runtime assumptions**

- Assumes Kaggle input mounts are available.
- Assumes offline wheel files are available under the input mounts.
- Assumes ultralytics/YOLO is available for lead localization.
- Assumes PyTorch checkpoint loading is available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.

**Outputs created or updated**

- open: submission.csv
- open[w]: submission.csv

## Phase 1 Closure Status

| Field | Value |
| --- | --- |
| Notebook summary | present |
| Editorial cell coverage | 7/7 |
| Editorial output translations | 0 |
| Delta notes | 5 |
| Open questions | 0 |
| Confidence | high |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- EffB3 deployment notebook that replaces the earlier V41 fix with a more explicitly robust V42 inference engine.
- The notebook still values mapping diagnostics, but the main change is a stronger final engine with deskewing, trimming, model selection, and quality gating.

**Delta notes**

- Compared with notebook (54), the diagnostic cell stays in place but the main engine is replaced by a more heavily quality-gated V42 path.
- The apparent motivation is to bring the EfficientNet-B3 branch into the active deployment flow and determine whether it should replace or complement the older segmentation weights.
- It retains the compact no-internet runner, the renderer, and the final validation shell from the prior deployment families.
- The workflow effect is a new inference-routing era where the notebook must decide between old and new checkpoints instead of assuming one inherited phase-10 default.
- What becomes obsolete is the assumption that the older single-model path is sufficient on its own; checkpoint selection and fallback logic become part of the deployment contract.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb`, cell count changed from 7 to 7, stored output types changed from 11 to 9, and exact shared cell sources = 5.
- New imports: `math`
- Removed imports: None
- New model refs: None
- Removed model refs: `YOLO: /kaggle/input/ecg-final-models1/best.pt`
- New first-line titles: `# --- Cell 22 (REPLACEMENT): V42 Robust Inference (Deskew + Trim + Model-Select + Quality Gate) ---`, `# --- Cell 2: Offline install/import fix (NO internet) + Path Resolver ---`
- Removed first-line titles: `# --- Cell 22: V41 FIX (Smart pid->image path index + sanity check + keep V40 pipeline) ---`, `# --- Cell 2: Offline install/import fix + model path resolver (NO internet) ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
- Stored notebook outputs contain 1 execution error(s); treat those cells as unresolved at snapshot time.
- Stored outputs include 4 warning-like lines worth checking during reruns.
- Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.
- Notebook depends on both object detection and segmentation stacks, increasing environment complexity.
- Checkpoint loading is embedded in the workflow; model file availability is a runtime prerequisite.

## Cell-By-Cell Audit

### Cell 1

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 1 |
| First non-empty line | `# --- Cell 1: Smart Offline Install (SAFE & MINIMAL) ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Uses the smallest safe offline install path, reducing package churn so the notebook can focus on inference rather than repeated environment repair.

**Imports**

- sys
- os
- glob
- subprocess
- torch

**Functions defined**

- ok_whl

**Classes defined**

- None

**Constants / bindings**

- FORBIDDEN = ['torch', 'torchvision', 'torchaudio', 'numpy', 'pandas', 'opencv', 'matplotlib', 'scipy', 'pillow']
- NEEDED_HINTS = ['segmentation_models_pytorch', 'ultralytics', 'timm']
- all_whls = /kaggle/input/**/*.whl
- n = p
- ok = 0
- picked = ['p']
- py_tag = cpsys.version_info.majorsys.version_info.minor

**Paths mentioned**

- /kaggle/input/**/*.whl

**File reads**

- glob.glob: /kaggle/input/**/*.whl

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install whl --no-deps --ignore-installed --quiet

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 7 line(s); excerpt: ⚙️ Smart offline install (minimal + compatible wheels only)... 🐍 Python tag: cp311 📦 Found wheels: 95 ✅ Will try install: 3 wheels ✅ Installed 3/3 wheels safely. ⚡ Torch: 2.6.0+cu1...

**Exceptions**

- None

**Warnings**

- None

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 2 |
| First non-empty line | `# --- Cell 2: Offline install/import fix (NO internet) + Path Resolver ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Imports the runtime stack and resolves model and data paths dynamically, making the notebook less dependent on one hard-coded Kaggle directory layout.

**Imports**

- sys
- os
- glob
- subprocess
- site
- importlib
- torch
- segmentation_models_pytorch
- pyarrow

**Functions defined**

- ensure_pkg

**Classes defined**

- None

**Constants / bindings**

- NEW_UNET_PATH = /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- OLD_UNET_PATH = /kaggle/input/ecg-final-models1/best_model_phase10.pth
- YOLO_PATH = /kaggle/input/ecg-final-models1/best.pt
- target = subscript[0]
- wheels = /kaggle/input/**/*{wheel_hint}*.whl

**Paths mentioned**

- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth

**File reads**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install subscript[0] --no-deps --ignore-installed --quiet

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt

**Stored outputs**

- stream[stdout] with 1 line(s); excerpt: 🔧 Cell 2: Offline install/import fix (no internet).
- stream[stderr] with 4 line(s); excerpt: /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Fi...
- stream[stdout] with 14 line(s); excerpt: ✅ Already available: timm ✅ Installed offline: segmentation_models_pytorch ✅ Already available: ultralytics ✅ pyarrow available (parquet OK) ------ Environment Check ------ torch: ...

**Exceptions**

- None

**Warnings**

- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Field()` function, which has no effect in 
- warnings.warn(
- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'frozen' attribute with value True was provided to the `Field()` function, which has no effect in

### Cell 3

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 3 |
| First non-empty line | `# --- Cell 2.5: Attach NEW trained model (EffB3) to inference ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Attaches the newer EfficientNet-B3 checkpoint to the inference stack and defines how it should replace or complement the older segmentation weights.

**Imports**

- os
- shutil

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- NEW_BEST_DST = /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- NEW_BEST_SRC = /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

**Paths mentioned**

- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

**File reads**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

**Stored outputs**

- stream[stdout] with 2 line(s); excerpt: ✅ NEW model ready: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth Exists: True

**Exceptions**

- None

**Warnings**

- None

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 4 |
| First non-empty line | `# # --- الخلية 3: محرك الرسم الحي (Ultimate Renderer) - [M3: UPDATED] ---` |
| Role summary | Rendering / synthetic ECG image generation cell. |

**Editorial interpretation**

- Keeps the high-quality renderer in the notebook as a debugging surface, so predicted masks and extracted signals can still be inspected visually before submission export.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- None

**Paths mentioned**

- None

**File reads**

- None

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 1 line(s); excerpt: ✅ Cell 3 disabled: Renderer/PTB-XL not needed for submission.

**Exceptions**

- None

**Warnings**

- None

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 5 |
| First non-empty line | `# --- NEW DIAGNOSTIC CELL: Check real coverage of pid->path mapping ---` |
| Role summary | Definition cell that defines 4 function(s). |

**Editorial interpretation**

- Measures how many competition IDs can be matched to discovered image files, exposing mapping gaps before an expensive inference pass begins.

**Imports**

- os
- glob
- re
- pandas
- collections

**Functions defined**

- clean_pid
- parse_rid
- first_int
- get_path

**Classes defined**

- None

**Constants / bindings**

- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- hits = 0
- miss = ['pid']

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- {IMAGE_DIR}/sample_submission.parquet

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 30 line(s); excerpt: ✅ Unique PIDs sampled: 2 🧪 Coverage: 2/2 = 100.0% ❌ Missing PID examples (up to 25): [] 📌 Example image basenames (first 25): - 2352854581 - 1053922973 - 735384893-0005 - 735384893...

**Exceptions**

- None

**Warnings**

- None

### Cell 6

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 6 |
| First non-empty line | `# --- Cell 22 (REPLACEMENT): V42 Robust Inference (Deskew + Trim + Model-Select + Quality Gate) ---` |
| Role summary | Inference / submission generation cell. |

**Editorial interpretation**

- Replaces the prior V41 path with a V42 robust inference engine that explicitly deskews the image, trims strips, selects between models, and quality-gates the recovered signal before export.

**Imports**

- gc
- os
- csv
- glob
- math
- numpy
- pandas
- cv2
- torch
- collections
- tqdm
- scipy.signal
- segmentation_models_pytorch
- ultralytics

**Functions defined**

- _normalize_lead_name
- build_unet_resnet50
- clean_pid
- get_image_path
- safe_read_rgb
- rotate_keep_white
- estimate_skew_angle
- preprocess_remove_grid_rgb
- apply_high_pass
- viterbi_dp_y
- viterbi_adaptive_y
- trim_prob_map
- quality_score
- get_crops_yolo_mapped
- prepare_unet_batch
- predict_probmaps
- prob_to_signal_mv
- compute_patient_leads

**Classes defined**

- None

**Constants / bindings**

- DP_MAX_W = 1500
- DP_SMOOTH = 0.45
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE = 8
- MAX_W = 2048
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv
- TARGET_H = 256
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- YOLO_CONF = 0.08
- YOLO_INF_MAX = 1280
- angles = ['ang']
- best_prev = stacked[which]
- c_0 = dp[idx]
- idx = subscript[0]
- img_inf = img_rgb
- items = []
- li = lead_indices[j]
- mtx = patient_cache[pid]
- nw = 2048
- out = []
- p = prob[y]
- ppmv = 250.0
- prev = dp[idx]
- scale = 1.0
- t_len = 5000
- val = v
- w_i = widths[i]

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- open: submission.csv

**File writes**

- open: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 11 line(s); excerpt: ⚡ Device: cuda 📌 Paths exist: | NEW: True | OLD: True | YOLO: True ✅ Template rows: 75000 ✅ test.csv columns: ['id', 'lead', 'fs', 'number_of_rows'] ✅ fs_map: 2 | patient_lengths(f...
- error RuntimeError: Error(s) in loading state_dict for Unet:
	Missing key(s) in state_dict: "encoder.conv1.weight", "encoder.bn1.weight", "encoder.bn1.bias", "encoder.bn1.running_mean", "encoder.bn1.running_var", "encoder.layer1.0.conv1.weight", "encoder.layer1.0.bn1.weight", "encoder.layer1.0.bn1.bias", "encoder.layer1.0.bn1.running_mean", "encoder.layer1.0.bn1.running_var", "encoder.layer1.0.conv2.weight", "encoder.layer1.0.bn2.weight", "encoder.layer1.0.bn2.bias", "encoder.layer1.0.bn2.running_mean", "encoder.layer1.0.bn2.running_var", "encoder.layer1.0.conv3.weight", "encoder.layer1.0.bn3.weight", "encoder.layer1.0.bn3.bias", "encoder.layer1.0.bn3.running_mean", "encoder.layer1.0.bn3.running_var", "encoder.layer1.0.downsample.0.weight", "encoder.layer1.0.downsample.1.weight", "encoder.layer1.0.downsample.1.bias", "encoder.layer1.0.downsample.1.running_mean", "encoder.layer1.0.downsample.1.running_var", "encoder.layer1.1.conv1.weight", "encoder.layer1.1.bn1.weight", "encoder.layer1.1.bn1.bias", "encoder.layer1.1.bn1.running_mean", "encoder.layer1.1.bn1.running_var", "encoder.layer1.1.conv2.weight", "encoder.layer1.1.bn2.weight", "encoder.layer1.1.bn2.bias", "encoder.layer1.1.bn2.running_mean", "encoder.layer1.1.bn2.running_var", "encoder.layer1.1.conv3.weight", "encoder.layer1.1.bn3.weight", "encoder.layer1.1.bn3.bias", "encoder.layer1.1.bn3.running_mean", "encoder.layer1.1.bn3.running_var", "encoder.layer1.2.conv1.weight", "encoder.layer1.2.bn1.weight", "encoder.layer1.2.bn1.bias", "encoder.layer1.2.bn1.running_mean", "encoder.layer1.2.bn1.running_var", "encoder.layer1.2.conv2.weight", "encoder.layer1.2.bn2.weight", "encoder.layer1.2.bn2.bias", "encoder.layer1.2.bn2.running_mean", "encoder.layer1.2.bn2.running_var", "encoder.layer1.2.conv3.weight", "encoder.layer1.2.bn3.weight", "encoder.layer1.2.bn3.bias", "encoder.layer1.2.bn3.running_mean", "encoder.layer1.2.bn3.running_var", "encoder.layer2.0.conv1.weight", "encoder.layer2.0.bn1.weight", "encoder.layer2.0.bn1.bias", "encoder.layer2.0.bn1.running_mean", "encoder.layer2.0.bn1.running_var", "encoder.layer2.0.conv2.weight", "encoder.layer2.0.bn2.weight", "encoder.layer2.0.bn2.bias", "encoder.layer2.0.bn2.running_mean", "encoder.layer2.0.bn2.running_var", "encoder.layer2.0.conv3.weight", "encoder.layer2.0.bn3.weight", "encoder.layer2.0.bn3.bias", "encoder.layer2.0.bn3.running_mean", "encoder.layer2.0.bn3.running_var", "encoder.layer2.0.downsample.0.weight", "encoder.layer2.0.downsample.1.weight", "encoder.layer2.0.downsample.1.bias", "encoder.layer2.0.downsample.1.running_mean", "encoder.layer2.0.downsample.1.running_var", "encoder.layer2.1.conv1.weight", "encoder.layer2.1.bn1.weight", "encoder.layer2.1.bn1.bias", "encoder.layer2.1.bn1.running_mean", "encoder.layer2.1.bn1.running_var", "encoder.layer2.1.conv2.weight", "encoder.layer2.1.bn2.weight", "encoder.layer2.1.bn2.bias", "encoder.layer2.1.bn2.running_mean", "encoder.layer2.1.bn2.running_var", "encoder.layer2.1.conv3.weight", "encoder.layer2.1.bn3.weight", "encoder.layer2.1.bn3.bias", "encoder.layer2.1.bn3.running_mean", "encoder.layer2.1.bn3.running_var", "encoder.layer2.2.conv1.weight", "encoder.layer2.2.bn1.weight", "encoder.layer2.2.bn1.bias", "encoder.layer2.2.bn1.running_mean", "encoder.layer2.2.bn1.running_var", "encoder.layer2.2.conv2.weight", "encoder.layer2.2.bn2.weight", "encoder.layer2.2.bn2.bias", "encoder.layer2.2.bn2.running_mean", "encoder.layer2.2.bn2.running_var", "encoder.layer2.2.conv3.weight", "encoder.layer2.2.bn3.weight", "encoder.layer2.2.bn3.bias", "encoder.layer2.2.bn3.running_mean", "encoder.layer2.2.bn3.running_var", "encoder.layer2.3.conv1.weight", "encoder.layer2.3.bn1.weight", "encoder.layer2.3.bn1.bias", "encoder.layer2.3.bn1.running_mean", "encoder.layer2.3.bn1.running_var", "encoder.layer2.3.conv2.weight", "encoder.layer2.3.bn2.weight", "encoder.layer2.3.bn2.bias", "encoder.layer2.3.bn2.running_mean", "encoder.layer2.3.bn2.running_var", "encoder.layer2.3.conv3.weight", "encoder.layer2.3.bn3.weight", "encoder.layer2.3.bn3.bias", "encoder.layer2.3.bn3.running_mean", "encoder.layer2.3.bn3.running_var", "encoder.layer3.0.conv1.weight", "encoder.layer3.0.bn1.weight", "encoder.layer3.0.bn1.bias", "encoder.layer3.0.bn1.running_mean", "encoder.layer3.0.bn1.running_var", "encoder.layer3.0.conv2.weight", "encoder.layer3.0.bn2.weight", "encoder.layer3.0.bn2.bias", "encoder.layer3.0.bn2.running_mean", "encoder.layer3.0.bn2.running_var", "encoder.layer3.0.conv3.weight", "encoder.layer3.0.bn3.weight", "encoder.layer3.0.bn3.bias", "encoder.layer3.0.bn3.running_mean", "encoder.layer3.0.bn3.running_var", "encoder.layer3.0.downsample.0.weight", "encoder.layer3.0.downsample.1.weight", "encoder.layer3.0.downsample.1.bias", "encoder.layer3.0.downsample.1.running_mean", "encoder.layer3.0.downsample.1.running_var", "encoder.layer3.1.conv1.weight", "encoder.layer3.1.bn1.weight", "encoder.layer3.1.bn1.bias", "encoder.layer3.1.bn1.running_mean", "encoder.layer3.1.bn1.running_var", "encoder.layer3.1.conv2.weight", "encoder.layer3.1.bn2.weight", "encoder.layer3.1.bn2.bias", "encoder.layer3.1.bn2.running_mean", "encoder.layer3.1.bn2.running_var", "encoder.layer3.1.conv3.weight", "encoder.layer3.1.bn3.weight", "encoder.layer3.1.bn3.bias", "encoder.layer3.1.bn3.running_mean", "encoder.layer3.1.bn3.running_var", "encoder.layer3.2.conv1.weight", "encoder.layer3.2.bn1.weight", "encoder.layer3.2.bn1.bias", "encoder.layer3.2.bn1.running_mean", "encoder.layer3.2.bn1.running_var", "encoder.layer3.2.conv2.weight", "encoder.layer3.2.bn2.weight", "encoder.layer3.2.bn2.bias", "encoder.layer3.2.bn2.running_mean", "encoder.layer3.2.bn2.running_var", "encoder.layer3.2.conv3.weight", "encoder.layer3.2.bn3.weight", "encoder.layer3.2.bn3.bias", "encoder.layer3.2.bn3.running_mean", "encoder.layer3.2.bn3.running_var", "encoder.layer3.3.conv1.weight", "encoder.layer3.3.bn1.weight", "encoder.layer3.3.bn1.bias", "encoder.layer3.3.bn1.running_mean", "encoder.layer3.3.bn1.running_var", "encoder.layer3.3.conv2.weight", "encoder.layer3.3.bn2.weight", "encoder.layer3.3.bn2.bias", "encoder.layer3.3.bn2.running_mean", "encoder.layer3.3.bn2.running_var", "encoder.layer3.3.conv3.weight", "encoder.layer3.3.bn3.weight", "encoder.layer3.3.bn3.bias", "encoder.layer3.3.bn3.running_mean", "encoder.layer3.3.bn3.running_var", "encoder.layer3.4.conv1.weight", "encoder.layer3.4.bn1.weight", "encoder.layer3.4.bn1.bias", "encoder.layer3.4.bn1.running_mean", "encoder.layer3.4.bn1.running_var", "encoder.layer3.4.conv2.weight", "encoder.layer3.4.bn2.weight", "encoder.layer3.4.bn2.bias", "encoder.layer3.4.bn2.running_mean", "encoder.layer3.4.bn2.running_var", "encoder.layer3.4.conv3.weight", "encoder.layer3.4.bn3.weight", "encoder.layer3.4.bn3.bias", "encoder.layer3.4.bn3.running_mean", "encoder.layer3.4.bn3.running_var", "encoder.layer3.5.conv1.weight", "encoder.layer3.5.bn1.weight", "encoder.layer3.5.bn1.bias", "encoder.layer3.5.bn1.running_mean", "encoder.layer3.5.bn1.running_var", "encoder.layer3.5.conv2.weight", "encoder.layer3.5.bn2.weight", "encoder.layer3.5.bn2.bias", "encoder.layer3.5.bn2.running_mean", "encoder.layer3.5.bn2.running_var", "encoder.layer3.5.conv3.weight", "encoder.layer3.5.bn3.weight", "encoder.layer3.5.bn3.bias", "encoder.layer3.5.bn3.running_mean", "encoder.layer3.5.bn3.running_var", "encoder.layer4.0.conv1.weight", "encoder.layer4.0.bn1.weight", "encoder.layer4.0.bn1.bias", "encoder.layer4.0.bn1.running_mean", "encoder.layer4.0.bn1.running_var", "encoder.layer4.0.conv2.weight", "encoder.layer4.0.bn2.weight", "encoder.layer4.0.bn2.bias", "encoder.layer4.0.bn2.running_mean", "encoder.layer4.0.bn2.running_var", "encoder.layer4.0.conv3.weight", "encoder.layer4.0.bn3.weight", "encoder.layer4.0.bn3.bias", "encoder.layer4.0.bn3.running_mean", "encoder.layer4.0.bn3.running_var", "encoder.layer4.0.downsample.0.weight", "encoder.layer4.0.downsample.1.weight", "encoder.layer4.0.downsample.1.bias", "encoder.layer4.0.downsample.1.running_mean", "encoder.layer4.0.downsample.1.running_var", "encoder.layer4.1.conv1.weight", "encoder.layer4.1.bn1.weight", "encoder.layer4.1.bn1.bias", "encoder.layer4.1.bn1.running_mean", "encoder.layer4.1.bn1.running_var", "encoder.layer4.1.conv2.weight", "encoder.layer4.1.bn2.weight", "encoder.layer4.1.bn2.bias", "encoder.layer4.1.bn2.running_mean", "encoder.layer4.1.bn2.running_var", "encoder.layer4.1.conv3.weight", "encoder.layer4.1.bn3.weight", "encoder.layer4.1.bn3.bias", "encoder.layer4.1.bn3.running_mean", "encoder.layer4.1.bn3.running_var", "encoder.layer4.2.conv1.weight", "encoder.layer4.2.bn1.weight", "encoder.layer4.2.bn1.bias", "encoder.layer4.2.bn1.running_mean", "encoder.layer4.2.bn1.running_var", "encoder.layer4.2.conv2.weight", "encoder.layer4.2.bn2.weight", "encoder.layer4.2.bn2.bias", "encoder.layer4.2.bn2.running_mean", "encoder.layer4.2.bn2.running_var", "encoder.layer4.2.conv3.weight", "encoder.layer4.2.bn3.weight", "encoder.layer4.2.bn3.bias", "encoder.layer4.2.bn3.running_mean", "encoder.layer4.2.bn3.running_var". 
	Unexpected key(s) in state_dict: "encoder._conv_stem.weight", "encoder._bn0.weight", "encoder._bn0.bias", "encoder._bn0.running_mean", "encoder._bn0.running_var", "encoder._blocks.0._depthwise_conv.weight", "encoder._blocks.0._bn1.weight", "encoder._blocks.0._bn1.bias", "encoder._blocks.0._bn1.running_mean", "encoder._blocks.0._bn1.running_var", "encoder._blocks.0._se_reduce.weight", "encoder._blocks.0._se_reduce.bias", "encoder._blocks.0._se_expand.weight", "encoder._blocks.0._se_expand.bias", "encoder._blocks.0._project_conv.weight", "encoder._blocks.0._bn2.weight", "encoder._blocks.0._bn2.bias", "encoder._blocks.0._bn2.running_mean", "encoder._blocks.0._bn2.running_var", "encoder._blocks.1._depthwise_conv.weight", "encoder._blocks.1._bn1.weight", "encoder._blocks.1._bn1.bias", "encoder._blocks.1._bn1.running_mean", "encoder._blocks.1._bn1.running_var", "encoder._blocks.1._se_reduce.weight", "encoder._blocks.1._se_reduce.bias", "encoder._blocks.1._se_expand.weight", "encoder._blocks.1._se_expand.bias", "encoder._blocks.1._project_conv.weight", "encoder._blocks.1._bn2.weight", "encoder._blocks.1._bn2.bias", "encoder._blocks.1._bn2.running_mean", "encoder._blocks.1._bn2.running_var", "encoder._blocks.2._expand_conv.weight", "encoder._blocks.2._bn0.weight", "encoder._blocks.2._bn0.bias", "encoder._blocks.2._bn0.running_mean", "encoder._blocks.2._bn0.running_var", "encoder._blocks.2._depthwise_conv.weight", "encoder._blocks.2._bn1.weight", "encoder._blocks.2._bn1.bias", "encoder._blocks.2._bn1.running_mean", "encoder._blocks.2._bn1.running_var", "encoder._blocks.2._se_reduce.weight", "encoder._blocks.2._se_reduce.bias", "encoder._blocks.2._se_expand.weight", "encoder._blocks.2._se_expand.bias", "encoder._blocks.2._project_conv.weight", "encoder._blocks.2._bn2.weight", "encoder._blocks.2._bn2.bias", "encoder._blocks.2._bn2.running_mean", "encoder._blocks.2._bn2.running_var", "encoder._blocks.3._expand_conv.weight", "encoder._blocks.3._bn0.weight", "encoder._blocks.3._bn0.bias", "encoder._blocks.3._bn0.running_mean", "encoder._blocks.3._bn0.running_var", "encoder._blocks.3._depthwise_conv.weight", "encoder._blocks.3._bn1.weight", "encoder._blocks.3._bn1.bias", "encoder._blocks.3._bn1.running_mean", "encoder._blocks.3._bn1.running_var", "encoder._blocks.3._se_reduce.weight", "encoder._blocks.3._se_reduce.bias", "encoder._blocks.3._se_expand.weight", "encoder._blocks.3._se_expand.bias", "encoder._blocks.3._project_conv.weight", "encoder._blocks.3._bn2.weight", "encoder._blocks.3._bn2.bias", "encoder._blocks.3._bn2.running_mean", "encoder._blocks.3._bn2.running_var", "encoder._blocks.4._expand_conv.weight", "encoder._blocks.4._bn0.weight", "encoder._blocks.4._bn0.bias", "encoder._blocks.4._bn0.running_mean", "encoder._blocks.4._bn0.running_var", "encoder._blocks.4._depthwise_conv.weight", "encoder._blocks.4._bn1.weight", "encoder._blocks.4._bn1.bias", "encoder._blocks.4._bn1.running_mean", "encoder._blocks.4._bn1.running_var", "encoder._blocks.4._se_reduce.weight", "encoder._blocks.4._se_reduce.bias", "encoder._blocks.4._se_expand.weight", "encoder._blocks.4._se_expand.bias", "encoder._blocks.4._project_conv.weight", "encoder._blocks.4._bn2.weight", "encoder._blocks.4._bn2.bias", "encoder._blocks.4._bn2.running_mean", "encoder._blocks.4._bn2.running_var", "encoder._blocks.5._expand_conv.weight", "encoder._blocks.5._bn0.weight", "encoder._blocks.5._bn0.bias", "encoder._blocks.5._bn0.running_mean", "encoder._blocks.5._bn0.running_var", "encoder._blocks.5._depthwise_conv.weight", "encoder._blocks.5._bn1.weight", "encoder._blocks.5._bn1.bias", "encoder._blocks.5._bn1.running_mean", "encoder._blocks.5._bn1.running_var", "encoder._blocks.5._se_reduce.weight", "encoder._blocks.5._se_reduce.bias", "encoder._blocks.5._se_expand.weight", "encoder._blocks.5._se_expand.bias", "encoder._blocks.5._project_conv.weight", "encoder._blocks.5._bn2.weight", "encoder._blocks.5._bn2.bias", "encoder._blocks.5._bn2.running_mean", "encoder._blocks.5._bn2.running_var", "encoder._blocks.6._expand_conv.weight", "encoder._blocks.6._bn0.weight", "encoder._blocks.6._bn0.bias", "encoder._blocks.6._bn0.running_mean", "encoder._blocks.6._bn0.running_var", "encoder._blocks.6._depthwise_conv.weight", "encoder._blocks.6._bn1.weight", "encoder._blocks.6._bn1.bias", "encoder._blocks.6._bn1.running_mean", "encoder._blocks.6._bn1.running_var", "encoder._blocks.6._se_reduce.weight", "encoder._blocks.6._se_reduce.bias", "encoder._blocks.6._se_expand.weight", "encoder._blocks.6._se_expand.bias", "encoder._blocks.6._project_conv.weight", "encoder._blocks.6._bn2.weight", "encoder._blocks.6._bn2.bias", "encoder._blocks.6._bn2.running_mean", "encoder._blocks.6._bn2.running_var", "encoder._blocks.7._expand_conv.weight", "encoder._blocks.7._bn0.weight", "encoder._blocks.7._bn0.bias", "encoder._blocks.7._bn0.running_mean", "encoder._blocks.7._bn0.running_var", "encoder._blocks.7._depthwise_conv.weight", "encoder._blocks.7._bn1.weight", "encoder._blocks.7._bn1.bias", "encoder._blocks.7._bn1.running_mean", "encoder._blocks.7._bn1.running_var", "encoder._blocks.7._se_reduce.weight", "encoder._blocks.7._se_reduce.bias", "encoder._blocks.7._se_expand.weight", "encoder._blocks.7._se_expand.bias", "encoder._blocks.7._project_conv.weight", "encoder._blocks.7._bn2.weight", "encoder._blocks.7._bn2.bias", "encoder._blocks.7._bn2.running_mean", "encoder._blocks.7._bn2.running_var", "encoder._blocks.8._expand_conv.weight", "encoder._blocks.8._bn0.weight", "encoder._blocks.8._bn0.bias", "encoder._blocks.8._bn0.running_mean", "encoder._blocks.8._bn0.running_var", "encoder._blocks.8._depthwise_conv.weight", "encoder._blocks.8._bn1.weight", "encoder._blocks.8._bn1.bias", "encoder._blocks.8._bn1.running_mean", "encoder._blocks.8._bn1.running_var", "encoder._blocks.8._se_reduce.weight", "encoder._blocks.8._se_reduce.bias", "encoder._blocks.8._se_expand.weight", "encoder._blocks.8._se_expand.bias", "encoder._blocks.8._project_conv.weight", "encoder._blocks.8._bn2.weight", "encoder._blocks.8._bn2.bias", "encoder._blocks.8._bn2.running_mean", "encoder._blocks.8._bn2.running_var", "encoder._blocks.9._expand_conv.weight", "encoder._blocks.9._bn0.weight", "encoder._blocks.9._bn0.bias", "encoder._blocks.9._bn0.running_mean", "encoder._blocks.9._bn0.running_var", "encoder._blocks.9._depthwise_conv.weight", "encoder._blocks.9._bn1.weight", "encoder._blocks.9._bn1.bias", "encoder._blocks.9._bn1.running_mean", "encoder._blocks.9._bn1.running_var", "encoder._blocks.9._se_reduce.weight", "encoder._blocks.9._se_reduce.bias", "encoder._blocks.9._se_expand.weight", "encoder._blocks.9._se_expand.bias", "encoder._blocks.9._project_conv.weight", "encoder._blocks.9._bn2.weight", "encoder._blocks.9._bn2.bias", "encoder._blocks.9._bn2.running_mean", "encoder._blocks.9._bn2.running_var", "encoder._blocks.10._expand_conv.weight", "encoder._blocks.10._bn0.weight", "encoder._blocks.10._bn0.bias", "encoder._blocks.10._bn0.running_mean", "encoder._blocks.10._bn0.running_var", "encoder._blocks.10._depthwise_conv.weight", "encoder._blocks.10._bn1.weight", "encoder._blocks.10._bn1.bias", "encoder._blocks.10._bn1.running_mean", "encoder._blocks.10._bn1.running_var", "encoder._blocks.10._se_reduce.weight", "encoder._blocks.10._se_reduce.bias", "encoder._blocks.10._se_expand.weight", "encoder._blocks.10._se_expand.bias", "encoder._blocks.10._project_conv.weight", "encoder._blocks.10._bn2.weight", "encoder._blocks.10._bn2.bias", "encoder._blocks.10._bn2.running_mean", "encoder._blocks.10._bn2.running_var", "encoder._blocks.11._expand_conv.weight", "encoder._blocks.11._bn0.weight", "encoder._blocks.11._bn0.bias", "encoder._blocks.11._bn0.running_mean", "encoder._blocks.11._bn0.running_var", "encoder._blocks.11._depthwise_conv.weight", "encoder._blocks.11._bn1.weight", "encoder._blocks.11._bn1.bias", "encoder._blocks.11._bn1.running_mean", "encoder._blocks.11._bn1.running_var", "encoder._blocks.11._se_reduce.weight", "encoder._blocks.11._se_reduce.bias", "encoder._blocks.11._se_expand.weight", "encoder._blocks.11._se_expand.bias", "encoder._blocks.11._project_conv.weight", "encoder._blocks.11._bn2.weight", "encoder._blocks.11._bn2.bias", "encoder._blocks.11._bn2.running_mean", "encoder._blocks.11._bn2.running_var", "encoder._blocks.12._expand_conv.weight", "encoder._blocks.12._bn0.weight", "encoder._blocks.12._bn0.bias", "encoder._blocks.12._bn0.running_mean", "encoder._blocks.12._bn0.running_var", "encoder._blocks.12._depthwise_conv.weight", "encoder._blocks.12._bn1.weight", "encoder._blocks.12._bn1.bias", "encoder._blocks.12._bn1.running_mean", "encoder._blocks.12._bn1.running_var", "encoder._blocks.12._se_reduce.weight", "encoder._blocks.12._se_reduce.bias", "encoder._blocks.12._se_expand.weight", "encoder._blocks.12._se_expand.bias", "encoder._blocks.12._project_conv.weight", "encoder._blocks.12._bn2.weight", "encoder._blocks.12._bn2.bias", "encoder._blocks.12._bn2.running_mean", "encoder._blocks.12._bn2.running_var", "encoder._blocks.13._expand_conv.weight", "encoder._blocks.13._bn0.weight", "encoder._blocks.13._bn0.bias", "encoder._blocks.13._bn0.running_mean", "encoder._blocks.13._bn0.running_var", "encoder._blocks.13._depthwise_conv.weight", "encoder._blocks.13._bn1.weight", "encoder._blocks.13._bn1.bias", "encoder._blocks.13._bn1.running_mean", "encoder._blocks.13._bn1.running_var", "encoder._blocks.13._se_reduce.weight", "encoder._blocks.13._se_reduce.bias", "encoder._blocks.13._se_expand.weight", "encoder._blocks.13._se_expand.bias", "encoder._blocks.13._project_conv.weight", "encoder._blocks.13._bn2.weight", "encoder._blocks.13._bn2.bias", "encoder._blocks.13._bn2.running_mean", "encoder._blocks.13._bn2.running_var", "encoder._blocks.14._expand_conv.weight", "encoder._blocks.14._bn0.weight", "encoder._blocks.14._bn0.bias", "encoder._blocks.14._bn0.running_mean", "encoder._blocks.14._bn0.running_var", "encoder._blocks.14._depthwise_conv.weight", "encoder._blocks.14._bn1.weight", "encoder._blocks.14._bn1.bias", "encoder._blocks.14._bn1.running_mean", "encoder._blocks.14._bn1.running_var", "encoder._blocks.14._se_reduce.weight", "encoder._blocks.14._se_reduce.bias", "encoder._blocks.14._se_expand.weight", "encoder._blocks.14._se_expand.bias", "encoder._blocks.14._project_conv.weight", "encoder._blocks.14._bn2.weight", "encoder._blocks.14._bn2.bias", "encoder._blocks.14._bn2.running_mean", "encoder._blocks.14._bn2.running_var", "encoder._blocks.15._expand_conv.weight", "encoder._blocks.15._bn0.weight", "encoder._blocks.15._bn0.bias", "encoder._blocks.15._bn0.running_mean", "encoder._blocks.15._bn0.running_var", "encoder._blocks.15._depthwise_conv.weight", "encoder._blocks.15._bn1.weight", "encoder._blocks.15._bn1.bias", "encoder._blocks.15._bn1.running_mean", "encoder._blocks.15._bn1.running_var", "encoder._blocks.15._se_reduce.weight", "encoder._blocks.15._se_reduce.bias", "encoder._blocks.15._se_expand.weight", "encoder._blocks.15._se_expand.bias", "encoder._blocks.15._project_conv.weight", "encoder._blocks.15._bn2.weight", "encoder._blocks.15._bn2.bias", "encoder._blocks.15._bn2.running_mean", "encoder._blocks.15._bn2.running_var", "encoder._blocks.16._expand_conv.weight", "encoder._blocks.16._bn0.weight", "encoder._blocks.16._bn0.bias", "encoder._blocks.16._bn0.running_mean", "encoder._blocks.16._bn0.running_var", "encoder._blocks.16._depthwise_conv.weight", "encoder._blocks.16._bn1.weight", "encoder._blocks.16._bn1.bias", "encoder._blocks.16._bn1.running_mean", "encoder._blocks.16._bn1.running_var", "encoder._blocks.16._se_reduce.weight", "encoder._blocks.16._se_reduce.bias", "encoder._blocks.16._se_expand.weight", "encoder._blocks.16._se_expand.bias", "encoder._blocks.16._project_conv.weight", "encoder._blocks.16._bn2.weight", "encoder._blocks.16._bn2.bias", "encoder._blocks.16._bn2.running_mean", "encoder._blocks.16._bn2.running_var", "encoder._blocks.17._expand_conv.weight", "encoder._blocks.17._bn0.weight", "encoder._blocks.17._bn0.bias", "encoder._blocks.17._bn0.running_mean", "encoder._blocks.17._bn0.running_var", "encoder._blocks.17._depthwise_conv.weight", "encoder._blocks.17._bn1.weight", "encoder._blocks.17._bn1.bias", "encoder._blocks.17._bn1.running_mean", "encoder._blocks.17._bn1.running_var", "encoder._blocks.17._se_reduce.weight", "encoder._blocks.17._se_reduce.bias", "encoder._blocks.17._se_expand.weight", "encoder._blocks.17._se_expand.bias", "encoder._blocks.17._project_conv.weight", "encoder._blocks.17._bn2.weight", "encoder._blocks.17._bn2.bias", "encoder._blocks.17._bn2.running_mean", "encoder._blocks.17._bn2.running_var", "encoder._blocks.18._expand_conv.weight", "encoder._blocks.18._bn0.weight", "encoder._blocks.18._bn0.bias", "encoder._blocks.18._bn0.running_mean", "encoder._blocks.18._bn0.running_var", "encoder._blocks.18._depthwise_conv.weight", "encoder._blocks.18._bn1.weight", "encoder._blocks.18._bn1.bias", "encoder._blocks.18._bn1.running_mean", "encoder._blocks.18._bn1.running_var", "encoder._blocks.18._se_reduce.weight", "encoder._blocks.18._se_reduce.bias", "encoder._blocks.18._se_expand.weight", "encoder._blocks.18._se_expand.bias", "encoder._blocks.18._project_conv.weight", "encoder._blocks.18._bn2.weight", "encoder._blocks.18._bn2.bias", "encoder._blocks.18._bn2.running_mean", "encoder._blocks.18._bn2.running_var", "encoder._blocks.19._expand_conv.weight", "encoder._blocks.19._bn0.weight", "encoder._blocks.19._bn0.bias", "encoder._blocks.19._bn0.running_mean", "encoder._blocks.19._bn0.running_var", "encoder._blocks.19._depthwise_conv.weight", "encoder._blocks.19._bn1.weight", "encoder._blocks.19._bn1.bias", "encoder._blocks.19._bn1.running_mean", "encoder._blocks.19._bn1.running_var", "encoder._blocks.19._se_reduce.weight", "encoder._blocks.19._se_reduce.bias", "encoder._blocks.19._se_expand.weight", "encoder._blocks.19._se_expand.bias", "encoder._blocks.19._project_conv.weight", "encoder._blocks.19._bn2.weight", "encoder._blocks.19._bn2.bias", "encoder._blocks.19._bn2.running_mean", "encoder._blocks.19._bn2.running_var", "encoder._blocks.20._expand_conv.weight", "encoder._blocks.20._bn0.weight", "encoder._blocks.20._bn0.bias", "encoder._blocks.20._bn0.running_mean", "encoder._blocks.20._bn0.running_var", "encoder._blocks.20._depthwise_conv.weight", "encoder._blocks.20._bn1.weight", "encoder._blocks.20._bn1.bias", "encoder._blocks.20._bn1.running_mean", "encoder._blocks.20._bn1.running_var", "encoder._blocks.20._se_reduce.weight", "encoder._blocks.20._se_reduce.bias", "encoder._blocks.20._se_expand.weight", "encoder._blocks.20._se_expand.bias", "encoder._blocks.20._project_conv.weight", "encoder._blocks.20._bn2.weight", "encoder._blocks.20._bn2.bias", "encoder._blocks.20._bn2.running_mean", "encoder._blocks.20._bn2.running_var", "encoder._blocks.21._expand_conv.weight", "encoder._blocks.21._bn0.weight", "encoder._blocks.21._bn0.bias", "encoder._blocks.21._bn0.running_mean", "encoder._blocks.21._bn0.running_var", "encoder._blocks.21._depthwise_conv.weight", "encoder._blocks.21._bn1.weight", "encoder._blocks.21._bn1.bias", "encoder._blocks.21._bn1.running_mean", "encoder._blocks.21._bn1.running_var", "encoder._blocks.21._se_reduce.weight", "encoder._blocks.21._se_reduce.bias", "encoder._blocks.21._se_expand.weight", "encoder._blocks.21._se_expand.bias", "encoder._blocks.21._project_conv.weight", "encoder._blocks.21._bn2.weight", "encoder._blocks.21._bn2.bias", "encoder._blocks.21._bn2.running_mean", "encoder._blocks.21._bn2.running_var", "encoder._blocks.22._expand_conv.weight", "encoder._blocks.22._bn0.weight", "encoder._blocks.22._bn0.bias", "encoder._blocks.22._bn0.running_mean", "encoder._blocks.22._bn0.running_var", "encoder._blocks.22._depthwise_conv.weight", "encoder._blocks.22._bn1.weight", "encoder._blocks.22._bn1.bias", "encoder._blocks.22._bn1.running_mean", "encoder._blocks.22._bn1.running_var", "encoder._blocks.22._se_reduce.weight", "encoder._blocks.22._se_reduce.bias", "encoder._blocks.22._se_expand.weight", "encoder._blocks.22._se_expand.bias", "encoder._blocks.22._project_conv.weight", "encoder._blocks.22._bn2.weight", "encoder._blocks.22._bn2.bias", "encoder._blocks.22._bn2.running_mean", "encoder._blocks.22._bn2.running_var", "encoder._blocks.23._expand_conv.weight", "encoder._blocks.23._bn0.weight", "encoder._blocks.23._bn0.bias", "encoder._blocks.23._bn0.running_mean", "encoder._blocks.23._bn0.running_var", "encoder._blocks.23._depthwise_conv.weight", "encoder._blocks.23._bn1.weight", "encoder._blocks.23._bn1.bias", "encoder._blocks.23._bn1.running_mean", "encoder._blocks.23._bn1.running_var", "encoder._blocks.23._se_reduce.weight", "encoder._blocks.23._se_reduce.bias", "encoder._blocks.23._se_expand.weight", "encoder._blocks.23._se_expand.bias", "encoder._blocks.23._project_conv.weight", "encoder._blocks.23._bn2.weight", "encoder._blocks.23._bn2.bias", "encoder._blocks.23._bn2.running_mean", "encoder._blocks.23._bn2.running_var", "encoder._blocks.24._expand_conv.weight", "encoder._blocks.24._bn0.weight", "encoder._blocks.24._bn0.bias", "encoder._blocks.24._bn0.running_mean", "encoder._blocks.24._bn0.running_var", "encoder._blocks.24._depthwise_conv.weight", "encoder._blocks.24._bn1.weight", "encoder._blocks.24._bn1.bias", "encoder._blocks.24._bn1.running_mean", "encoder._blocks.24._bn1.running_var", "encoder._blocks.24._se_reduce.weight", "encoder._blocks.24._se_reduce.bias", "encoder._blocks.24._se_expand.weight", "encoder._blocks.24._se_expand.bias", "encoder._blocks.24._project_conv.weight", "encoder._blocks.24._bn2.weight", "encoder._blocks.24._bn2.bias", "encoder._blocks.24._bn2.running_mean", "encoder._blocks.24._bn2.running_var", "encoder._blocks.25._expand_conv.weight", "encoder._blocks.25._bn0.weight", "encoder._blocks.25._bn0.bias", "encoder._blocks.25._bn0.running_mean", "encoder._blocks.25._bn0.running_var", "encoder._blocks.25._depthwise_conv.weight", "encoder._blocks.25._bn1.weight", "encoder._blocks.25._bn1.bias", "encoder._blocks.25._bn1.running_mean", "encoder._blocks.25._bn1.running_var", "encoder._blocks.25._se_reduce.weight", "encoder._blocks.25._se_reduce.bias", "encoder._blocks.25._se_expand.weight", "encoder._blocks.25._se_expand.bias", "encoder._blocks.25._project_conv.weight", "encoder._blocks.25._bn2.weight", "encoder._blocks.25._bn2.bias", "encoder._blocks.25._bn2.running_mean", "encoder._blocks.25._bn2.running_var", "encoder._conv_head.weight", "encoder._bn1.weight", "encoder._bn1.bias", "encoder._bn1.running_mean", "encoder._bn1.running_var". 
	size mismatch for decoder.blocks.0.conv1.0.weight: copying a param with shape torch.Size([256, 520, 3, 3]) from checkpoint, the shape in current model is torch.Size([256, 3072, 3, 3]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([32, 520, 1, 1]) from checkpoint, the shape in current model is torch.Size([192, 3072, 1, 1]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([32]) from checkpoint, the shape in current model is torch.Size([192]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([520, 32, 1, 1]) from checkpoint, the shape in current model is torch.Size([3072, 192, 1, 1]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([520]) from checkpoint, the shape in current model is torch.Size([3072]).
	size mismatch for decoder.blocks.0.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 520, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 3072, 1, 1]).
	size mismatch for decoder.blocks.1.conv1.0.weight: copying a param with shape torch.Size([128, 304, 3, 3]) from checkpoint, the shape in current model is torch.Size([128, 768, 3, 3]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([19, 304, 1, 1]) from checkpoint, the shape in current model is torch.Size([48, 768, 1, 1]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([19]) from checkpoint, the shape in current model is torch.Size([48]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([304, 19, 1, 1]) from checkpoint, the shape in current model is torch.Size([768, 48, 1, 1]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([304]) from checkpoint, the shape in current model is torch.Size([768]).
	size mismatch for decoder.blocks.1.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 304, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 768, 1, 1]).
	size mismatch for decoder.blocks.2.conv1.0.weight: copying a param with shape torch.Size([64, 160, 3, 3]) from checkpoint, the shape in current model is torch.Size([64, 384, 3, 3]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([10, 160, 1, 1]) from checkpoint, the shape in current model is torch.Size([24, 384, 1, 1]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([10]) from checkpoint, the shape in current model is torch.Size([24]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([160, 10, 1, 1]) from checkpoint, the shape in current model is torch.Size([384, 24, 1, 1]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([160]) from checkpoint, the shape in current model is torch.Size([384]).
	size mismatch for decoder.blocks.2.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 160, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 384, 1, 1]).
	size mismatch for decoder.blocks.3.conv1.0.weight: copying a param with shape torch.Size([32, 104, 3, 3]) from checkpoint, the shape in current model is torch.Size([32, 128, 3, 3]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([6, 104, 1, 1]) from checkpoint, the shape in current model is torch.Size([8, 128, 1, 1]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([6]) from checkpoint, the shape in current model is torch.Size([8]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([104, 6, 1, 1]) from checkpoint, the shape in current model is torch.Size([128, 8, 1, 1]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([104]) from checkpoint, the shape in current model is torch.Size([128]).
	size mismatch for decoder.blocks.3.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 104, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 128, 1, 1]).

**Exceptions**

- RuntimeError: Error(s) in loading state_dict for Unet:
	Missing key(s) in state_dict: "encoder.conv1.weight", "encoder.bn1.weight", "encoder.bn1.bias", "encoder.bn1.running_mean", "encoder.bn1.running_var", "encoder.layer1.0.conv1.weight", "encoder.layer1.0.bn1.weight", "encoder.layer1.0.bn1.bias", "encoder.layer1.0.bn1.running_mean", "encoder.layer1.0.bn1.running_var", "encoder.layer1.0.conv2.weight", "encoder.layer1.0.bn2.weight", "encoder.layer1.0.bn2.bias", "encoder.layer1.0.bn2.running_mean", "encoder.layer1.0.bn2.running_var", "encoder.layer1.0.conv3.weight", "encoder.layer1.0.bn3.weight", "encoder.layer1.0.bn3.bias", "encoder.layer1.0.bn3.running_mean", "encoder.layer1.0.bn3.running_var", "encoder.layer1.0.downsample.0.weight", "encoder.layer1.0.downsample.1.weight", "encoder.layer1.0.downsample.1.bias", "encoder.layer1.0.downsample.1.running_mean", "encoder.layer1.0.downsample.1.running_var", "encoder.layer1.1.conv1.weight", "encoder.layer1.1.bn1.weight", "encoder.layer1.1.bn1.bias", "encoder.layer1.1.bn1.running_mean", "encoder.layer1.1.bn1.running_var", "encoder.layer1.1.conv2.weight", "encoder.layer1.1.bn2.weight", "encoder.layer1.1.bn2.bias", "encoder.layer1.1.bn2.running_mean", "encoder.layer1.1.bn2.running_var", "encoder.layer1.1.conv3.weight", "encoder.layer1.1.bn3.weight", "encoder.layer1.1.bn3.bias", "encoder.layer1.1.bn3.running_mean", "encoder.layer1.1.bn3.running_var", "encoder.layer1.2.conv1.weight", "encoder.layer1.2.bn1.weight", "encoder.layer1.2.bn1.bias", "encoder.layer1.2.bn1.running_mean", "encoder.layer1.2.bn1.running_var", "encoder.layer1.2.conv2.weight", "encoder.layer1.2.bn2.weight", "encoder.layer1.2.bn2.bias", "encoder.layer1.2.bn2.running_mean", "encoder.layer1.2.bn2.running_var", "encoder.layer1.2.conv3.weight", "encoder.layer1.2.bn3.weight", "encoder.layer1.2.bn3.bias", "encoder.layer1.2.bn3.running_mean", "encoder.layer1.2.bn3.running_var", "encoder.layer2.0.conv1.weight", "encoder.layer2.0.bn1.weight", "encoder.layer2.0.bn1.bias", "encoder.layer2.0.bn1.running_mean", "encoder.layer2.0.bn1.running_var", "encoder.layer2.0.conv2.weight", "encoder.layer2.0.bn2.weight", "encoder.layer2.0.bn2.bias", "encoder.layer2.0.bn2.running_mean", "encoder.layer2.0.bn2.running_var", "encoder.layer2.0.conv3.weight", "encoder.layer2.0.bn3.weight", "encoder.layer2.0.bn3.bias", "encoder.layer2.0.bn3.running_mean", "encoder.layer2.0.bn3.running_var", "encoder.layer2.0.downsample.0.weight", "encoder.layer2.0.downsample.1.weight", "encoder.layer2.0.downsample.1.bias", "encoder.layer2.0.downsample.1.running_mean", "encoder.layer2.0.downsample.1.running_var", "encoder.layer2.1.conv1.weight", "encoder.layer2.1.bn1.weight", "encoder.layer2.1.bn1.bias", "encoder.layer2.1.bn1.running_mean", "encoder.layer2.1.bn1.running_var", "encoder.layer2.1.conv2.weight", "encoder.layer2.1.bn2.weight", "encoder.layer2.1.bn2.bias", "encoder.layer2.1.bn2.running_mean", "encoder.layer2.1.bn2.running_var", "encoder.layer2.1.conv3.weight", "encoder.layer2.1.bn3.weight", "encoder.layer2.1.bn3.bias", "encoder.layer2.1.bn3.running_mean", "encoder.layer2.1.bn3.running_var", "encoder.layer2.2.conv1.weight", "encoder.layer2.2.bn1.weight", "encoder.layer2.2.bn1.bias", "encoder.layer2.2.bn1.running_mean", "encoder.layer2.2.bn1.running_var", "encoder.layer2.2.conv2.weight", "encoder.layer2.2.bn2.weight", "encoder.layer2.2.bn2.bias", "encoder.layer2.2.bn2.running_mean", "encoder.layer2.2.bn2.running_var", "encoder.layer2.2.conv3.weight", "encoder.layer2.2.bn3.weight", "encoder.layer2.2.bn3.bias", "encoder.layer2.2.bn3.running_mean", "encoder.layer2.2.bn3.running_var", "encoder.layer2.3.conv1.weight", "encoder.layer2.3.bn1.weight", "encoder.layer2.3.bn1.bias", "encoder.layer2.3.bn1.running_mean", "encoder.layer2.3.bn1.running_var", "encoder.layer2.3.conv2.weight", "encoder.layer2.3.bn2.weight", "encoder.layer2.3.bn2.bias", "encoder.layer2.3.bn2.running_mean", "encoder.layer2.3.bn2.running_var", "encoder.layer2.3.conv3.weight", "encoder.layer2.3.bn3.weight", "encoder.layer2.3.bn3.bias", "encoder.layer2.3.bn3.running_mean", "encoder.layer2.3.bn3.running_var", "encoder.layer3.0.conv1.weight", "encoder.layer3.0.bn1.weight", "encoder.layer3.0.bn1.bias", "encoder.layer3.0.bn1.running_mean", "encoder.layer3.0.bn1.running_var", "encoder.layer3.0.conv2.weight", "encoder.layer3.0.bn2.weight", "encoder.layer3.0.bn2.bias", "encoder.layer3.0.bn2.running_mean", "encoder.layer3.0.bn2.running_var", "encoder.layer3.0.conv3.weight", "encoder.layer3.0.bn3.weight", "encoder.layer3.0.bn3.bias", "encoder.layer3.0.bn3.running_mean", "encoder.layer3.0.bn3.running_var", "encoder.layer3.0.downsample.0.weight", "encoder.layer3.0.downsample.1.weight", "encoder.layer3.0.downsample.1.bias", "encoder.layer3.0.downsample.1.running_mean", "encoder.layer3.0.downsample.1.running_var", "encoder.layer3.1.conv1.weight", "encoder.layer3.1.bn1.weight", "encoder.layer3.1.bn1.bias", "encoder.layer3.1.bn1.running_mean", "encoder.layer3.1.bn1.running_var", "encoder.layer3.1.conv2.weight", "encoder.layer3.1.bn2.weight", "encoder.layer3.1.bn2.bias", "encoder.layer3.1.bn2.running_mean", "encoder.layer3.1.bn2.running_var", "encoder.layer3.1.conv3.weight", "encoder.layer3.1.bn3.weight", "encoder.layer3.1.bn3.bias", "encoder.layer3.1.bn3.running_mean", "encoder.layer3.1.bn3.running_var", "encoder.layer3.2.conv1.weight", "encoder.layer3.2.bn1.weight", "encoder.layer3.2.bn1.bias", "encoder.layer3.2.bn1.running_mean", "encoder.layer3.2.bn1.running_var", "encoder.layer3.2.conv2.weight", "encoder.layer3.2.bn2.weight", "encoder.layer3.2.bn2.bias", "encoder.layer3.2.bn2.running_mean", "encoder.layer3.2.bn2.running_var", "encoder.layer3.2.conv3.weight", "encoder.layer3.2.bn3.weight", "encoder.layer3.2.bn3.bias", "encoder.layer3.2.bn3.running_mean", "encoder.layer3.2.bn3.running_var", "encoder.layer3.3.conv1.weight", "encoder.layer3.3.bn1.weight", "encoder.layer3.3.bn1.bias", "encoder.layer3.3.bn1.running_mean", "encoder.layer3.3.bn1.running_var", "encoder.layer3.3.conv2.weight", "encoder.layer3.3.bn2.weight", "encoder.layer3.3.bn2.bias", "encoder.layer3.3.bn2.running_mean", "encoder.layer3.3.bn2.running_var", "encoder.layer3.3.conv3.weight", "encoder.layer3.3.bn3.weight", "encoder.layer3.3.bn3.bias", "encoder.layer3.3.bn3.running_mean", "encoder.layer3.3.bn3.running_var", "encoder.layer3.4.conv1.weight", "encoder.layer3.4.bn1.weight", "encoder.layer3.4.bn1.bias", "encoder.layer3.4.bn1.running_mean", "encoder.layer3.4.bn1.running_var", "encoder.layer3.4.conv2.weight", "encoder.layer3.4.bn2.weight", "encoder.layer3.4.bn2.bias", "encoder.layer3.4.bn2.running_mean", "encoder.layer3.4.bn2.running_var", "encoder.layer3.4.conv3.weight", "encoder.layer3.4.bn3.weight", "encoder.layer3.4.bn3.bias", "encoder.layer3.4.bn3.running_mean", "encoder.layer3.4.bn3.running_var", "encoder.layer3.5.conv1.weight", "encoder.layer3.5.bn1.weight", "encoder.layer3.5.bn1.bias", "encoder.layer3.5.bn1.running_mean", "encoder.layer3.5.bn1.running_var", "encoder.layer3.5.conv2.weight", "encoder.layer3.5.bn2.weight", "encoder.layer3.5.bn2.bias", "encoder.layer3.5.bn2.running_mean", "encoder.layer3.5.bn2.running_var", "encoder.layer3.5.conv3.weight", "encoder.layer3.5.bn3.weight", "encoder.layer3.5.bn3.bias", "encoder.layer3.5.bn3.running_mean", "encoder.layer3.5.bn3.running_var", "encoder.layer4.0.conv1.weight", "encoder.layer4.0.bn1.weight", "encoder.layer4.0.bn1.bias", "encoder.layer4.0.bn1.running_mean", "encoder.layer4.0.bn1.running_var", "encoder.layer4.0.conv2.weight", "encoder.layer4.0.bn2.weight", "encoder.layer4.0.bn2.bias", "encoder.layer4.0.bn2.running_mean", "encoder.layer4.0.bn2.running_var", "encoder.layer4.0.conv3.weight", "encoder.layer4.0.bn3.weight", "encoder.layer4.0.bn3.bias", "encoder.layer4.0.bn3.running_mean", "encoder.layer4.0.bn3.running_var", "encoder.layer4.0.downsample.0.weight", "encoder.layer4.0.downsample.1.weight", "encoder.layer4.0.downsample.1.bias", "encoder.layer4.0.downsample.1.running_mean", "encoder.layer4.0.downsample.1.running_var", "encoder.layer4.1.conv1.weight", "encoder.layer4.1.bn1.weight", "encoder.layer4.1.bn1.bias", "encoder.layer4.1.bn1.running_mean", "encoder.layer4.1.bn1.running_var", "encoder.layer4.1.conv2.weight", "encoder.layer4.1.bn2.weight", "encoder.layer4.1.bn2.bias", "encoder.layer4.1.bn2.running_mean", "encoder.layer4.1.bn2.running_var", "encoder.layer4.1.conv3.weight", "encoder.layer4.1.bn3.weight", "encoder.layer4.1.bn3.bias", "encoder.layer4.1.bn3.running_mean", "encoder.layer4.1.bn3.running_var", "encoder.layer4.2.conv1.weight", "encoder.layer4.2.bn1.weight", "encoder.layer4.2.bn1.bias", "encoder.layer4.2.bn1.running_mean", "encoder.layer4.2.bn1.running_var", "encoder.layer4.2.conv2.weight", "encoder.layer4.2.bn2.weight", "encoder.layer4.2.bn2.bias", "encoder.layer4.2.bn2.running_mean", "encoder.layer4.2.bn2.running_var", "encoder.layer4.2.conv3.weight", "encoder.layer4.2.bn3.weight", "encoder.layer4.2.bn3.bias", "encoder.layer4.2.bn3.running_mean", "encoder.layer4.2.bn3.running_var". 
	Unexpected key(s) in state_dict: "encoder._conv_stem.weight", "encoder._bn0.weight", "encoder._bn0.bias", "encoder._bn0.running_mean", "encoder._bn0.running_var", "encoder._blocks.0._depthwise_conv.weight", "encoder._blocks.0._bn1.weight", "encoder._blocks.0._bn1.bias", "encoder._blocks.0._bn1.running_mean", "encoder._blocks.0._bn1.running_var", "encoder._blocks.0._se_reduce.weight", "encoder._blocks.0._se_reduce.bias", "encoder._blocks.0._se_expand.weight", "encoder._blocks.0._se_expand.bias", "encoder._blocks.0._project_conv.weight", "encoder._blocks.0._bn2.weight", "encoder._blocks.0._bn2.bias", "encoder._blocks.0._bn2.running_mean", "encoder._blocks.0._bn2.running_var", "encoder._blocks.1._depthwise_conv.weight", "encoder._blocks.1._bn1.weight", "encoder._blocks.1._bn1.bias", "encoder._blocks.1._bn1.running_mean", "encoder._blocks.1._bn1.running_var", "encoder._blocks.1._se_reduce.weight", "encoder._blocks.1._se_reduce.bias", "encoder._blocks.1._se_expand.weight", "encoder._blocks.1._se_expand.bias", "encoder._blocks.1._project_conv.weight", "encoder._blocks.1._bn2.weight", "encoder._blocks.1._bn2.bias", "encoder._blocks.1._bn2.running_mean", "encoder._blocks.1._bn2.running_var", "encoder._blocks.2._expand_conv.weight", "encoder._blocks.2._bn0.weight", "encoder._blocks.2._bn0.bias", "encoder._blocks.2._bn0.running_mean", "encoder._blocks.2._bn0.running_var", "encoder._blocks.2._depthwise_conv.weight", "encoder._blocks.2._bn1.weight", "encoder._blocks.2._bn1.bias", "encoder._blocks.2._bn1.running_mean", "encoder._blocks.2._bn1.running_var", "encoder._blocks.2._se_reduce.weight", "encoder._blocks.2._se_reduce.bias", "encoder._blocks.2._se_expand.weight", "encoder._blocks.2._se_expand.bias", "encoder._blocks.2._project_conv.weight", "encoder._blocks.2._bn2.weight", "encoder._blocks.2._bn2.bias", "encoder._blocks.2._bn2.running_mean", "encoder._blocks.2._bn2.running_var", "encoder._blocks.3._expand_conv.weight", "encoder._blocks.3._bn0.weight", "encoder._blocks.3._bn0.bias", "encoder._blocks.3._bn0.running_mean", "encoder._blocks.3._bn0.running_var", "encoder._blocks.3._depthwise_conv.weight", "encoder._blocks.3._bn1.weight", "encoder._blocks.3._bn1.bias", "encoder._blocks.3._bn1.running_mean", "encoder._blocks.3._bn1.running_var", "encoder._blocks.3._se_reduce.weight", "encoder._blocks.3._se_reduce.bias", "encoder._blocks.3._se_expand.weight", "encoder._blocks.3._se_expand.bias", "encoder._blocks.3._project_conv.weight", "encoder._blocks.3._bn2.weight", "encoder._blocks.3._bn2.bias", "encoder._blocks.3._bn2.running_mean", "encoder._blocks.3._bn2.running_var", "encoder._blocks.4._expand_conv.weight", "encoder._blocks.4._bn0.weight", "encoder._blocks.4._bn0.bias", "encoder._blocks.4._bn0.running_mean", "encoder._blocks.4._bn0.running_var", "encoder._blocks.4._depthwise_conv.weight", "encoder._blocks.4._bn1.weight", "encoder._blocks.4._bn1.bias", "encoder._blocks.4._bn1.running_mean", "encoder._blocks.4._bn1.running_var", "encoder._blocks.4._se_reduce.weight", "encoder._blocks.4._se_reduce.bias", "encoder._blocks.4._se_expand.weight", "encoder._blocks.4._se_expand.bias", "encoder._blocks.4._project_conv.weight", "encoder._blocks.4._bn2.weight", "encoder._blocks.4._bn2.bias", "encoder._blocks.4._bn2.running_mean", "encoder._blocks.4._bn2.running_var", "encoder._blocks.5._expand_conv.weight", "encoder._blocks.5._bn0.weight", "encoder._blocks.5._bn0.bias", "encoder._blocks.5._bn0.running_mean", "encoder._blocks.5._bn0.running_var", "encoder._blocks.5._depthwise_conv.weight", "encoder._blocks.5._bn1.weight", "encoder._blocks.5._bn1.bias", "encoder._blocks.5._bn1.running_mean", "encoder._blocks.5._bn1.running_var", "encoder._blocks.5._se_reduce.weight", "encoder._blocks.5._se_reduce.bias", "encoder._blocks.5._se_expand.weight", "encoder._blocks.5._se_expand.bias", "encoder._blocks.5._project_conv.weight", "encoder._blocks.5._bn2.weight", "encoder._blocks.5._bn2.bias", "encoder._blocks.5._bn2.running_mean", "encoder._blocks.5._bn2.running_var", "encoder._blocks.6._expand_conv.weight", "encoder._blocks.6._bn0.weight", "encoder._blocks.6._bn0.bias", "encoder._blocks.6._bn0.running_mean", "encoder._blocks.6._bn0.running_var", "encoder._blocks.6._depthwise_conv.weight", "encoder._blocks.6._bn1.weight", "encoder._blocks.6._bn1.bias", "encoder._blocks.6._bn1.running_mean", "encoder._blocks.6._bn1.running_var", "encoder._blocks.6._se_reduce.weight", "encoder._blocks.6._se_reduce.bias", "encoder._blocks.6._se_expand.weight", "encoder._blocks.6._se_expand.bias", "encoder._blocks.6._project_conv.weight", "encoder._blocks.6._bn2.weight", "encoder._blocks.6._bn2.bias", "encoder._blocks.6._bn2.running_mean", "encoder._blocks.6._bn2.running_var", "encoder._blocks.7._expand_conv.weight", "encoder._blocks.7._bn0.weight", "encoder._blocks.7._bn0.bias", "encoder._blocks.7._bn0.running_mean", "encoder._blocks.7._bn0.running_var", "encoder._blocks.7._depthwise_conv.weight", "encoder._blocks.7._bn1.weight", "encoder._blocks.7._bn1.bias", "encoder._blocks.7._bn1.running_mean", "encoder._blocks.7._bn1.running_var", "encoder._blocks.7._se_reduce.weight", "encoder._blocks.7._se_reduce.bias", "encoder._blocks.7._se_expand.weight", "encoder._blocks.7._se_expand.bias", "encoder._blocks.7._project_conv.weight", "encoder._blocks.7._bn2.weight", "encoder._blocks.7._bn2.bias", "encoder._blocks.7._bn2.running_mean", "encoder._blocks.7._bn2.running_var", "encoder._blocks.8._expand_conv.weight", "encoder._blocks.8._bn0.weight", "encoder._blocks.8._bn0.bias", "encoder._blocks.8._bn0.running_mean", "encoder._blocks.8._bn0.running_var", "encoder._blocks.8._depthwise_conv.weight", "encoder._blocks.8._bn1.weight", "encoder._blocks.8._bn1.bias", "encoder._blocks.8._bn1.running_mean", "encoder._blocks.8._bn1.running_var", "encoder._blocks.8._se_reduce.weight", "encoder._blocks.8._se_reduce.bias", "encoder._blocks.8._se_expand.weight", "encoder._blocks.8._se_expand.bias", "encoder._blocks.8._project_conv.weight", "encoder._blocks.8._bn2.weight", "encoder._blocks.8._bn2.bias", "encoder._blocks.8._bn2.running_mean", "encoder._blocks.8._bn2.running_var", "encoder._blocks.9._expand_conv.weight", "encoder._blocks.9._bn0.weight", "encoder._blocks.9._bn0.bias", "encoder._blocks.9._bn0.running_mean", "encoder._blocks.9._bn0.running_var", "encoder._blocks.9._depthwise_conv.weight", "encoder._blocks.9._bn1.weight", "encoder._blocks.9._bn1.bias", "encoder._blocks.9._bn1.running_mean", "encoder._blocks.9._bn1.running_var", "encoder._blocks.9._se_reduce.weight", "encoder._blocks.9._se_reduce.bias", "encoder._blocks.9._se_expand.weight", "encoder._blocks.9._se_expand.bias", "encoder._blocks.9._project_conv.weight", "encoder._blocks.9._bn2.weight", "encoder._blocks.9._bn2.bias", "encoder._blocks.9._bn2.running_mean", "encoder._blocks.9._bn2.running_var", "encoder._blocks.10._expand_conv.weight", "encoder._blocks.10._bn0.weight", "encoder._blocks.10._bn0.bias", "encoder._blocks.10._bn0.running_mean", "encoder._blocks.10._bn0.running_var", "encoder._blocks.10._depthwise_conv.weight", "encoder._blocks.10._bn1.weight", "encoder._blocks.10._bn1.bias", "encoder._blocks.10._bn1.running_mean", "encoder._blocks.10._bn1.running_var", "encoder._blocks.10._se_reduce.weight", "encoder._blocks.10._se_reduce.bias", "encoder._blocks.10._se_expand.weight", "encoder._blocks.10._se_expand.bias", "encoder._blocks.10._project_conv.weight", "encoder._blocks.10._bn2.weight", "encoder._blocks.10._bn2.bias", "encoder._blocks.10._bn2.running_mean", "encoder._blocks.10._bn2.running_var", "encoder._blocks.11._expand_conv.weight", "encoder._blocks.11._bn0.weight", "encoder._blocks.11._bn0.bias", "encoder._blocks.11._bn0.running_mean", "encoder._blocks.11._bn0.running_var", "encoder._blocks.11._depthwise_conv.weight", "encoder._blocks.11._bn1.weight", "encoder._blocks.11._bn1.bias", "encoder._blocks.11._bn1.running_mean", "encoder._blocks.11._bn1.running_var", "encoder._blocks.11._se_reduce.weight", "encoder._blocks.11._se_reduce.bias", "encoder._blocks.11._se_expand.weight", "encoder._blocks.11._se_expand.bias", "encoder._blocks.11._project_conv.weight", "encoder._blocks.11._bn2.weight", "encoder._blocks.11._bn2.bias", "encoder._blocks.11._bn2.running_mean", "encoder._blocks.11._bn2.running_var", "encoder._blocks.12._expand_conv.weight", "encoder._blocks.12._bn0.weight", "encoder._blocks.12._bn0.bias", "encoder._blocks.12._bn0.running_mean", "encoder._blocks.12._bn0.running_var", "encoder._blocks.12._depthwise_conv.weight", "encoder._blocks.12._bn1.weight", "encoder._blocks.12._bn1.bias", "encoder._blocks.12._bn1.running_mean", "encoder._blocks.12._bn1.running_var", "encoder._blocks.12._se_reduce.weight", "encoder._blocks.12._se_reduce.bias", "encoder._blocks.12._se_expand.weight", "encoder._blocks.12._se_expand.bias", "encoder._blocks.12._project_conv.weight", "encoder._blocks.12._bn2.weight", "encoder._blocks.12._bn2.bias", "encoder._blocks.12._bn2.running_mean", "encoder._blocks.12._bn2.running_var", "encoder._blocks.13._expand_conv.weight", "encoder._blocks.13._bn0.weight", "encoder._blocks.13._bn0.bias", "encoder._blocks.13._bn0.running_mean", "encoder._blocks.13._bn0.running_var", "encoder._blocks.13._depthwise_conv.weight", "encoder._blocks.13._bn1.weight", "encoder._blocks.13._bn1.bias", "encoder._blocks.13._bn1.running_mean", "encoder._blocks.13._bn1.running_var", "encoder._blocks.13._se_reduce.weight", "encoder._blocks.13._se_reduce.bias", "encoder._blocks.13._se_expand.weight", "encoder._blocks.13._se_expand.bias", "encoder._blocks.13._project_conv.weight", "encoder._blocks.13._bn2.weight", "encoder._blocks.13._bn2.bias", "encoder._blocks.13._bn2.running_mean", "encoder._blocks.13._bn2.running_var", "encoder._blocks.14._expand_conv.weight", "encoder._blocks.14._bn0.weight", "encoder._blocks.14._bn0.bias", "encoder._blocks.14._bn0.running_mean", "encoder._blocks.14._bn0.running_var", "encoder._blocks.14._depthwise_conv.weight", "encoder._blocks.14._bn1.weight", "encoder._blocks.14._bn1.bias", "encoder._blocks.14._bn1.running_mean", "encoder._blocks.14._bn1.running_var", "encoder._blocks.14._se_reduce.weight", "encoder._blocks.14._se_reduce.bias", "encoder._blocks.14._se_expand.weight", "encoder._blocks.14._se_expand.bias", "encoder._blocks.14._project_conv.weight", "encoder._blocks.14._bn2.weight", "encoder._blocks.14._bn2.bias", "encoder._blocks.14._bn2.running_mean", "encoder._blocks.14._bn2.running_var", "encoder._blocks.15._expand_conv.weight", "encoder._blocks.15._bn0.weight", "encoder._blocks.15._bn0.bias", "encoder._blocks.15._bn0.running_mean", "encoder._blocks.15._bn0.running_var", "encoder._blocks.15._depthwise_conv.weight", "encoder._blocks.15._bn1.weight", "encoder._blocks.15._bn1.bias", "encoder._blocks.15._bn1.running_mean", "encoder._blocks.15._bn1.running_var", "encoder._blocks.15._se_reduce.weight", "encoder._blocks.15._se_reduce.bias", "encoder._blocks.15._se_expand.weight", "encoder._blocks.15._se_expand.bias", "encoder._blocks.15._project_conv.weight", "encoder._blocks.15._bn2.weight", "encoder._blocks.15._bn2.bias", "encoder._blocks.15._bn2.running_mean", "encoder._blocks.15._bn2.running_var", "encoder._blocks.16._expand_conv.weight", "encoder._blocks.16._bn0.weight", "encoder._blocks.16._bn0.bias", "encoder._blocks.16._bn0.running_mean", "encoder._blocks.16._bn0.running_var", "encoder._blocks.16._depthwise_conv.weight", "encoder._blocks.16._bn1.weight", "encoder._blocks.16._bn1.bias", "encoder._blocks.16._bn1.running_mean", "encoder._blocks.16._bn1.running_var", "encoder._blocks.16._se_reduce.weight", "encoder._blocks.16._se_reduce.bias", "encoder._blocks.16._se_expand.weight", "encoder._blocks.16._se_expand.bias", "encoder._blocks.16._project_conv.weight", "encoder._blocks.16._bn2.weight", "encoder._blocks.16._bn2.bias", "encoder._blocks.16._bn2.running_mean", "encoder._blocks.16._bn2.running_var", "encoder._blocks.17._expand_conv.weight", "encoder._blocks.17._bn0.weight", "encoder._blocks.17._bn0.bias", "encoder._blocks.17._bn0.running_mean", "encoder._blocks.17._bn0.running_var", "encoder._blocks.17._depthwise_conv.weight", "encoder._blocks.17._bn1.weight", "encoder._blocks.17._bn1.bias", "encoder._blocks.17._bn1.running_mean", "encoder._blocks.17._bn1.running_var", "encoder._blocks.17._se_reduce.weight", "encoder._blocks.17._se_reduce.bias", "encoder._blocks.17._se_expand.weight", "encoder._blocks.17._se_expand.bias", "encoder._blocks.17._project_conv.weight", "encoder._blocks.17._bn2.weight", "encoder._blocks.17._bn2.bias", "encoder._blocks.17._bn2.running_mean", "encoder._blocks.17._bn2.running_var", "encoder._blocks.18._expand_conv.weight", "encoder._blocks.18._bn0.weight", "encoder._blocks.18._bn0.bias", "encoder._blocks.18._bn0.running_mean", "encoder._blocks.18._bn0.running_var", "encoder._blocks.18._depthwise_conv.weight", "encoder._blocks.18._bn1.weight", "encoder._blocks.18._bn1.bias", "encoder._blocks.18._bn1.running_mean", "encoder._blocks.18._bn1.running_var", "encoder._blocks.18._se_reduce.weight", "encoder._blocks.18._se_reduce.bias", "encoder._blocks.18._se_expand.weight", "encoder._blocks.18._se_expand.bias", "encoder._blocks.18._project_conv.weight", "encoder._blocks.18._bn2.weight", "encoder._blocks.18._bn2.bias", "encoder._blocks.18._bn2.running_mean", "encoder._blocks.18._bn2.running_var", "encoder._blocks.19._expand_conv.weight", "encoder._blocks.19._bn0.weight", "encoder._blocks.19._bn0.bias", "encoder._blocks.19._bn0.running_mean", "encoder._blocks.19._bn0.running_var", "encoder._blocks.19._depthwise_conv.weight", "encoder._blocks.19._bn1.weight", "encoder._blocks.19._bn1.bias", "encoder._blocks.19._bn1.running_mean", "encoder._blocks.19._bn1.running_var", "encoder._blocks.19._se_reduce.weight", "encoder._blocks.19._se_reduce.bias", "encoder._blocks.19._se_expand.weight", "encoder._blocks.19._se_expand.bias", "encoder._blocks.19._project_conv.weight", "encoder._blocks.19._bn2.weight", "encoder._blocks.19._bn2.bias", "encoder._blocks.19._bn2.running_mean", "encoder._blocks.19._bn2.running_var", "encoder._blocks.20._expand_conv.weight", "encoder._blocks.20._bn0.weight", "encoder._blocks.20._bn0.bias", "encoder._blocks.20._bn0.running_mean", "encoder._blocks.20._bn0.running_var", "encoder._blocks.20._depthwise_conv.weight", "encoder._blocks.20._bn1.weight", "encoder._blocks.20._bn1.bias", "encoder._blocks.20._bn1.running_mean", "encoder._blocks.20._bn1.running_var", "encoder._blocks.20._se_reduce.weight", "encoder._blocks.20._se_reduce.bias", "encoder._blocks.20._se_expand.weight", "encoder._blocks.20._se_expand.bias", "encoder._blocks.20._project_conv.weight", "encoder._blocks.20._bn2.weight", "encoder._blocks.20._bn2.bias", "encoder._blocks.20._bn2.running_mean", "encoder._blocks.20._bn2.running_var", "encoder._blocks.21._expand_conv.weight", "encoder._blocks.21._bn0.weight", "encoder._blocks.21._bn0.bias", "encoder._blocks.21._bn0.running_mean", "encoder._blocks.21._bn0.running_var", "encoder._blocks.21._depthwise_conv.weight", "encoder._blocks.21._bn1.weight", "encoder._blocks.21._bn1.bias", "encoder._blocks.21._bn1.running_mean", "encoder._blocks.21._bn1.running_var", "encoder._blocks.21._se_reduce.weight", "encoder._blocks.21._se_reduce.bias", "encoder._blocks.21._se_expand.weight", "encoder._blocks.21._se_expand.bias", "encoder._blocks.21._project_conv.weight", "encoder._blocks.21._bn2.weight", "encoder._blocks.21._bn2.bias", "encoder._blocks.21._bn2.running_mean", "encoder._blocks.21._bn2.running_var", "encoder._blocks.22._expand_conv.weight", "encoder._blocks.22._bn0.weight", "encoder._blocks.22._bn0.bias", "encoder._blocks.22._bn0.running_mean", "encoder._blocks.22._bn0.running_var", "encoder._blocks.22._depthwise_conv.weight", "encoder._blocks.22._bn1.weight", "encoder._blocks.22._bn1.bias", "encoder._blocks.22._bn1.running_mean", "encoder._blocks.22._bn1.running_var", "encoder._blocks.22._se_reduce.weight", "encoder._blocks.22._se_reduce.bias", "encoder._blocks.22._se_expand.weight", "encoder._blocks.22._se_expand.bias", "encoder._blocks.22._project_conv.weight", "encoder._blocks.22._bn2.weight", "encoder._blocks.22._bn2.bias", "encoder._blocks.22._bn2.running_mean", "encoder._blocks.22._bn2.running_var", "encoder._blocks.23._expand_conv.weight", "encoder._blocks.23._bn0.weight", "encoder._blocks.23._bn0.bias", "encoder._blocks.23._bn0.running_mean", "encoder._blocks.23._bn0.running_var", "encoder._blocks.23._depthwise_conv.weight", "encoder._blocks.23._bn1.weight", "encoder._blocks.23._bn1.bias", "encoder._blocks.23._bn1.running_mean", "encoder._blocks.23._bn1.running_var", "encoder._blocks.23._se_reduce.weight", "encoder._blocks.23._se_reduce.bias", "encoder._blocks.23._se_expand.weight", "encoder._blocks.23._se_expand.bias", "encoder._blocks.23._project_conv.weight", "encoder._blocks.23._bn2.weight", "encoder._blocks.23._bn2.bias", "encoder._blocks.23._bn2.running_mean", "encoder._blocks.23._bn2.running_var", "encoder._blocks.24._expand_conv.weight", "encoder._blocks.24._bn0.weight", "encoder._blocks.24._bn0.bias", "encoder._blocks.24._bn0.running_mean", "encoder._blocks.24._bn0.running_var", "encoder._blocks.24._depthwise_conv.weight", "encoder._blocks.24._bn1.weight", "encoder._blocks.24._bn1.bias", "encoder._blocks.24._bn1.running_mean", "encoder._blocks.24._bn1.running_var", "encoder._blocks.24._se_reduce.weight", "encoder._blocks.24._se_reduce.bias", "encoder._blocks.24._se_expand.weight", "encoder._blocks.24._se_expand.bias", "encoder._blocks.24._project_conv.weight", "encoder._blocks.24._bn2.weight", "encoder._blocks.24._bn2.bias", "encoder._blocks.24._bn2.running_mean", "encoder._blocks.24._bn2.running_var", "encoder._blocks.25._expand_conv.weight", "encoder._blocks.25._bn0.weight", "encoder._blocks.25._bn0.bias", "encoder._blocks.25._bn0.running_mean", "encoder._blocks.25._bn0.running_var", "encoder._blocks.25._depthwise_conv.weight", "encoder._blocks.25._bn1.weight", "encoder._blocks.25._bn1.bias", "encoder._blocks.25._bn1.running_mean", "encoder._blocks.25._bn1.running_var", "encoder._blocks.25._se_reduce.weight", "encoder._blocks.25._se_reduce.bias", "encoder._blocks.25._se_expand.weight", "encoder._blocks.25._se_expand.bias", "encoder._blocks.25._project_conv.weight", "encoder._blocks.25._bn2.weight", "encoder._blocks.25._bn2.bias", "encoder._blocks.25._bn2.running_mean", "encoder._blocks.25._bn2.running_var", "encoder._conv_head.weight", "encoder._bn1.weight", "encoder._bn1.bias", "encoder._bn1.running_mean", "encoder._bn1.running_var". 
	size mismatch for decoder.blocks.0.conv1.0.weight: copying a param with shape torch.Size([256, 520, 3, 3]) from checkpoint, the shape in current model is torch.Size([256, 3072, 3, 3]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([32, 520, 1, 1]) from checkpoint, the shape in current model is torch.Size([192, 3072, 1, 1]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([32]) from checkpoint, the shape in current model is torch.Size([192]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([520, 32, 1, 1]) from checkpoint, the shape in current model is torch.Size([3072, 192, 1, 1]).
	size mismatch for decoder.blocks.0.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([520]) from checkpoint, the shape in current model is torch.Size([3072]).
	size mismatch for decoder.blocks.0.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 520, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 3072, 1, 1]).
	size mismatch for decoder.blocks.1.conv1.0.weight: copying a param with shape torch.Size([128, 304, 3, 3]) from checkpoint, the shape in current model is torch.Size([128, 768, 3, 3]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([19, 304, 1, 1]) from checkpoint, the shape in current model is torch.Size([48, 768, 1, 1]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([19]) from checkpoint, the shape in current model is torch.Size([48]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([304, 19, 1, 1]) from checkpoint, the shape in current model is torch.Size([768, 48, 1, 1]).
	size mismatch for decoder.blocks.1.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([304]) from checkpoint, the shape in current model is torch.Size([768]).
	size mismatch for decoder.blocks.1.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 304, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 768, 1, 1]).
	size mismatch for decoder.blocks.2.conv1.0.weight: copying a param with shape torch.Size([64, 160, 3, 3]) from checkpoint, the shape in current model is torch.Size([64, 384, 3, 3]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([10, 160, 1, 1]) from checkpoint, the shape in current model is torch.Size([24, 384, 1, 1]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([10]) from checkpoint, the shape in current model is torch.Size([24]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([160, 10, 1, 1]) from checkpoint, the shape in current model is torch.Size([384, 24, 1, 1]).
	size mismatch for decoder.blocks.2.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([160]) from checkpoint, the shape in current model is torch.Size([384]).
	size mismatch for decoder.blocks.2.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 160, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 384, 1, 1]).
	size mismatch for decoder.blocks.3.conv1.0.weight: copying a param with shape torch.Size([32, 104, 3, 3]) from checkpoint, the shape in current model is torch.Size([32, 128, 3, 3]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.1.weight: copying a param with shape torch.Size([6, 104, 1, 1]) from checkpoint, the shape in current model is torch.Size([8, 128, 1, 1]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.1.bias: copying a param with shape torch.Size([6]) from checkpoint, the shape in current model is torch.Size([8]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.3.weight: copying a param with shape torch.Size([104, 6, 1, 1]) from checkpoint, the shape in current model is torch.Size([128, 8, 1, 1]).
	size mismatch for decoder.blocks.3.attention1.attention.cSE.3.bias: copying a param with shape torch.Size([104]) from checkpoint, the shape in current model is torch.Size([128]).
	size mismatch for decoder.blocks.3.attention1.attention.sSE.0.weight: copying a param with shape torch.Size([1, 104, 1, 1]) from checkpoint, the shape in current model is torch.Size([1, 128, 1, 1]).

**Warnings**

- [1;32m    137[0m                 [0mwarnings[0m[0;34m.[0m[0mwarn[0m[0;34m([0m[0mtext[0m[0;34m,[0m [0mstacklevel[0m[0;34m=[0m[0;34m-[0m[0;36m1[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

### Cell 7

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# =========================` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Runs a stricter final logic check before writing the submission so schema drift, row-count mismatches, or malformed IDs are caught at the last stage.

**Imports**

- os
- numpy
- pandas

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- submission.csv

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- pd.read_csv: submission.csv
- os.path.exists: submission.csv

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- None

**Exceptions**

- None

**Warnings**

- None
