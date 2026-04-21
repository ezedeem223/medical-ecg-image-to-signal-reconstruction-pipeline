# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 15 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-14.md |
| SHA-256 | 1e564ce1e148b39f7d5e39038d57d6b903cd1c702260472d3622c8531415f2dd |
| Size (bytes) | 44,806 |
| Modified (UTC) | 2026-04-18T19:38:53.889853+00:00 |
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

- cv2
- glob
- matplotlib.pyplot
- numpy
- os
- pandas
- scipy.signal
- segmentation_models_pytorch
- skimage.measure
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

- .csv
- .parquet
- /kaggle/input/*{keyword}*
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- best.pt
- submission.csv

## Symbols Defined

**Functions**

- __init__
- adaptive_viterbi
- advanced_perspective_correction
- apply_high_pass_filter
- find_dataset_path
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

- glob.glob: /kaggle/input/*{keyword}*
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth
- os.path.exists: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: submission.csv
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: best_model_phase10.pth
- wfdb.rdsamp: self.db_dir/{rec_name}

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install --no-index --find-links={yolo_dir} --find-links={smp_dir} timm segmentation-models-pytorch ultralytics

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

- stream: 3
- error: 1

**MIME types**

- None

**Exceptions captured in outputs**

- ModuleNotFoundError: No module named 'segmentation_models_pytorch'

**Warnings / warning-like lines**

- ⚠️ حدث خطأ أثناء تثبيت pip: Command '['/usr/bin/python3', '-m', 'pip', 'install', '--no-index', '--find-links=/kaggle/input/ultralytics', '--find-links=/kaggle/input/segmentation-models-pytorch', 'timm', 'segmentation-mo

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- best_model_phase10.pt

**Referenced datasets**

- .csv
- .parquet
- /kaggle/input/*{keyword}*
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- /kaggle/input/physionet-ecg-image-digitization/test.csv

**External files**

- glob.glob: /kaggle/input/*{keyword}*
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: best.pt

**Required runtime assumptions**

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

- Compact offline deployment notebook that preserves the fixed final engine while experimenting with different bootstrap tactics.
- The notebook is inference-only; the only moving part between revisions is how aggressively it repairs the environment before running the submission path.

**Delta notes**

- Compared with notebook (13), this revision changes the bootstrap strategy to depend on uploaded offline wheels rather than a standard restart and install path.
- The apparent motivation is to collapse the large research notebooks into a compact Kaggle runner that can be executed quickly during submission iteration.
- It retains the renderer, the current best final engine, and the export-validation pattern from the prior final-build notebook family.
- The workflow effect is shorter rerun time and less hidden dependency on earlier cells, which is valuable once the focus shifts from training to deployment reliability.
- What becomes obsolete is in-notebook training and most exploratory branch work; those remain part of provenance, not part of the active submission path.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb`, cell count changed from 5 to 5, stored output types changed from 8 to 4, and exact shared cell sources = 3.
- New imports: `subprocess`
- Removed imports: `albumentations`, `gc`, `io`, `random`, `scipy.fft`, `shutil`, `skimage.transform`, `sklearn.model_selection`, `torch.nn`, `torch.optim.lr_scheduler`, `torch.utils.data`, `warnings`, `wfdb`
- New model refs: None
- Removed model refs: None
- New first-line titles: `# --- الخلية 1: تثبيت المكتبات من ملفاتك المرفوعة (Smart Offline Mode) ---`, `# --- الخلية 2: استيراد المكتبات وتجهيز البيئة ---`
- Removed first-line titles: `# --- الخلية 1: التثبيت وإعادة التشغيل ---`, `# --- الخلية 2: الاستيرادات المحدثة (Updated Imports) ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
- Stored notebook outputs contain 1 execution error(s); treat those cells as unresolved at snapshot time.
- Stored outputs include 1 warning-like lines worth checking during reruns.
- Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.
- Notebook depends on both object detection and segmentation stacks, increasing environment complexity.
- Checkpoint loading is embedded in the workflow; model file availability is a runtime prerequisite.

## Cell-By-Cell Audit

### Cell 1

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 1 |
| First non-empty line | `# --- الخلية 1: تثبيت المكتبات من ملفاتك المرفوعة (Smart Offline Mode) ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Installs libraries from user-uploaded wheel files in a smart offline mode, assuming Kaggle internet is unavailable but curated wheels are present.

**Imports**

- sys
- os
- glob
- subprocess

**Functions defined**

- find_dataset_path

**Classes defined**

- None

**Constants / bindings**

- find_links_args = ['--find-links={yolo_dir}', '--find-links={smp_dir}']
- paths = /kaggle/input/*{keyword}*

**Paths mentioned**

- /kaggle/input/*{keyword}*

**File reads**

- glob.glob: /kaggle/input/*{keyword}*

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install --no-index --find-links={yolo_dir} --find-links={smp_dir} timm segmentation-models-pytorch ultralytics

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 57 line(s); excerpt: ⚙️ جاري البحث عن ملفات المكتبات وتثبيتها (Offline)... 📍 مسار Ultralytics المكتشف: /kaggle/input/ultralytics 📍 مسار SMP/Timm المكتشف: /kaggle/input/segmentation-models-pytorch 📦 جار...
- stream[stderr] with 2 line(s); excerpt: ERROR: Could not find a version that satisfies the requirement nvidia-cuda-nvrtc-cu12==12.4.127; platform_system == "Linux" and platform_machine == "x86_64" (from torch) (from vers...

**Exceptions**

- None

**Warnings**

- ⚠️ حدث خطأ أثناء تثبيت pip: Command '['/usr/bin/python3', '-m', 'pip', 'install', '--no-index', '--find-links=/kaggle/input/ultralytics', '--find-links=/kaggle/input/segmentation-models-pytorch', 'timm', 'segmentation-mo

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 2 |
| First non-empty line | `# --- الخلية 2: استيراد المكتبات وتجهيز البيئة ---` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Imports the runtime stack and prepares the compact inference environment after the chosen offline installation strategy completes.

**Imports**

- numpy
- pandas
- cv2
- torch
- os
- glob
- tqdm
- matplotlib.pyplot
- scipy.signal
- skimage.measure
- segmentation_models_pytorch
- ultralytics

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

- stream[stdout] with 2 line(s); excerpt: ❌ خطأ فادح: فشل الاستيراد! تأكد من تشغيل الخلية 1 بنجاح. الخطأ: No module named 'segmentation_models_pytorch'
- error ModuleNotFoundError: No module named 'segmentation_models_pytorch'

**Exceptions**

- ModuleNotFoundError: No module named 'segmentation_models_pytorch'

**Warnings**

- None

### Cell 3

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 22: المحرك البلاتيني (Phase 14+15) - [FINAL FIXED BUILD] ---` |
| Role summary | Definition cell that defines 9 function(s). |

**Editorial interpretation**

- Keeps the fixed phase-14 and phase-15 final engine as the stable inference core while the surrounding bootstrap strategy changes.

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- خلية 23: التحقق النهائي (Updated for CSV) ---` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Performs the updated CSV-aware validation and writes the submission file once the compact engine completes.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- MY_SUB_PATH = submission.csv
- OFFICIAL_SAMPLE_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- first_id = my_sub.iloc[0][id]
- first_value = my_sub.iloc[0][value]
- has_sample = False

**Paths mentioned**

- .csv
- .parquet
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- submission.csv

**File reads**

- pd.read_csv: submission.csv
- os.path.exists: submission.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv

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
