# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 32 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-31.md |
| SHA-256 | 86562c53e55691078ac804acecc50dfca87706c9de4c4ec670ea6ac63f3de1ee |
| Size (bytes) | 41,808 |
| Modified (UTC) | 2026-04-18T20:13:05.906565+00:00 |
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
| Interpretation confidence | medium |
| Open questions | 1 |
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
- numpy
- os
- pandas
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

- /kaggle/input/**/*.pth
- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_name_part}*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv

## Symbols Defined

**Functions**

- __init__
- advanced_perspective_correction
- apply_high_pass_filter
- batch_predict_unet
- clean_pid
- compute_patient_leads
- ensure_import
- fast_viterbi
- get_image_path_safe
- get_real_signal
- get_yolo_crops_with_fallback
- install_wheel_by_part
- is_forbidden_wheel
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
- FORBIDDEN_PARTS
- I
- II
- III
- IMAGE_DIR
- LEAD_NAMES
- LEAD_TO_IDX
- M
- MAX_CACHE_PATIENTS
- SAMPLE_PARQUET_PATH
- SUBMISSION_FILE
- TEST_CSV_PATH
- UNET_PATH
- YOLO_PATH
- dpi
- fs_val
- is_forbidden
- pad
- smooth
- success_count
- target_h
- val
- yolo_model

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/**/*.pt
- glob.glob: /kaggle/input/**/*.pth
- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_name_part}*.whl
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
- torch.load: /kaggle/input/**/*.pth[0]
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

- stream: 2
- error: 1

**MIME types**

- None

**Exceptions captured in outputs**

- ModuleNotFoundError: No module named 'segmentation_models_pytorch'

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
- ⚠️ No wheel found for: segmentation_models_pytorch

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- best_model_phase10.pt

**Referenced datasets**

- /kaggle/input/**/*.pth
- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_name_part}*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet

**External files**

- glob.glob: /kaggle/input/**/*.pt
- glob.glob: /kaggle/input/**/*.pth
- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_name_part}*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
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
| Open questions | 1 |
| Confidence | medium |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Self-contained compact inference notebook that replaces repeated phase-14 and phase-15 boilerplate with helper-driven offline installation and a consolidated engine.
- This file is the clearest compact bridge between the earlier research notebooks and the later packaged deployment notebooks.

**Delta notes**

- Compared with notebook (30), this revision internalizes package discovery and collapses the engine into a helper-driven compact deployment block.
- The apparent motivation is to refactor the compact deployment notebooks into more helper-driven and self-contained offline runners that behave predictably in no-internet Kaggle sessions.
- It retains the offline-deployment focus, the qualitative renderer, and the idea that one dominant engine cell should still drive submission export.
- The workflow effect is less boilerplate duplication and a clearer separation between environment repair, helper setup, inference, and export sanity checks.
- What becomes obsolete is the earlier pattern of repeating large inline engine scaffolds and ad hoc install logic across many nearly identical notebooks.

**Open questions**

- This helper-driven offline refactor is clearly important, but it is not fully explicit whether the later no-internet notebooks inherit the helpers themselves or only the engine ideas.

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb`, cell count changed from 5 to 5, stored output types changed from 8 to 3, and exact shared cell sources = 2.
- New imports: `collections`
- Removed imports: `math`, `matplotlib.pyplot`, `timm`
- New model refs: None
- Removed model refs: `YOLO: best.pt`, `YOLO: yolov8n.pt`, `os.path.exists: best.pt`, `os.path.exists: best_model_phase10.pth`, `torch.load: best_model_phase10.pth`
- New first-line titles: `# =========================`
- Removed first-line titles: `# --- الخلية 22: المحرك البلاتيني (Version 32: Literal ID Match & Robust Length) ---`, `# --- الخلية 23: التحقق الآمن (Final Logic Check) ---`, `# --- الخلية 2: الاستيراد والإصلاح الفوري (Import & Fix) ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
- Stored notebook outputs contain 1 execution error(s); treat those cells as unresolved at snapshot time.
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

- Scans local wheel directories and installs what is needed, so package bootstrap becomes data-driven instead of hard-coded.

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
| First non-empty line | `# =========================` |
| Role summary | Definition cell that defines 3 function(s). |

**Editorial interpretation**

- Defines helper functions that filter wheels by Python and platform compatibility and execute the offline installer pipeline.

**Imports**

- sys
- os
- glob
- subprocess
- site
- importlib
- torch
- numpy
- pandas
- cv2
- tqdm
- segmentation_models_pytorch
- ultralytics

**Functions defined**

- is_forbidden_wheel
- install_wheel_by_part
- ensure_import

**Classes defined**

- None

**Constants / bindings**

- FORBIDDEN_PARTS = ['torch', 'torchvision', 'torchaudio', 'triton', 'nvidia_', 'cublas', 'cudnn', 'cuda', 'numpy', 'pandas', 'opencv', 'matplotlib', 'scipy', 'pillow']
- target = subscript[0]
- wheels = /kaggle/input/**/*{wheel_name_part}*.whl

**Paths mentioned**

- /kaggle/input/**/*{wheel_name_part}*.whl

**File reads**

- glob.glob: /kaggle/input/**/*{wheel_name_part}*.whl

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

- stream[stdout] with 5 line(s); excerpt: 🔧 Cell 2: Offline install/import fix (no internet). ⚙️ Installing missing: segmentation_models_pytorch ⚠️ No wheel found for: segmentation_models_pytorch ✅ Already available: timm ...
- error ModuleNotFoundError: No module named 'segmentation_models_pytorch'

**Exceptions**

- ModuleNotFoundError: No module named 'segmentation_models_pytorch'

**Warnings**

- ⚠️ No wheel found for: segmentation_models_pytorch

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
| First non-empty line | `# =========================` |
| Role summary | Definition cell that defines 11 function(s). |

**Editorial interpretation**

- Builds a consolidated inference engine around `/kaggle/input/ecg-final-models/best.pt` and `best_model_phase10.pth`, using the detector for lead localization and the segmentation model for trace recovery.

**Imports**

- gc
- os
- csv
- glob
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
- get_image_path_safe
- apply_high_pass_filter
- smart_einthoven_fix
- advanced_perspective_correction
- robust_multi_point_calibration
- preprocess_remove_grid_rgb
- get_yolo_crops_with_fallback
- batch_predict_unet
- fast_viterbi
- compute_patient_leads

**Classes defined**

- None

**Constants / bindings**

- I = leads_dict[I][idx]
- II = leads_dict[II][idx]
- III = leads_dict[III][idx]
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE_PATIENTS = 16
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- UNET_PATH = /kaggle/input/ecg-final-models/best_model_phase10.pth
- YOLO_PATH = /kaggle/input/ecg-final-models/best.pt
- angles = ['ang']
- c_0 = dp[idx]
- candidates = /kaggle/input/**/*.pth
- clean_crops = []
- fs_val = 500.0
- grid_sizes = []
- lead_part = parts[2]
- leads_matrix = patient_cache[pid_clean_str]
- lname = I[real_idx]
- pad = 5
- pid_part = parts[0]
- prev = dp[idx]
- prob = prob_maps[j]
- processed = ['tens']
- row_id = rid
- scale = scale[j]
- scales = ['scale']
- shapes = ['256', 'new_w']
- smooth = 0.5
- target_h = 256
- val = v
- valid_idx = ['i']

**Paths mentioned**

- /kaggle/input/**/*.pth
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/**/*.pt
- glob.glob: /kaggle/input/**/*.pth
- open: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- torch.load: /kaggle/input/ecg-final-models/best_model_phase10.pth
- torch.load: /kaggle/input/**/*.pth[0]

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
| First non-empty line | `# =========================` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Performs submission integrity checks on the assembled dataframe before writing it, treating row count and column layout as first-class invariants.

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
