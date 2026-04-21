# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 22 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-21.md |
| SHA-256 | bcb5077a9249f67dd911e9bf67e37101efee1ef38a4c0b24bfff898c45e1d7dd |
| Size (bytes) | 41,811 |
| Modified (UTC) | 2026-04-18T19:42:34.775471+00:00 |
| Inferred role | Offline Kaggle inference pipeline variant with packaged dependencies. |

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

- csv
- cv2
- gc
- glob
- importlib
- matplotlib.pyplot
- numpy
- os
- pandas
- scipy.signal
- segmentation_models_pytorch
- site
- subprocess
- sys
- timm
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
- /kaggle/input/**/*.whl
- /kaggle/input/**/*{package_name_part}*.whl
- /kaggle/input/**/ultralytics
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
- advanced_perspective_correction
- apply_high_pass_filter
- batch_predict_unet
- fast_viterbi
- force_install
- get_real_signal
- get_yolo_crops_with_fallback
- preprocess_remove_grid_rgb
- render_to_memory
- robust_multi_point_calibration
- smart_einthoven_fix

**Classes**

- UltimateRenderer

**Constants / assigned names**

- BUFFER_SIZE
- DB_DIR
- DEVICE
- FORBIDDEN_PACKAGES
- I
- II
- III
- IMAGE_DIR
- LEAD_NAMES
- M
- MY_SUB_PATH
- OFFICIAL_SAMPLE_PATH
- SUBMISSION_FILE
- TEST_CSV_PATH
- UNET_MODEL_PATH
- YOLO_MODEL_PATH
- dpi
- fallback_path
- has_sample
- is_forbidden
- pad
- smooth_factor
- success_count
- target_h
- yolo_model

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{package_name_part}*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
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

- open: submission.csv
- open[a]: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install path --no-deps --ignore-installed
- subprocess.check_call: sys.executable -m pip install subscript[0] --no-deps --ignore-installed --quiet

**Model loads**

- YOLO: /kaggle/input/ecg-final-models/best.pt
- YOLO: best.pt
- YOLO: yolov8n.pt
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

- ⚠️ فشل تثبيت: pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: triton-3.5.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: triton-3.0.0-1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
- ⚠️ فشل تثبيت: pyyaml-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
- ⚠️ فشل تثبيت: markupsafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: fonttools-4.53.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: charset_normalizer-3.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: contourpy-1.2.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ SMP غير موجود، جاري التثبيت...
- ⚠️ تحذير: لا تزال هناك مشكلة في المكتبات، لكن سنحاول الاستمرار. الخطأ: ❌  Download failure for https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt. Environment is not online.
- ⚠️ تحذير: فشل التحميل (name 'wfdb' is not defined)، سيتم استخدام التوليد الاحتياطي.

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- yolov8n.pt
- best_model_phase10.pt

**Referenced datasets**

- .csv
- .parquet
- /kaggle/input/**/*.whl
- /kaggle/input/**/*{package_name_part}*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization

**External files**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{package_name_part}*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- open[a]: submission.csv
- open[w]: submission.csv

**Required runtime assumptions**

- Assumes Kaggle input mounts are available.
- Assumes offline wheel files are available under the input mounts.
- Assumes ultralytics/YOLO is available for lead localization.
- Assumes PyTorch checkpoint loading is available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.

**Outputs created or updated**

- open: submission.csv
- open[a]: submission.csv
- open[w]: submission.csv

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

- Compact offline inference notebook built to run on Kaggle without internet access.
- The workflow is stable by this point; the notebook series now iterates mainly on the central inference engine and its validation rules.

**Delta notes**

- Compared with notebook (20), this revision sacrifices throughput to reduce OOM and long-run instability.
- The apparent motivation is to harden the compact deployment flow against concrete Kaggle failures such as schema mismatches, identifier parsing problems, memory pressure, and filesystem restrictions.
- It retains the five-cell compact shell and the renderer-to-engine-to-validation cadence established in the previous compact notebooks.
- The workflow effect is cumulative robustness: each revision tunes the same basic submission runner so it survives more edge cases without reopening training.
- What becomes obsolete is the earlier, more fragile assumption that IDs, lengths, row ordering, and writable paths will behave perfectly by default.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb`, cell count changed from 5 to 5, stored output types changed from 9 to 8, and exact shared cell sources = 4.
- New imports: `csv`
- Removed imports: `skimage.measure`
- New model refs: None
- Removed model refs: None
- New first-line titles: `# --- الخلية 22: المحرك البلاتيني (Memory Safe Edition - Streaming) ---`
- Removed first-line titles: `# --- الخلية 22: المحرك البلاتيني المسرّع (GPU Batch Edition) - [CORRECTED] ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
- Stored outputs include 13 warning-like lines worth checking during reruns.
- Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.
- Notebook depends on both object detection and segmentation stacks, increasing environment complexity.
- Checkpoint loading is embedded in the workflow; model file availability is a runtime prerequisite.

## Cell-By-Cell Audit

### Cell 1

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 1 |
| First non-empty line | `# --- الخلية 1: التثبيت الذكي (Smart Offline Install) ---` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Bootstraps the environment in smart offline mode by scanning local wheel sources first, reflecting the assumption that internet access may be unavailable on Kaggle.

**Imports**

- sys
- os
- glob
- subprocess
- torch

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- FORBIDDEN_PACKAGES = ['torch-', 'torchvision', 'torchaudio', 'numpy', 'pandas', 'opencv', 'matplotlib', 'scipy', 'pillow']
- all_whls = /kaggle/input/**/*.whl
- is_forbidden = True
- parent = d
- src_dirs = /kaggle/input/**/ultralytics
- success_count = 0

**Paths mentioned**

- /kaggle/input/**/*.whl
- /kaggle/input/**/ultralytics

**File reads**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/ultralytics

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install path --no-deps --ignore-installed

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 17 line(s); excerpt: ⚙️ جاري تثبيت المكتبات الضرورية فقط (حماية الـ GPU)... 📦 تم العثور على 95 ملف في الداتا سيت. ⚠️ فشل تثبيت: pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manyl...

**Exceptions**

- None

**Warnings**

- ⚠️ فشل تثبيت: pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: triton-3.5.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: triton-3.0.0-1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
- ⚠️ فشل تثبيت: pyyaml-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
- ⚠️ فشل تثبيت: markupsafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: fonttools-4.53.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: charset_normalizer-3.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: contourpy-1.2.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 2 |
| First non-empty line | `# --- الخلية 2: الاستيراد والإصلاح الفوري (Import & Fix) ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Imports the runtime stack and applies the notebook's path or package fixes immediately, so later cells can assume a stable offline inference environment.

**Imports**

- sys
- os
- glob
- subprocess
- numpy
- pandas
- cv2
- torch
- tqdm
- matplotlib.pyplot
- scipy.signal
- segmentation_models_pytorch
- ultralytics
- timm
- site
- importlib

**Functions defined**

- force_install

**Classes defined**

- None

**Constants / bindings**

- files = /kaggle/input/**/*{package_name_part}*.whl
- target_whl = subscript[0]

**Paths mentioned**

- /kaggle/input/**/*{package_name_part}*.whl

**File reads**

- glob.glob: /kaggle/input/**/*{package_name_part}*.whl

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install subscript[0] --no-deps --ignore-installed --quiet

**Model loads**

- YOLO: yolov8n.pt

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 9 line(s); excerpt: 🔧 جاري التحقق من المكتبات المفقودة وتثبيتها يدوياً... ⚠️ SMP غير موجود، جاري التثبيت... ✅ تم التثبيت اليدوي بنجاح: segmentation_models_pytorch-0.5.0-py3-none-any.whl 🎉 تم استيراد S...

**Exceptions**

- None

**Warnings**

- ⚠️ SMP غير موجود، جاري التثبيت...
- ⚠️ تحذير: لا تزال هناك مشكلة في المكتبات، لكن سنحاول الاستمرار. الخطأ: ❌  Download failure for https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt. Environment is not online.

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

- stream[stdout] with 3 line(s); excerpt: ⬇️ جاري تحميل سجلات PTB-XL الأساسية... ⚠️ تحذير: فشل التحميل (name 'wfdb' is not defined)، سيتم استخدام التوليد الاحتياطي. ✅ تم تحديث الخلية 3: محرك الرسم الحي جاهز (DPI=200).

**Exceptions**

- None

**Warnings**

- ⚠️ تحذير: فشل التحميل (name 'wfdb' is not defined)، سيتم استخدام التوليد الاحتياطي.

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 4 |
| First non-empty line | `# --- الخلية 22: المحرك البلاتيني (Memory Safe Edition - Streaming) ---` |
| Role summary | Definition cell that defines 8 function(s). |

**Editorial interpretation**

- Rewrites the engine into a streaming memory-safe variant, trading raw speed for survival on constrained Kaggle sessions.

**Imports**

- gc
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
- csv

**Functions defined**

- apply_high_pass_filter
- smart_einthoven_fix
- fast_viterbi
- batch_predict_unet
- robust_multi_point_calibration
- advanced_perspective_correction
- get_yolo_crops_with_fallback
- preprocess_remove_grid_rgb

**Classes defined**

- None

**Constants / bindings**

- BUFFER_SIZE = 100000
- I = leads[I][idx]
- II = leads[II][idx]
- III = leads[III][idx]
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- SUBMISSION_FILE = submission.csv
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- UNET_MODEL_PATH = /kaggle/input/ecg-final-models/best_model_phase10.pth
- YOLO_MODEL_PATH = /kaggle/input/ecg-final-models/best.pt
- buffer_rows = []
- c_0 = dp[idx]
- clean = grid_sizes[idx]
- clean_crops = []
- conf = box.conf[0]
- crop_orig = clean_crops[idx_in_batch]
- fallback_path = best.pt
- grid_sizes = []
- lname = I[real_idx]
- pad = 5
- prev_cost = dp[idx]
- prob = prob_maps[idx_in_batch]
- processed_inputs = ['tens']
- s = leads_vals[l]
- scale = scale[idx_in_batch]
- scales = ['scale']
- shapes = ['256', 'new_w']
- sid = row[id]
- smooth_factor = 0.5
- target_h = 256
- valid_indices = ['i']

**Paths mentioned**

- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- best.pt
- submission.csv

**File reads**

- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: best.pt
- os.path.exists: best_model_phase10.pth
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- open: submission.csv
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: best_model_phase10.pth

**File writes**

- open: submission.csv
- open[w]: submission.csv
- open[a]: submission.csv

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

- stream[stdout] with 3 line(s); excerpt: ⚡ حالة المسرع: cuda ⚙️ جاري تحميل المحرك البلاتيني... 🚀 بدء الاستخراج البلاتيني (Memory Safe Mode)...
- stream[stderr] with 1 line(s); excerpt: Processing: 100%|██████████| 24/24 [00:30<00:00,  1.29s/it]
- stream[stdout] with 1 line(s); excerpt: ✅ تم حفظ submission.csv بنجاح! الذاكرة آمنة الآن.
- stream[stderr] with 1 line(s)

**Exceptions**

- None

**Warnings**

- None

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 5 |
| First non-empty line | `# --- خلية 23: التحقق النهائي (Updated for CSV) ---` |
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

- stream[stdout] with 12 line(s); excerpt: 🔍 جاري التحقق من ملف CSV (Long Format)... ✅ تم تحميل ملفك: submission.csv ✅ أسماء الأعمدة صحيحة (id, value). ✅ نوع البيانات (float/number) صحيح. 🔍 عينة من الـ ID في ملفك: 105392297...

**Exceptions**

- None

**Warnings**

- None
