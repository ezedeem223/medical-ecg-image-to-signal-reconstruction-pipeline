# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 57 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-56.md |
| SHA-256 | 4df1802bd172c5889a27f5b1557cf9a56128870a5904e5240353ce2eefb67769 |
| Size (bytes) | 35,505 |
| Modified (UTC) | 2026-04-18T21:17:47.111638+00:00 |
| Inferred role | Offline Kaggle inference pipeline variant with packaged dependencies. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 5 |
| Cell count | 8 |
| Code cells | 8 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 0 |
| Editorial cell notes | 8 |
| Editorial output notes | 0 |
| Interpretation confidence | medium |
| Open questions | 2 |
| Editorial complete | yes |
| Kernel | {"display_name": "Python 3", "language": "python", "name": "python3"} |
| Language info | {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.11.13"} |

## Dependencies

**Imports**

- contextlib
- cv2
- gc
- glob
- importlib.util
- numpy
- os
- pandas
- random
- re
- segmentation_models_pytorch
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

- , round(os.path.getsize(SUB_PATH)/1024/1024, 2),
- .bmp
- .jpeg
- .jpg
- .png
- /kaggle/input/**/**/*.whl
- /kaggle/input/**/*{ext}
- /kaggle/input/**/{pat}
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- min/max:
- submission.csv

## Symbols Defined

**Functions**

- _guess_encoder
- _run
- _unwrap_state_dict
- autocast_ctx
- build_signal_from_crop
- build_unet
- cv_mask
- estimate_small_box_px
- fallback_split_12leads
- find_first
- format_like_example
- get_id_series
- lead_to_idx
- load_unet_auto
- mask_to_wave
- peak_period
- read_image
- resolve_image_path
- unet_mask
- yolo_lead_crops

**Classes**

- None

**Constants / assigned names**

- CLASS_TO_LEAD_IDX
- DEVICE
- IMG_EXTS
- NEW_UNET_PATH
- OLD_UNET_PATH
- SAMPLE_SUB
- SUB_PATH
- TEST_CSV
- USE_OLD_FALLBACK
- USE_UNET
- YOLO_CONF
- YOLO_IOU
- YOLO_PATH
- base
- idx
- k
- ok
- resolved
- small_box
- test_df

## File Operations And Model Loads

**File reads**

- glob.glob: /kaggle/input/**/**/*.whl
- glob.glob: /kaggle/input/**/*{ext}
- glob.glob: /kaggle/input/**/{pat}
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.run: cmd

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth

## Stored Output Inventory

**Output types**

- error: 1
- stream: 1

**MIME types**

- None

**Exceptions captured in outputs**

- ModuleNotFoundError: No module named 'segmentation_models_pytorch'

**Warnings / warning-like lines**

- None

## Observed Dependency Summary

**Referenced checkpoints**

- best_model_effb3_phase9_ddp.pt
- best.pt
- best_model_phase10.pt

**Referenced datasets**

- /kaggle/input/**/**/*.whl
- /kaggle/input/**/*{ext}
- /kaggle/input/**/{pat}
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth
- submission.csv
- glob.glob: /kaggle/input/**/**/*.whl

**External files**

- glob.glob: /kaggle/input/**/**/*.whl
- glob.glob: /kaggle/input/**/*{ext}
- glob.glob: /kaggle/input/**/{pat}
- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth

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
| Editorial cell coverage | 8/8 |
| Editorial output translations | 0 |
| Delta notes | 5 |
| Open questions | 2 |
| Confidence | medium |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Final modular rewrite that abandons descriptive headings and decomposes the pipeline into install, config, indexing, model loading, utility, formatting, validation, and debug blocks.
- This notebook is structurally cleaner than the earlier compact series, but its generic headings make manual editorial notes essential for readability.

**Delta notes**

- Compared with notebook (55), this revision fully decomposes the pipeline into modular helpers and abandons descriptive headings; the editorial notes restore the missing semantics.
- The apparent motivation is to modularize the final notebook so install, configuration, loading, execution, and debugging can be understood as separate responsibilities before later synthesis work.
- It retains the same detector-plus-segmentation submission goal as the preceding deployment notebooks even though the code layout changes dramatically.
- The workflow effect is a cleaner operational shape that is easier to map into a future synthesis, because the notebook is no longer a single large opaque engine cell.
- What becomes obsolete is the old habit of encoding meaning only in descriptive cell headings or one monolithic inference cell; the logic is now spread across modular blocks.

**Open questions**

- This notebook auto-discovers model paths, so the intended final checkpoint pairing may still depend on the exact Kaggle input layout present at execution time.
- The debug cell is clearly useful, but it is not entirely certain whether it was meant as a permanent operational step or only as a troubleshooting convenience.

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`, cell count changed from 7 to 8, stored output types changed from 9 to 2, and exact shared cell sources = 0.
- New imports: `contextlib`, `importlib.util`, `random`
- Removed imports: `collections`, `csv`, `importlib`, `math`, `pyarrow`, `scipy.signal`, `shutil`, `site`
- New model refs: None
- Removed model refs: None
- New first-line titles: None
- Removed first-line titles: `# # --- الخلية 3: محرك الرسم الحي (Ultimate Renderer) - [M3: UPDATED] ---`, `# --- Cell 1: Smart Offline Install (SAFE & MINIMAL) ---`, `# --- Cell 2.5: Attach NEW trained model (EffB3) to inference ---`, `# --- Cell 22 (REPLACEMENT): V42 Robust Inference (Deskew + Trim + Model-Select + Quality Gate) ---`, `# --- Cell 2: Offline install/import fix (NO internet) + Path Resolver ---`, `# --- NEW DIAGNOSTIC CELL: Check real coverage of pid->path mapping ---`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- subprocess-based installation or path manipulation introduces extra runtime coupling.
- Stored notebook outputs contain 1 execution error(s); treat those cells as unresolved at snapshot time.
- Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.
- Notebook depends on both object detection and segmentation stacks, increasing environment complexity.
- Checkpoint loading is embedded in the workflow; model file availability is a runtime prerequisite.
- Because model paths are auto-discovered in this notebook, a wrong match could silently swap checkpoints unless the discovered filenames are reviewed carefully.

## Cell-By-Cell Audit

### Cell 1

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 1 |
| First non-empty line | `# =========================` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Implements a minimal offline wheel installer with a small helper wrapper, making dependency bootstrap explicit but intentionally lightweight.

**Imports**

- os
- glob
- subprocess
- sys
- re
- importlib.util

**Functions defined**

- _run

**Classes defined**

- None

**Constants / bindings**

- compatible = ['w']
- name = w
- need = ['segmentation_models_pytorch', 'ultralytics']
- ok = 0
- py_tag = cpsys.version_info.majorsys.version_info.minor
- to_install = ['candidates[0]']
- wheel_paths = /kaggle/input/**/**/*.whl

**Paths mentioned**

- /kaggle/input/**/**/*.whl

**File reads**

- glob.glob: /kaggle/input/**/**/*.whl

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- subprocess.run: cmd

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 4 line(s); excerpt: 🐍 Python tag: cp311 📦 Found wheels: 190 ✅ Will try install: 0 wheels ✅ Installed 0/0 wheels safely.

**Exceptions**

- None

**Warnings**

- None

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 2 |
| First non-empty line | `# =========================` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Loads imports, runtime configuration, and path-discovery logic for the new UNet checkpoint, the old fallback UNet checkpoint, and the YOLO detector bundle.

**Imports**

- os
- glob
- re
- gc
- numpy
- pandas
- torch
- segmentation_models_pytorch
- ultralytics

**Functions defined**

- find_first

**Classes defined**

- None

**Constants / bindings**

- NEW_UNET_PATH = /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- OLD_UNET_PATH = /kaggle/input/ecg-final-models1/best_model_phase10.pth
- USE_OLD_FALLBACK = True
- USE_UNET = True
- YOLO_CONF = 0.25
- YOLO_IOU = 0.45
- YOLO_PATH = /kaggle/input/ecg-final-models1/best.pt
- hits = /kaggle/input/**/{pat}

**Paths mentioned**

- /kaggle/input/**/{pat}
- /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- /kaggle/input/ecg-final-models1/best.pt
- /kaggle/input/ecg-final-models1/best_model_phase10.pth

**File reads**

- os.path.exists: /kaggle/input/best-dd4/best_model_effb3_phase9_ddp.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt
- glob.glob: /kaggle/input/**/{pat}

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
- os.path.exists: /kaggle/input/ecg-final-models1/best_model_phase10.pth
- os.path.exists: /kaggle/input/ecg-final-models1/best.pt

**Stored outputs**

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
| First non-empty line | `# =========================` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Indexes discovered test images and checks coverage against competition IDs, ensuring the pipeline knows which files are actually available before loading models.

**Imports**

- os
- glob

**Functions defined**

- get_id_series

**Classes defined**

- None

**Constants / bindings**

- IMG_EXTS = ['.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff', '.webp']
- all_imgs = []
- base = subscript[0]
- resolved = 0
- x2 = subscript[0]

**Paths mentioned**

- .bmp
- .jpeg
- .jpg
- .png
- /kaggle/input/**/*{ext}

**File reads**

- glob.glob: /kaggle/input/**/*{ext}

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
| Role summary | Definition cell that defines 4 function(s). |

**Editorial interpretation**

- Builds the model-loading layer: it unwraps checkpoint state dicts, guesses encoder families from key patterns, constructs the UNet, and loads YOLO for lead localization.

**Imports**

- None

**Functions defined**

- _unwrap_state_dict
- _guess_encoder
- build_unet
- load_unet_auto

**Classes defined**

- None

**Constants / bindings**

- best = ['s2', 'alt', 'm2']
- obj = obj[state_dict][model]

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
| Role summary | Definition cell that defines 11 function(s). |

**Editorial interpretation**

- Defines the crop-extraction and waveform utility functions that convert detector boxes and segmentation masks into per-lead numeric traces.

**Imports**

- cv2
- contextlib

**Functions defined**

- autocast_ctx
- read_image
- fallback_split_12leads
- yolo_lead_crops
- estimate_small_box_px
- unet_mask
- cv_mask
- mask_to_wave
- build_signal_from_crop
- resolve_image_path
- peak_period

**Classes defined**

- None

**Constants / bindings**

- ac = ac[idx]
- boxes = boxes
- col = subscript[0]
- idx = 0
- k = 9
- lead_idx = CLASS_TO_LEAD_IDX[cls]
- m = m2
- s = sample_id
- s2 = subscript[0]
- small_box = 10
- ys = ys2

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 6

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# =========================` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Formats reconstructed outputs against the sample-submission contract so the modular helper stack can still emit the required competition schema.

**Imports**

- tqdm

**Functions defined**

- format_like_example
- lead_to_idx

**Classes defined**

- None

**Constants / bindings**

- c = signal[0]
- lead_val = base.loc[i]
- sid = base.loc[i]
- target_cols = ['signal']

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 7

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# =========================` |
| Role summary | General computation cell. |

**Editorial interpretation**

- Runs validation and writes `submission.csv`, making this the main execution cell that turns the modular helpers into a real deliverable.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- SUB_PATH = submission.csv

**Paths mentioned**

- , round(os.path.getsize(SUB_PATH)/1024/1024, 2),
- submission.csv

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

- None

**Exceptions**

- None

**Warnings**

- None

### Cell 8

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# =========================` |
| Role summary | Import / dependency declaration cell. |

**Editorial interpretation**

- Provides an optional one-ID debug path for focused troubleshooting, useful when the main execution succeeds structurally but a particular record still looks wrong.

**Imports**

- random

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- sid = iloc[idx]

**Paths mentioned**

- min/max:

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

- None

**Exceptions**

- None

**Warnings**

- None
