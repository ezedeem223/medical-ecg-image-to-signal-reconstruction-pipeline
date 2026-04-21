# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 38 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-37.md |
| SHA-256 | e891ca6123794882c97d43ff156a21ab3b375c5e77e6920f3e60360fad07cff2 |
| Size (bytes) | 40,216 |
| Modified (UTC) | 2026-04-18T20:15:27.340870+00:00 |
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
- scipy.signal
- segmentation_models_pytorch
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
- /kaggle/input/**/ultralytics
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {DATA_DIR}/**/*.jpg
- {DATA_DIR}/**/*.png
- {DATA_DIR}/sample_submission.parquet
- {DATA_DIR}/test.csv

## Symbols Defined

**Functions**

- __init__
- apply_filters
- clean_pid
- compute_patient
- ensure_pkg
- extract_path_fast
- get_crops_strict
- get_image_path
- get_real_signal
- lead_quality_ok
- preprocess_remove_grid_rgb
- render_to_memory
- robust_grid_spacing_px

**Classes**

- UltimateRenderer

**Constants / assigned names**

- CLASS_TO_LEAD_IDX
- DATA_DIR
- DB_DIR
- DEVICE
- FORBIDDEN_PACKAGES
- I2
- III2
- L2
- LEAD_NAMES
- LEAD_TO_IDX
- MAX_CACHE
- MAX_W
- SAMPLE_PARQUET_PATH
- SUBMISSION_FILE
- TARGET_H
- TEST_CSV_PATH
- UNET_PATH
- YOLO_CONF
- YOLO_MIN_DET
- YOLO_PATH
- detected
- dpi
- is_forbidden
- p
- ppmv
- scale
- success_count
- val
- yolo_model

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: submission.csv
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- wfdb.rdsamp: self.db_dir/{rec_name}

**File writes**

- open: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install path --no-deps --ignore-installed
- subprocess.check_call: sys.executable -m pip install subscript[0] --no-deps --ignore-installed --quiet

**Model loads**

- YOLO: /kaggle/input/ecg-final-models/best.pt
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth

## Stored Output Inventory

**Output types**

- stream: 9

**MIME types**

- None

**Exceptions captured in outputs**

- None

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
- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Field()` function, which has no effect in 
- warnings.warn(
- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'frozen' attribute with value True was provided to the `Field()` function, which has no effect in
- ⚠️ تحذير: فشل التحميل (name 'wfdb' is not defined)، سيتم استخدام التوليد الاحتياطي.

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- best_model_phase10.pt

**Referenced datasets**

- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv

**External files**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
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
| Editorial cell coverage | 5/5 |
| Editorial output translations | 0 |
| Delta notes | 5 |
| Open questions | 0 |
| Confidence | high |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Compact no-internet deployment notebook that keeps only the offline bootstrap, renderer, final engine, and schema check.
- By this stage the notebook family is primarily an engine-tuning series, with each revision swapping one inference policy for another inside the same shell.

**Delta notes**

- Compared with notebook (36), the core engine is refactored into a title-less cell rather than replaced outright.
- The apparent motivation is to refactor the compact deployment notebooks into more helper-driven and self-contained offline runners that behave predictably in no-internet Kaggle sessions.
- It retains the offline-deployment focus, the qualitative renderer, and the idea that one dominant engine cell should still drive submission export.
- The workflow effect is less boilerplate duplication and a clearer separation between environment repair, helper setup, inference, and export sanity checks.
- What becomes obsolete is the earlier pattern of repeating large inline engine scaffolds and ad hoc install logic across many nearly identical notebooks.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb`, cell count changed from 5 to 5, stored output types changed from 7 to 9, and exact shared cell sources = 4.
- New imports: None
- Removed imports: `fractions`
- New model refs: None
- Removed model refs: None
- New first-line titles: `# ============================`
- Removed first-line titles: `# --- Cell 22: V43 ULTIMATE (Lead Map + Dynamic Length + TTA + Per-Lead Sniper Gate + Robust ID Parse) ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
- Stored outputs include 14 warning-like lines worth checking during reruns.
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
| First non-empty line | `# --- Cell 2: Offline install/import fix (NO internet) ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Repairs imports and resolves local package paths explicitly for a no-internet Kaggle session, so the remaining cells can run without external downloads.

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

- target = subscript[0]
- wheels = /kaggle/input/**/*{wheel_hint}*.whl

**Paths mentioned**

- /kaggle/input/**/*{wheel_hint}*.whl

**File reads**

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

- None

**Stored outputs**

- stream[stdout] with 1 line(s); excerpt: 🔧 Cell 2: Offline install/import fix (no internet).
- stream[stderr] with 4 line(s); excerpt: /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Fi...
- stream[stdout] with 10 line(s); excerpt: ✅ Already available: timm ✅ Installed offline: segmentation_models_pytorch ✅ Already available: ultralytics ✅ pyarrow available (parquet OK) ------ Environment Check ------ torch: ...

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
| First non-empty line | `# ============================` |
| Role summary | Definition cell that defines 9 function(s). |

**Editorial interpretation**

- Refactors the same V43-family engine into a generic-titled block; the code still serves as the main inference engine even though the heading no longer says so.

**Imports**

- os
- gc
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

- clean_pid
- get_image_path
- preprocess_remove_grid_rgb
- robust_grid_spacing_px
- apply_filters
- get_crops_strict
- extract_path_fast
- lead_quality_ok
- compute_patient

**Classes defined**

- None

**Constants / bindings**

- DATA_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE = 12
- MAX_W = 2048
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv
- TARGET_H = 256
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- UNET_PATH = /kaggle/input/ecg-final-models/best_model_phase10.pth
- YOLO_CONF = 0.12
- YOLO_MIN_DET = 8
- YOLO_PATH = /kaggle/input/ecg-final-models/best.pt
- clean_crops = ['c']
- detected = 0
- img_inf = img
- inputs = ['t']
- lead = parts[2]
- nw = 2048
- out_dict = patient_cache[pid[idx]]
- pid = pid[idx]
- ppmv = 50.0
- prob = preds[li]
- scale = 1.0
- scales = ['s']
- val = v
- valid = diffs[idx]
- w_orig = shape[2]

**Paths mentioned**

- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {DATA_DIR}/**/*.jpg
- {DATA_DIR}/**/*.png
- {DATA_DIR}/sample_submission.parquet
- {DATA_DIR}/test.csv

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- open: submission.csv
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth

**File writes**

- open: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: /kaggle/input/ecg-final-models/best.pt
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth

**Stored outputs**

- stream[stdout] with 12 line(s); excerpt: ⚡ Device: cuda 📦 Reading template ids... ✅ Template rows: 75,000 ✅ test.csv parsed: 24 rows | unique pids: 2 pid: 1053922973 | lens: {'I': 2500, 'II': 10000, 'III': 2500, 'aVR': 25...
- stream[stderr] with 1 line(s); excerpt: Processing: 100%|██████████| 75000/75000 [00:03<00:00, 21328.01it/s]
- stream[stdout] with 1 line(s); excerpt: ✅ Done. submission.csv ready.

**Exceptions**

- None

**Warnings**

- None

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 5 |
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

- stream[stdout] with 4 line(s); excerpt: 🔍 Validating submission.csv strictly... ✅ All checks passed. 📦 submission.csv size: 1.94 MB 🎉 Ready to Submit.

**Exceptions**

- None

**Warnings**

- None
