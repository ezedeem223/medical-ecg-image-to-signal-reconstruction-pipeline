# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 48 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-47.md |
| SHA-256 | 6bf96f9f4aae6f1b2c37b7c2de50113f01532b799292e755411598d95d2de8e6 |
| Size (bytes) | 41,483 |
| Modified (UTC) | 2026-04-18T21:15:30.110048+00:00 |
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
- re
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

- /kaggle/input
- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/ecg-final-models1
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {MODELS_DIR}/best_model_deeplab_ph10.pth
- {MODELS_DIR}/best_model_efficientnet_ph10.pth
- {MODELS_DIR}/best_model_phase10.pth

## Symbols Defined

**Functions**

- __init__
- apply_high_pass
- ensure_pkg
- get_image_path_robust
- get_real_signal
- get_yolo_crops_mapped
- normalize_id
- predict_ensemble
- preprocess_remove_grid_rgb
- process_patient
- render_to_memory
- safe_read_rgb
- viterbi_adaptive

**Classes**

- UltimateRenderer

**Constants / assigned names**

- CLASS_TO_LEAD_IDX
- DB_DIR
- DEVICE
- DP_MAX_W
- DP_SMOOTH
- FORBIDDEN_PACKAGES
- IMAGE_DIRS
- LEAD_NAMES
- LEAD_TO_IDX
- MAX_CACHE
- MAX_W
- MODELS_DIR
- SAMPLE_PARQUET_PATH
- SUBMISSION_FILE
- TARGET_H
- TEST_CSV_PATH
- USE_DEEPLAB
- USE_EFFICIENTNET
- USE_RESNET
- YOLO_CONF
- YOLO_INF_MAX
- YOLO_PATH
- debug_counter
- dpi
- final_preds
- is_forbidden
- scale
- scale_factor
- success_count
- val
- yolo_model

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: {d}/**/*.jpg
- glob.glob: {d}/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: submission.csv
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
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

- YOLO: /kaggle/input/ecg-final-models1/best.pt
- torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth

## Stored Output Inventory

**Output types**

- stream: 14

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
- ⚠️ تحذير: فشل التحميل (name 'wfdb' is not defined)، سيتم استخدام التوليد الاحتياطي.

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- best_model_deeplab_ph10.pt
- best_model_efficientnet_ph10.pt
- best_model_phase10.pt

**Referenced datasets**

- /kaggle/input
- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/ecg-final-models1
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- /kaggle/input/physionet-ecg-image-digitization

**External files**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: {d}/**/*.jpg
- glob.glob: {d}/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
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

- Compact offline deployment notebook that consumes the notebook (42) model bundle rather than training in place.
- The shell stays minimal while the main engine cell swaps between ensemble, baseline, or benchmark variants.

**Delta notes**

- Compared with notebook (46), the goal shifts from hybridization to benchmarking around the current winner.
- The apparent motivation is to package the notebook (42) checkpoint branch into compact offline runners that can compare ensemble, baseline, hybrid, and benchmark behavior quickly.
- It retains the compact no-internet shell that had already proved useful for Kaggle deployment, as well as the renderer plus final-validation pattern.
- The workflow effect is faster comparison across model strategies without rerunning the heavy training notebook, which is exactly what Phase 1 needs before synthesis.
- What becomes obsolete is the need to keep the ensemble notebook itself open for every comparison; the compact descendants become the operational interface.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb`, cell count changed from 5 to 5, stored output types changed from 14 to 14, and exact shared cell sources = 4.
- New imports: None
- Removed imports: None
- New model refs: `os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth`, `torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth`
- Removed model refs: None
- New first-line titles: `# --- Cell 22: V47 Benchmarking Engine (Based on Winner V46) ---`
- Removed first-line titles: `# --- Cell 22: V43 Hybrid (Ensemble + Robust Paths + Fixed Calibration) ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
- Stored outputs include 11 warning-like lines worth checking during reruns.
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

- stream[stdout] with 11 line(s); excerpt: 🔧 Cell 2: Offline install/import fix (no internet). ✅ Already available: timm ✅ Installed offline: segmentation_models_pytorch ✅ Already available: ultralytics ✅ pyarrow available ...

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
| First non-empty line | `# --- Cell 22: V47 Benchmarking Engine (Based on Winner V46) ---` |
| Role summary | Definition cell that defines 9 function(s). |

**Editorial interpretation**

- Packages a benchmarking engine built from the earlier winning configuration, treating the notebook as a comparative reference point for later fixes.

**Imports**

- gc
- os
- csv
- glob
- math
- re
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

- normalize_id
- get_image_path_robust
- safe_read_rgb
- preprocess_remove_grid_rgb
- apply_high_pass
- viterbi_adaptive
- predict_ensemble
- get_yolo_crops_mapped
- process_patient

**Classes defined**

- None

**Constants / bindings**

- DP_MAX_W = 1400
- DP_SMOOTH = 0.45
- IMAGE_DIRS = ['/kaggle/input/physionet-ecg-image-digitization', '/kaggle/input']
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE = 15
- MAX_W = 2048
- MODELS_DIR = /kaggle/input/ecg-final-models1
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv
- TARGET_H = 256
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- USE_DEEPLAB = False
- USE_EFFICIENTNET = True
- USE_RESNET = False
- YOLO_CONF = 0.1
- YOLO_INF_MAX = 1280
- YOLO_PATH = /kaggle/input/ecg-final-models1/best.pt
- debug_counter = 0
- final_preds = out
- fname = p
- image_paths = []
- img_in = img
- l_idx = valid_indices[k]
- leads_data = patient_cache[pid_clean]
- names = yolo_model.names
- p = /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- pid = parts[0]
- pmap = out[i]
- results = ['out[i]', 'scales[i]']
- scale = 1.0
- scale_factor = 250.0
- template_ids = []
- unet_models = []
- val = patient_cache[pid_clean][valid_indices[k]]
- w_real = widths[i]

**Paths mentioned**

- /kaggle/input
- /kaggle/input/ecg-final-models1
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {MODELS_DIR}/best_model_deeplab_ph10.pth
- {MODELS_DIR}/best_model_efficientnet_ph10.pth
- {MODELS_DIR}/best_model_phase10.pth

**File reads**

- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- glob.glob: {d}/**/*.png
- glob.glob: {d}/**/*.jpg
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth
- open: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
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
- torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth

**Stored outputs**

- stream[stdout] with 5 line(s); excerpt: ⚡ Device: cuda 🧪 Testing Configuration: ResNet=False | EffNet=True | DeepLab=False 📦 Reading Parquet template ids... ✅ Template rows: 75,000 🧠 Scanning template for patient lengths...
- stream[stderr] with 1 line(s); excerpt: Scanning Lengths: 100%|██████████| 75000/75000 [00:00<00:00, 607194.31it/s]
- stream[stdout] with 2 line(s); excerpt: ✅ Lengths mapped for 2 patients. 🗂️ Indexing images (Robust Mode)...
- stream[stderr] with 1 line(s)
- stream[stdout] with 7 line(s); excerpt: ✅ Indexed images: 8,795 (Unique numeric IDs) ✅ fs_map loaded: 2 items ⚙️ Loading models based on configuration... ✅ YOLO loaded. 🔹 Loading EfficientNet-B3... ✅ EfficientNet-B3 Load...
- stream[stderr] with 1 line(s); excerpt: Processing:  36%|███▋      | 27227/75000 [00:02<00:02, 17562.86it/s]
- stream[stdout] with 1 line(s); excerpt: ✅ Processed 1053922973: Found signal!
- stream[stderr] with 1 line(s); excerpt: Processing: 100%|██████████| 75000/75000 [00:02<00:00, 28239.63it/s]
- stream[stdout] with 2 line(s); excerpt: ✅ Processed 2352854581: Found signal! ✅ Submission file generated successfully.
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
