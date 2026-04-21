# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 54 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-53.md |
| SHA-256 | bdd9fb3eecd1193e91d0d8f2357d6e24fc35f4de4fa8d50c61de1441721706dc |
| Size (bytes) | 48,390 |
| Modified (UTC) | 2026-04-18T21:16:48.170521+00:00 |
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
- numpy
- os
- pandas
- pyarrow
- re
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
- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {IMAGE_DIR}/sample_submission.parquet
- {IMAGE_DIR}/test.csv

## Symbols Defined

**Functions**

- _normalize_lead_name
- apply_high_pass
- build_unet_effb3
- build_unet_resnet50
- choose_ppmv
- clean_pid
- compute_patient_leads
- ensure_pkg
- estimate_grid_spacing_px
- extract_trace
- find_first
- first_int
- get_crops_yolo_mapped
- get_fs
- get_image_path
- load_state
- norm_chw
- ok_whl
- parse_rid
- predict_probmaps
- prepare_batch
- preprocess_remove_red_grid
- run_model
- safe_read_rgb
- score
- viterbi_dp

**Classes**

- None

**Constants / assigned names**

- ALPHA_NEW
- CLASS_TO_LEAD_IDX
- DEVICE
- DP_MAX_W
- DP_SMOOTH
- FORBIDDEN
- IMAGE_DIR
- IM_MEAN
- IM_STD
- LEAD_NAMES
- LEAD_TO_IDX
- MAX_CACHE
- MAX_W
- NEEDED_HINTS
- NEW_BEST_DST
- NEW_BEST_SRC
- NEW_UNET_PATH
- OLD_UNET_PATH
- SAMPLE_PARQUET_PATH
- SUBMISSION_FILE
- TARGET_H
- TEST_CSV_PATH
- USE_OLD
- YOLO_CONF
- YOLO_INF_MAX
- YOLO_PATH
- hit
- ok
- old_model
- scale
- t_len
- val
- yolo_model

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
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

- subprocess.check_call: sys.executable -m pip install subscript[0] --no-deps --ignore-installed --quiet
- subprocess.check_call: sys.executable -m pip install whl --no-deps --ignore-installed --quiet

**Model loads**

- YOLO: /kaggle/input/ecg-final-models1/best.pt

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth

## Stored Output Inventory

**Output types**

- stream: 10

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
- best_model_effb3_phase9_ddp.pt
- best_model_phase10.pt

**Referenced datasets**

- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet

**External files**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
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

- EffB3-focused inference notebook that repairs the pid-to-image lookup layer without abandoning the V40 core.
- These notebooks keep the same compact shell but make the new EffB3 checkpoint a first-class participant in inference decisions.

**Delta notes**

- Compared with notebook (52), the primary change is safer mapping from competition IDs to actual image paths.
- The apparent motivation is to bring the EfficientNet-B3 branch into the active deployment flow and determine whether it should replace or complement the older segmentation weights.
- It retains the compact no-internet runner, the renderer, and the final validation shell from the prior deployment families.
- The workflow effect is a new inference-routing era where the notebook must decide between old and new checkpoints instead of assuming one inherited phase-10 default.
- What becomes obsolete is the assumption that the older single-model path is sufficient on its own; checkpoint selection and fallback logic become part of the deployment contract.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb`, cell count changed from 6 to 6, stored output types changed from 10 to 10, and exact shared cell sources = 5.
- New imports: `re`
- Removed imports: None
- New model refs: None
- Removed model refs: None
- New first-line titles: `# --- Cell 22: V41 FIX (Smart pid->image path index + sanity check + keep V40 pipeline) ---`
- Removed first-line titles: `# --- Cell 22: V40 FINAL (test.csv path map + ImageNet norm + NEW/OLD ensemble + robust DP) ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
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
| First non-empty line | `# --- Cell 1: Smart Offline Install (SAFE & MINIMAL) ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Uses the smallest safe offline install path, reducing package churn so the notebook can focus on inference rather than repeated environment repair.

**Imports**

- sys
- os
- glob
- subprocess
- torch

**Functions defined**

- ok_whl

**Classes defined**

- None

**Constants / bindings**

- FORBIDDEN = ['torch', 'torchvision', 'torchaudio', 'numpy', 'pandas', 'opencv', 'matplotlib', 'scipy', 'pillow']
- NEEDED_HINTS = ['segmentation_models_pytorch', 'ultralytics', 'timm']
- all_whls = /kaggle/input/**/*.whl
- n = p
- ok = 0
- picked = ['p']
- py_tag = cpsys.version_info.majorsys.version_info.minor

**Paths mentioned**

- /kaggle/input/**/*.whl

**File reads**

- glob.glob: /kaggle/input/**/*.whl

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.check_call: sys.executable -m pip install whl --no-deps --ignore-installed --quiet

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 7 line(s); excerpt: ⚙️ Smart offline install (minimal + compatible wheels only)... 🐍 Python tag: cp311 📦 Found wheels: 95 ✅ Will try install: 3 wheels ✅ Installed 3/3 wheels safely. ⚡ Torch: 2.6.0+cu1...

**Exceptions**

- None

**Warnings**

- None

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
| First non-empty line | `# --- Cell 22: V41 FIX (Smart pid->image path index + sanity check + keep V40 pipeline) ---` |
| Role summary | Definition cell that defines 23 function(s). |

**Editorial interpretation**

- Adds a smart pid-to-image path index and sanity checks, fixing the fragile lookup layer while keeping the V40-style inference core.

**Imports**

- os
- gc
- csv
- glob
- re
- numpy
- pandas
- cv2
- torch
- tqdm
- collections
- scipy.signal
- segmentation_models_pytorch
- ultralytics

**Functions defined**

- norm_chw
- clean_pid
- parse_rid
- get_fs
- first_int
- get_image_path
- safe_read_rgb
- _normalize_lead_name
- load_state
- build_unet_effb3
- build_unet_resnet50
- preprocess_remove_red_grid
- estimate_grid_spacing_px
- choose_ppmv
- apply_high_pass
- viterbi_dp
- extract_trace
- get_crops_yolo_mapped
- prepare_batch
- run_model
- predict_probmaps
- compute_patient_leads
- score

**Classes defined**

- None

**Constants / bindings**

- ALPHA_NEW = 0.75
- DP_MAX_W = 1400
- DP_SMOOTH = 0.45
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE = 8
- MAX_W = 2048
- NEW_UNET_PATH = /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- OLD_UNET_PATH = /kaggle/input/ecg-final-models1/best_model_phase10.pth
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv
- TARGET_H = 256
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- YOLO_CONF = 0.1
- YOLO_INF_MAX = 1280
- YOLO_PATH = /kaggle/input/ecg-final-models1/best.pt
- base = subscript[0]
- best_prev = stacked[which]
- c_0 = dp[idx]
- diffs = []
- hit = 0
- img_inf = img_rgb
- items = []
- lead_idx = lead_indices[j]
- local_grid = global_grid
- miss_examples = ['pid']
- mtx = patient_cache[pid_raw]
- nw = 2048
- path = path2
- preds = p_new
- prev = dp[idx]
- prob = prob_maps[j]
- prob_maps = []
- sample_pids = ['pid_raw']
- sc = scales[j]
- scale = 1.0
- t_len = 5000
- val = v
- w_i = widths[i]

**Paths mentioned**

- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {IMAGE_DIR}/sample_submission.parquet
- {IMAGE_DIR}/test.csv

**File reads**

- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- open: submission.csv

**File writes**

- open: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: /kaggle/input/ecg-final-models1/best.pt

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth

**Stored outputs**

- stream[stdout] with 14 line(s); excerpt: ⚡ Device: cuda 📌 Paths exist: | NEW: True | OLD: True | YOLO: True ✅ Template rows: 75000 ✅ patient_lengths mapped: 2 ✅ test.csv columns: ['id', 'lead', 'fs', 'number_of_rows'] ✅ f...
- stream[stderr] with 1 line(s); excerpt: Processing Rows: 100%|██████████| 75000/75000 [00:17<00:00, 4347.56it/s]
- stream[stdout] with 1 line(s); excerpt: ✅ Done. submission.csv ready.

**Exceptions**

- None

**Warnings**

- None

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
