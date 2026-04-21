# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 13 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-12.md |
| SHA-256 | daecfd1472a8b8b46bfc24afc38765bd04e5f9927d5158baa17ca01a4f88b837 |
| Size (bytes) | 94,932 |
| Modified (UTC) | 2026-04-18T19:35:18.609125+00:00 |
| Inferred role | Kaggle ECG digitization inference notebook combining YOLO and segmentation. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 5 |
| Cell count | 5 |
| Code cells | 5 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 0 |
| Editorial cell notes | 5 |
| Editorial output notes | 0 |
| Interpretation confidence | high |
| Open questions | 0 |
| Editorial complete | yes |
| Kernel | {"display_name": "Python 3", "language": "python", "name": "python3"} |
| Language info | {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.11.13"} |

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

- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- best.pt
- submission.parquet

## Symbols Defined

**Functions**

- __init__
- adaptive_viterbi
- advanced_perspective_correction
- apply_high_pass_filter
- get_real_signal
- get_yolo_crops_with_fallback
- predict_with_tta
- preprocess_remove_grid_rgb
- render_to_memory
- robust_multi_point_calibration
- smart_einthoven_fix
- suppress_vertical_artifacts

**Classes**

- UltimateRenderer

**Constants / assigned names**

- DB_DIR
- DEVICE
- I
- II
- III
- IMAGE_DIR
- LEAD_NAMES
- M
- MY_SUB_PATH
- OFFICIAL_SAMPLE_PATH
- TEST_CSV_PATH
- UNET_MODEL_PATH
- YOLO_MODEL_PATH
- dpi
- fallback_path
- has_sample
- pad
- target_h
- yolo_model

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- pd.read_parquet: submission.parquet
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: best_model_phase10.pth
- wfdb.rdsamp: self.db_dir/{rec_name}

**File writes**

- None

**Shell commands**

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image pyarrow fastparquet wfdb
- !pip install ultralytics

**subprocess calls**

- None

**Model loads**

- YOLO: /kaggle/input/ecg-final-models/best.pt
- YOLO: best.pt
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: best_model_phase10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth

## Stored Output Inventory

**Output types**

- stream: 8

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
- best_model_phase10.pt

**Referenced datasets**

- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.parquet
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png

**External files**

- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv

**Required runtime assumptions**

- Assumes in-notebook shell execution is allowed for package installation or environment repair.
- Assumes in-notebook dependency installation is permitted.
- Assumes Kaggle input mounts are available.
- Assumes ultralytics/YOLO is available for lead localization.
- Assumes PyTorch checkpoint loading is available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.

**Outputs created or updated**

- None

## Phase 1 Closure Status

| Field | Value |
| --- | --- |
| Notebook summary | present |
| Editorial cell coverage | 5/5 |
| Editorial output translations | 0 |
| Delta notes | 5 |
| Open questions | 0 |
| Confidence | high |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Compact submission-focused notebook that keeps only environment bootstrap, imports, renderer, final engine, and export validation.
- The training and exploratory branches are removed so the notebook can act as a fast Kaggle inference run rather than a research diary.

**Delta notes**

- Compared with notebook (11), the main change is a repaired final engine cell rather than a new workflow shape.
- The apparent motivation is to collapse the large research notebooks into a compact Kaggle runner that can be executed quickly during submission iteration.
- It retains the renderer, the current best final engine, and the export-validation pattern from the prior final-build notebook family.
- The workflow effect is shorter rerun time and less hidden dependency on earlier cells, which is valuable once the focus shifts from training to deployment reliability.
- What becomes obsolete is in-notebook training and most exploratory branch work; those remain part of provenance, not part of the active submission path.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb`, cell count changed from 5 to 5, stored output types changed from 8 to 8, and exact shared cell sources = 4.
- New imports: None
- Removed imports: None
- New model refs: None
- Removed model refs: None
- New first-line titles: `# --- الخلية 22: المحرك البلاتيني (Phase 14+15) - [FINAL FIXED BUILD] ---`
- Removed first-line titles: `# --- الخلية 22: المحرك البلاتيني (Phase 14+15) مع المسارات الدائمة - [FINAL & FIXED] ---`

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
| Execution count | 1 |
| First non-empty line | `# --- الخلية 1: التثبيت وإعادة التشغيل ---` |
| Role summary | Environment bootstrap cell with package installation commands. |

**Editorial interpretation**

- Bootstraps the environment again for another compact inference-only run.

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

- Imports the trimmed inference stack and resolves the runtime state needed by the repaired engine cell.

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

- Keeps the high-quality renderer in the notebook as a debugging surface, so predicted masks and extracted signals can still be inspected visually before submission export.

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
| First non-empty line | `# --- الخلية 22: المحرك البلاتيني (Phase 14+15) - [FINAL FIXED BUILD] ---` |
| Role summary | Definition cell that defines 9 function(s). |

**Editorial interpretation**

- Applies another fixed-build edit to the phase-14 and phase-15 engine, targeting remaining path or runtime issues while keeping the compact form.

**Imports**

- torch
- ultralytics
- pandas
- numpy
- cv2
- os
- glob
- tqdm
- scipy.signal
- segmentation_models_pytorch
- matplotlib.pyplot
- skimage.measure

**Functions defined**

- apply_high_pass_filter
- smart_einthoven_fix
- suppress_vertical_artifacts
- predict_with_tta
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
- UNET_MODEL_PATH = /kaggle/input/ecg-final-models/best_model_phase10.pth
- YOLO_MODEL_PATH = /kaggle/input/ecg-final-models/best.pt
- center = []
- clean_grid = grid_sizes[idx]
- conf = box.conf[0]
- crops = ['image[idx]']
- fallback_path = best.pt
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

- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- best.pt

**File reads**

- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: best_model_phase10.pth

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: /kaggle/input/ecg-final-models/best.pt
- YOLO: best.pt
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: best_model_phase10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth

**Stored outputs**

- stream[stdout] with 4 line(s); excerpt: ⚙️ جاري تحميل المحرك البلاتيني (Phase 14+15)... ✅ YOLO (Combat): مفعل (تم التحميل من Input). 💎 U-Net (Phase 10): مفعل (تم التحميل من Input). 🚀 بدء الاستخراج البلاتيني (Phase 14+15)...
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 24/24 [11:04<00:00, 27.68s/it]
- stream[stdout] with 2 line(s); excerpt: 💾 الحفظ النهائي (CSV Format)... ✅ تم حفظ submission.csv بنجاح! الملف جاهز للمسابقة.

**Exceptions**

- None

**Warnings**

- None

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 5 |
| First non-empty line | `# خلية 23` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Validates the assembled dataframe against the sample-submission schema and writes the final CSV only after row count and column layout look consistent.

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

- stream[stdout] with 3 line(s); excerpt: 🔍 جاري التحقق من التنسيق الطويل (Long Format)... ❌ حدث خطأ أثناء التحقق: [Errno 2] No such file or directory: 'submission.parquet'

**Exceptions**

- None

**Warnings**

- None
