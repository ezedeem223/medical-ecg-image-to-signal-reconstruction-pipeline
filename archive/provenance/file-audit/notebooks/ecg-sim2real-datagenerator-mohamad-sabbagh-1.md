# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 2 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-1.md |
| SHA-256 | 68388a3ca356d72bfb05ab34c7bef9470915aafaabdf9304d301cc5083d4e097 |
| Size (bytes) | 877,339 |
| Modified (UTC) | 2026-04-18T19:30:37.902879+00:00 |
| Inferred role | Prototype notebook with custom dataset / model helper definitions. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 4 |
| Cell count | 8 |
| Code cells | 8 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 5 |
| Editorial cell notes | 8 |
| Editorial output notes | 5 |
| Interpretation confidence | high |
| Open questions | 0 |
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
- sklearn.model_selection
- sys
- torch
- torch.utils.data
- tqdm

**Packages requested via pip/install commands**

- albumentations
- fastparquet
- matplotlib
- numpy<2
- opencv-python
- pandas
- pyarrow
- scikit-image
- scikit-learn
- scipy
- segmentation-models-pytorch
- tqdm

## Hard-Coded Paths And External Environment Markers

**Environment markers**

- Kaggle input mount
- Colab runtime detection
- pip install usage
- segmentation_models_pytorch

**Literal paths / artifacts**

- /kaggle/input
- /kaggle/input/dirname
- dataset_path/test.csv
- self.data_dir/images/self.images[idx]
- self.data_dir/masks/self.masks[idx]
- test.csv
- {OUTPUT_DIR}/images
- {OUTPUT_DIR}/masks
- {dataset_path}/**/*.jpg
- {dataset_path}/**/*.png

## Symbols Defined

**Functions**

- __getitem__
- __init__
- __len__
- augment_pair
- calibrate_signal
- correct_skew_orientation
- estimate_grid_size
- generate_synthetic_heartbeat
- plot_signal_to_image
- preprocess_remove_grid
- smart_crop_12_leads
- viterbi_extract_actual_signal

**Classes**

- ECGDataset
- ECGGenerator

**Constants / assigned names**

- DEVICE
- INPUT_DIR
- LEAD_NAMES
- M
- OUTPUT_DIR
- dataset_path
- dpi
- epoch_loss

## File Operations And Model Loads

**File reads**

- cv2.imread: self.data_dir/images/self.images[idx]
- cv2.imread: self.data_dir/masks/self.masks[idx]
- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- os.listdir: /kaggle/input
- os.listdir: data_dir/images
- os.listdir: data_dir/masks
- os.path.exists: dataset_path/test.csv
- pd.read_csv: dataset_path/test.csv

**File writes**

- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png

**Shell commands**

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image pyarrow fastparquet

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

## Stored Output Inventory

**Output types**

- stream: 8
- display_data: 5

**MIME types**

- image/png: 5
- text/plain: 5

**Exceptions captured in outputs**

- None

**Warnings / warning-like lines**

- None

## Observed Dependency Summary

**Referenced checkpoints**

- None

**Referenced datasets**

- /kaggle/input
- /kaggle/input/dirname
- dataset_path/test.csv
- test.csv
- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- os.listdir: /kaggle/input
- os.path.exists: dataset_path/test.csv

**External files**

- cv2.imread: self.data_dir/images/self.images[idx]
- cv2.imread: self.data_dir/masks/self.masks[idx]
- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- os.listdir: /kaggle/input
- os.listdir: data_dir/images
- os.listdir: data_dir/masks
- os.path.exists: dataset_path/test.csv
- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png

**Required runtime assumptions**

- Assumes in-notebook shell execution is allowed for package installation or environment repair.
- Assumes in-notebook dependency installation is permitted.
- Assumes Kaggle input mounts are available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.

**Outputs created or updated**

- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png

## Phase 1 Closure Status

| Field | Value |
| --- | --- |
| Notebook summary | present |
| Editorial cell coverage | 8/8 |
| Editorial output translations | 5 |
| Delta notes | 5 |
| Open questions | 0 |
| Confidence | high |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Compact proof-of-concept rewrite of the monolithic notebook: it keeps synthetic training, visual QC, calibration, and real-image testing while dropping most exploratory branches.
- This file is the clearest early demonstration notebook because almost every major stage still emits plots for manual inspection.

**Delta notes**

- Compared with the original notebook, this revision compresses the workflow into eight cells and emphasizes visual validation over exploratory side branches.
- The apparent motivation is to compress the monolithic exploratory notebook into a smaller proof-of-concept that can be rerun and visually checked without stepping through every research branch.
- It retains the core synthetic training, calibration, and real-image smoke-test ideas from the first notebook instead of throwing away the earlier pipeline entirely.
- The workflow effect is a much clearer demonstration notebook whose stored plots are easier to interpret as a single run rather than as an interleaved lab notebook.
- What becomes less central is the sprawling mix of side experiments from the original notebook; this revision treats them as background rather than as the main interface.

**Open questions**

- None

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`, cell count changed from 15 to 8, stored output types changed from 42 to 13, and exact shared cell sources = 0.
- New imports: `sys`
- Removed imports: `skimage.io`, `skimage.morphology`
- New model refs: None
- Removed model refs: `torch.save: best_model.pth`
- New first-line titles: `# --- Cell 2: Global Imports & Device Config ---`, `# --- الخلية 1: التثبيت وإعادة التشغيل ---`, `# --- الخلية 3: مولد البيانات وتدريب الموديل ---`, `# --- الخلية 4: التدريب ورسم النتائج ---`, `# --- الخلية 5: خوارزميات المعالجة واختبارها بصرياً ---`, `# --- الخلية 6: المعايرة واكتشاف الشبكة (مع الرسم) ---`, `# --- الخلية 7: اختبار على صور واقعية (مع الرسم) ---`, `# --- الخلية 8: الحفظ النهائي ---`
- Removed first-line titles: `# --- الخلية 10: نظام المعايرة وكشف الشبكة (Grid Detection & Calibration) ---`, `# --- الخلية 11 (مصححة): اختبار المعايرة الشامل ---`, `# --- الخلية 12: الاستخراج بتقنية النافذة المنزلقة (Sliding Window Inference) ---`, `# --- الخلية 13: تحديث خوارزمية Viterbi لتسمح بالقفزات العالية (ECG Tuned) ---`, `# --- الخلية 14 (الحل الجذري): المعالجة بناءً على الصور الموجودة فعلياً ---`, `# --- الخلية 3: كود توليد البيانات ---`, `# --- الخلية 4: تدريب الموديل ---`, `# --- الخلية 5 (محدثة): اختبار استخراج الإشارة باستخدام Viterbi ---`, `# --- الخلية 6 (محدثة): معالجة صفحة كاملة باستخدام Viterbi ---`, `# --- الخلية 7 (محدثة): إنشاء ملف التسليم باستخدام Viterbi ---`, `# --- الخلية 8 (نسخة Kaggle Notebook): ربط وقراءة البيانات الرسمية ---`, `# --- الخلية 9 (الذكية): اختبار الموديل على صور موجودة فعلياً ---`, `# تثبيت كل ما يحتاجه المشروع من البداية للنهاية (بما فيها معالجة البيانات وملفات CSV)`, `# خلية 4.5`, `import os`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- Colab runtime detection is present; behavior may differ between Kaggle and Colab.
- Dependency installation is embedded in notebook cells, so reproducibility depends on runtime package availability.
- Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.

## Cell-By-Cell Audit

### Cell 1

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | None |
| First non-empty line | `# --- الخلية 1: التثبيت وإعادة التشغيل ---` |
| Role summary | Environment bootstrap cell with package installation commands. |

**Editorial interpretation**

- Installs the required packages and expects a runtime restart, creating a clean environment for the compact eight-cell prototype.

**Imports**

- os
- sys

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

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image pyarrow fastparquet

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

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 8 |
| First non-empty line | `# --- Cell 2: Global Imports & Device Config ---` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Loads the scientific stack, configures device and runtime defaults, and keeps only the globals needed for the reduced demonstration workflow.

**Imports**

- os
- cv2
- numpy
- pandas
- matplotlib.pyplot
- random
- glob
- tqdm
- scipy.signal
- torch
- torch.utils.data
- albumentations
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

- stream[stdout] with 2 line(s); excerpt: 🚀 الجهاز الجاهز للعمل: cuda ✅ تم استيراد كافة المكتبات بنجاح.

**Exceptions**

- None

**Warnings**

- None

### Cell 3

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 9 |
| First non-empty line | `# --- الخلية 3: مولد البيانات وتدريب الموديل ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Defines the synthetic generator and training inputs that feed the prototype segmentation model, preserving the data-creation side of the original notebook.

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

- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-03-output-01.png; text excerpt: <Figure size 1000x400 with 2 Axes>
- stream[stdout] with 1 line(s); excerpt: جاري توليد 50 عينة...
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 50/50 [00:10<00:00,  4.89it/s]

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-03-output-01.png

**Output interpretation**

- Output 1: Two-panel data-generation sanity check titled Generated Image (Augmented) / Ground Truth Mask. The left panel shows a synthetic ECG strip on paper with grid and waveform distortions, while the right panel isolates the waveform alone as a white trace on black. The pair confirms that the renderer and mask generator are aligned and that the supervision target excludes the grid.

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 10 |
| First non-empty line | `# --- الخلية 4: التدريب ورسم النتائج ---` |
| Role summary | Training or fine-tuning orchestration cell. |

**Editorial interpretation**

- Runs model training and plots the learning outcomes, so this cell acts as the main quality checkpoint for the compact experiment.

**Imports**

- None

**Functions defined**

- __init__
- __len__
- __getitem__

**Classes defined**

- ECGDataset

**Constants / bindings**

- epoch_loss = 0
- history = ['avg_loss']
- img_path = self.data_dir/images/self.images[idx]
- mask_path = self.data_dir/masks/self.masks[idx]

**Paths mentioned**

- self.data_dir/images/self.images[idx]
- self.data_dir/masks/self.masks[idx]

**File reads**

- cv2.imread: self.data_dir/images/self.images[idx]
- cv2.imread: self.data_dir/masks/self.masks[idx]
- os.listdir: data_dir/images
- os.listdir: data_dir/masks

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

- stream[stdout] with 11 line(s); excerpt: 🚀 بدء التدريب... Epoch 1 | Loss: 0.7765 Epoch 2 | Loss: 0.6709 Epoch 3 | Loss: 0.5949 Epoch 4 | Loss: 0.5104 Epoch 5 | Loss: 0.4189 Epoch 6 | Loss: 0.3252 Epoch 7 | Loss: 0.2497 Ep...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-04-output-02.png; text excerpt: <Figure size 600x400 with 1 Axes>

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-04-output-02.png

**Output interpretation**

- Output 2: Single training plot titled Training Loss Curve. Dice loss decreases monotonically from about 0.78 at epoch 0 to about 0.14 by epoch 9 with no upward reversals. The output supports the claim that the synthetic segmentation run is learning steadily rather than oscillating.

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 11 |
| First non-empty line | `# --- الخلية 5: خوارزميات المعالجة واختبارها بصرياً ---` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Packages the extraction algorithms and tests them visually on controlled examples, letting the author inspect whether the decoded signal follows the rendered trace.

**Imports**

- None

**Functions defined**

- viterbi_extract_actual_signal
- preprocess_remove_grid

**Classes defined**

- None

**Constants / bindings**

- final_signal = []
- prev_costs = dp[idx]
- prob_map = subscript[0][0]
- total = dp[idx]dist_penalty
- w_slice = prob_map[x]
- y_sub = y_int

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

- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-05-output-01.png; text excerpt: <Figure size 1200x800 with 3 Axes>

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-05-output-01.png

**Output interpretation**

- Output 1: Three-panel Viterbi demonstration titled 1. Input Image / 2. AI Probability Map / 3. Viterbi Extracted Signal. The heatmap tracks the synthetic trace closely, but the recovered blue signal sits on a long plateau near the mid-70s with jitter and a late upward drift instead of reproducing repeated beats. The extractor is therefore only partially faithful even on synthetic input.

### Cell 6

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 12 |
| First non-empty line | `# --- الخلية 6: المعايرة واكتشاف الشبكة (مع الرسم) ---` |
| Role summary | Rendering / synthetic ECG image generation cell. |

**Editorial interpretation**

- Adds calibration and grid-detection diagnostics with plotted overlays, checking whether page scale can be recovered before real-image inference.

**Imports**

- None

**Functions defined**

- estimate_grid_size
- calibrate_signal

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

- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-06-output-01.png; text excerpt: <Figure size 1000x400 with 1 Axes>

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-06-output-01.png

**Output interpretation**

- Output 1: Grid-detection diagnostic titled Grid Detection (Size: 13.00 px). The green edge-intensity curve contains repeated tall spikes and red X markers across the rendered strip width. The regular spacing and clean separation are consistent with a synthetic image whose grid size is easier to estimate than the photographed real examples.

### Cell 7

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 14 |
| First non-empty line | `# --- الخلية 7: اختبار على صور واقعية (مع الرسم) ---` |
| Role summary | Rendering / synthetic ECG image generation cell. |

**Editorial interpretation**

- Applies the current stack to real ECG images with visual output, explicitly measuring the synthetic-to-real gap instead of assuming the model transfers cleanly.

**Imports**

- None

**Functions defined**

- correct_skew_orientation

**Classes defined**

- None

**Constants / bindings**

- INPUT_DIR = /kaggle/input
- angle = subscript[idx]
- crop = corrected[idx]
- dataset_path = /kaggle/input/dirname
- prob = subscript[0][0]
- thresh = subscript[1]

**Paths mentioned**

- /kaggle/input
- /kaggle/input/dirname
- {dataset_path}/**/*.jpg
- {dataset_path}/**/*.png

**File reads**

- os.listdir: /kaggle/input
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

- stream[stdout] with 1 line(s); excerpt: ✅ وجدنا 8795 صورة حقيقية. نعرض عينة:
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-07-output-02.png; text excerpt: <Figure size 1000x800 with 3 Axes>

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-1/cell-07-output-02.png

**Output interpretation**

- Output 2: Three-panel real-crop test titled Original Real Crop / Cleaned & Grid Removed / Digitized Signal (mV). The top crop centers on lead aVR over ECG paper, the middle panel removes much of the red grid but leaves faint label remnants, and the bottom red signal shows a sharp startup spike followed by low-amplitude oscillations around zero. The pipeline can isolate the line visually, but the digitized waveform still contains noticeable artifacts.

### Cell 8

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 16 |
| First non-empty line | `# --- الخلية 8: الحفظ النهائي ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Saves the final model artifacts and any required outputs, turning the notebook from a pure demo into a reusable checkpoint-producing run.

**Imports**

- None

**Functions defined**

- smart_crop_12_leads

**Classes defined**

- None

**Constants / bindings**

- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- active_img = image[idx]
- crops = ['image[idx][idx]']
- current_leads = ['final']
- long_ids = []
- long_values = []
- prob = subscript[0][0]
- sample_id = row[id]
- test_csv = dataset_path/test.csv

**Paths mentioned**

- dataset_path/test.csv
- test.csv

**File reads**

- os.path.exists: dataset_path/test.csv
- pd.read_csv: dataset_path/test.csv

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

- stream[stdout] with 1 line(s); excerpt: 🚀 بدء المعالجة النهائية لـ 24 ملف...
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 24/24 [05:30<00:00, 13.76s/it]
- stream[stdout] with 1 line(s); excerpt: ✅ تم الحفظ بنجاح.

**Exceptions**

- None

**Warnings**

- None
