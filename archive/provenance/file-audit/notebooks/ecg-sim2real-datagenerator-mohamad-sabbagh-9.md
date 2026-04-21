# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 10 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-9.md |
| SHA-256 | 1f999b030165487a615c120ae992d81156fa2cdbd322f737f8a1a0933800305f |
| Size (bytes) | 93,092 |
| Modified (UTC) | 2026-04-18T19:34:05.184121+00:00 |
| Inferred role | Phase 10 real-world fine-tuning notebook. |

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
- gc
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
- torch.nn
- torch.optim.lr_scheduler
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
- Fine-Tuning {epoch+1}/{EPOCHS}
- best.pt
- best_model_phase10.pth
- best_model_phase2.pth
- best_model_phase9.pth
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
- {img_dir}/**/*.jpg
- {img_dir}/**/*.png
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
- _generate_pseudo_labels
- adaptive_viterbi
- add_distractors
- advanced_perspective_correction
- apply_high_pass_filter
- calibrate_signal
- correct_skew_backup
- correct_skew_fft
- correct_skew_orientation
- create_combat_page
- create_submission_file
- estimate_grid_size
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
- predict_with_tta
- preprocess_remove_grid
- preprocess_remove_grid_rgb
- process_full_page
- render_to_memory
- robust_multi_point_calibration
- smart_einthoven_fix
- suppress_vertical_artifacts
- test_robust_real_image
- viterbi_extract_actual_signal
- viterbi_path

**Classes**

- CombatYOLOGenerator
- RealSignalDataset
- RealWorldDataset
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
- I
- II
- III
- IMAGE_DIR
- INPUT_DIR
- LEAD_NAMES
- LR
- M
- MY_SUB_PATH
- NEW_MODEL_NAME
- OFFICIAL_SAMPLE_PATH
- PREV_MODEL_PATH
- REAL_IMG_DIR
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
- glob.glob: {img_dir}/**/*.jpg
- glob.glob: {img_dir}/**/*.png
- glob.glob: {root}/**/*.jpg
- glob.glob: {root}/**/*.png
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- os.listdir: /kaggle/input
- os.listdir: /kaggle/input/dirname
- os.listdir: dataset_path/train
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/train.csv
- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth
- os.path.exists: best_model_phase9.pth
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
- torch.load: best_model_phase10.pth
- torch.load: best_model_phase9.pth
- torch.load: best_model_real_data.pth
- wfdb.rdsamp: self.db_dir/{rec_name}

**File writes**

- cv2.imwrite: yolo_dataset/images/{subset}/{filename}.jpg
- df.to_csv: submission_simulated.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: yolo_dataset/data.yaml
- open[w]: yolo_dataset/labels/{subset}/{filename}.txt
- torch.save: best_model_phase10.pth
- torch.save: best_model_phase2.pth

**Shell commands**

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image pyarrow fastparquet wfdb
- !pip install ultralytics

**subprocess calls**

- None

**Model loads**

- YOLO: best.pt
- YOLO: yolov8x.pt
- torch.load: best_model_phase10.pth
- torch.load: best_model_phase9.pth
- torch.load: best_model_real_data.pth

**Model saves**

- torch.save: best_model_phase10.pth
- torch.save: best_model_phase2.pth

**Model existence probes**

- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth
- os.path.exists: best_model_phase9.pth
- os.path.exists: best_model_real_data.pth
- os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt

## Stored Output Inventory

**Output types**

- stream: 49

**MIME types**

- None

**Exceptions captured in outputs**

- None

**Warnings / warning-like lines**

- None

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- yolov8x.pt
- best_model_phase10.pt
- best_model_phase9.pt
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

- torch.save: best_model_phase10.pth
- torch.save: best_model_phase2.pth
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

- Phase-10 research notebook that fine-tunes toward real-world competition pages while retaining the combat detector and hardening branches.
- This is the last large single-model research notebook before the series collapses into compact submission-only variants.

**Delta notes**

- Compared with notebook (8), this revision turns the main segmentation branch toward real-world fine-tuning and produces the first explicit platinum final build.
- The apparent motivation is to improve final reconstruction quality through architecture search, harder detector training, and eventually real-image pseudo-label fine-tuning.
- It retains the late-stage geometry, combat-detector, and hardening ideas from the immediately preceding research notebooks instead of restarting the pipeline from scratch.
- The workflow effect is that the notebook becomes a late-stage model-selection and final-build source, not just another intermediate research checkpoint.
- What starts to become obsolete is the assumption that the older baseline segmentation branch alone is the intended deployment path; newer architecture and fine-tuning branches take over.

**Open questions**

- The late research notebooks clearly evolve toward a final build, but the exact handoff from these in-notebook training runs to the later compact deployment notebooks is still partly historical rather than explicit.

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`, cell count changed from 23 to 23, stored output types changed from 16 to 49, and exact shared cell sources = 20.
- New imports: `gc`, `torch.optim.lr_scheduler`
- Removed imports: None
- New model refs: `YOLO: best.pt`, `os.path.exists: best.pt`, `os.path.exists: best_model_phase10.pth`, `os.path.exists: best_model_phase9.pth`, `torch.load: best_model_phase10.pth`, `torch.load: best_model_phase9.pth`, `torch.save: best_model_phase10.pth`
- Removed model refs: `YOLO: runs/detect/ecg_combat_detector/weights/best.pt`, `os.path.exists: best_model_phase8.pth`, `torch.load: best_model_phase8.pth`, `torch.save: best_model_phase8.pth`
- New first-line titles: `# --- الخلية 22: المحرك البلاتيني (Phase 14: Signal Processing + Phase 15: TTA) - [FINAL BUILD] ---`, `# --- الخلية 4: الضبط الدقيق على الواقع (Phase 10: Real World Fine-Tuning) - [M10: PSEUDO] ---`
- Removed first-line titles: `# --- الخلية 22: محرك الاستخراج النهائي (Phase 8 Weights) - [M8: UPDATED] ---`, `# --- الخلية 4: تدريب المرحلة 8 (Hybrid Loss & AdamW) - [M8: OPTIMIZED] ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- Colab runtime detection is present; behavior may differ between Kaggle and Colab.
- Dependency installation is embedded in notebook cells, so reproducibility depends on runtime package availability.
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
| Execution count | 17 |
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
- torch.nn
- gc
- skimage.transform
- skimage.measure
- scipy.fft
- torch.optim.lr_scheduler

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

- stream[stdout] with 2 line(s); excerpt: ✅ تم تحديث المكتبات: جاهزون للمعالجة الهندسية والفيزيائية. 🚀 الجهاز المستخدم: cuda

**Exceptions**

- None

**Warnings**

- None

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
| Execution count | 5 |
| First non-empty line | `# --- الخلية 4: الضبط الدقيق على الواقع (Phase 10: Real World Fine-Tuning) - [M10: PSEUDO] ---` |
| Role summary | Definition cell that defines 4 function(s) and 1 class(es). |

**Editorial interpretation**

- Fine-tunes the segmentation stack on real or pseudo-labeled competition data, explicitly targeting the synthetic-to-real gap instead of only improving synthetic training.

**Imports**

- None

**Functions defined**

- __init__
- _generate_pseudo_labels
- __len__
- __getitem__

**Classes defined**

- RealWorldDataset

**Constants / bindings**

- EPOCHS = 20
- LR = 0.0001
- REAL_IMG_DIR = /kaggle/input/physionet-ecg-image-digitization
- best_loss = avg_loss
- epoch_loss = 0
- img = augmented[image]
- mask = augmented[mask]
- path = self.image_paths[idx]

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization
- Fine-Tuning {epoch+1}/{EPOCHS}
- best_model_phase10.pth
- best_model_phase9.pth
- {img_dir}/**/*.jpg
- {img_dir}/**/*.png

**File reads**

- os.path.exists: best_model_phase9.pth
- torch.load: best_model_phase9.pth
- glob.glob: {img_dir}/**/*.png
- glob.glob: {img_dir}/**/*.jpg

**File writes**

- torch.save: best_model_phase10.pth

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- torch.load: best_model_phase9.pth

**Model saves**

- torch.save: best_model_phase10.pth

**Model existence probes**

- os.path.exists: best_model_phase9.pth

**Stored outputs**

- stream[stdout] with 2 line(s); excerpt: 👨‍🏫 تحميل المعلم (Phase 9 Model) لتوليد التسميات الزائفة (Pseudo-Labels)... 🔄 جاري توليد الأقنعة لـ 1500 صورة حقيقية...
- stream[stderr] with 1 line(s); excerpt: Generating Pseudo-Labels: 100%|██████████| 1500/1500 [07:40<00:00,  3.26it/s]
- stream[stdout] with 2 line(s); excerpt: 🔥 بدء الضبط الدقيق على الواقع (Phase 10: Real Fine-Tuning)... 📊 المواصفات: 1500 Real Images | LR=0.0001 | 20 Epochs
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 1: Real Loss=0.20827
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 2: Real Loss=0.15751
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 3: Real Loss=0.14280
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 4: Real Loss=0.13850
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 5: Real Loss=0.13343
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 6: Real Loss=0.12821
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 7: Real Loss=0.12594
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 8: Real Loss=0.12467
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 9: Real Loss=0.12068
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 10: Real Loss=0.12071
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 11: Real Loss=0.11776
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 12: Real Loss=0.11707
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 13: Real Loss=0.11419
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 14: Real Loss=0.11358
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 15: Real Loss=0.11188
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 16: Real Loss=0.11156
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 17: Real Loss=0.11037
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 18: Real Loss=0.11144
- stream[stderr] with 1 line(s)
- stream[stdout] with 1 line(s); excerpt: Epoch 19: Real Loss=0.11090
- stream[stderr] with 1 line(s)
- stream[stdout] with 3 line(s); excerpt: Epoch 20: Real Loss=0.10952 ✅ انتهى الضبط الدقيق! أفضل خسارة واقعية: 0.10952 💾 تم حفظ النموذج النهائي: best_model_phase10.pth

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
| Execution count | None |
| First non-empty line | `# --- الخلية 18: إعداد بيانات YOLO القتالية (Combat Mode) - [M4: UPDATED] ---` |
| Role summary | Definition cell that defines 3 function(s) and 1 class(es). |

**Editorial interpretation**

- Prepares the combat-mode localization dataset once more so page detection can keep pace with the new phase-10 segmentation branch.

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 19

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 19: تدريب YOLOv8x القتالي [M4: COMBAT TRAINING] ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Retrains or refreshes the combat YOLO detector, preserving robust lead localization as part of the final build recipe.

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

- None

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

- Maintains the phase-2 hardening branch as a fallback path for difficult pages and noisy scans.

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

- Adds the integration helpers that let detector outputs, calibration data, and segmentation masks flow into a single final engine contract.

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
| Execution count | 18 |
| First non-empty line | `# --- الخلية 22: المحرك البلاتيني (Phase 14: Signal Processing + Phase 15: TTA) - [FINAL BUILD] ---` |
| Role summary | Definition cell that defines 9 function(s). |

**Editorial interpretation**

- Defines the platinum final build that combines later signal-processing ideas and test-time augmentation on top of the phase-10 weights.

**Imports**

- skimage.measure

**Functions defined**

- apply_high_pass_filter
- smart_einthoven_fix
- predict_with_tta
- suppress_vertical_artifacts
- adaptive_viterbi
- robust_multi_point_calibration
- advanced_perspective_correction
- get_yolo_crops_with_fallback
- preprocess_remove_grid_rgb

**Classes defined**

- None

**Constants / bindings**

- I = leads[I][idx]
- II = leads[II][idx]
- III = leads[III][idx]
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- UNET_MODEL_PATH = best_model_phase10.pth
- YOLO_MODEL_PATH = best.pt
- center = []
- clean_grid = grid_sizes[idx]
- conf = box.conf[0]
- crops = ['image[idx]']
- final_path = []
- grid_sizes = []
- horizontal_points = ['x1', 'y1', 'x2', 'y2']
- lname = I[i]
- pad = 5
- prev_col = dp[idx]
- prob_flip = subscript[0][0]
- prob_orig = subscript[0][0]
- sid = row[id]
- target_h = 256
- vector = model.params[1]
- weights = prob_map[x]

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- best.pt
- best_model_phase10.pth

**File reads**

- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- torch.load: best_model_phase10.pth

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: best.pt
- torch.load: best_model_phase10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth

**Stored outputs**

- stream[stdout] with 4 line(s); excerpt: ⚙️ جاري تحميل المحرك البلاتيني (Phase 14+15)... ✅ YOLO (Combat): مفعل. 💎 U-Net (Phase 10): مفعل. 🚀 بدء الاستخراج البلاتيني (Phase 14+15: TTA & Medical Polish) لـ 24 ملف...
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 24/24 [04:41<00:00, 11.72s/it]
- stream[stdout] with 2 line(s); excerpt: 💾 الحفظ النهائي (Platinum Edition)... 🏆 تمت المهمة! هذا أقوى ما يمكن أن تنتجه التكنولوجيا الحالية.

**Exceptions**

- None

**Warnings**

- None

### Cell 23

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 20 |
| First non-empty line | `# خلية 23` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Runs the parquet and sample validation pass so the new platinum engine can be treated as a submission candidate rather than only a research artifact.

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
