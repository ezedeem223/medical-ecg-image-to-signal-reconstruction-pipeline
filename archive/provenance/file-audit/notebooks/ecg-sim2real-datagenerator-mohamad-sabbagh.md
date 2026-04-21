# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 1 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh.md |
| SHA-256 | c565f1aff4759d39a7b1a6acc00d3556a0baa300ffdf16ae84b0ff0e38db6287 |
| Size (bytes) | 6,231,560 |
| Modified (UTC) | 2026-04-18T19:25:30.882755+00:00 |
| Inferred role | End-to-end synthetic data generation and training notebook. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 4 |
| Cell count | 15 |
| Code cells | 15 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 8 |
| Editorial cell notes | 15 |
| Editorial output notes | 9 |
| Interpretation confidence | medium |
| Open questions | 2 |
| Editorial complete | yes |
| Kernel | {"language": "python", "display_name": "Python 3", "name": "python3"} |
| Language info | {"name": "python", "version": "3.11.13", "mimetype": "text/x-python", "codemirror_mode": {"name": "ipython", "version": 3}, "pygments_lexer": "ipython3", "nbconvert_exporter": "python", "file_extension": ".py"} |

## Dependencies

**Imports**

- albumentations
- cv2
- glob
- matplotlib.pyplot
- numpy
- os
- pandas
- random
- scipy.signal
- segmentation_models_pytorch
- skimage.io
- skimage.morphology
- sklearn.model_selection
- torch
- torch.utils.data
- tqdm

**Packages requested via pip/install commands**

- albumentations
- matplotlib
- numpy<2
- opencv-python
- pandas
- scikit-image
- scikit-learn
- scipy
- segmentation-models-pytorch
- tqdm

## Hard-Coded Paths And External Environment Markers

**Environment markers**

- Kaggle input mount
- pip install usage
- segmentation_models_pytorch

**Literal paths / artifacts**

- *.jpg
- *.png
- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- /kaggle/input/physionet-ecg-image-digitization
- best_model.pth
- dataset_path/train/*.jpg
- dataset_path/train/*.png
- self.data_dir/images/self.images[idx]
- self.data_dir/masks/self.masks[idx]
- submission_from_images.csv
- {OUTPUT_DIR}/images
- {OUTPUT_DIR}/masks
- {dataset_path}/**/*.jpg
- {dataset_path}/**/*.png
- {root_path}/**/**/*.png
- {root_path}/**/*.jpg
- {root_path}/**/*.png
- {root}/**/*.jpg
- {root}/**/*.png

## Symbols Defined

**Functions**

- __getitem__
- __init__
- __len__
- augment_pair
- calibrate_signal
- create_submission_file
- estimate_grid_size
- extract_signal_simple_argmax
- extract_signal_viterbi
- generate_synthetic_heartbeat
- get_12_leads_crops
- get_any_image_path
- plot_signal_to_image
- predict_long_image
- process_full_page
- test_robust_real_image
- viterbi_path
- viterbi_path_tuned

**Classes**

- ECGDataset
- ECGGenerator

**Constants / assigned names**

- BATCH_SIZE
- COMPETITION_NAME
- DEVICE
- EPOCHS
- INPUT_DIR
- LR
- NUM_SAMPLES
- OUTPUT_DIR
- crop_h
- csv_file
- dataset_path
- dpi
- epoch_loss
- final_grid_size
- grid_height
- grid_size
- grid_size_scaled
- grid_width
- target_h
- target_len
- win

## File Operations And Model Loads

**File reads**

- cv2.imread: self.data_dir/images/self.images[idx]
- cv2.imread: self.data_dir/masks/self.masks[idx]
- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- glob.glob: dataset_path/test/*.jpg
- glob.glob: dataset_path/test/*.png
- glob.glob: dataset_path/train/*.jpg
- glob.glob: dataset_path/train/*.png
- glob.glob: {root}/**/*.jpg
- glob.glob: {root}/**/*.png
- os.listdir: /kaggle/input
- os.listdir: /kaggle/input/dirname
- os.listdir: data_dir/images
- os.listdir: data_dir/masks
- os.listdir: dataset_path/train
- os.path.exists: dataset_path/train
- pd.read_csv: /kaggle/input/dirname/f

**File writes**

- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png
- df.to_csv: submission_simulated.csv
- torch.save: best_model.pth

**Shell commands**

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- torch.save: best_model.pth

**Model existence probes**

- None

## Stored Output Inventory

**Output types**

- stream: 31
- display_data: 11

**MIME types**

- text/plain: 11
- image/png: 8
- application/vnd.jupyter.widget-view+json: 2
- text/html: 1

**Exceptions captured in outputs**

- None

**Warnings / warning-like lines**

- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Field()` function, which has no effect in 
- warnings.warn(
- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'frozen' attribute with value True was provided to the `Field()` function, which has no effect in
- 0%|          | 0/50 [00:00<?, ?it/s]/tmp/ipykernel_144/3773411413.py:93: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise
- /tmp/ipykernel_144/3773411413.py:93: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise
- ⚠️ مجلد train يبدو فارغاً أو الصور في مكان آخر، سأبحث في test...
- /tmp/ipykernel_144/3820492745.py:60: FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.

## Observed Dependency Summary

**Referenced checkpoints**

- best_model.pt

**Referenced datasets**

- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- /kaggle/input/physionet-ecg-image-digitization
- submission_from_images.csv
- glob.glob: /kaggle/input/dirname/**/*.jpg

**External files**

- cv2.imread: self.data_dir/images/self.images[idx]
- cv2.imread: self.data_dir/masks/self.masks[idx]
- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- glob.glob: dataset_path/test/*.jpg
- glob.glob: dataset_path/test/*.png
- glob.glob: dataset_path/train/*.jpg
- glob.glob: dataset_path/train/*.png
- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png
- df.to_csv: submission_simulated.csv
- torch.save: best_model.pth

**Required runtime assumptions**

- Assumes in-notebook shell execution is allowed for package installation or environment repair.
- Assumes in-notebook dependency installation is permitted.
- Assumes Kaggle input mounts are available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.

**Outputs created or updated**

- torch.save: best_model.pth
- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png
- df.to_csv: submission_simulated.csv

## Phase 1 Closure Status

| Field | Value |
| --- | --- |
| Notebook summary | present |
| Editorial cell coverage | 15/15 |
| Editorial output translations | 9 |
| Delta notes | 1 |
| Open questions | 2 |
| Confidence | medium |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Initial monolithic research notebook that mixes synthetic data generation, baseline training, Viterbi decoding, Kaggle ingestion, and calibration experiments in one place.
- Later notebooks split these responsibilities, but this file remains the provenance source for the earliest end-to-end assumption that mask probabilities can be converted into 1D ECG signals.

**Delta notes**

- First notebook in review order; there is no earlier revision to diff against.

**Open questions**

- Because this notebook mixes synthetic training, Viterbi decoding, Kaggle ingestion, and calibration in one file, some behavior may still depend on execution order rather than explicit interfaces.
- Several stored outputs in this notebook document visible reconstruction failures; it remains unclear which early branches were considered dead ends versus reusable prototypes.

## Differences Vs Previous Notebook In Review Order

- This is the first notebook in the mandated review order; no prior notebook exists for comparison.

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- Dependency installation is embedded in notebook cells, so reproducibility depends on runtime package availability.
- Stored outputs include 8 warning-like lines worth checking during reruns.
- Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.

## Cell-By-Cell Audit

### Cell 1

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# تثبيت كل ما يحتاجه المشروع من البداية للنهاية (بما فيها معالجة البيانات وملفات CSV)` |
| Role summary | Environment bootstrap cell with package installation commands. |

**Editorial interpretation**

- Bootstraps the runtime by installing the full dependency set needed for data generation, CSV handling, model training, and image processing, assuming the environment can restart after package installation.

**Imports**

- os

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

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 178 line(s); excerpt: Requirement already satisfied: numpy<2 in /usr/local/lib/python3.11/dist-packages (1.26.4) Requirement already satisfied: matplotlib in /usr/local/lib/python3.11/dist-packages (3.7...

**Exceptions**

- None

**Warnings**

- None

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 1 |
| First non-empty line | `import os` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Imports the core scientific stack, selects device and runtime globals, and establishes the shared configuration objects that every later stage in the notebook reuses.

**Imports**

- os
- cv2
- numpy
- pandas
- matplotlib.pyplot
- scipy.signal
- random
- tqdm
- albumentations
- skimage.io
- skimage.morphology
- torch
- torch.utils.data
- segmentation_models_pytorch
- sklearn.model_selection

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

- stream[stderr] with 4 line(s); excerpt: /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Fi...
- stream[stdout] with 2 line(s); excerpt: ✅ تم تجهيز المعمل بالكامل (Data, AI, CSV, Processing). 🚀 الجهاز الجاهز للعمل: cuda

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
| Execution count | 2 |
| First non-empty line | `# --- الخلية 3: كود توليد البيانات ---` |
| Role summary | Definition cell that defines 4 function(s) and 1 class(es). |

**Editorial interpretation**

- Builds the earliest synthetic ECG image factory, turning numeric signal templates into rasterized traces plus labels that can supervise a segmentation model.

**Imports**

- None

**Functions defined**

- __init__
- generate_synthetic_heartbeat
- plot_signal_to_image
- augment_pair

**Classes defined**

- ECGGenerator

**Constants / bindings**

- NUM_SAMPLES = 50
- OUTPUT_DIR = synthetic_dataset
- beat = p_waveq_waver_waves_wavet_wave
- dpi = 100

**Paths mentioned**

- {OUTPUT_DIR}/images
- {OUTPUT_DIR}/masks

**File reads**

- None

**File writes**

- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png

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

- stream[stdout] with 1 line(s); excerpt: جاري توليد 50 عينة تدريب...
- stream[stderr] with 3 line(s); excerpt: 0%|          | 0/50 [00:00<?, ?it/s]/tmp/ipykernel_144/3773411413.py:93: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise A.GaussNoise(var_limit=(10.0, 5...
- stream[stdout] with 1 line(s); excerpt: ✅ تم توليد البيانات بنجاح.
- stream[stderr] with 1 line(s)

**Exceptions**

- None

**Warnings**

- 0%|          | 0/50 [00:00<?, ?it/s]/tmp/ipykernel_144/3773411413.py:93: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 3 |
| First non-empty line | `# --- الخلية 4: تدريب الموديل ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Defines and launches the baseline segmentation training loop, making this the first cell where synthetic ECG images become reusable trace-mask weights.

**Imports**

- None

**Functions defined**

- __init__
- __len__
- __getitem__

**Classes defined**

- ECGDataset

**Constants / bindings**

- BATCH_SIZE = 8
- EPOCHS = 10
- LR = 0.0005
- epoch_loss = 0
- history = ['avg_loss']
- img_path = self.data_dir/images/self.images[idx]
- mask_path = self.data_dir/masks/self.masks[idx]
- pred_mask = subscript[0][0]

**Paths mentioned**

- best_model.pth
- self.data_dir/images/self.images[idx]
- self.data_dir/masks/self.masks[idx]

**File reads**

- cv2.imread: self.data_dir/images/self.images[idx]
- cv2.imread: self.data_dir/masks/self.masks[idx]
- os.listdir: data_dir/images
- os.listdir: data_dir/masks

**File writes**

- torch.save: best_model.pth

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- torch.save: best_model.pth

**Model existence probes**

- None

**Stored outputs**

- display_data MIME=application/vnd.jupyter.widget-view+json, text/plain; text excerpt: config.json:   0%|          | 0.00/156 [00:00<?, ?B/s]
- display_data MIME=application/vnd.jupyter.widget-view+json, text/plain; text excerpt: model.safetensors:   0%|          | 0.00/46.8M [00:00<?, ?B/s]
- stream[stdout] with 12 line(s); excerpt: 🚀 بدء التدريب على 50 صورة لمدة 10 دورات... Epoch [1/10] | Loss: 0.7935 Epoch [2/10] | Loss: 0.7201 Epoch [3/10] | Loss: 0.6771 Epoch [4/10] | Loss: 0.6393 Epoch [5/10] | Loss: 0.59...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-04-output-04.png; text excerpt: <Figure size 1200x400 with 3 Axes>

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-04-output-04.png

**Output interpretation**

- Output 4: Three-panel training sanity check titled Input / Target / AI Prediction. The left panel shows a synthetic Lead II strip on red ECG paper; the middle panel is the binary trace mask on black; the right panel is the predicted mask. The prediction preserves the timing of the tall R peaks and most baseline undulations, with small thickness and alignment errors in the low-amplitude parts of the waveform.

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 4 |
| First non-empty line | `# خلية 4.5` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Introduces Viterbi-style decoding from a probability map to a single waveform path, which is the conceptual bridge from segmentation output to signal reconstruction.

**Imports**

- None

**Functions defined**

- viterbi_path
- extract_signal_viterbi

**Classes defined**

- None

**Constants / bindings**

- min_cost = dp[idx]dist_penalty[best_idx]
- prev_costs = dp[idx]
- refined_signal = []
- total_costs = dp[idx]dist_penalty
- weights = prob_map[x]
- win = 2
- y_subpixel = y_int

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
| Execution count | 5 |
| First non-empty line | `# --- الخلية 5 (محدثة): اختبار استخراج الإشارة باستخدام Viterbi ---` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Scales the same decoding idea from one strip to a full ECG page, coordinating per-strip processing and showing whether page segmentation can be stitched into usable lead-level signals.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- extracted_signal = values
- prob_map = subscript[0][0]

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

- stream[stderr] with 2 line(s); excerpt: /tmp/ipykernel_144/3773411413.py:93: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise A.GaussNoise(var_limit=(10.0, 50.0), p=0.5),
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-06-output-02.png; text excerpt: <Figure size 1200x800 with 3 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ تم استخدام Viterbi بنجاح!

**Exceptions**

- None

**Warnings**

- /tmp/ipykernel_144/3773411413.py:93: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-06-output-02.png

**Output interpretation**

- Output 2: Three stacked panels titled 1. Original Input, 2. AI Probability Map (Input to Viterbi), and 3. Viterbi Extracted Signal (Smoother & Connected). The first panel shows a noisy single-lead strip on a gray background; the heatmap highlights the trace but also forms a saturated bright blob near the right edge; the extracted 1D signal is nearly flat for long stretches with localized spikes. This figure documents that the mask is visible but the Viterbi decoding is not yet recovering a faithful physiologic waveform.

### Cell 7

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 6 |
| First non-empty line | `# --- الخلية 6 (محدثة): معالجة صفحة كاملة باستخدام Viterbi ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Packages the page-level decoder into submission-oriented output formatting, so this cell is the first attempt to align reconstructed signals with the competition deliverable.

**Imports**

- None

**Functions defined**

- process_full_page

**Classes defined**

- None

**Constants / bindings**

- full_signals = ['values']
- prob_map = subscript[0][0]
- rows = ['aug_img']
- signal_clean = values
- strip = image_full[idx]

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

- stream[stdout] with 1 line(s); excerpt: 1️⃣ جاري توليد صفحة ECG كاملة وهمية...
- stream[stderr] with 2 line(s); excerpt: /tmp/ipykernel_144/3773411413.py:93: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise A.GaussNoise(var_limit=(10.0, 50.0), p=0.5),
- stream[stdout] with 2 line(s); excerpt: 2️⃣ تشغيل نظام الرقمنة (Viterbi Engine)... بدء معالجة الصفحة (الحجم: 1200x1600) - تقسيمها إلى 4 صفوف...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-07-output-04.png; text excerpt: <Figure size 1500x1200 with 8 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ تمت المهمة! حصلنا على 4 إشارات رقمية.

**Exceptions**

- None

**Warnings**

- /tmp/ipykernel_144/3773411413.py:93: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-07-output-04.png

**Output interpretation**

- Output 4: Eight-panel page-level comparison arranged as four original strips on the left and four extracted signals on the right. The original strips remain visually readable despite varied noise, rotation, and grid intensity, but the recovered signals are almost flat with only mild drift. The page-scale Viterbi pass is therefore failing to preserve beat morphology even when QRS complexes are obvious in the image.

### Cell 8

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 7 |
| First non-empty line | `# --- الخلية 7 (محدثة): إنشاء ملف التسليم باستخدام Viterbi ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Switches from synthetic experiments to official Kaggle assets by mounting and reading the released metadata and sample files that define the real evaluation surface.

**Imports**

- None

**Functions defined**

- create_submission_file

**Classes defined**

- None

**Constants / bindings**

- full_signals = ['signal_resampled']
- prob_map = subscript[0][0]
- sample_id = sample_i1
- signal_clean = values
- submission_data = ['row_dict']
- target_len = 1000

**Paths mentioned**

- None

**File reads**

- None

**File writes**

- df.to_csv: submission_simulated.csv

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

- stream[stdout] with 8 line(s); excerpt: 📦 جاري تجهيز ملف التسليم لـ 3 عينات (باستخدام Viterbi)... ✅ تم إنشاء ملف التسليم بنجاح. معاينة البيانات: [67.9995 68.0052 67.9988 67.9933 68.0001 68.0054 67.9988 67.9949 68.0026 68...

**Exceptions**

- None

**Warnings**

- None

### Cell 9

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 8 |
| First non-empty line | `# --- الخلية 8 (نسخة Kaggle Notebook): ربط وقراءة البيانات الرسمية ---` |
| Role summary | Rendering / synthetic ECG image generation cell. |

**Editorial interpretation**

- Runs the current model on real stored images rather than synthetic renders, exposing the domain gap between clean training data and actual scanned ECG pages.

**Imports**

- os
- pandas
- glob

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- COMPETITION_NAME = physionet-ecg-image-digitization
- INPUT_DIR = /kaggle/input
- csv_file = /kaggle/input/dirname/f
- dataset_path = /kaggle/input/dirname
- image_example = /kaggle/input/dirname/**/*.jpg

**Paths mentioned**

- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- {dataset_path}/**/*.jpg
- {dataset_path}/**/*.png

**File reads**

- os.listdir: /kaggle/input
- os.listdir: /kaggle/input/dirname
- pd.read_csv: /kaggle/input/dirname/f
- glob.glob: /kaggle/input/dirname/**/*.png
- glob.glob: /kaggle/input/dirname/**/*.jpg

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

- stream[stdout] with 8 line(s); excerpt: ✅ تم العثور على مجلد البيانات في: /kaggle/input/physionet-ecg-image-digitization 📂 محتويات المجلد الرئيسي: ['sample_submission.parquet', 'train.csv', 'test.csv', 'test', 'train'] 📄...
- display_data MIME=text/html, text/plain; text excerpt: id    fs  sig_len 0   7663343   500     5000 1  10140238  1000    10000 2  11842146  1000    10000 3  19030958   250     2500 4  19585145   512     5120; html lines=57
- stream[stdout] with 4 line(s); excerpt: 🔍 فحص مسارات الصور... ✅ تم العثور على صور! مثال لمسار صورة: /kaggle/input/physionet-ecg-image-digitization/test/2352854581.png

**Exceptions**

- None

**Warnings**

- None

**Output interpretation**

- Output 2: HTML dataframe preview of the loaded metadata table. The visible columns are id, fs, and sig_len, and the first visible records include 7663343, 10140238, 11842146, 19030958, and 19585145. This output confirms that the notebook is reading a structured signal index rather than raw image pixels at this stage.

### Cell 10

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 9 |
| First non-empty line | `# --- الخلية 9 (الذكية): اختبار الموديل على صور موجودة فعلياً ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Defines the first dedicated grid-detection and calibration subsystem, explicitly modeling paper scale so later extraction code can convert pixels into physiologically meaningful amplitudes and durations.

**Imports**

- glob
- random
- os
- cv2
- matplotlib.pyplot
- torch
- numpy

**Functions defined**

- test_robust_real_image

**Classes defined**

- None

**Constants / bindings**

- crop_h = 400
- image_name = img_path
- prob_map = subscript[0][0]
- real_strip = real_img[idx]
- search_pattern_jpg = dataset_path/train/*.jpg
- search_pattern_png = dataset_path/train/*.png

**Paths mentioned**

- *.jpg
- *.png
- dataset_path/train/*.jpg
- dataset_path/train/*.png

**File reads**

- glob.glob: dataset_path/train/*.png
- glob.glob: dataset_path/train/*.jpg
- glob.glob: dataset_path/test/*.png
- glob.glob: dataset_path/test/*.jpg
- os.path.exists: dataset_path/train
- os.listdir: dataset_path/train

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

- stream[stdout] with 6 line(s); excerpt: 🕵️‍♂️ جاري البحث عن ملفات صور حقيقية داخل المجلدات... ⚠️ مجلد train يبدو فارغاً أو الصور في مكان آخر، سأبحث في test... ✅ تم العثور على 2 صورة. 📸 تم اختيار الصورة: 1053922973.png 📂 ...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-10-output-02.png; text excerpt: <Figure size 1500x1200 with 3 Axes>

**Exceptions**

- None

**Warnings**

- ⚠️ مجلد train يبدو فارغاً أو الصور في مكان آخر، سأبحث في test...

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-10-output-02.png

**Output interpretation**

- Output 2: Three-panel real-image test titled 1. Real Image, 2. AI Probability Heatmap (Bright areas = Signal), and 3. Extracted Signal (Viterbi). The top panel is a full 12-lead ECG sheet with patient header text, lead labels, and a red grid; the middle heatmap strongly activates on QRS complexes and several grid intersections; the bottom blue trace stays noisy around a narrow baseline band instead of a clinically scaled lead waveform. The figure shows partial localization success but weak end-to-end digitization.

### Cell 11

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 10 |
| First non-empty line | `# --- الخلية 10: نظام المعايرة وكشف الشبكة (Grid Detection & Calibration) ---` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Stress-tests the calibration helpers against representative examples and visual diagnostics, surfacing whether the grid estimate is reliable enough to support downstream measurement.

**Imports**

- scipy.signal

**Functions defined**

- estimate_grid_size
- calibrate_signal

**Classes defined**

- None

**Constants / bindings**

- final_grid_size = 25.0
- grid_height = 0
- grid_width = 0
- img = image_path_or_array

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

- stream[stdout] with 1 line(s); excerpt: ✅ تم تفعيل نظام المعايرة (Grid Calibrator).

**Exceptions**

- None

**Warnings**

- None

### Cell 12

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 11 |
| First non-empty line | `# --- الخلية 11 (مصححة): اختبار المعايرة الشامل ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds sliding-window inference for long or irregular strips, addressing the failure mode where a whole lead cannot be decoded robustly in one pass.

**Imports**

- glob
- random
- os
- cv2
- matplotlib.pyplot
- torch
- numpy
- scipy.signal

**Functions defined**

- get_any_image_path

**Classes defined**

- None

**Constants / bindings**

- crop_h = 400
- dataset_path = r
- files = p
- patterns = ['{root_path}/**/*.png', '{root_path}/**/*.jpg', '{root_path}/**/**/*.png']
- possible_roots = ['/kaggle/input/physionet-ecg-image-digitization', '/kaggle/input']
- prob_map = subscript[0][0]
- real_strip = original_img[idx]

**Paths mentioned**

- /kaggle/input
- /kaggle/input/physionet-ecg-image-digitization
- {root_path}/**/**/*.png
- {root_path}/**/*.jpg
- {root_path}/**/*.png

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

- stream[stdout] with 4 line(s); excerpt: 🔍 جاري البحث عن صور في كل المجلدات... 🧪 تحليل الصورة: 1524001991-0004.png 📂 المسار: /kaggle/input/physionet-ecg-image-digitization/train/1524001991/1524001991-0004.png 1️⃣ جاري حسا...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-12-output-02.png; text excerpt: <Figure size 1000x400 with 1 Axes>
- stream[stdout] with 3 line(s); excerpt: 📏 حجم المربع الصغير المقدر: 14.00 بكسل 2️⃣ استخراج الإشارة... 📏 حجم الشبكة المعدل (للمعايرة): 14.00 بكسل
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-12-output-04.png; text excerpt: <Figure size 1200x800 with 3 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ النتيجة النهائية: انظر للرسم الأحمر، هل القيم منطقية؟

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-12-output-02.png
- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-12-output-04.png

**Output interpretation**

- Output 2: Single-axis grid detection diagnostic titled Grid Detection Analysis. A green edge-intensity trace spans the strip width and red X markers identify candidate grid-line peaks. The title reports an estimated box size of 14.00 pixels in this snapshot. Peak spacing is not perfectly regular, so the detector is seeing repetitive vertical structure but still produces many extra candidate peaks.
- Output 4: Three-panel calibration check titled Original Strip / Before: Raw Signal (Pixel Heights) / After: Calibrated Signal (mV). The top crop retains multiple lead labels such as I, aVR, V1, V4, II, aVL, V2, and V5; the middle plot shows a staircase-like raw pixel trend; the bottom red signal stays close to 0 mV between dashed +/-0.5 mV reference lines. This indicates that the calibration step is suppressing most of the visible morphology instead of converting it into a clinically scaled waveform.

### Cell 13

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 12 |
| First non-empty line | `# --- الخلية 12: الاستخراج بتقنية النافذة المنزلقة (Sliding Window Inference) ---` |
| Role summary | Inference / submission generation cell. |

**Editorial interpretation**

- Retunes the Viterbi transition logic to allow larger jumps, a direct attempt to preserve sharp QRS morphology instead of over-smoothing the recovered waveform.

**Imports**

- None

**Functions defined**

- predict_long_image

**Classes defined**

- None

**Constants / bindings**

- crop_h = 400
- prob = subscript[0][0]
- real_strip = original_img[idx]
- target_h = 256
- window = pad

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

- stream[stdout] with 7 line(s); excerpt: 🚀 تشغيل نظام Sliding Window على صورة حقيقية... 📄 الصورة: 972085095-0010.png 1️⃣ حساب الشبكة... 2️⃣ بناء خريطة الاحتمالات الكاملة... 3️⃣ استخراج المسار (Viterbi)... - حجم الشبكة الأ...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-13-output-02.png; text excerpt: <Figure size 1500x800 with 3 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ هل ترى الآن موجات القلب (QRS) واضحة في الرسم الأحمر؟

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-13-output-02.png

**Output interpretation**

- Output 2: Three-panel sliding-window inference summary titled Stitched Probability Map (Full Length) / Extracted Raw Signal / Final Calibrated Signal (mV). The stitched heatmap clearly highlights narrow vertical complexes across the strip and also catches some printed lead text. The raw signal contains repeated downward spikes, while the final calibrated red trace remains near zero with frequent negative dips around the -0.01 mV range. The figure shows that spatial localization is sharper than the final numeric signal reconstruction.

### Cell 14

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 13 |
| First non-empty line | `# --- الخلية 13: تحديث خوارزمية Viterbi لتسمح بالقفزات العالية (ECG Tuned) ---` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Rewrites processing around the images that actually exist on disk, replacing earlier assumed paths with file-driven discovery so inference no longer depends on guessed artifacts.

**Imports**

- None

**Functions defined**

- viterbi_path_tuned
- extract_signal_simple_argmax

**Classes defined**

- None

**Constants / bindings**

- grid_size_scaled = 10.0
- min_cost = dp[idx][idx]dist_penalty[best_idx_local]
- prev_col_costs = dp[idx]
- raw_signal_tuned = []
- total_cost = dp[idx][idx]dist_penalty
- weights = big_prob_map[x]
- window_costs = dp[idx][idx]
- y_sub = y

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

- stream[stdout] with 3 line(s); excerpt: 🔧 إعادة استخراج الإشارة بإعدادات معدلة... 1️⃣ تشغيل Viterbi (Tuned)... السماح بقفزات تصل لـ 100 بكسل 2️⃣ تشغيل ArgMax (Simple)...
- stream[stderr] with 2 line(s); excerpt: /tmp/ipykernel_144/3820492745.py:60: FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead. return pd....
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-14-output-03.png; text excerpt: <Figure size 1500x1000 with 3 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ قارن بين الرسمين (الأحمر والأزرق). أيهما يلتقط القمم العالية (QRS) بشكل أفضل؟

**Exceptions**

- None

**Warnings**

- /tmp/ipykernel_144/3820492745.py:60: FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh/cell-14-output-03.png

**Output interpretation**

- Output 3: Three-panel algorithm comparison titled Reference: Probability Heatmap / Option A: Tuned Viterbi (Should catch peaks) / Option B: Simple Max Intensity (Baseline). The tuned Viterbi trace repeatedly jumps between a near-zero baseline and clipped negative values around -3 mV, while the baseline panel is effectively degenerate. This plot records that the tuned path is overly aggressive and the simple baseline extractor fails altogether.

### Cell 15

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 17 |
| First non-empty line | `# --- الخلية 14 (الحل الجذري): المعالجة بناءً على الصور الموجودة فعلياً ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Closes the notebook by running the image-driven extraction path end to end, making this cell the practical handoff from exploratory research to a file-based reconstruction workflow.

**Imports**

- pandas
- numpy
- cv2
- torch
- os
- glob
- random
- scipy.signal
- tqdm

**Functions defined**

- get_12_leads_crops

**Classes defined**

- None

**Constants / bindings**

- active_area = image[idx]
- crops = ['image[idx][idx]']
- file_name = img_path
- grid_size = 15.0
- image_files = []
- img_id = subscript[0]
- leads_data = ['final_sig']
- search_roots = ['/kaggle/input', 'dataset_path']
- submission_rows = ['row_dict']
- target_len = 1000

**Paths mentioned**

- /kaggle/input
- submission_from_images.csv
- {root}/**/*.jpg
- {root}/**/*.png

**File reads**

- glob.glob: {root}/**/*.png
- glob.glob: {root}/**/*.jpg

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

- stream[stdout] with 3 line(s); excerpt: 🕵️‍♂️ جاري جرد الصور المتاحة فعلياً... ✅ وجدنا 17590 صورة في المجلدات. 🚀 بدء معالجة 3 صور عشوائية من الموجودة فعلاً...
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 3/3 [00:40<00:00, 13.40s/it]
- stream[stdout] with 4 line(s); excerpt: 🎉 النتيجة النهائية (أرقام حقيقية): [0.112, 0.13, 0.127, 0.11, 0.11, 0.134, 0.143, 0.115, 0.088, 0.117, 0.177, 0.163, 0.008, -0.216, -0.361, -0.368, -0.321, -0.313, -0.327, -0.271, ...
- stream[stderr] with 1 line(s)

**Exceptions**

- None

**Warnings**

- None
