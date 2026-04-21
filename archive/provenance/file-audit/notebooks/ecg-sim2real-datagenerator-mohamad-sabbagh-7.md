# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 8 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-7.md |
| SHA-256 | 4a581ff8dff6271222ec881306cf9c8fc897c1172b36120d81511c7bccfae89b |
| Size (bytes) | 102,242 |
| Modified (UTC) | 2026-04-18T19:33:24.375553+00:00 |
| Inferred role | Kaggle ECG digitization inference notebook combining YOLO and segmentation. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 4 |
| Cell count | 23 |
| Code cells | 23 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 0 |
| Editorial cell notes | 23 |
| Editorial output notes | 0 |
| Interpretation confidence | medium |
| Open questions | 1 |
| Editorial complete | yes |
| Kernel | {"language": "python", "display_name": "Python 3", "name": "python3"} |
| Language info | {"name": "python", "version": "3.11.13", "mimetype": "text/x-python", "codemirror_mode": {"name": "ipython", "version": 3}, "pygments_lexer": "ipython3", "nbconvert_exporter": "python", "file_extension": ".py"} |

## Dependencies

**Imports**

- albumentations
- cv2
- glob
- io
- matplotlib.pyplot
- numpy
- os
- pandas
- random
- scipy.fft
- scipy.signal
- segmentation_models_pytorch
- shutil
- skimage.measure
- skimage.transform
- sklearn.model_selection
- sys
- torch
- torch.utils.data
- tqdm
- ultralytics
- warnings
- wfdb

**Packages requested via pip/install commands**

- albumentations
- fastparquet
- matplotlib
- numpy<2
- opencv-python
- pandas
- pyarrow
- scikit-image
- scikit-learn
- scipy
- segmentation-models-pytorch
- tqdm
- ultralytics
- wfdb

## Hard-Coded Paths And External Environment Markers

**Environment markers**

- Kaggle input mount
- Colab runtime detection
- pip install usage
- YOLO loader
- segmentation_models_pytorch
- torch.load

**Literal paths / artifacts**

- *.jpg
- *.png
- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- /kaggle/input/physionet-ecg-image-digitization/train
- /kaggle/input/physionet-ecg-image-digitization/train.csv
- 10mm/mV
- 25mm/s
- best_model_phase2.pth
- best_model_phase7.pth
- best_model_real_data.pth
- dataset_path/train/*.jpg
- dataset_path/train/*.png
- runs/detect/ecg_combat_detector/weights/best.pt
- self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- submission.parquet
- submission_from_images.csv
- submission_simulated.csv
- yolo_dataset/data.yaml
- yolo_dataset/labels/{subset}/{filename}.txt
- yolov8l.pt
- yolov8m.pt
- yolov8x.pt
- {BASE_DIR}/images/train
- {BASE_DIR}/images/val
- {BASE_DIR}/labels/train
- {BASE_DIR}/labels/val
- {dataset_path}/**/*.jpg
- {dataset_path}/**/*.png
- {root_path}/**/**/*.png
- {root_path}/**/*.jpg
- {root_path}/**/*.png
- {root}/**/*.jpg
- {root}/**/*.png

## Symbols Defined

**Functions**

- __getitem__
- __init__
- __len__
- add_distractors
- advanced_perspective_correction
- calibrate_signal
- correct_skew_backup
- correct_skew_fft
- correct_skew_orientation
- create_combat_page
- create_submission_file
- einthoven
- estimate_grid_size
- estimate_local_grid_size
- extract_signal_viterbi
- fix_image_orientation
- generate_image_pair
- get_12_leads_crops
- get_any_image_path
- get_heavy_augmentations
- get_real_signal
- get_yolo_crops
- get_yolo_crops_with_fallback
- predict_long_image
- predict_sliding_window
- preprocess_remove_grid
- preprocess_remove_grid_rgb
- process_full_page
- render_to_memory
- sub_pixel_viterbi
- test_robust_real_image
- viterbi_extract_actual_signal
- viterbi_path

**Classes**

- CombatYOLOGenerator
- DynamicUltimateDataset
- RealSignalDataset
- UltimateRenderer

**Constants / assigned names**

- BASE_DIR
- BATCH_SIZE
- COMPETITION_NAME
- DATA_DIR
- DATA_YAML
- DB_DIR
- DEVICE
- EPOCHS
- IMAGE_DIR
- INPUT_DIR
- LEAD_NAMES
- LR
- M
- MY_SUB_PATH
- NEW_MODEL_NAME
- OFFICIAL_SAMPLE_PATH
- PREV_MODEL_PATH
- TEST_CSV_PATH
- TRAIN_CSV_PATH
- UNET_MODEL_PATH
- YOLO_MODEL_PATH
- best_path
- crop_h
- csv_file
- dataset_path
- dpi
- epoch_loss
- final_grid_size
- grid_height
- grid_size
- grid_width
- has_sample
- lead_idx
- pad
- r
- step
- target_h
- target_len
- train_loss
- val_loss
- win
- yolo_model

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: dataset_path/test/*.jpg
- glob.glob: dataset_path/test/*.png
- glob.glob: dataset_path/train/*.jpg
- glob.glob: dataset_path/train/*.png
- glob.glob: self.root_dir/self.df.iloc[idx][id]/*.csv
- glob.glob: {root}/**/*.jpg
- glob.glob: {root}/**/*.png
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- os.listdir: /kaggle/input
- os.listdir: /kaggle/input/dirname
- os.listdir: dataset_path/train
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/train.csv
- os.path.exists: best_model_phase7.pth
- os.path.exists: best_model_real_data.pth
- os.path.exists: dataset_path/train
- os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt
- os.path.exists: self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- pd.read_csv: /kaggle/input/dirname/f
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/train.csv
- pd.read_csv: self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- pd.read_parquet: submission.parquet
- torch.load: best_model_phase7.pth
- torch.load: best_model_real_data.pth
- wfdb.rdsamp: self.db_dir/{rec_name}

**File writes**

- cv2.imwrite: yolo_dataset/images/{subset}/{filename}.jpg
- df.to_csv: submission_simulated.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: yolo_dataset/data.yaml
- open[w]: yolo_dataset/labels/{subset}/{filename}.txt
- torch.save: best_model_phase2.pth
- torch.save: best_model_phase7.pth

**Shell commands**

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image pyarrow fastparquet wfdb
- !pip install ultralytics

**subprocess calls**

- None

**Model loads**

- YOLO: runs/detect/ecg_combat_detector/weights/best.pt
- YOLO: yolov8x.pt
- torch.load: best_model_phase7.pth
- torch.load: best_model_real_data.pth

**Model saves**

- torch.save: best_model_phase2.pth
- torch.save: best_model_phase7.pth

**Model existence probes**

- os.path.exists: best_model_phase7.pth
- os.path.exists: best_model_real_data.pth
- os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt

## Stored Output Inventory

**Output types**

- stream: 16

**MIME types**

- None

**Exceptions captured in outputs**

- None

**Warnings / warning-like lines**

- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Field()` function, which has no effect in 
- warnings.warn(
- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'frozen' attribute with value True was provided to the `Field()` function, which has no effect in

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- yolov8x.pt
- best_model_phase7.pt
- best_model_real_data.pt
- best_model_phase2.pt
- yolov8l.pt
- yolov8m.pt

**Referenced datasets**

- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv

**External files**

- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: dataset_path/test/*.jpg
- glob.glob: dataset_path/test/*.png
- glob.glob: dataset_path/train/*.jpg
- glob.glob: dataset_path/train/*.png
- cv2.imwrite: yolo_dataset/images/{subset}/{filename}.jpg
- df.to_csv: submission_simulated.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt

**Required runtime assumptions**

- Assumes in-notebook shell execution is allowed for package installation or environment repair.
- Assumes in-notebook dependency installation is permitted.
- Assumes Kaggle input mounts are available.
- Assumes ultralytics/YOLO is available for lead localization.
- Assumes PyTorch checkpoint loading is available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.

**Outputs created or updated**

- torch.save: best_model_phase2.pth
- torch.save: best_model_phase7.pth
- cv2.imwrite: yolo_dataset/images/{subset}/{filename}.jpg
- df.to_csv: submission_simulated.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: yolo_dataset/data.yaml
- open[w]: yolo_dataset/labels/{subset}/{filename}.txt

## Phase 1 Closure Status

| Field | Value |
| --- | --- |
| Notebook summary | present |
| Editorial cell coverage | 23/23 |
| Editorial output translations | 0 |
| Delta notes | 5 |
| Open questions | 1 |
| Confidence | medium |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Late-stage research notebook that swaps in a stronger ResNet50 plus scSE segmentation architecture while keeping the combat YOLO branch alive.
- This file marks the point where architecture search, detector robustness, and hardened inference are all treated as parts of the same submission strategy.

**Delta notes**

- Compared with notebook (6), this revision changes the segmentation architecture itself and makes detector hardening an explicit combat-mode branch.
- The apparent motivation is to improve final reconstruction quality through architecture search, harder detector training, and eventually real-image pseudo-label fine-tuning.
- It retains the late-stage geometry, combat-detector, and hardening ideas from the immediately preceding research notebooks instead of restarting the pipeline from scratch.
- The workflow effect is that the notebook becomes a late-stage model-selection and final-build source, not just another intermediate research checkpoint.
- What starts to become obsolete is the assumption that the older baseline segmentation branch alone is the intended deployment path; newer architecture and fine-tuning branches take over.

**Open questions**

- The late research notebooks clearly evolve toward a final build, but the exact handoff from these in-notebook training runs to the later compact deployment notebooks is still partly historical rather than explicit.

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`, cell count changed from 23 to 23, stored output types changed from 58 to 16, and exact shared cell sources = 16.
- New imports: `io`, `wfdb`
- Removed imports: None
- New model refs: `YOLO: runs/detect/ecg_combat_detector/weights/best.pt`, `YOLO: yolov8x.pt`, `os.path.exists: best_model_phase7.pth`, `os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt`, `torch.load: best_model_phase7.pth`, `torch.save: best_model_phase7.pth`
- Removed model refs: `YOLO: runs/detect/ecg_layout_detector/weights/best.pt`, `YOLO: yolov8n.pt`, `os.path.exists: best_model_phase2.pth`, `os.path.exists: runs/detect/ecg_layout_detector/weights/best.pt`, `torch.save: best_model.pth`
- New first-line titles: `# --- الخلية 18: إعداد بيانات YOLO القتالية (Combat Mode) - [M4: UPDATED] ---`, `# --- الخلية 19: تدريب YOLOv8x القتالي [M4: COMBAT TRAINING] ---`, `# --- الخلية 22: محرك الاستخراج النهائي (Phase 7 Architecture) - [M7: UPDATED] ---`, `# --- الخلية 3: محرك الرسم الحي (Ultimate Renderer) - [M3: UPDATED] ---`, `# --- الخلية 4: تدريب المعمارية المتقدمة (Phase 7: ResNet50 + scse) ---`
- Removed first-line titles: `# --- الخلية 22: محرك الاستخراج عالي الدقة (Phase 3: High-Fidelity Inference) ---`, `# خلية 18`, `# خلية 19`, `# خلية 3`, `# خلية 4`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- Colab runtime detection is present; behavior may differ between Kaggle and Colab.
- Dependency installation is embedded in notebook cells, so reproducibility depends on runtime package availability.
- Stored outputs include 3 warning-like lines worth checking during reruns.
- Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.
- Notebook depends on both object detection and segmentation stacks, increasing environment complexity.
- Checkpoint loading is embedded in the workflow; model file availability is a runtime prerequisite.

## Cell-By-Cell Audit

### Cell 1

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 1: التثبيت وإعادة التشغيل ---` |
| Role summary | Environment bootstrap cell with package installation commands. |

**Editorial interpretation**

- Bootstraps the environment and prepares for a runtime restart, preserving the assumption that package installation happens inside the notebook rather than upstream.

**Imports**

- os
- sys

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

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image pyarrow fastparquet wfdb
- !pip install ultralytics

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

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 1 |
| First non-empty line | `# --- الخلية 2: الاستيرادات المحدثة (Updated Imports) ---` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Loads the runtime stack, shared imports, and path configuration so the rest of the notebook can move between synthetic assets and Kaggle inputs without repeating setup logic.

**Imports**

- os
- cv2
- numpy
- pandas
- matplotlib.pyplot
- scipy.signal
- random
- tqdm
- albumentations
- torch
- torch.utils.data
- segmentation_models_pytorch
- sklearn.model_selection
- glob
- ultralytics
- shutil
- warnings
- wfdb
- io
- skimage.transform
- skimage.measure
- scipy.fft

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- DEVICE

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

- stream[stderr] with 4 line(s); excerpt: /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Fi...
- stream[stdout] with 2 line(s); excerpt: ✅ تم تحديث المكتبات: جاهزون للمعالجة الهندسية والفيزيائية. 🚀 الجهاز المستخدم: cuda

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
| First non-empty line | `# --- الخلية 3: محرك الرسم الحي (Ultimate Renderer) - [M3: UPDATED] ---` |
| Role summary | Rendering / synthetic ECG image generation cell. |

**Editorial interpretation**

- Keeps a reusable synthetic rendering and data-generation cell in the notebook, because every later training or detector branch still depends on controllable ECG imagery.

**Imports**

- None

**Functions defined**

- __init__
- get_real_signal
- render_to_memory

**Classes defined**

- UltimateRenderer

**Constants / bindings**

- DB_DIR = physionet_db
- dpi = 200
- selected_records = records[idx]
- signal = record[lead_idx]

**Paths mentioned**

- None

**File reads**

- wfdb.rdsamp: self.db_dir/{rec_name}

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

- stream[stdout] with 1 line(s); excerpt: ✅ تم تحديث الخلية 3: محرك الرسم الحي جاهز (DPI=200).

**Exceptions**

- None

**Warnings**

- None

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 4 |
| First non-empty line | `# --- الخلية 4: تدريب المعمارية المتقدمة (Phase 7: ResNet50 + scse) ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Trains the phase-7 ResNet50 plus scSE segmentation architecture, testing whether a stronger encoder and attention stack improve trace-mask quality.

**Imports**

- None

**Functions defined**

- __init__
- add_distractors
- __len__
- __getitem__

**Classes defined**

- DynamicUltimateDataset

**Constants / bindings**

- BATCH_SIZE = 8
- EPOCHS = 1
- LR = 0.0001
- color = ['0', '0', '0']
- epoch_loss = 0
- font = cv2.FONT_HERSHEY_SIMPLEX
- img = augmented[image]
- mask = augmented[mask]
- pos = []
- texts = ['V1', 'II', '25mm/s', '10mm/mV', 'HR: 72', 'Patient: X', 'FILTER 50Hz']

**Paths mentioned**

- 10mm/mV
- 25mm/s
- best_model_phase7.pth

**File reads**

- None

**File writes**

- torch.save: best_model_phase7.pth

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- torch.save: best_model_phase7.pth

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 3 line(s); excerpt: 🏗️ بناء النموذج المتقدم (ResNet50 + scSE Attention)... 🔥 بدء تدريب المرحلة 7 (Advanced Architecture)... 📊 المواصفات: ResNet50 | scSE Attention | 40,000 عينة
- stream[stderr] with 1 line(s); excerpt: Training Phase 7: 100%|██████████| 5000/5000 [2:01:13<00:00,  1.45s/it, loss=0.0387]
- stream[stdout] with 2 line(s); excerpt: ✅ انتهى التدريب! متوسط الخسارة: 0.0666 💾 تم حفظ النموذج المتقدم: best_model_phase7.pth
- stream[stderr] with 1 line(s)

**Exceptions**

- None

**Warnings**

- None

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --الخلية 5 ---` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Defines the mask-to-signal post-processing helpers, including the dynamic-programming and Viterbi-style logic that translates probability maps into one-dimensional traces.

**Imports**

- None

**Functions defined**

- viterbi_path
- extract_signal_viterbi

**Classes defined**

- None

**Constants / bindings**

- min_cost = dp[idx]dist_penalty[best_idx]
- prev_costs = dp[idx]
- refined_signal = []
- total_costs = dp[idx]dist_penalty
- weights = prob_map[x]
- win = 2
- y_subpixel = y_int

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 6

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 6---` |
| Role summary | General computation cell. |

**Editorial interpretation**

- Executes a focused smoke test with stored outputs so the author can inspect whether the current model and decoder recover a plausible strip before moving to page-level logic.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- extracted_signal = values
- prob_map = subscript[0][0]

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 7

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 7 ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Wraps the strip decoder into a full-page or multi-lead processing helper, which is required before the notebook can touch real Kaggle pages.

**Imports**

- None

**Functions defined**

- process_full_page

**Classes defined**

- None

**Constants / bindings**

- full_signals = ['values']
- prob_map = subscript[0][0]
- rows = ['aug_img']
- signal_clean = values
- strip = image_full[idx]

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 8

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 8:  ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Introduces submission-oriented formatting helpers that reshape reconstructed leads into the schema expected by the competition files.

**Imports**

- None

**Functions defined**

- create_submission_file

**Classes defined**

- None

**Constants / bindings**

- full_signals = ['signal_resampled']
- prob_map = subscript[0][0]
- sample_id = sample_i1
- signal_clean = values
- submission_data = ['row_dict']
- target_len = 1000

**Paths mentioned**

- submission_simulated.csv

**File reads**

- None

**File writes**

- df.to_csv: submission_simulated.csv

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

### Cell 9

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 9:  ---` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Loads the official Kaggle metadata and image inventory, turning the notebook from a synthetic-only experiment into one that can address real evaluation inputs.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- COMPETITION_NAME = physionet-ecg-image-digitization
- INPUT_DIR = /kaggle/input
- csv_file = /kaggle/input/dirname/f
- dataset_path = /kaggle/input/dirname
- image_example = /kaggle/input/dirname/**/*.jpg

**Paths mentioned**

- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- {dataset_path}/**/*.jpg
- {dataset_path}/**/*.png

**File reads**

- os.listdir: /kaggle/input
- os.listdir: /kaggle/input/dirname
- pd.read_csv: /kaggle/input/dirname/f
- glob.glob: /kaggle/input/dirname/**/*.png
- glob.glob: /kaggle/input/dirname/**/*.jpg

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

### Cell 10

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# الخلية 10` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds a real-image inference harness that points the current model stack at actual competition pages and exposes the remaining domain mismatch.

**Imports**

- None

**Functions defined**

- test_robust_real_image

**Classes defined**

- None

**Constants / bindings**

- crop_h = 400
- image_name = img_path
- prob_map = subscript[0][0]
- real_strip = real_img[idx]
- search_pattern_jpg = dataset_path/train/*.jpg
- search_pattern_png = dataset_path/train/*.png

**Paths mentioned**

- *.jpg
- *.png
- dataset_path/train/*.jpg
- dataset_path/train/*.png

**File reads**

- glob.glob: dataset_path/train/*.png
- glob.glob: dataset_path/train/*.jpg
- glob.glob: dataset_path/test/*.png
- glob.glob: dataset_path/test/*.jpg
- os.path.exists: dataset_path/train
- os.listdir: dataset_path/train

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

### Cell 11

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# الخلية 11` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Defines grid-detection and calibration helpers so waveform extraction can be normalized against paper spacing rather than raw pixels alone.

**Imports**

- None

**Functions defined**

- estimate_grid_size
- calibrate_signal

**Classes defined**

- None

**Constants / bindings**

- final_grid_size = 25.0
- grid_height = 0
- grid_width = 0
- img = image_path_or_array

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 12

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 12` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Runs a calibration or visualization sanity pass, confirming whether the grid estimate and lead geometry look stable on representative samples.

**Imports**

- None

**Functions defined**

- get_any_image_path

**Classes defined**

- None

**Constants / bindings**

- crop_h = 400
- dataset_path = r
- files = p
- patterns = ['{root_path}/**/*.png', '{root_path}/**/*.jpg', '{root_path}/**/**/*.png']
- possible_roots = ['/kaggle/input/physionet-ecg-image-digitization', '/kaggle/input']
- prob_map = subscript[0][0]
- real_strip = original_img[idx]

**Paths mentioned**

- /kaggle/input
- /kaggle/input/physionet-ecg-image-digitization
- {root_path}/**/**/*.png
- {root_path}/**/*.jpg
- {root_path}/**/*.png

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 13

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 13` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds a sliding-window or segmented decoding helper for long traces, reducing the chance that local failures corrupt the entire lead.

**Imports**

- None

**Functions defined**

- predict_long_image

**Classes defined**

- None

**Constants / bindings**

- crop_h = 400
- prob = subscript[0][0]
- real_strip = original_img[idx]
- target_h = 256
- window = pad

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 14

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 14` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adjusts the waveform path solver and post-processing rules so sharp transitions can survive decoding instead of collapsing into an over-smoothed line.

**Imports**

- None

**Functions defined**

- viterbi_extract_actual_signal

**Classes defined**

- None

**Constants / bindings**

- final_signal = []
- prev_col_costs = dp[idx]
- total = dp[idx][idx]dist_penalty
- weights = prob_map[x]
- window_costs = dp[idx][idx]
- y_sub = y_int

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 15

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 15: المحرك الهندسي المتقدم (Advanced Geometry Engine) ---` |
| Role summary | Definition cell that defines 3 function(s). |

**Editorial interpretation**

- Expands the geometry subsystem into an explicit advanced engine that handles rotation, alignment, and spatial normalization more aggressively than earlier revisions.

**Imports**

- None

**Functions defined**

- correct_skew_fft
- correct_skew_backup
- fix_image_orientation

**Classes defined**

- None

**Constants / bindings**

- angle = subscript[idx]
- angles = ['angle']
- center = []
- r = 20
- thresh = subscript[1]

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 16

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 16` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds cleanup logic that strips grid remnants or background clutter before the trace is decoded, improving robustness outside the synthetic domain.

**Imports**

- None

**Functions defined**

- preprocess_remove_grid

**Classes defined**

- None

**Constants / bindings**

- grid_mask = mask1mask2

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 17

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 17: اختبار يدوي (مصحح) ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Provides a corrected manual validation helper for chosen examples, indicating that earlier ad hoc tests were not reliable enough for later high-stakes inference cells.

**Imports**

- None

**Functions defined**

- get_12_leads_crops

**Classes defined**

- None

**Constants / bindings**

- active_area = image[idx]
- crops = ['image[idx][idx]']
- file_name = img_path
- grid_size = 15.0
- image_files = []
- img_id = subscript[0]
- leads_data = ['final_sig']
- search_roots = ['/kaggle/input', 'dataset_path']
- submission_rows = ['row_dict']
- target_len = 1000

**Paths mentioned**

- /kaggle/input
- submission_from_images.csv
- {root}/**/*.jpg
- {root}/**/*.png

**File reads**

- glob.glob: {root}/**/*.png
- glob.glob: {root}/**/*.jpg

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

### Cell 18

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 10 |
| First non-empty line | `# --- الخلية 18: إعداد بيانات YOLO القتالية (Combat Mode) - [M4: UPDATED] ---` |
| Role summary | Definition cell that defines 3 function(s) and 1 class(es). |

**Editorial interpretation**

- Prepares a more aggressive combat-mode YOLO dataset with harder augmentations and clutter, aiming to make lead localization survive messy page layouts.

**Imports**

- None

**Functions defined**

- __init__
- add_distractors
- create_combat_page

**Classes defined**

- CombatYOLOGenerator

**Constants / bindings**

- BASE_DIR = yolo_dataset
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- font = cv2.FONT_HERSHEY_SIMPLEX
- img = subscript[image]
- label_path = yolo_dataset/labels/{subset}/{filename}.txt
- labels_data = ['0 {x_center} {y_center} {expr} {expr}']
- lead_idx = 0
- lead_name = I[0]
- sig = sig[idx]
- texts = ['CONFIDENTIAL', 'ECG REPORT', 'PhysioNet', 'Error: 404', 'Leads V1-V6']
- yaml_content = 
path: {expr} 
train: images/train
val: images/val
nc: 12
names: I


**Paths mentioned**

- yolo_dataset/labels/{subset}/{filename}.txt
- {BASE_DIR}/images/train
- {BASE_DIR}/images/val
- {BASE_DIR}/labels/train
- {BASE_DIR}/labels/val

**File reads**

- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt

**File writes**

- open: yolo_dataset/data.yaml
- open[w]: yolo_dataset/data.yaml
- cv2.imwrite: yolo_dataset/images/{subset}/{filename}.jpg
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: yolo_dataset/labels/{subset}/{filename}.txt

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

- stream[stdout] with 1 line(s); excerpt: 🏭 بدء إنتاج صور YOLO القتالية (Combat Mode)...
- stream[stderr] with 2 line(s); excerpt: Train Data: 100%|██████████| 200/200 [01:02<00:00,  3.22it/s] Val Data: 100%|██████████| 50/50 [00:15<00:00,  3.20it/s]
- stream[stdout] with 1 line(s); excerpt: ✅ البيانات القتالية جاهزة.
- stream[stderr] with 1 line(s)

**Exceptions**

- None

**Warnings**

- None

### Cell 19

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 11 |
| First non-empty line | `# --- الخلية 19: تدريب YOLOv8x القتالي [M4: COMBAT TRAINING] ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Trains the combat YOLOv8x detector on that harsher dataset so detector robustness stops being the bottleneck for the final submission engine.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- best_path = runs/detect/ecg_combat_detector/weights/best.pt

**Paths mentioned**

- runs/detect/ecg_combat_detector/weights/best.pt
- yolo_dataset/data.yaml
- yolov8l.pt
- yolov8m.pt
- yolov8x.pt

**File reads**

- os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: yolov8x.pt

**Model saves**

- None

**Model existence probes**

- os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt

**Stored outputs**

- stream[stdout] with 154 line(s); excerpt: 🦕 تحميل الوحش YOLOv8x... [KDownloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8x.pt to 'yolov8x.pt': 100% ━━━━━━━━━━━━ 130.5MB 288.7MB/s 0.5s 0.4s<0.1...

**Exceptions**

- None

**Warnings**

- None

### Cell 20

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 20: مصنع البيانات المصفح والتدريب التكميلي (Phase 2: Hardening) ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Keeps the phase-2 hardening segmentation branch in the workflow as a fallback or complementary weight set for difficult pages.

**Imports**

- None

**Functions defined**

- get_heavy_augmentations
- __init__
- __len__
- generate_image_pair
- __getitem__

**Classes defined**

- RealSignalDataset

**Constants / bindings**

- BATCH_SIZE = 16
- DATA_DIR = /kaggle/input/physionet-ecg-image-digitization/train
- EPOCHS = 5
- LR = 0.0001
- NEW_MODEL_NAME = best_model_phase2.pth
- PREV_MODEL_PATH = best_model_real_data.pth
- TRAIN_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/train.csv
- best_val_loss = avg_val_loss
- dpi = 120
- full_signal = values
- rec_id = self.df.iloc[idx][id]
- row = self.df.iloc[idx]
- sig_path = self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- signal_segment = values[idx]
- train_loss = 0
- val_loss = 0

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization/train
- /kaggle/input/physionet-ecg-image-digitization/train.csv
- best_model_phase2.pth
- best_model_real_data.pth
- self.root_dir/self.df.iloc[idx][id]/*.csv[0]

**File reads**

- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/train.csv
- os.path.exists: best_model_real_data.pth
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/train.csv
- torch.load: best_model_real_data.pth
- pd.read_csv: self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- os.path.exists: self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- glob.glob: self.root_dir/self.df.iloc[idx][id]/*.csv

**File writes**

- torch.save: best_model_phase2.pth

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- torch.load: best_model_real_data.pth

**Model saves**

- torch.save: best_model_phase2.pth

**Model existence probes**

- os.path.exists: best_model_real_data.pth

**Stored outputs**

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 21

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 21` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Adds the integration helpers that translate detector crops, calibration metadata, and segmentation outputs into a common inference contract.

**Imports**

- None

**Functions defined**

- correct_skew_orientation
- get_yolo_crops

**Classes defined**

- None

**Constants / bindings**

- angle = subscript[idx]
- center = []
- conf = box.conf[0]
- ordered_crops = ['image[idx]']
- thresh = subscript[1]
- xyxy = box.xyxy[0]

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 22

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 5 |
| First non-empty line | `# --- الخلية 22: محرك الاستخراج النهائي (Phase 7 Architecture) - [M7: UPDATED] ---` |
| Role summary | Definition cell that defines 7 function(s). |

**Editorial interpretation**

- Defines the final phase-7 inference engine, now centered on the ResNet50 plus scSE weights rather than the earlier baseline checkpoint.

**Imports**

- skimage.measure

**Functions defined**

- advanced_perspective_correction
- preprocess_remove_grid_rgb
- estimate_local_grid_size
- get_yolo_crops_with_fallback
- predict_sliding_window
- sub_pixel_viterbi
- einthoven

**Classes defined**

- None

**Constants / bindings**

- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- UNET_MODEL_PATH = best_model_phase7.pth
- YOLO_MODEL_PATH = runs/detect/ecg_combat_detector/weights/best.pt
- center = []
- conf = box.conf[0]
- crop = img_rz[idx]
- crops = ['image[idx]']
- final = []
- horizontal_points = ['x1', 'y1', 'x2', 'y2']
- lname = I[i]
- p = subscript[0][0]
- pad = 5
- prev = dp[idx]
- prob = subscript[0][0]
- sid = row[id]
- step = 384
- t_in = img_rz[idx]
- target_h = 256
- vector = model.params[1]
- w = prob_map[x]
- win = 512

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- best_model_phase7.pth
- runs/detect/ecg_combat_detector/weights/best.pt

**File reads**

- os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt
- os.path.exists: best_model_phase7.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- torch.load: best_model_phase7.pth

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: runs/detect/ecg_combat_detector/weights/best.pt
- torch.load: best_model_phase7.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt
- os.path.exists: best_model_phase7.pth

**Stored outputs**

- stream[stdout] with 4 line(s); excerpt: ⚙️ جاري تحميل المحرك المتقدم (Phase 7)... ✅ YOLO (Combat): مفعل. 💎 U-Net (ResNet50+scSE): مفعل. 🚀 بدء الاستخراج (Phase 7: ResNet50+scSE) لـ 24 ملف...
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 24/24 [07:17<00:00, 18.23s/it]
- stream[stdout] with 2 line(s); excerpt: 💾 الحفظ النهائي (Phase 7)... ✅ اكتملت المهمة.

**Exceptions**

- None

**Warnings**

- None

### Cell 23

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 6 |
| First non-empty line | `# خلية 23` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Performs the final parquet and template validation step to ensure the generated submission still matches competition schema constraints.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- MY_SUB_PATH = submission.parquet
- OFFICIAL_SAMPLE_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- first_id = my_sub.iloc[0][id]
- first_value = my_sub.iloc[0][value]
- has_sample = False

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- submission.parquet

**File reads**

- pd.read_parquet: submission.parquet
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet

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

- stream[stdout] with 11 line(s); excerpt: 🔍 جاري التحقق من التنسيق الطويل (Long Format)... ✅ أسماء الأعمدة صحيحة (id, value). ✅ نوع البيانات (float) صحيح. 🔍 عينة من الـ ID في ملفك: 1053922973_0_I 📊 إجمالي عدد الصفوف في ملف...

**Exceptions**

- None

**Warnings**

- None
