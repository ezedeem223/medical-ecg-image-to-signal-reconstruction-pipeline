# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (51).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 52 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (51).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-51.md |
| SHA-256 | ded83ec38a685b6c115422eee92d846c54ec426802048f1664f46c388074e198 |
| Size (bytes) | 57,721 |
| Modified (UTC) | 2026-04-18T21:16:18.033543+00:00 |
| Inferred role | Offline Kaggle inference pipeline variant with packaged dependencies. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 5 |
| Cell count | 6 |
| Code cells | 6 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 0 |
| Editorial cell notes | 6 |
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
- shutil
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
- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv

## Symbols Defined

**Functions**

- _normalize_lead_name
- amplitude_safety
- apply_high_pass
- choose_ppmv
- clean_pid
- compute_patient_leads
- ensure_pkg
- estimate_grid_spacing_px
- find_first
- get_crops_yolo_mapped
- get_image_path
- lead_token_to_idx
- load_state_safely
- model_predict_prob
- parse_rid
- predict_unet_probmaps
- prepare_unet_batch
- preprocess_remove_grid_rgb
- safe_read_rgb
- score
- smart_einthoven_fix
- viterbi_adaptive
- viterbi_dp

**Classes**

- None

**Constants / assigned names**

- CLASS_TO_LEAD_IDX
- DEVICE
- DP_MAX_W
- DP_SMOOTH
- FALLBACK_PPMV_RESIZED
- FORBIDDEN_PACKAGES
- I
- II
- III
- IMAGE_DIR
- LEAD_NAMES
- LEAD_TO_IDX
- MAX_CACHE
- MAX_W
- NEW_BEST_DST
- NEW_BEST_SRC
- NEW_UNET_PATH
- OLD_UNET_PATH
- SAMPLE_PARQUET_PATH
- SUBMISSION_FILE
- TARGET_H
- TEST_CSV_PATH
- USE_OLD_FALLBACK
- YOLO_CONF
- YOLO_INF_MAX
- YOLO_PATH
- bad_parse
- fs
- is_forbidden
- old_unet
- scale
- success_count
- t_len
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
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: submission.csv
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet

**File writes**

- open: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install path --no-deps --ignore-installed
- subprocess.check_call: sys.executable -m pip install subscript[0] --no-deps --ignore-installed --quiet

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

## Stored Output Inventory

**Output types**

- stream: 14

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
- Processing Rows:   0%|          | 0/75000 [00:00<?, ?it/s]/tmp/ipykernel_20/2459418948.py:537: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.

## Observed Dependency Summary

**Referenced checkpoints**

- best_model_effb3_phase9_ddp.pt

**Referenced datasets**

- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
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
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
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
| Editorial cell coverage | 6/6 |
| Editorial output translations | 0 |
| Delta notes | 5 |
| Open questions | 0 |
| Confidence | high |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- EffB3-focused inference notebook that hardens ID parsing and path resolution around the new checkpoint.
- These notebooks keep the same compact shell but make the new EffB3 checkpoint a first-class participant in inference decisions.

**Delta notes**

- Compared with notebook (50), the emphasis moves from counters and warnings to safer identifier and path handling.
- The apparent motivation is to bring the EfficientNet-B3 branch into the active deployment flow and determine whether it should replace or complement the older segmentation weights.
- It retains the compact no-internet runner, the renderer, and the final validation shell from the prior deployment families.
- The workflow effect is a new inference-routing era where the notebook must decide between old and new checkpoints instead of assuming one inherited phase-10 default.
- What becomes obsolete is the assumption that the older single-model path is sufficient on its own; checkpoint selection and fallback logic become part of the deployment contract.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb`, cell count changed from 6 to 6, stored output types changed from 10 to 14, and exact shared cell sources = 3.
- New imports: None
- Removed imports: `warnings`
- New model refs: None
- Removed model refs: `YOLO: /kaggle/input/ecg-final-models1/best.pt`, `os.path.exists: /kaggle/input/ecg-final-models1/best.pt`, `os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth`, `os.path.exists: /kaggle/working/best_model_effb3_phase9_ddp.pth`, `torch.load: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth`, `torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth`
- New first-line titles: `# --- Cell 22: V39+++ Ultimate (Robust ID Parser + NEW EffB3 UNet + Safe Calibration + Optional OLD fallback) ---`, `# --- Cell 2: Offline install/import fix + model path resolver (NO internet) ---`
- Removed first-line titles: `# --- Cell 22: V39++ Ultimate (NEW effb3 + OLD fallback) + fs-based length + better calibration + debug counters ---`, `# --- Cell 2: Offline install/import fix (NO internet) + model paths + quiet warnings ---`

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
| First non-empty line | `# --- Cell 2: Offline install/import fix + model path resolver (NO internet) ---` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Imports the runtime stack and resolves model and data paths dynamically, making the notebook less dependent on one hard-coded Kaggle directory layout.

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
- find_first

**Classes defined**

- None

**Constants / bindings**

- hits = []
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
- stream[stdout] with 14 line(s); excerpt: ✅ Already available: timm ✅ Installed offline: segmentation_models_pytorch ✅ Already available: ultralytics ✅ pyarrow available (parquet OK) ------ Environment Check ------ torch: ...

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
| First non-empty line | `# --- Cell 2.5: Attach NEW trained model (EffB3) to inference ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Attaches the newer EfficientNet-B3 checkpoint to the inference stack and defines how it should replace or complement the older segmentation weights.

**Imports**

- os
- shutil

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- NEW_BEST_DST = /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- NEW_BEST_SRC = /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

**Paths mentioned**

- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

**File reads**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

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

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

**Stored outputs**

- stream[stdout] with 2 line(s); excerpt: ✅ NEW model ready: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth Exists: True

**Exceptions**

- None

**Warnings**

- None

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 4 |
| First non-empty line | `# # --- الخلية 3: محرك الرسم الحي (Ultimate Renderer) - [M3: UPDATED] ---` |
| Role summary | Rendering / synthetic ECG image generation cell. |

**Editorial interpretation**

- Keeps the high-quality renderer in the notebook as a debugging surface, so predicted masks and extracted signals can still be inspected visually before submission export.

**Imports**

- None

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

- stream[stdout] with 1 line(s); excerpt: ✅ Cell 3 disabled: Renderer/PTB-XL not needed for submission.

**Exceptions**

- None

**Warnings**

- None

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 5 |
| First non-empty line | `# --- Cell 22: V39+++ Ultimate (Robust ID Parser + NEW EffB3 UNet + Safe Calibration + Optional OLD fallback) ---` |
| Role summary | Definition cell that defines 21 function(s). |

**Editorial interpretation**

- Hardens the same dual-model engine with a more robust ID parser and safer calibration choices so mismatched paths do not poison the submission.

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

- parse_rid
- clean_pid
- get_image_path
- _normalize_lead_name
- load_state_safely
- safe_read_rgb
- preprocess_remove_grid_rgb
- apply_high_pass
- smart_einthoven_fix
- estimate_grid_spacing_px
- choose_ppmv
- amplitude_safety
- viterbi_dp
- viterbi_adaptive
- get_crops_yolo_mapped
- prepare_unet_batch
- model_predict_prob
- predict_unet_probmaps
- compute_patient_leads
- lead_token_to_idx
- score

**Classes defined**

- None

**Constants / bindings**

- DP_MAX_W = 1400
- DP_SMOOTH = 0.45
- FALLBACK_PPMV_RESIZED = 220.0
- I = leads[I][idx]
- II = leads[II][idx]
- III = leads[III][idx]
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE = 12
- MAX_W = 2048
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv
- TARGET_H = 256
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- USE_OLD_FALLBACK = False
- YOLO_CONF = 0.1
- YOLO_INF_MAX = 1280
- bad_parse = 0
- best_prev = stacked[which]
- c_0 = dp[idx]
- diffs = []
- fs = 500.0
- img_inf = img_rgb
- items = []
- lead_idx = lead_indices[j]
- local_grid = global_grid
- mtx = patient_cache[pid]
- nw = 2048
- prev = dp[idx]
- prob = pm[j]
- prob_maps = ['pm']
- q95s = []
- sc = scales[j]
- scale = 1.0
- t_len = 5000
- val = v
- w_i = widths[i]

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- open: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv

**File writes**

- open: submission.csv
- open[w]: submission.csv

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

- stream[stdout] with 9 line(s); excerpt: ⚡ Device: cuda 📌 Paths: - NEW_UNET_PATH: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth | exists: True - OLD_UNET_PATH: /kaggle/input/ecg-final-models1/best_model_phase10.p...
- stream[stderr] with 1 line(s); excerpt: Build Lengths: 100%|██████████| 75000/75000 [00:00<00:00, 750707.70it/s]
- stream[stdout] with 2 line(s); excerpt: ✅ patient_lengths mapped for 2 patients. 🗂️ Indexing images...
- stream[stderr] with 1 line(s)
- stream[stdout] with 9 line(s); excerpt: ✅ Indexed images: 8,795 ✅ fs_map loaded: 2 items ⚙️ Loading YOLO (offline)... ✅ YOLO loaded: /kaggle/input/ecg-final-models1/best.pt ✅ CLASS_TO_LEAD_IDX: {0: 0, 1: 1, 2: 2, 3: 3, 4...
- stream[stderr] with 3 line(s); excerpt: Processing Rows:   0%|          | 0/75000 [00:00<?, ?it/s]/tmp/ipykernel_20/2459418948.py:537: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.am...
- stream[stdout] with 2 line(s); excerpt: ✅ Done. submission.csv ready. Bad parse rows: 0 out of 75000

**Exceptions**

- None

**Warnings**

- Processing Rows:   0%|          | 0/75000 [00:00<?, ?it/s]/tmp/ipykernel_20/2459418948.py:537: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.

### Cell 6

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 6 |
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
