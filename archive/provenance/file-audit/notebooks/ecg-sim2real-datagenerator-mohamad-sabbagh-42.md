# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 43 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-42.md |
| SHA-256 | 928f2aa8fc3a5f832393afa4f1e9b6b7daebebbda257b07caa5f52687a1a1cee |
| Size (bytes) | 206,108 |
| Modified (UTC) | 2026-04-18T20:16:42.847390+00:00 |
| Inferred role | Phase 10 real-world fine-tuning notebook. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 5 |
| Cell count | 26 |
| Code cells | 26 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 0 |
| Editorial cell notes | 26 |
| Editorial output notes | 0 |
| Interpretation confidence | medium |
| Open questions | 2 |
| Editorial complete | yes |
| Kernel | {"display_name": "Python 3", "language": "python", "name": "python3"} |
| Language info | {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.11.13"} |

## Dependencies

**Imports**

- albumentations
- collections
- csv
- cv2
- gc
- glob
- io
- math
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
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/ecg-final-models1
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- /kaggle/input/physionet-ecg-image-digitization/train
- /kaggle/input/physionet-ecg-image-digitization/train.csv
- 10mm/mV
- 25mm/s
- DeepLab Real-Epoch {epoch+1}/15
- DeepLab Syn-Epoch {epoch+1}/30
- EffNet Real-Epoch {epoch+1}/15
- EffNet Syn-Epoch {epoch+1}/30
- Fine-Tuning {epoch+1}/{EPOCHS}
- best_model_deeplab_ph10.pth
- best_model_efficientnet_ph10.pth
- best_model_phase10.pth
- best_model_phase2.pth
- best_model_phase9.pth
- best_model_real_data.pth
- dataset_path/train/*.jpg
- dataset_path/train/*.png
- runs/detect/ecg_combat_detector/weights/best.pt
- self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- submission.csv
- submission.parquet
- submission_from_images.csv
- submission_simulated.csv
- temp_deeplab_base.pth
- temp_effnet_base.pth
- yolo_dataset/data.yaml
- yolo_dataset/labels/{subset}/{filename}.txt
- yolov8l.pt
- yolov8m.pt
- yolov8x.pt
- {BASE_DIR}/images/train
- {BASE_DIR}/images/val
- {BASE_DIR}/labels/train
- {BASE_DIR}/labels/val
- {MODELS_DIR}/best.pt
- {MODELS_DIR}/best_model_deeplab_ph10.pth
- {MODELS_DIR}/best_model_efficientnet_ph10.pth
- {MODELS_DIR}/best_model_phase10.pth
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
- _normalize_lead_name
- add_distractors
- apply_high_pass
- calibrate_signal
- choose_ppmv
- clean_pid
- combined_loss
- compute_patient_leads
- correct_skew_backup
- correct_skew_fft
- correct_skew_orientation
- create_combat_page
- create_submission_file
- estimate_grid_size
- estimate_grid_spacing_px
- extract_signal_viterbi
- fix_image_orientation
- generate_image_pair
- get_12_leads_crops
- get_any_image_path
- get_crops_yolo_mapped
- get_heavy_augmentations
- get_image_path
- get_real_signal
- get_yolo_crops
- predict_ensemble_probmaps
- predict_long_image
- prepare_unet_batch
- preprocess_remove_grid
- preprocess_remove_grid_rgb
- process_full_page
- render_to_memory
- safe_read_rgb
- score_candidate
- smart_einthoven_fix
- test_robust_real_image
- viterbi_adaptive
- viterbi_dp
- viterbi_extract_actual_signal
- viterbi_path

**Classes**

- CombatYOLOGenerator
- DynamicUltimateDataset
- RealSignalDataset
- RealWorldDataset
- UltimateRenderer

**Constants / assigned names**

- BASE_DIR
- BATCH_SIZE
- CLASS_TO_LEAD_IDX
- COMPETITION_NAME
- DATA_DIR
- DATA_YAML
- DB_DIR
- DEVICE
- DP_MAX_W
- DP_SMOOTH
- EPOCHS
- IMAGE_DIR
- INPUT_DIR
- LEAD_NAMES
- LEAD_TO_IDX
- LR
- M
- MAX_CACHE
- MAX_W
- MODELS_DIR
- MY_SUB_PATH
- NEW_MODEL_NAME
- OFFICIAL_SAMPLE_PATH
- PREV_MODEL_PATH
- REAL_IMG_DIR
- SAMPLE_PARQUET_PATH
- SUBMISSION_FILE
- TARGET_H
- TEACHER_PATH
- TEST_CSV_PATH
- TRAIN_CSV_PATH
- YOLO_CONF
- YOLO_INF_MAX
- YOLO_PATH
- accumulated_preds
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
- r
- scale
- t_len
- target_h
- target_len
- train_loss
- val
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
- open: submission.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- os.listdir: /kaggle/input
- os.listdir: /kaggle/input/dirname
- os.listdir: dataset_path/train
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/train.csv
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
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- torch.load: best_model_phase9.pth
- torch.load: best_model_real_data.pth
- torch.load: temp_deeplab_base.pth
- torch.load: temp_effnet_base.pth
- wfdb.rdsamp: self.db_dir/{rec_name}

**File writes**

- cv2.imwrite: yolo_dataset/images/{subset}/{filename}.jpg
- df.to_csv: submission_simulated.csv
- open: submission.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: submission.csv
- open[w]: yolo_dataset/data.yaml
- open[w]: yolo_dataset/labels/{subset}/{filename}.txt
- torch.save: best_model_deeplab_ph10.pth
- torch.save: best_model_efficientnet_ph10.pth
- torch.save: best_model_phase10.pth
- torch.save: best_model_phase2.pth
- torch.save: temp_deeplab_base.pth
- torch.save: temp_effnet_base.pth

**Shell commands**

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image pyarrow fastparquet wfdb
- !pip install ultralytics

**subprocess calls**

- None

**Model loads**

- YOLO: /kaggle/input/ecg-final-models1/best.pt
- YOLO: yolov8x.pt
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- torch.load: best_model_phase9.pth
- torch.load: best_model_real_data.pth
- torch.load: temp_deeplab_base.pth
- torch.load: temp_effnet_base.pth

**Model saves**

- torch.save: best_model_deeplab_ph10.pth
- torch.save: best_model_efficientnet_ph10.pth
- torch.save: best_model_phase10.pth
- torch.save: best_model_phase2.pth
- torch.save: temp_deeplab_base.pth
- torch.save: temp_effnet_base.pth

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: best_model_phase9.pth
- os.path.exists: best_model_real_data.pth
- os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt

## Stored Output Inventory

**Output types**

- stream: 6
- error: 1

**MIME types**

- None

**Exceptions captured in outputs**

- FileNotFoundError: [Errno 2] No such file or directory: 'best_model_phase9.pth'

**Warnings / warning-like lines**

- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Field()` function, which has no effect in 
- warnings.warn(
- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'frozen' attribute with value True was provided to the `Field()` function, which has no effect in
- ⚠️ تحذير: موديل المرحلة 9 غير موجود، نستخدم تهيئة عشوائية (غير مستحسن).

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- yolov8x.pt
- best_model_phase10.pt
- best_model_deeplab_ph10.pt
- best_model_efficientnet_ph10.pt
- best_model_phase9.pt
- best_model_real_data.pt
- temp_deeplab_base.pt
- temp_effnet_base.pt
- best_model_phase2.pt
- yolov8l.pt
- yolov8m.pt

**Referenced datasets**

- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/ecg-final-models1
- /kaggle/input/ecg-final-models1/best.pt

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
- open: submission.csv
- open: yolo_dataset/data.yaml

**Required runtime assumptions**

- Assumes in-notebook shell execution is allowed for package installation or environment repair.
- Assumes in-notebook dependency installation is permitted.
- Assumes Kaggle input mounts are available.
- Assumes ultralytics/YOLO is available for lead localization.
- Assumes PyTorch checkpoint loading is available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.

**Outputs created or updated**

- torch.save: best_model_deeplab_ph10.pth
- torch.save: best_model_efficientnet_ph10.pth
- torch.save: best_model_phase10.pth
- torch.save: best_model_phase2.pth
- cv2.imwrite: yolo_dataset/images/{subset}/{filename}.jpg
- df.to_csv: submission_simulated.csv
- open: submission.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: submission.csv

## Phase 1 Closure Status

| Field | Value |
| --- | --- |
| Notebook summary | present |
| Editorial cell coverage | 26/26 |
| Editorial output translations | 0 |
| Delta notes | 5 |
| Open questions | 2 |
| Confidence | medium |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Largest late-stage research notebook; it extends the phase-10 branch into a three-model ensemble consisting of the ResNet-based phase-10 model, an EfficientNet-B3 competitor, and a DeepLabV3+ competitor.
- This file is the provenance notebook for the extra competition checkpoints that later compact notebooks consume directly.

**Delta notes**

- Compared with notebook (41), this revision leaves the compact submission format entirely and reopens training to build a multi-checkpoint ensemble.
- The apparent motivation is to reopen the now-compact deployment story and test whether a broader multi-checkpoint ensemble can outperform the single-model final builds.
- It retains the phase-10 lineage, the detector branch, the geometry logic, and the hardening-era understanding of difficult pages from the preceding notebooks.
- The workflow effect is a major expansion of the checkpoint universe: later notebooks can now benchmark or deploy multiple segmentation families rather than only one inherited winner.
- What becomes less final is the single-model-only assumption that dominated notebooks (10) through (41); from this point onward, ensemble and competitor checkpoints become first-class options.

**Open questions**

- The ensemble direction is well defined technically, but Phase 1 evidence does not fully resolve whether it became the long-term preferred path or remained a benchmarking branch.
- Notebook evidence references temporary base checkpoints for the EfficientNet and DeepLab branches, and those base artifacts are not present in the audited bundle.

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`, cell count changed from 6 to 26, stored output types changed from 8 to 7, and exact shared cell sources = 1.
- New imports: `albumentations`, `io`, `matplotlib.pyplot`, `random`, `scipy.fft`, `shutil`, `skimage.measure`, `skimage.transform`, `sklearn.model_selection`, `torch.nn`, `torch.optim.lr_scheduler`, `torch.utils.data`, `warnings`, `wfdb`
- Removed imports: `importlib`, `pyarrow`, `site`, `subprocess`
- New model refs: `YOLO: /kaggle/input/ecg-final-models1/best.pt`, `YOLO: yolov8x.pt`, `os.path.exists: /kaggle/input/ecg-final-models1/best.pt`, `os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth`, `os.path.exists: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth`, `os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth`, `os.path.exists: best_model_phase9.pth`, `os.path.exists: best_model_real_data.pth`, `os.path.exists: runs/detect/ecg_combat_detector/weights/best.pt`, `torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth`, `torch.load: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth`, `torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth`, `torch.load: best_model_phase9.pth`, `torch.load: best_model_real_data.pth`, `torch.load: temp_deeplab_base.pth`, `torch.load: temp_effnet_base.pth`, `torch.save: best_model_deeplab_ph10.pth`, `torch.save: best_model_efficientnet_ph10.pth`, `torch.save: best_model_phase10.pth`, `torch.save: best_model_phase2.pth`, `torch.save: temp_deeplab_base.pth`, `torch.save: temp_effnet_base.pth`
- Removed model refs: `YOLO: /kaggle/input/ecg-final-models/best.pt`, `os.path.exists: /kaggle/input/ecg-final-models/best.pt`
- New first-line titles: `# --- Cell 22: V39 Ultimate (Ensemble: ResNet + EffNet + DeepLab) ---`, `# --- الخلية 15: المحرك الهندسي المتقدم (Advanced Geometry Engine) ---`, `# --- الخلية 17: اختبار يدوي (مصحح) ---`, `# --- الخلية 18: إعداد بيانات YOLO القتالية (Combat Mode) - [M4: UPDATED] ---`, `# --- الخلية 19: تدريب YOLOv8x القتالي [M4: COMBAT TRAINING] ---`, `# --- الخلية 1: التثبيت وإعادة التشغيل ---`, `# --- الخلية 20: مصنع البيانات المصفح والتدريب التكميلي (Phase 2: Hardening) ---`, `# --- الخلية 2: الاستيرادات المحدثة (Updated Imports) ---`, `# --- الخلية 4: الضبط الدقيق على الواقع (Phase 10: Real World Fine-Tuning) - [M10: PSEUDO] ---`, `# --- الخلية 6---`, `# --- الخلية 7 ---`, `# --- الخلية 8:  ---`, `# --- الخلية 9:  ---`, `# --- الخلية الإضافية 1 (النسخة الآمنة): تدريب المنافس الأول (EfficientNet-B3) ---`, `# --- الخلية الإضافية 4.8 تدريب النموذج الثاني: تدريب المنافس الثاني (DeepLabV3+) ---`, `# --الخلية 5 ---`, `# الخلية 10`, `# الخلية 11`, `# بديل الخلية الرباعه من اجل التعريفات 4.5`, `# خلية 12`, `# خلية 13`, `# خلية 14`, `# خلية 16`, `# خلية 21`, `# خلية 23`
- Removed first-line titles: `# --- Cell 22: V42 (Per-Lead Lengths + Per-Lead FS + Safe Gating) ---`, `# --- Cell 2: Offline install/import fix (NO internet) ---`, `# --- الخلية 1: التثبيت الذكي (Smart Offline Install) ---`, `# =========================`, `print(len(tdf), tdf['id'].nunique())`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- Colab runtime detection is present; behavior may differ between Kaggle and Colab.
- Dependency installation is embedded in notebook cells, so reproducibility depends on runtime package availability.
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
| First non-empty line | `# --- الخلية 1: التثبيت وإعادة التشغيل ---` |
| Role summary | Environment bootstrap cell with package installation commands. |

**Editorial interpretation**

- Bootstraps the full research environment again, because this notebook reopens training rather than staying in submission-only mode.

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

- stream[stdout] with 265 line(s); excerpt: Requirement already satisfied: numpy<2 in /usr/local/lib/python3.11/dist-packages (1.26.4) Requirement already satisfied: matplotlib in /usr/local/lib/python3.11/dist-packages (3.7...

**Exceptions**

- None

**Warnings**

- None

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 2 |
| First non-empty line | `# --- الخلية 2: الاستيرادات المحدثة (Updated Imports) ---` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Loads the updated import stack and runtime configuration shared by the ensemble experiments.

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

- stream[stderr] with 4 line(s); excerpt: /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Fi...
- stream[stdout] with 5 line(s); excerpt: Creating new Ultralytics Settings v0.0.6 file ✅ View Ultralytics Settings with 'yolo settings' or at '/root/.config/Ultralytics/settings.json' Update Settings with 'yolo settings k...

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

- Keeps the renderer and synthetic ECG utilities available for qualitative debugging and data generation across all ensemble branches.

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

- stream[stdout] with 405 line(s); excerpt: ⬇️ جاري تحميل سجلات PTB-XL الأساسية... Generating record list for: records100/00000/00001_lr Generating record list for: records100/00000/00002_lr Generating record list for: recor...

**Exceptions**

- None

**Warnings**

- None

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 4 |
| First non-empty line | `# --- الخلية 4: الضبط الدقيق على الواقع (Phase 10: Real World Fine-Tuning) - [M10: PSEUDO] ---` |
| Role summary | Definition cell that defines 4 function(s) and 1 class(es). |

**Editorial interpretation**

- Fine-tunes the phase-10 segmentation branch on real or pseudo-labeled data, preserving the main ResNet-style path from notebook (9).

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

- stream[stdout] with 3 line(s); excerpt: 👨‍🏫 تحميل المعلم (Phase 9 Model) لتوليد التسميات الزائفة (Pseudo-Labels)... ⚠️ تحذير: موديل المرحلة 9 غير موجود، نستخدم تهيئة عشوائية (غير مستحسن). 🔄 جاري توليد الأقنعة لـ 1500 صور...
- stream[stderr] with 1 line(s); excerpt: Generating Pseudo-Labels: 100%|██████████| 1500/1500 [07:26<00:00,  3.36it/s]
- error FileNotFoundError: [Errno 2] No such file or directory: 'best_model_phase9.pth'

**Exceptions**

- FileNotFoundError: [Errno 2] No such file or directory: 'best_model_phase9.pth'

**Warnings**

- ⚠️ تحذير: موديل المرحلة 9 غير موجود، نستخدم تهيئة عشوائية (غير مستحسن).

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# بديل الخلية الرباعه من اجل التعريفات 4.5` |
| Role summary | Definition cell that defines 6 function(s) and 2 class(es). |

**Editorial interpretation**

- Replaces and expands the phase-10 helper definitions with stronger losses, richer pseudo-label dataset handling, and safer training utilities that the ensemble branches can reuse.

**Imports**

- gc
- torch
- torch.nn
- segmentation_models_pytorch
- albumentations
- torch.utils.data
- cv2
- glob
- numpy
- tqdm
- os

**Functions defined**

- combined_loss
- __init__
- add_distractors
- __len__
- __getitem__
- _generate_pseudo_labels

**Classes defined**

- DynamicUltimateDataset
- RealWorldDataset

**Constants / bindings**

- REAL_IMG_DIR = /kaggle/input/physionet-ecg-image-digitization
- TEACHER_PATH = /kaggle/input/ecg-final-models/best_model_phase10.pth
- font = cv2.FONT_HERSHEY_SIMPLEX
- img = augmented[image]
- mask = augmented[mask]
- path = self.image_paths[idx]
- pos = []
- texts = ['V1', 'II', '25mm/s', '10mm/mV', 'HR: 72', 'Patient: X', 'FILTER 50Hz']

**Paths mentioned**

- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- 10mm/mV
- 25mm/s
- {img_dir}/**/*.jpg
- {img_dir}/**/*.png

**File reads**

- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- glob.glob: {img_dir}/**/*.png
- glob.glob: {img_dir}/**/*.jpg

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth

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
| First non-empty line | `# --- الخلية الإضافية 1 (النسخة الآمنة): تدريب المنافس الأول (EfficientNet-B3) ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Trains the EfficientNet-B3 competitor model, creating the lighter segmentation checkpoint that later notebooks can compare or ensemble against the ResNet branch.

**Imports**

- gc
- torch
- segmentation_models_pytorch
- torch.optim.lr_scheduler
- torch.utils.data
- tqdm
- numpy
- os

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- BATCH_SIZE = 16
- DB_DIR = physionet_db
- best_loss = avg_loss
- best_real_loss = avg_loss
- epoch_loss = 0

**Paths mentioned**

- EffNet Real-Epoch {epoch+1}/15
- EffNet Syn-Epoch {epoch+1}/30
- best_model_efficientnet_ph10.pth
- temp_effnet_base.pth

**File reads**

- torch.load: temp_effnet_base.pth

**File writes**

- torch.save: temp_effnet_base.pth
- torch.save: best_model_efficientnet_ph10.pth

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- torch.load: temp_effnet_base.pth

**Model saves**

- torch.save: temp_effnet_base.pth
- torch.save: best_model_efficientnet_ph10.pth

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
| First non-empty line | `# --- الخلية الإضافية 4.8 تدريب النموذج الثاني: تدريب المنافس الثاني (DeepLabV3+) ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Trains the DeepLabV3+ competitor model, giving the notebook a third segmentation family with a different decoder bias.

**Imports**

- gc
- torch
- segmentation_models_pytorch

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- BATCH_SIZE = 16
- best_loss = avg_loss
- best_real_loss = avg_loss
- epoch_loss = 0

**Paths mentioned**

- DeepLab Real-Epoch {epoch+1}/15
- DeepLab Syn-Epoch {epoch+1}/30
- best_model_deeplab_ph10.pth
- temp_deeplab_base.pth

**File reads**

- torch.load: temp_deeplab_base.pth

**File writes**

- torch.save: temp_deeplab_base.pth
- torch.save: best_model_deeplab_ph10.pth

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- torch.load: temp_deeplab_base.pth

**Model saves**

- torch.save: temp_deeplab_base.pth
- torch.save: best_model_deeplab_ph10.pth

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
| First non-empty line | `# --الخلية 5 ---` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Reintroduces the mask-to-signal decoding helpers so all three segmentation branches can be evaluated under the same waveform-reconstruction logic.

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

### Cell 9

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 6---` |
| Role summary | General computation cell. |

**Editorial interpretation**

- Runs a focused smoke test that checks whether the revised helpers still produce sensible outputs after the ensemble-related refactor.

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

### Cell 10

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 7 ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Wraps the decoder into a page-level processing helper so real Kaggle pages can be passed through the revised reconstruction stack.

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

### Cell 11

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 8:  ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Keeps the submission-formatting helper in place so ensemble results can still be shaped into the competition schema.

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

### Cell 12

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 9:  ---` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Loads the official Kaggle metadata and page inventory, giving the ensemble notebook direct access to the true evaluation surface.

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

### Cell 13

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# الخلية 10` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds a real-image inference harness so the multiple segmentation branches can be compared on actual scanned pages rather than only synthetic examples.

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

### Cell 14

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# الخلية 11` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Defines grid-detection and calibration helpers for the ensemble era, ensuring all candidate models share the same measurement assumptions.

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

### Cell 15

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 12` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Runs calibration validation on representative examples so errors in paper-scale estimation are not mistaken for model-quality differences.

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

### Cell 16

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 13` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Keeps the sliding-window decoder available for long or awkward strips, preventing whole-lead failures when a single pass is unreliable.

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

### Cell 17

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 14` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Preserves the tuned high-jump waveform solver so sharp ECG deflections can survive decoding across all ensemble candidates.

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

### Cell 18

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 15: المحرك الهندسي المتقدم (Advanced Geometry Engine) ---` |
| Role summary | Definition cell that defines 3 function(s). |

**Editorial interpretation**

- Carries forward the advanced geometry engine, which remains necessary for consistent detector crops and lead alignment.

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

### Cell 19

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 16` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds the cleanup helper that removes grid and background clutter before segmentation and decoding.

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

### Cell 20

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 17: اختبار يدوي (مصحح) ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Provides a corrected manual test helper for carefully inspecting selected examples under the new ensemble setup.

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

### Cell 21

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 18: إعداد بيانات YOLO القتالية (Combat Mode) - [M4: UPDATED] ---` |
| Role summary | Definition cell that defines 3 function(s) and 1 class(es). |

**Editorial interpretation**

- Builds the combat-mode YOLO training dataset again so detector robustness stays aligned with the new segmentation experiments.

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

### Cell 22

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 19: تدريب YOLOv8x القتالي [M4: COMBAT TRAINING] ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Trains or refreshes the combat YOLO detector that later compact notebooks use for lead localization.

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

### Cell 23

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 20: مصنع البيانات المصفح والتدريب التكميلي (Phase 2: Hardening) ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Keeps the phase-2 hardening segmentation branch alive as an additional robustness path in case the ensemble alone is not enough.

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

### Cell 24

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 21` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Adds the integration helpers that let detector outputs, calibration data, and multiple segmentation predictions share one inference contract.

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

### Cell 25

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- Cell 22: V39 Ultimate (Ensemble: ResNet + EffNet + DeepLab) ---` |
| Role summary | Definition cell that defines 16 function(s). |

**Editorial interpretation**

- Defines the final ensemble inference engine that combines YOLO localization with the phase-10 ResNet weights, the EfficientNet-B3 competitor, and the DeepLabV3+ competitor.

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
- clean_pid
- get_image_path
- safe_read_rgb
- preprocess_remove_grid_rgb
- apply_high_pass
- smart_einthoven_fix
- estimate_grid_spacing_px
- choose_ppmv
- viterbi_dp
- viterbi_adaptive
- get_crops_yolo_mapped
- prepare_unet_batch
- predict_ensemble_probmaps
- compute_patient_leads
- score_candidate

**Classes defined**

- None

**Constants / bindings**

- DP_MAX_W = 1400
- DP_SMOOTH = 0.45
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE = 12
- MAX_W = 2048
- MODELS_DIR = /kaggle/input/ecg-final-models1
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv
- TARGET_H = 256
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- YOLO_CONF = 0.1
- YOLO_INF_MAX = 1280
- YOLO_PATH = /kaggle/input/ecg-final-models1/best.pt
- accumulated_preds = preds_model
- best_prev = stacked[which]
- c_0 = dp[idx]
- diffs = []
- img_inf = img_rgb
- lead_idx = lead_indices[j]
- local_grid = global_grid
- mtx = patient_cache[pid[idx]]
- names = yolo_model.names
- nw = 2048
- p1 = /kaggle/input/ecg-final-models1/best_model_phase10.pth
- p2 = /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- p3 = /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- pid = pid[idx]
- prev = dp[idx]
- prob = p_map[j]
- prob_maps = ['p_map']
- sc = scales[j]
- scale = 1.0
- t_len = 5000
- unet_models = []
- val = v
- w_i = widths[i]

**Paths mentioned**

- /kaggle/input/ecg-final-models1
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {MODELS_DIR}/best.pt
- {MODELS_DIR}/best_model_deeplab_ph10.pth
- {MODELS_DIR}/best_model_efficientnet_ph10.pth
- {MODELS_DIR}/best_model_phase10.pth

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- open: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth

**File writes**

- open: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: /kaggle/input/ecg-final-models1/best.pt
- torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_efficientnet_ph10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth

**Stored outputs**

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 26

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# خلية 23` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Validates the ensemble output against the parquet and template expectation before treating the notebook as the provenance run for later deployment notebooks.

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

- None

**Exceptions**

- None

**Warnings**

- None
