# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 50 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-49.md |
| SHA-256 | 26e84faf98089bea58df8adebd10f2c6c27710799272fcfa6b3b82063f6c9281 |
| Size (bytes) | 58,278 |
| Modified (UTC) | 2026-04-18T21:15:51.866027+00:00 |
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
- re
- scipy.signal
- segmentation_models_pytorch
- shutil
- site
- skimage.morphology
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
- Kaggle working directory
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
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- /kaggle/working/best_model_effb3_phase9_ddp.pth
- submission.csv

## Symbols Defined

**Functions**

- __init__
- _postprocess_prob_to_mask
- _predict_model_probmaps
- _skeletonize_mask
- apply_high_pass
- build_effb3_unet
- choose_ppmv
- clean_pid
- compute_patient_leads
- ensure_pkg
- estimate_grid_spacing_px
- get_crops_yolo_mapped
- get_image_path
- get_real_signal
- normalize_lead_name
- parse_template_id
- predict_unet_probmaps_tta
- prepare_unet_batch
- preprocess_remove_grid_rgb
- render_to_memory
- safe_read_rgb
- score_candidate
- smart_einthoven_fix
- viterbi_adaptive
- viterbi_dp

**Classes**

- UltimateRenderer

**Constants / assigned names**

- CLASS_TO_LEAD_IDX
- DB_DIR
- DEVICE
- DP_BOOST_SKELETON
- DP_MAX_W
- DP_SMOOTH
- FORBIDDEN_PACKAGES
- I
- II
- III
- IMAGE_DIR
- LEAD_NAMES
- LEAD_TO_IDX
- MAX_CACHE
- MAX_W
- MIN_COMP_AREA
- MORPH_K
- NEW_BEST_DST
- NEW_BEST_SRC
- SAMPLE_PARQUET_PATH
- SKIMAGE_OK
- SUBMISSION_FILE
- TARGET_H
- TEST_CSV_PATH
- TH_NEW
- TH_OLD
- TTA_HFLIP
- TTA_SCALES
- UNET_NEW_PATH
- UNET_OLD_PATH
- USE_OLD
- YOLO_CONF
- YOLO_INF_MAX
- YOLO_PATH
- acc_new
- acc_old
- base_scales
- base_scales_old
- dpi
- is_forbidden
- lead_found
- lead_pos
- probO
- scale
- success_count
- t_len
- unet_old
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
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/working/best_model_effb3_phase9_ddp.pth
- os.path.exists: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: submission.csv
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- torch.load: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth
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
- torch.load: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/working/best_model_effb3_phase9_ddp.pth

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
- ⚠️ تحذير: فشل التحميل (name 'wfdb' is not defined)، سيتم استخدام التوليد الاحتياطي.

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- best_model_effb3_phase9_ddp.pt
- best_model_phase10.pt

**Referenced datasets**

- /kaggle/input/**/*.whl
- /kaggle/input/**/*{wheel_hint}*.whl
- /kaggle/input/**/ultralytics
- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization

**External files**

- glob.glob: /kaggle/input/**/*.whl
- glob.glob: /kaggle/input/**/*{wheel_hint}*.whl
- glob.glob: /kaggle/input/**/ultralytics
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- open: submission.csv
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- open[w]: submission.csv

**Required runtime assumptions**

- Assumes Kaggle input mounts are available.
- Assumes offline wheel files are available under the input mounts.
- Assumes ultralytics/YOLO is available for lead localization.
- Assumes PyTorch checkpoint loading is available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.
- Assumes a writable working directory such as /kaggle/working exists.

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

- Inference notebook that introduces the new EfficientNet-B3 checkpoint into the compact offline pipeline.
- These notebooks keep the same compact shell but make the new EffB3 checkpoint a first-class participant in inference decisions.

**Delta notes**

- Compared with notebook (48), this revision pivots from ensemble benchmarking toward integrating the newly trained EffB3 checkpoint.
- The apparent motivation is to bring the EfficientNet-B3 branch into the active deployment flow and determine whether it should replace or complement the older segmentation weights.
- It retains the compact no-internet runner, the renderer, and the final validation shell from the prior deployment families.
- The workflow effect is a new inference-routing era where the notebook must decide between old and new checkpoints instead of assuming one inherited phase-10 default.
- What becomes obsolete is the assumption that the older single-model path is sufficient on its own; checkpoint selection and fallback logic become part of the deployment contract.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`, cell count changed from 5 to 6, stored output types changed from 16 to 14, and exact shared cell sources = 4.
- New imports: `shutil`, `skimage.morphology`
- Removed imports: None
- New model refs: `YOLO: /kaggle/input/ecg-final-models/best.pt`, `os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth`, `os.path.exists: /kaggle/input/ecg-final-models/best.pt`, `os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth`, `os.path.exists: /kaggle/working/best_model_effb3_phase9_ddp.pth`, `torch.load: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth`, `torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth`
- Removed model refs: `YOLO: /kaggle/input/ecg-final-models1/best.pt`, `os.path.exists: /kaggle/input/ecg-final-models1/best.pt`, `os.path.exists: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth`, `torch.load: /kaggle/input/ecg-final-models1/best_model_deeplab_ph10.pth`
- New first-line titles: `# --- Cell 2.5: Attach NEW trained model (EffB3) to inference ---`, `# --- Cell 22: V39++ Ultimate (NEW EffB3 + Optional Old Model + TTA + DP boost + Robust parsing) ---`
- Removed first-line titles: `# --- Cell 22: V47 Benchmarking Engine (Based on Winner V46) ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- Notebook assumes writable Kaggle working storage for intermediate artifacts.
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

- NEW_BEST_DST = /kaggle/working/best_model_effb3_phase9_ddp.pth
- NEW_BEST_SRC = /kaggle/working/best_model_effb3_phase9_ddp.pth

**Paths mentioned**

- /kaggle/input/<your-dataset>/best_model_effb3_phase9_ddp.pth
- /kaggle/working/best_model_effb3_phase9_ddp.pth

**File reads**

- os.path.exists: /kaggle/working/best_model_effb3_phase9_ddp.pth

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

- os.path.exists: /kaggle/working/best_model_effb3_phase9_ddp.pth

**Stored outputs**

- stream[stdout] with 2 line(s); excerpt: ❌ NEW model not found at: /kaggle/working/best_model_effb3_phase9_ddp.pth Exists: False

**Exceptions**

- None

**Warnings**

- None

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 4 |
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

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 5 |
| First non-empty line | `# --- Cell 22: V39++ Ultimate (NEW EffB3 + Optional Old Model + TTA + DP boost + Robust parsing) ---` |
| Role summary | Definition cell that defines 21 function(s). |

**Editorial interpretation**

- Introduces the new EfficientNet-B3 segmentation checkpoint as the preferred inference model while still keeping the older model path as an optional fallback.

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
- skimage.morphology

**Functions defined**

- clean_pid
- normalize_lead_name
- parse_template_id
- get_image_path
- build_effb3_unet
- safe_read_rgb
- preprocess_remove_grid_rgb
- apply_high_pass
- smart_einthoven_fix
- estimate_grid_spacing_px
- choose_ppmv
- viterbi_dp
- viterbi_adaptive
- get_crops_yolo_mapped
- _postprocess_prob_to_mask
- _skeletonize_mask
- prepare_unet_batch
- _predict_model_probmaps
- predict_unet_probmaps_tta
- compute_patient_leads
- score_candidate

**Classes defined**

- None

**Constants / bindings**

- DP_BOOST_SKELETON = True
- DP_MAX_W = 1400
- DP_SMOOTH = 0.45
- I = leads[I][idx]
- II = leads[II][idx]
- III = leads[III][idx]
- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- MAX_CACHE = 12
- MAX_W = 1536
- MIN_COMP_AREA = 120
- MORPH_K = 3
- SAMPLE_PARQUET_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- SKIMAGE_OK = False
- SUBMISSION_FILE = submission.csv
- TARGET_H = 384
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- TH_NEW = 0.45
- TH_OLD = 0.5
- TTA_HFLIP = True
- TTA_SCALES = ['0.95', '1.0', '1.15']
- UNET_NEW_PATH = /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- UNET_OLD_PATH = /kaggle/input/ecg-final-models1/best_model_phase10.pth
- USE_OLD = False
- YOLO_CONF = 0.1
- YOLO_INF_MAX = 1280
- YOLO_PATH = /kaggle/input/ecg-final-models/best.pt
- acc_new = pm2
- acc_old = pm2
- area = stats[i]
- base_scales = scs
- base_scales_old = scs
- best_prev = stacked[which]
- c_0 = dp[idx]
- diffs = []
- img_inf = img_rgb
- items = []
- k = 3
- lead_idx = lead_indices[j]
- local_grid = global_grid
- mtx = patient_cache[pid]
- nw = 1536
- preds = p1
- prev = dp[idx]
- probN = prob_new[j]
- probO = prob_old[j]
- prob_maps = []
- prob_mix = prob_new
- prob_use = prob_new[j]
- sc = scs[j]
- scale = 1.0
- scales_new = scs
- scales_old = scs
- sk_use = skN
- t_len = 5000
- val = v
- w_i = widths[i]

**Paths mentioned**

- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- submission.csv

**File reads**

- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- open: submission.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- torch.load: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth

**File writes**

- open: submission.csv
- open[w]: submission.csv

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: /kaggle/input/ecg-final-models/best.pt
- torch.load: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- torch.load: /kaggle/input/ecg-final-models1/best_model_phase10.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/ecg-final-models/best.pt
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth

**Stored outputs**

- stream[stdout] with 4 line(s); excerpt: ⚡ Device: cuda 📦 Reading Parquet template ids... ✅ Template rows: 75,000 🧠 Scanning template for patient lengths...
- stream[stderr] with 1 line(s); excerpt: Scanning Lengths: 100%|██████████| 75000/75000 [00:00<00:00, 521535.16it/s]
- stream[stdout] with 2 line(s); excerpt: ✅ Lengths mapped for 2 patients. 🗂️ Indexing images...
- stream[stderr] with 1 line(s)
- stream[stdout] with 7 line(s); excerpt: ✅ Indexed images: 8,795 ✅ fs_map loaded: 2 items ⚙️ Loading models (offline)... ✅ NEW UNet loaded: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth ✅ OLD UNet loaded: /kaggle...
- stream[stderr] with 1 line(s); excerpt: Processing Rows: 100%|██████████| 75000/75000 [00:00<00:00, 116897.50it/s]
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

- stream[stdout] with 4 line(s); excerpt: 🔍 Validating submission.csv strictly... ✅ All checks passed. 📦 submission.csv size: 1.92 MB 🎉 Ready to Submit.

**Exceptions**

- None

**Warnings**

- None
