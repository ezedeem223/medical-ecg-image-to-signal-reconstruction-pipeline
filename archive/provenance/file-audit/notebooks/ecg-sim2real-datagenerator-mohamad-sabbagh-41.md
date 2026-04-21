# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 42 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-41.md |
| SHA-256 | 7d81a35965f43a9a68644b27e26c25164f13c87ed1ece67c824020deb20dcb63 |
| Size (bytes) | 45,337 |
| Modified (UTC) | 2026-04-18T20:16:30.652580+00:00 |
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
- {IMAGE_DIR}/sample_submission.parquet
- {IMAGE_DIR}/test.csv

## Symbols Defined

**Functions**

- __init__
- _normalize_lead_name
- apply_high_pass
- choose_ppmv
- clean_pid
- compute_patient_leads
- ensure_pkg
- estimate_grid_spacing_px
- get_crops_yolo_mapped
- get_image_path
- get_real_signal
- predict_unet_probmaps
- prepare_unet_batch
- preprocess_remove_grid_rgb
- render_to_memory
- safe_read_rgb
- score
- viterbi_adaptive
- viterbi_dp

**Classes**

- UltimateRenderer

**Constants / assigned names**

- CLASS_TO_LEAD_IDX
- DB_DIR
- DEVICE
- DP_MAX_W
- DP_SMOOTH
- F
- FORBIDDEN_PACKAGES
- IMAGE_DIR
- L
- LEAD_NAMES
- LEAD_TO_IDX
- MAX_CACHE
- MAX_P2P_MV
- MAX_W
- MIN_MEAN_PROB
- MIN_P2P_MV
- SAMPLE_PARQUET_PATH
- SUBMISSION_FILE
- TARGET_H
- TEST_CSV_PATH
- UNET_PATH
- YOLO_CONF
- YOLO_INF_MAX
- YOLO_PATH
- dpi
- is_forbidden
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
| Editorial cell coverage | 6/6 |
| Editorial output translations | 0 |
| Delta notes | 5 |
| Open questions | 0 |
| Confidence | high |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Compact no-internet deployment notebook that adds one more explicit sanity cell after the usual five-cell inference flow.
- The extra cell shows that row count and ID uniqueness had become important enough to warrant a dedicated post-run check.

**Delta notes**

- Compared with notebook (40), this revision adds a dedicated final sanity cell instead of relying only on inline validation inside the engine and export path.
- The apparent motivation is to refactor the compact deployment notebooks into more helper-driven and self-contained offline runners that behave predictably in no-internet Kaggle sessions.
- It retains the offline-deployment focus, the qualitative renderer, and the idea that one dominant engine cell should still drive submission export.
- The workflow effect is less boilerplate duplication and a clearer separation between environment repair, helper setup, inference, and export sanity checks.
- What becomes obsolete is the earlier pattern of repeating large inline engine scaffolds and ad hoc install logic across many nearly identical notebooks.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb`, cell count changed from 5 to 6, stored output types changed from 9 to 8, and exact shared cell sources = 4.
- New imports: None
- Removed imports: None
- New model refs: None
- Removed model refs: None
- New first-line titles: `# --- Cell 22: V42 (Per-Lead Lengths + Per-Lead FS + Safe Gating) ---`, `print(len(tdf), tdf['id'].nunique())`
- Removed first-line titles: `# --- Cell 22: V40 Ultimate (Per-Lead Length from test.csv + Safe Mode + 0.5mm Grid + Confidence Gate + Linear-Phase Resample) ---`

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
| First non-empty line | `# --- Cell 22: V42 (Per-Lead Lengths + Per-Lead FS + Safe Gating) ---` |
| Role summary | Definition cell that defines 15 function(s). |

**Editorial interpretation**

- Runs a V42-style engine that derives per-lead lengths and sampling frequencies while applying safe gating before export.

**Imports**

- os
- csv
- glob
- gc
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
- safe_read_rgb
- _normalize_lead_name
- preprocess_remove_grid_rgb
- apply_high_pass
- estimate_grid_spacing_px
- choose_ppmv
- viterbi_dp
- viterbi_adaptive
- get_crops_yolo_mapped
- prepare_unet_batch
- predict_unet_probmaps
- compute_patient_leads
- score

**Classes defined**

- None

**Constants / bindings**

- DP_MAX_W = 1400
- DP_SMOOTH = 0.45
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE = 16
- MAX_P2P_MV = 12.0
- MAX_W = 2048
- MIN_MEAN_PROB = 0.03
- MIN_P2P_MV = 0.05
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SUBMISSION_FILE = submission.csv
- TARGET_H = 256
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- UNET_PATH = /kaggle/input/ecg-final-models/best_model_phase10.pth
- YOLO_CONF = 0.1
- YOLO_INF_MAX = 1280
- YOLO_PATH = /kaggle/input/ecg-final-models/best.pt
- best_prev = stacked[which]
- c_0 = dp[idx]
- diffs = []
- exp_fs = ['F']
- exp_len = ['L']
- fs = F[lead_idx]
- img_inf = img_rgb
- key = ['pid', 'lead']
- local_grid = global_grid
- nw = 2048
- prev = dp[idx]
- prob = prob_maps[j]
- prob_maps = []
- sc = scales[j]
- scale = 1.0
- sig = patient_cache[pid][lead_idx]
- sigs = patient_cache[pid]
- target_len = L[lead_idx]
- val = v
- w_i = widths[i]

**Paths mentioned**

- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv
- {IMAGE_DIR}/sample_submission.parquet
- {IMAGE_DIR}/test.csv

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models/best_model_phase10.pth
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

- stream[stdout] with 15 line(s); excerpt: ⚡ Device: cuda 📦 Reading Parquet template ids... ✅ Template rows: 75,000 🧠 Reading test.csv (per-lead lengths + fs)... ✅ len_map entries: 24 ✅ unique patients in test.csv: 2 🔎 Exam...
- stream[stderr] with 1 line(s); excerpt: Processing Rows: 100%|██████████| 75000/75000 [00:03<00:00, 21399.45it/s]
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

- stream[stdout] with 4 line(s); excerpt: 🔍 Validating submission.csv strictly... ✅ All checks passed. 📦 submission.csv size: 1.95 MB 🎉 Ready to Submit.

**Exceptions**

- None

**Warnings**

- None

### Cell 6

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 6 |
| First non-empty line | `print(len(tdf), tdf['id'].nunique())` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Prints final row-count and unique-ID statistics as an extra sanity check, making silent duplication or truncation easier to catch.

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

- stream[stdout] with 1 line(s); excerpt: 24 2

**Exceptions**

- None

**Warnings**

- None
