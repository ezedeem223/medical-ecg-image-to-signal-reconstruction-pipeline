# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 20 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-19.md |
| SHA-256 | 1a54cd37bf76dbdd755feaf1cfba44177c7439eeff12daa1a88d1ba80387269b |
| Size (bytes) | 43,419 |
| Modified (UTC) | 2026-04-18T19:42:02.500041+00:00 |
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
- /kaggle/input/**/*.whl
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
- get_real_signal
- get_yolo_crops_with_fallback
- preprocess_remove_grid_rgb
- render_to_memory
- robust_multi_point_calibration
- smart_einthoven_fix

**Classes**

- UltimateRenderer

**Constants / assigned names**

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
- target_fs
- target_h
- yolo_model

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/ultralytics
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

- subprocess.check_call: sys.executable -m pip install path --no-deps --ignore-installed

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

- stream: 2
- error: 1

**MIME types**

- None

**Exceptions captured in outputs**

- ModuleNotFoundError: No module named 'segmentation_models_pytorch'

**Warnings / warning-like lines**

- ⚠️ فشل تثبيت: triton-3.0.0-1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
- ⚠️ فشل تثبيت: pyyaml-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
- ⚠️ فشل تثبيت: markupsafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: fonttools-4.53.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: charset_normalizer-3.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: contourpy-1.2.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: triton-3.5.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- best_model_phase10.pt

**Referenced datasets**

- .csv
- .parquet
- /kaggle/input/**/*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv

**External files**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv

**Required runtime assumptions**

- Assumes Kaggle input mounts are available.
- Assumes offline wheel files are available under the input mounts.
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

- Compact offline inference notebook built to run on Kaggle without internet access.
- The workflow is stable by this point; the notebook series now iterates mainly on the central inference engine and its validation rules.

**Delta notes**

- Compared with notebook (18), this revision returns to a smart offline install and pivots the engine toward GPU-batched throughput.
- The apparent motivation is to harden the compact deployment flow against concrete Kaggle failures such as schema mismatches, identifier parsing problems, memory pressure, and filesystem restrictions.
- It retains the five-cell compact shell and the renderer-to-engine-to-validation cadence established in the previous compact notebooks.
- The workflow effect is cumulative robustness: each revision tunes the same basic submission runner so it survives more edge cases without reopening training.
- What becomes obsolete is the earlier, more fragile assumption that IDs, lengths, row ordering, and writable paths will behave perfectly by default.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (18).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (18).ipynb`, cell count changed from 5 to 5, stored output types changed from 8 to 3, and exact shared cell sources = 3.
- New imports: None
- Removed imports: None
- New model refs: None
- Removed model refs: None
- New first-line titles: `# --- الخلية 1: التثبيت الذكي (Smart Offline Install) ---`, `# --- الخلية 22: المحرك البلاتيني المسرّع (GPU Batch Edition) ---`
- Removed first-line titles: `# --- الخلية 1: التثبيت الشامل (Brute Force Installation) ---`, `# --- الخلية 22: المحرك البلاتيني (Phase 14+15) - [FINAL FIXED BUILD] ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
- Stored notebook outputs contain 1 execution error(s); treat those cells as unresolved at snapshot time.
- Stored outputs include 10 warning-like lines worth checking during reruns.
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

- stream[stdout] with 17 line(s); excerpt: ⚙️ جاري تثبيت المكتبات الضرورية فقط (حماية الـ GPU)... 📦 تم العثور على 95 ملف في الداتا سيت. ⚠️ فشل تثبيت: triton-3.0.0-1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl...

**Exceptions**

- None

**Warnings**

- ⚠️ فشل تثبيت: triton-3.0.0-1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl
- ⚠️ فشل تثبيت: pyyaml-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: kiwisolver-1.4.5-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
- ⚠️ فشل تثبيت: markupsafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: fonttools-4.53.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: charset_normalizer-3.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: contourpy-1.2.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
- ⚠️ فشل تثبيت: pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: triton-3.5.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl
- ⚠️ فشل تثبيت: markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 2 |
| First non-empty line | `# --- الخلية 2: استيراد المكتبات وتجهيز البيئة ---` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Imports the runtime stack and applies the notebook's path or package fixes immediately, so later cells can assume a stable offline inference environment.

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
| First non-empty line | `# --- الخلية 22: المحرك البلاتيني المسرّع (GPU Batch Edition) ---` |
| Role summary | Definition cell that defines 8 function(s). |

**Editorial interpretation**

- Deploys a GPU-batched version of the platinum engine, prioritizing throughput while still assuming rows and IDs are well-behaved.

**Imports**

- None

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

- I = leads[I][idx]
- II = leads[II][idx]
- III = leads[III][idx]
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- UNET_MODEL_PATH = /kaggle/input/ecg-final-models/best_model_phase10.pth
- YOLO_MODEL_PATH = /kaggle/input/ecg-final-models/best.pt
- angles = ['angle']
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
- prob = final_preds_np[i][idx_in_batch]
- prob_map = final_preds_np[i]
- prob_maps = ['final_preds_np[i]']
- processed_inputs = ['tens']
- s = leads_vals[l]
- scale = scale[idx_in_batch]
- scales = ['scale']
- shapes = ['256', 'new_w']
- sid = row[id]
- smooth_factor = 0.5
- sources = indicesshifts
- target_fs = 500.0
- target_h = 256
- v_0 = dp[idx]
- v_m1 = c_m10.5
- v_p1 = c_p10.5
- valid_indices = ['i']

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

- None

**Exceptions**

- None

**Warnings**

- None
