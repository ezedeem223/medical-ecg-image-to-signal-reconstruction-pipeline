# File Audit: `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`

## File Identity

| Field | Value |
| --- | --- |
| Review order | 5 |
| Original path | ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb |
| Report path | docs/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-4.md |
| SHA-256 | 6d99aa11d374feef73a1311277d65b2acb83c35dd85bc5e0d1529ce3e61c9377 |
| Size (bytes) | 2,885,036 |
| Modified (UTC) | 2026-04-18T19:31:38.504536+00:00 |
| Inferred role | End-to-end synthetic data generation and training notebook. |

## Notebook Metadata

| Field | Value |
| --- | --- |
| nbformat | 4 |
| nbformat_minor | 4 |
| Cell count | 23 |
| Code cells | 23 |
| Markdown cells | 0 |
| Raw cells | 0 |
| Extracted image outputs | 7 |
| Editorial cell notes | 23 |
| Editorial output notes | 8 |
| Interpretation confidence | medium |
| Open questions | 1 |
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
- shutil
- skimage.io
- skimage.morphology
- sklearn.model_selection
- sys
- torch
- torch.utils.data
- tqdm
- ultralytics

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
- ultralytics

## Hard-Coded Paths And External Environment Markers

**Environment markers**

- Kaggle input mount
- Colab runtime detection
- pip install usage
- YOLO loader
- segmentation_models_pytorch
- torch.load

**Literal paths / artifacts**

- *.jpg
- *.png
- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- /kaggle/input/physionet-ecg-image-digitization/train
- /kaggle/input/physionet-ecg-image-digitization/train.csv
- best_model.pth
- best_model_real_data.pth
- data.yaml
- dataset_path/train/*.jpg
- dataset_path/train/*.png
- runs/detect/ecg_layout_detector/weights/best.pt
- self.data_dir/images/self.images[idx]
- self.data_dir/masks/self.masks[idx]
- self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- submission.parquet
- submission_from_images.csv
- submission_simulated.csv
- yolo_dataset/data.yaml
- yolo_dataset/images/{subset}/{filename}.jpg
- yolo_dataset/labels/{subset}/{filename}.txt
- yolov8n.pt
- {BASE_DIR}/images/train
- {BASE_DIR}/images/val
- {BASE_DIR}/labels/train
- {BASE_DIR}/labels/val
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
- apply_smoothing
- augment_pair
- blind_crop_12_leads
- calibrate_signal
- correct_skew_orientation
- create_page_with_labels
- create_submission_file
- estimate_grid_size
- estimate_grid_size_simple
- extract_signal_viterbi
- generate_image_pair
- generate_signal
- generate_synthetic_heartbeat
- get_12_leads_crops
- get_any_image_path
- get_yolo_crops
- plot_signal_to_image
- predict_long_image
- preprocess_remove_grid
- process_full_page
- test_robust_real_image
- viterbi_extract_actual_signal
- viterbi_path

**Classes**

- ECGDataset
- ECGGenerator
- RealSignalDataset
- YOLO_ECG_Generator

**Constants / assigned names**

- BASE_DIR
- BATCH_SIZE
- COMPETITION_NAME
- DATA_DIR
- DATA_YAML
- DEVICE
- EPOCHS
- IMAGE_DIR
- INPUT_DIR
- LEAD_NAMES
- LR
- M
- MY_SUB_PATH
- NUM_SAMPLES
- OFFICIAL_SAMPLE_PATH
- OUTPUT_DIR
- TEST_CSV_PATH
- TRAIN_CSV_PATH
- UNET_MODEL_PATH
- YOLO_MODEL_PATH
- best_model_path
- crop_h
- csv_file
- dataset_path
- dpi
- epoch_loss
- final_grid_size
- grid_color
- grid_height
- grid_size
- grid_width
- has_sample
- lead_idx
- target_h
- target_len
- train_loss
- val_loss
- win
- yolo_model

## File Operations And Model Loads

**File reads**

- cv2.imread: self.data_dir/images/self.images[idx]
- cv2.imread: self.data_dir/masks/self.masks[idx]
- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: dataset_path/test/*.jpg
- glob.glob: dataset_path/test/*.png
- glob.glob: dataset_path/train/*.jpg
- glob.glob: dataset_path/train/*.png
- glob.glob: self.root_dir/self.df.iloc[idx][id]/*.csv
- glob.glob: {root}/**/*.jpg
- glob.glob: {root}/**/*.png
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- os.listdir: /kaggle/input
- os.listdir: /kaggle/input/dirname
- os.listdir: data_dir/images
- os.listdir: data_dir/masks
- os.listdir: dataset_path/train
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/train.csv
- os.path.exists: best_model_real_data.pth
- os.path.exists: dataset_path/train
- os.path.exists: runs/detect/ecg_layout_detector/weights/best.pt
- os.path.exists: self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- pd.read_csv: /kaggle/input/dirname/f
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/train.csv
- pd.read_csv: self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- pd.read_parquet: submission.parquet
- torch.load: best_model_real_data.pth

**File writes**

- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png
- df.to_csv: submission_simulated.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: yolo_dataset/data.yaml
- open[w]: yolo_dataset/labels/{subset}/{filename}.txt
- plt.savefig: yolo_dataset/images/{subset}/{filename}.jpg
- torch.save: best_model.pth
- torch.save: best_model_real_data.pth

**Shell commands**

- !pip install "numpy<2" matplotlib opencv-python scipy tqdm albumentations segmentation-models-pytorch pandas scikit-learn scikit-image pyarrow fastparquet
- !pip install ultralytics

**subprocess calls**

- None

**Model loads**

- YOLO: runs/detect/ecg_layout_detector/weights/best.pt
- YOLO: yolov8n.pt
- torch.load: best_model_real_data.pth

**Model saves**

- torch.save: best_model.pth
- torch.save: best_model_real_data.pth

**Model existence probes**

- os.path.exists: best_model_real_data.pth
- os.path.exists: runs/detect/ecg_layout_detector/weights/best.pt

## Stored Output Inventory

**Output types**

- stream: 61
- display_data: 12

**MIME types**

- text/plain: 12
- image/png: 7
- application/vnd.jupyter.widget-view+json: 4
- text/html: 1

**Exceptions captured in outputs**

- None

**Warnings / warning-like lines**

- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'repr' attribute with value False was provided to the `Field()` function, which has no effect in 
- warnings.warn(
- /usr/local/lib/python3.11/dist-packages/pydantic/_internal/_generate_schema.py:2249: UnsupportedFieldAttributeWarning: The 'frozen' attribute with value True was provided to the `Field()` function, which has no effect in
- ⚠️ مجلد train يبدو فارغاً أو الصور في مكان آخر، سأبحث في test...
- /usr/local/lib/python3.11/dist-packages/matplotlib/colors.py:721: RuntimeWarning: invalid value encountered in less
- /tmp/ipykernel_47/1342870666.py:36: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise

## Observed Dependency Summary

**Referenced checkpoints**

- best.pt
- yolov8n.pt
- best_model_real_data.pt
- best_model.pt

**Referenced datasets**

- .csv
- /kaggle/input
- /kaggle/input/dirname
- /kaggle/input/dirname/**/*.jpg
- /kaggle/input/dirname/f
- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- /kaggle/input/physionet-ecg-image-digitization/test.csv

**External files**

- cv2.imread: self.data_dir/images/self.images[idx]
- cv2.imread: self.data_dir/masks/self.masks[idx]
- glob.glob: /kaggle/input/dirname/**/*.jpg
- glob.glob: /kaggle/input/dirname/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: dataset_path/test/*.jpg
- glob.glob: dataset_path/test/*.png
- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png
- df.to_csv: submission_simulated.csv
- open: yolo_dataset/data.yaml

**Required runtime assumptions**

- Assumes in-notebook shell execution is allowed for package installation or environment repair.
- Assumes in-notebook dependency installation is permitted.
- Assumes Kaggle input mounts are available.
- Assumes ultralytics/YOLO is available for lead localization.
- Assumes PyTorch checkpoint loading is available.
- Assumes segmentation_models_pytorch is available for segmentation model construction.

**Outputs created or updated**

- torch.save: best_model.pth
- torch.save: best_model_real_data.pth
- cv2.imwrite: synthetic_dataset/images/sample_{i}.png
- cv2.imwrite: synthetic_dataset/masks/sample_{i}.png
- df.to_csv: submission_simulated.csv
- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: yolo_dataset/data.yaml

## Phase 1 Closure Status

| Field | Value |
| --- | --- |
| Notebook summary | present |
| Editorial cell coverage | 23/23 |
| Editorial output translations | 8 |
| Delta notes | 5 |
| Open questions | 1 |
| Confidence | medium |
| Editorial complete | yes |

## Manual Interpretation

Observed facts are listed in the structural sections above. The bullets below are editorial interpretation and historical inference.

**Notebook summary**

- Research revision that keeps the long-form structure but pivots the ending toward an explicit quality-boost inference factory.
- The notebook still trains and fine-tunes models in place, yet its last cells now focus on how detector crops and phase-2 logic should be assembled for inference.

**Delta notes**

- Compared with notebook (3), this revision keeps the same research skeleton but turns the ending into a deliberate quality-boost inference experiment.
- The apparent motivation is to turn the early prototype into a staged research pipeline that can separately evolve segmentation, calibration, detector preparation, and real-image adaptation.
- It retains the synthetic renderer, segmentation backbone, Viterbi-style decoding, and Kaggle-facing ingestion path from the earlier notebooks.
- The workflow effect is a broader experiment surface: later cells can now feed detector work, real-data tuning, and more deliberate page-level inference rather than only strip-level demos.
- What becomes less central is the purely compact visual-demo framing from notebook (1); the notebook now behaves like a research branch with durable intermediate stages.

**Open questions**

- These notebooks introduce detector preparation and real-data fine-tuning, but the exact checkpoint lineage from these branches into later compact deployment notebooks is not always explicit.

## Differences Vs Previous Notebook In Review Order

- Previous notebook: `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`
- Compared with `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`, cell count changed from 22 to 23, stored output types changed from 66 to 73, and exact shared cell sources = 17.
- New imports: None
- Removed imports: None
- New model refs: None
- Removed model refs: None
- New first-line titles: `# --- الخلية 22: المصنع النهائي المطور (Phase 2 Quality Boost) ---`, `# خلية 18`
- Removed first-line titles: `# خلية 22`

## Risks And Notes

- Hard-coded Kaggle input paths make the notebook environment-specific.
- Colab runtime detection is present; behavior may differ between Kaggle and Colab.
- Dependency installation is embedded in notebook cells, so reproducibility depends on runtime package availability.
- Stored outputs include 6 warning-like lines worth checking during reruns.
- Notebook contains no markdown commentary; intent must be inferred from code, comments, and outputs only.
- Notebook depends on both object detection and segmentation stacks, increasing environment complexity.
- Checkpoint loading is embedded in the workflow; model file availability is a runtime prerequisite.

## Cell-By-Cell Audit

### Cell 1

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 1 |
| First non-empty line | `# --- الخلية 1: التثبيت وإعادة التشغيل ---` |
| Role summary | Environment bootstrap cell with package installation commands. |

**Editorial interpretation**

- Bootstraps the environment and prepares for a runtime restart, preserving the assumption that package installation happens inside the notebook rather than upstream.

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
- !pip install ultralytics

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- None

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 250 line(s); excerpt: Requirement already satisfied: numpy<2 in /usr/local/lib/python3.11/dist-packages (1.26.4) Requirement already satisfied: matplotlib in /usr/local/lib/python3.11/dist-packages (3.7...

**Exceptions**

- None

**Warnings**

- None

### Cell 2

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 2 |
| First non-empty line | `# خلية 2` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Loads the runtime stack, shared imports, and path configuration so the rest of the notebook can move between synthetic assets and Kaggle inputs without repeating setup logic.

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
- glob
- ultralytics
- shutil

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
- stream[stdout] with 6 line(s); excerpt: Creating new Ultralytics Settings v0.0.6 file ✅ View Ultralytics Settings with 'yolo settings' or at '/root/.config/Ultralytics/settings.json' Update Settings with 'yolo settings k...

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
| First non-empty line | `# خلية 3` |
| Role summary | Definition cell that defines 4 function(s) and 1 class(es). |

**Editorial interpretation**

- Keeps a reusable synthetic rendering and data-generation cell in the notebook, because every later training or detector branch still depends on controllable ECG imagery.

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
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 50/50 [00:08<00:00,  5.91it/s]
- stream[stdout] with 1 line(s); excerpt: ✅ تم توليد البيانات بنجاح.
- stream[stderr] with 1 line(s)

**Exceptions**

- None

**Warnings**

- None

### Cell 4

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 4 |
| First non-empty line | `# خلية 4` |
| Role summary | Definition cell that defines 3 function(s) and 1 class(es). |

**Editorial interpretation**

- Keeps the baseline segmentation-training role but treats it as the starting point for a more inference-focused late-stage pipeline.

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
- stream[stdout] with 12 line(s); excerpt: 🚀 بدء التدريب على 50 صورة لمدة 10 دورات... Epoch [1/10] | Loss: 0.7992 Epoch [2/10] | Loss: 0.7151 Epoch [3/10] | Loss: 0.6690 Epoch [4/10] | Loss: 0.6272 Epoch [5/10] | Loss: 0.58...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-04-output-04.png; text excerpt: <Figure size 1200x400 with 3 Axes>

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-04-output-04.png

**Output interpretation**

- Output 4: Three-panel training sanity check titled Input / Target / AI Prediction. The left panel is a synthetic Lead II strip on red ECG paper, the middle panel is a binary mask, and the right panel is the predicted mask. Peak timing is preserved well, but small baseline details and trace thickness still drift between the target and the prediction.

### Cell 5

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 5 |
| First non-empty line | `# --الخلية 5 ---` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Defines the mask-to-signal post-processing helpers, including the dynamic-programming and Viterbi-style logic that translates probability maps into one-dimensional traces.

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
| Execution count | 6 |
| First non-empty line | `# --- الخلية 6---` |
| Role summary | Execution cell with stored outputs. |

**Editorial interpretation**

- Executes a focused smoke test with stored outputs so the author can inspect whether the current model and decoder recover a plausible strip before moving to page-level logic.

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

- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-06-output-01.png; text excerpt: <Figure size 1200x800 with 3 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ تم استخدام Viterbi بنجاح!

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-06-output-01.png

**Output interpretation**

- Output 1: Three-panel Viterbi demonstration titled 1. Original Input / 2. AI Probability Map (Input to Viterbi) / 3. Viterbi Extracted Signal (Smoother & Connected). The probability map follows the slanted single-lead strip convincingly, but the extracted blue signal collapses into broad baseline drift rather than repeated ECG complexes. The model output is usable as a spatial mask, while the 1D decoder remains the weak link.

### Cell 7

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 7 |
| First non-empty line | `# --- الخلية 7 ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Wraps the strip decoder into a full-page or multi-lead processing helper, which is required before the notebook can touch real Kaggle pages.

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

- stream[stdout] with 3 line(s); excerpt: 1️⃣ جاري توليد صفحة ECG كاملة وهمية... 2️⃣ تشغيل نظام الرقمنة (Viterbi Engine)... بدء معالجة الصفحة (الحجم: 1200x1600) - تقسيمها إلى 4 صفوف...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-07-output-02.png; text excerpt: <Figure size 1500x1200 with 8 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ تمت المهمة! حصلنا على 4 إشارات رقمية.

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-07-output-02.png

**Output interpretation**

- Output 2: Eight-panel page-level comparison with original strips on the left and extracted signals on the right. The image examples remain legible under different rotations and noise patterns, but the recovered signals are almost flat with only small drifts. This output documents that the current page-scale Viterbi pass does not preserve beat morphology across examples.

### Cell 8

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 8 |
| First non-empty line | `# --- الخلية 8:  ---` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Introduces submission-oriented formatting helpers that reshape reconstructed leads into the schema expected by the competition files.

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

- submission_simulated.csv

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

- stream[stdout] with 6 line(s); excerpt: 📦 جاري تجهيز ملف التسليم لـ 3 عينات (باستخدام Viterbi)... ✅ تم إنشاء ملف التسليم بنجاح. معاينة البيانات: [         68      68.001          68      67.999          68      68.001   ...

**Exceptions**

- None

**Warnings**

- None

### Cell 9

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 9 |
| First non-empty line | `# --- الخلية 9:  ---` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Loads the official Kaggle metadata and image inventory, turning the notebook from a synthetic-only experiment into one that can address real evaluation inputs.

**Imports**

- None

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

- Output 2: HTML dataframe preview of the loaded metadata table. The visible columns are id, fs, and sig_len, and the visible sample rows begin with ids such as 7663343 and 10140238. The notebook is therefore operating on an indexed signal catalog at this step, not only on raw image tensors.

### Cell 10

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 10 |
| First non-empty line | `# الخلية 10` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds a real-image inference harness that points the current model stack at actual competition pages and exposes the remaining domain mismatch.

**Imports**

- None

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

- stream[stdout] with 6 line(s); excerpt: 🕵️‍♂️ جاري البحث عن ملفات صور حقيقية داخل المجلدات... ⚠️ مجلد train يبدو فارغاً أو الصور في مكان آخر، سأبحث في test... ✅ تم العثور على 2 صورة. 📸 تم اختيار الصورة: 2352854581.png 📂 ...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-10-output-02.png; text excerpt: <Figure size 1500x1200 with 3 Axes>

**Exceptions**

- None

**Warnings**

- ⚠️ مجلد train يبدو فارغاً أو الصور في مكان آخر، سأبحث في test...

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-10-output-02.png

**Output interpretation**

- Output 2: Three-panel real-page inference example titled 1. Real Image / 2. AI Probability Heatmap (Bright areas = Signal) / 3. Extracted Signal (Viterbi). The top panel is a photographed 12-lead ECG sheet with header metadata, lead names, and red paper grid; the middle heatmap activates strongly on major complexes and some grid structure; the bottom extracted trace remains noisy and quasi-static instead of a clinically scaled lead waveform. The figure shows good localization cues but incomplete numeric reconstruction.

### Cell 11

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 11 |
| First non-empty line | `# الخلية 11` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Defines grid-detection and calibration helpers so waveform extraction can be normalized against paper spacing rather than raw pixels alone.

**Imports**

- None

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
| Execution count | 12 |
| First non-empty line | `# خلية 12` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Runs a calibration or visualization sanity pass, confirming whether the grid estimate and lead geometry look stable on representative samples.

**Imports**

- None

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

- stream[stdout] with 4 line(s); excerpt: 🔍 جاري البحث عن صور في كل المجلدات... 🧪 تحليل الصورة: 1012423188-0010.png 📂 المسار: /kaggle/input/physionet-ecg-image-digitization/train/1012423188/1012423188-0010.png 1️⃣ جاري حسا...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-12-output-02.png; text excerpt: <Figure size 1000x400 with 1 Axes>
- stream[stdout] with 3 line(s); excerpt: 📏 حجم المربع الصغير المقدر: 12.00 بكسل 2️⃣ استخراج الإشارة... 📏 حجم الشبكة المعدل (للمعايرة): 13.00 بكسل
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-12-output-04.png; text excerpt: <Figure size 1200x800 with 3 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ النتيجة النهائية: انظر للرسم الأحمر، هل القيم منطقية؟

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-12-output-02.png
- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-12-output-04.png

**Output interpretation**

- Output 2: Grid-detection diagnostic on a full-width real strip. A green edge-intensity curve spans the x-axis and red X markers show candidate grid intersections or line positions. The title reports an estimated box size in pixels for the current image. The detector captures recurring grid structure, but the high density of candidate peaks shows that spacing regularization is still incomplete on real paper textures.
- Output 4: Three-panel calibration check titled Original Strip / Before: Raw Signal (Pixel Heights) / After: Calibrated Signal (mV). The top crop retains the photographed paper texture and printed lead labels, the middle raw curve has downward spikes but limited vertical range, and the bottom calibrated red trace stays close to 0 mV between dashed +/-0.5 mV references. Most visible morphology is lost during the calibration step.

### Cell 13

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 13 |
| First non-empty line | `# خلية 13` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds a sliding-window or segmented decoding helper for long traces, reducing the chance that local failures corrupt the entire lead.

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

- stream[stdout] with 7 line(s); excerpt: 🚀 تشغيل نظام Sliding Window على صورة حقيقية... 📄 الصورة: 4087968066-0009.png 1️⃣ حساب الشبكة... 2️⃣ بناء خريطة الاحتمالات الكاملة... 3️⃣ استخراج المسار (Viterbi)... - حجم الشبكة ال...
- display_data MIME=image/png, text/plain; image payload present; artifact=image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-13-output-02.png; text excerpt: <Figure size 1500x800 with 3 Axes>
- stream[stdout] with 1 line(s); excerpt: ✅ هل ترى الآن موجات القلب (QRS) واضحة في الرسم الأحمر؟

**Exceptions**

- None

**Warnings**

- None

**Output artifacts**

- image-outputs/ecg-sim2real-datagenerator-mohamad-sabbagh-4/cell-13-output-02.png

**Output interpretation**

- Output 2: Three-panel sliding-window summary titled Stitched Probability Map (Full Length) / Extracted Raw Signal / Final Calibrated Signal (mV). The stitched heatmap highlights repeated complexes and some printed labels, the raw signal shows section-to-section baseline shifts, and the final calibrated red trace oscillates around zero with alternating plateaus and spikes. The output is more structured than the simple Viterbi traces, but it is still not a clean physiologic reconstruction.

### Cell 14

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 14 |
| First non-empty line | `# خلية 14` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adjusts the waveform path solver and post-processing rules so sharp transitions can survive decoding instead of collapsing into an over-smoothed line.

**Imports**

- None

**Functions defined**

- viterbi_extract_actual_signal

**Classes defined**

- None

**Constants / bindings**

- final_signal = []
- prev_col_costs = dp[idx]
- total = dp[idx][idx]dist_penalty
- weights = prob_map[x]
- window_costs = dp[idx][idx]
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

- stream[stdout] with 1 line(s); excerpt: ✅ تم تحديث دالة Viterbi لتخرج إشارة (Amplitude) مباشرة.

**Exceptions**

- None

**Warnings**

- None

### Cell 15

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 15 |
| First non-empty line | `# خلية 15` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Introduces geometry-aware lead or strip normalization, correcting rotation and alignment assumptions before later detector-assisted versions.

**Imports**

- None

**Functions defined**

- correct_skew_orientation

**Classes defined**

- None

**Constants / bindings**

- angle = subscript[idx]
- center = []
- thresh = subscript[1]

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

### Cell 16

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 16 |
| First non-empty line | `# خلية 16` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Adds cleanup logic that strips grid remnants or background clutter before the trace is decoded, improving robustness outside the synthetic domain.

**Imports**

- None

**Functions defined**

- preprocess_remove_grid

**Classes defined**

- None

**Constants / bindings**

- grid_mask = mask1mask2

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

### Cell 17

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 17 |
| First non-empty line | `# خلية 17` |
| Role summary | Definition cell that defines 1 function(s). |

**Editorial interpretation**

- Provides a manual validation or crop-level helper used to inspect the current pipeline on chosen examples before the notebook expands into new branches.

**Imports**

- None

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
- stream[stderr] with 1 line(s); excerpt: 0%|          | 0/3 [00:00<?, ?it/s]
- stream[stdout] with 1 line(s); excerpt: 📐 تم اكتشاف ميل وتصحيحه بزاوية: -0.57 درجة
- stream[stderr] with 1 line(s); excerpt: 67%|██████▋   | 2/3 [00:25<00:12, 12.88s/it]
- stream[stdout] with 1 line(s); excerpt: 📐 تم اكتشاف ميل وتصحيحه بزاوية: -0.60 درجة
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 3/3 [00:38<00:00, 12.92s/it]
- stream[stdout] with 4 line(s); excerpt: 🎉 النتيجة النهائية (أرقام حقيقية): [-1.431, -1.34, -1.321, -1.339, -1.349, -1.351, -1.368, -1.401, -1.419, -1.409, -1.401, -1.429, -1.47, -1.47, -1.419, -1.381, -1.422, -1.528, -1....
- stream[stderr] with 1 line(s)

**Exceptions**

- None

**Warnings**

- None

### Cell 18

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 18 |
| First non-empty line | `# خلية 18` |
| Role summary | Definition cell that defines 3 function(s) and 1 class(es). |

**Editorial interpretation**

- Creates the synthetic page and YOLO-label factory used to keep localization training aligned with the current rendering assumptions.

**Imports**

- None

**Functions defined**

- __init__
- generate_signal
- create_page_with_labels

**Classes defined**

- YOLO_ECG_Generator

**Constants / bindings**

- BASE_DIR = yolo_dataset
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- label_path = yolo_dataset/labels/{subset}/{filename}.txt
- labels_data = ['0 {x_center} {y_center} {w} {h}']
- lead_idx = 0
- lead_name = I[0]
- save_path = yolo_dataset/images/{subset}/{filename}.jpg
- yaml_content = 
path: {expr} 
train: images/train
val: images/val

nc: 12
names: I


**Paths mentioned**

- data.yaml
- yolo_dataset/images/{subset}/{filename}.jpg
- yolo_dataset/labels/{subset}/{filename}.txt
- {BASE_DIR}/images/train
- {BASE_DIR}/images/val
- {BASE_DIR}/labels/train
- {BASE_DIR}/labels/val

**File reads**

- open: yolo_dataset/data.yaml
- open: yolo_dataset/labels/{subset}/{filename}.txt

**File writes**

- open: yolo_dataset/data.yaml
- open[w]: yolo_dataset/data.yaml
- plt.savefig: yolo_dataset/images/{subset}/{filename}.jpg
- open: yolo_dataset/labels/{subset}/{filename}.txt
- open[w]: yolo_dataset/labels/{subset}/{filename}.txt

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

- stream[stdout] with 1 line(s); excerpt: 🏭 جاري تشغيل مصنع بيانات YOLO...
- stream[stderr] with 2 line(s); excerpt: Training Data: 100%|██████████| 200/200 [01:30<00:00,  2.21it/s] Validation Data: 100%|██████████| 50/50 [00:24<00:00,  2.08it/s]
- stream[stdout] with 3 line(s); excerpt: ✅ تم إنشاء البيانات في مجلد 'yolo_dataset'. ✅ تم إنشاء ملف التكوين 'data.yaml'.
- stream[stderr] with 1 line(s)

**Exceptions**

- None

**Warnings**

- None

### Cell 19

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 19 |
| First non-empty line | `# خلية 19` |
| Role summary | Model loading or model wiring cell. |

**Editorial interpretation**

- Bootstraps the detector branch around that generated dataset so page localization remains part of the end-to-end plan.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- best_model_path = runs/detect/ecg_layout_detector/weights/best.pt

**Paths mentioned**

- runs/detect/ecg_layout_detector/weights/best.pt
- yolo_dataset/data.yaml
- yolov8n.pt

**File reads**

- os.path.exists: runs/detect/ecg_layout_detector/weights/best.pt

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: yolov8n.pt

**Model saves**

- None

**Model existence probes**

- os.path.exists: runs/detect/ecg_layout_detector/weights/best.pt

**Stored outputs**

- stream[stdout] with 160 line(s); excerpt: [KDownloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8n.pt to 'yolov8n.pt': 100% ━━━━━━━━━━━━ 6.2MB 23.0MB/s 0.3s.2s<0.2s4s 🚀 بدء تدريب YOLOv8n على بي...
- stream[stderr] with 4 line(s); excerpt: /usr/local/lib/python3.11/dist-packages/matplotlib/colors.py:721: RuntimeWarning: invalid value encountered in less xa[xa < 0] = -1 /usr/local/lib/python3.11/dist-packages/matplotl...
- stream[stdout] with 17 line(s); excerpt: all         50        600      0.997          1      0.995      0.995 I         50         50      0.997          1      0.995      0.995 II         50         50      0.997       ...

**Exceptions**

- None

**Warnings**

- /usr/local/lib/python3.11/dist-packages/matplotlib/colors.py:721: RuntimeWarning: invalid value encountered in less

### Cell 20

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 20 |
| First non-empty line | `# خلية 20` |
| Role summary | Definition cell that defines 4 function(s) and 1 class(es). |

**Editorial interpretation**

- Runs the real-data fine-tuning branch that adapts segmentation weights toward scanned competition pages.

**Imports**

- None

**Functions defined**

- __init__
- __len__
- generate_image_pair
- __getitem__

**Classes defined**

- RealSignalDataset

**Constants / bindings**

- BATCH_SIZE = 16
- DATA_DIR = /kaggle/input/physionet-ecg-image-digitization/train
- EPOCHS = 8
- LR = 0.0003
- TRAIN_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/train.csv
- best_val_loss = avg_val_loss
- dpi = 100
- full_signal = values
- grid_color = #ffb6c1
- rec_id = self.df.iloc[idx][id]
- row = self.df.iloc[idx]
- sig_path = self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- signal_segment = values[idx]
- train_loss = 0
- val_loss = 0

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization/train
- /kaggle/input/physionet-ecg-image-digitization/train.csv
- self.root_dir/self.df.iloc[idx][id]/*.csv[0]

**File reads**

- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/train.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/train.csv
- pd.read_csv: self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- os.path.exists: self.root_dir/self.df.iloc[idx][id]/*.csv[0]
- glob.glob: self.root_dir/self.df.iloc[idx][id]/*.csv

**File writes**

- torch.save: best_model_real_data.pth

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- None

**Model saves**

- torch.save: best_model_real_data.pth

**Model existence probes**

- None

**Stored outputs**

- stream[stdout] with 1 line(s); excerpt: ✅ تم تحميل 977 ملف إشارة.
- stream[stderr] with 2 line(s); excerpt: /tmp/ipykernel_47/1342870666.py:36: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise A.GaussNoise(var_limit=(20.0, 100.0), p=0.3),
- display_data MIME=application/vnd.jupyter.widget-view+json, text/plain; text excerpt: config.json:   0%|          | 0.00/156 [00:00<?, ?B/s]
- display_data MIME=application/vnd.jupyter.widget-view+json, text/plain; text excerpt: model.safetensors:   0%|          | 0.00/87.3M [00:00<?, ?B/s]
- stream[stdout] with 1 line(s); excerpt: 🚀 بدء التدريب الذكي (Saving Best Model Only)...
- stream[stderr] with 1 line(s); excerpt: Epoch 1/8: 100%|██████████| 49/49 [11:18<00:00, 13.86s/it, loss=0.842]
- stream[stdout] with 2 line(s); excerpt: Epoch 1 -> Train Loss: 0.8920 | Val Loss: 0.8372 🔥 تحسن! (Loss انخفض من inf إلى 0.8372) -> جاري الحفظ...
- stream[stderr] with 1 line(s); excerpt: Epoch 2/8: 100%|██████████| 49/49 [11:34<00:00, 14.18s/it, loss=0.684]
- stream[stdout] with 2 line(s); excerpt: Epoch 2 -> Train Loss: 0.7698 | Val Loss: 0.6839 🔥 تحسن! (Loss انخفض من 0.8372 إلى 0.6839) -> جاري الحفظ...
- stream[stderr] with 1 line(s); excerpt: Epoch 3/8: 100%|██████████| 49/49 [11:24<00:00, 13.98s/it, loss=0.309]
- stream[stdout] with 2 line(s); excerpt: Epoch 3 -> Train Loss: 0.5113 | Val Loss: 0.3877 🔥 تحسن! (Loss انخفض من 0.6839 إلى 0.3877) -> جاري الحفظ...
- stream[stderr] with 1 line(s); excerpt: Epoch 4/8: 100%|██████████| 49/49 [11:20<00:00, 13.89s/it, loss=0.17]
- stream[stdout] with 2 line(s); excerpt: Epoch 4 -> Train Loss: 0.2562 | Val Loss: 0.1839 🔥 تحسن! (Loss انخفض من 0.3877 إلى 0.1839) -> جاري الحفظ...
- stream[stderr] with 1 line(s); excerpt: Epoch 5/8: 100%|██████████| 49/49 [11:21<00:00, 13.90s/it, loss=0.121]
- stream[stdout] with 2 line(s); excerpt: Epoch 5 -> Train Loss: 0.1443 | Val Loss: 0.1230 🔥 تحسن! (Loss انخفض من 0.1839 إلى 0.1230) -> جاري الحفظ...
- stream[stderr] with 1 line(s); excerpt: Epoch 6/8: 100%|██████████| 49/49 [11:27<00:00, 14.03s/it, loss=0.0978]
- stream[stdout] with 2 line(s); excerpt: Epoch 6 -> Train Loss: 0.1032 | Val Loss: 0.0895 🔥 تحسن! (Loss انخفض من 0.1230 إلى 0.0895) -> جاري الحفظ...
- stream[stderr] with 1 line(s); excerpt: Epoch 7/8: 100%|██████████| 49/49 [11:23<00:00, 13.95s/it, loss=0.0749]
- stream[stdout] with 2 line(s); excerpt: Epoch 7 -> Train Loss: 0.0822 | Val Loss: 0.0800 🔥 تحسن! (Loss انخفض من 0.0895 إلى 0.0800) -> جاري الحفظ...
- stream[stderr] with 1 line(s); excerpt: Epoch 8/8: 100%|██████████| 49/49 [11:22<00:00, 13.93s/it, loss=0.0575]
- stream[stdout] with 3 line(s); excerpt: Epoch 8 -> Train Loss: 0.0687 | Val Loss: 0.0616 🔥 تحسن! (Loss انخفض من 0.0800 إلى 0.0616) -> جاري الحفظ... ✅ انتهى التدريب. أفضل Val Loss تم تحقيقه: 0.0616

**Exceptions**

- None

**Warnings**

- /tmp/ipykernel_47/1342870666.py:36: UserWarning: Argument(s) 'var_limit' are not valid for transform GaussNoise

### Cell 21

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 21 |
| First non-empty line | `# خلية 21` |
| Role summary | Definition cell that defines 2 function(s). |

**Editorial interpretation**

- Adds glue code that reconciles page orientation, detector crops, and segmentation input formatting before the final inference factory runs.

**Imports**

- None

**Functions defined**

- correct_skew_orientation
- get_yolo_crops

**Classes defined**

- None

**Constants / bindings**

- angle = subscript[idx]
- center = []
- conf = box.conf[0]
- ordered_crops = ['image[idx]']
- thresh = subscript[1]
- xyxy = box.xyxy[0]

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

- stream[stdout] with 1 line(s); excerpt: ✅ تم تحديث الدوال الهندسية (Skew Safety + YOLO Fallback).

**Exceptions**

- None

**Warnings**

- None

### Cell 22

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 22 |
| First non-empty line | `# --- الخلية 22: المصنع النهائي المطور (Phase 2 Quality Boost) ---` |
| Role summary | Definition cell that defines 8 function(s). |

**Editorial interpretation**

- Defines the phase-2 quality-boost inference factory, an explicit attempt to increase reconstruction fidelity without reopening the whole training stack.

**Imports**

- None

**Functions defined**

- estimate_grid_size_simple
- viterbi_extract_actual_signal
- calibrate_signal
- apply_smoothing
- correct_skew_orientation
- preprocess_remove_grid
- blind_crop_12_leads
- get_yolo_crops

**Classes defined**

- None

**Constants / bindings**

- IMAGE_DIR = /kaggle/input/physionet-ecg-image-digitization
- LEAD_NAMES = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
- TEST_CSV_PATH = /kaggle/input/physionet-ecg-image-digitization/test.csv
- UNET_MODEL_PATH = best_model_real_data.pth
- YOLO_MODEL_PATH = runs/detect/ecg_layout_detector/weights/best.pt
- active = image[idx]
- angle = subscript[idx]
- center = []
- conf = b.conf[0]
- crops = ['image[idx]']
- current_leads_data = ['resampled']
- final_signal = []
- h_crop = crop.shape[0]
- img_corrected = original_img
- lead_name = I[lead_idx]
- long_ids = []
- long_values = []
- prev_col_costs = dp[idx]
- prob_map = subscript[0][0]
- r = subscript[0]
- sample_id = row[id]
- target_h = 256
- thresh = subscript[1]
- total = dp[idx][idx]dist_penalty
- weights = prob_map[x]
- window_costs = dp[idx][idx]
- xyxy = b.xyxy[0]
- y_sub = y_int

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization
- /kaggle/input/physionet-ecg-image-digitization/test.csv
- best_model_real_data.pth
- runs/detect/ecg_layout_detector/weights/best.pt

**File reads**

- os.path.exists: runs/detect/ecg_layout_detector/weights/best.pt
- os.path.exists: best_model_real_data.pth
- os.path.exists: /kaggle/input/physionet-ecg-image-digitization/test.csv
- pd.read_csv: /kaggle/input/physionet-ecg-image-digitization/test.csv
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.png
- glob.glob: /kaggle/input/physionet-ecg-image-digitization/**/*.jpg
- torch.load: best_model_real_data.pth

**File writes**

- None

**Shell commands**

- None

**subprocess calls**

- None

**Model loads**

- YOLO: runs/detect/ecg_layout_detector/weights/best.pt
- torch.load: best_model_real_data.pth

**Model saves**

- None

**Model existence probes**

- os.path.exists: runs/detect/ecg_layout_detector/weights/best.pt
- os.path.exists: best_model_real_data.pth

**Stored outputs**

- stream[stdout] with 4 line(s); excerpt: ⚙️ جاري تحميل ترسانة النماذج (Phase 2 + Smoothing)... ✅ YOLO: تم التحميل. ✅ U-Net (Real Data): تم التحميل. 🚀 بدء المصنع النهائي (Phase 2 + Smoothing)...
- stream[stderr] with 1 line(s); excerpt: 100%|██████████| 24/24 [05:54<00:00, 14.75s/it]
- stream[stdout] with 2 line(s); excerpt: 💾 حفظ النتائج النهائية... ✅ تم حفظ submission.parquet (جاهز للتسليم!)

**Exceptions**

- None

**Warnings**

- None

### Cell 23

| Field | Value |
| --- | --- |
| Cell type | code |
| Execution count | 26 |
| First non-empty line | `# خلية 23` |
| Role summary | Data I/O and pipeline coordination cell. |

**Editorial interpretation**

- Validates the phase-2 factory against the expected parquet and template layout before treating it as submission-ready.

**Imports**

- None

**Functions defined**

- None

**Classes defined**

- None

**Constants / bindings**

- MY_SUB_PATH = submission.parquet
- OFFICIAL_SAMPLE_PATH = /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- first_id = my_sub.iloc[0][id]
- first_value = my_sub.iloc[0][value]
- has_sample = False

**Paths mentioned**

- /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet
- submission.parquet

**File reads**

- pd.read_parquet: submission.parquet
- pd.read_parquet: /kaggle/input/physionet-ecg-image-digitization/sample_submission.parquet

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

- stream[stdout] with 11 line(s); excerpt: 🔍 جاري التحقق من التنسيق الطويل (Long Format)... ✅ أسماء الأعمدة صحيحة (id, value). ✅ نوع البيانات (float) صحيح. 🔍 عينة من الـ ID في ملفك: 1053922973_0_I 📊 إجمالي عدد الصفوف في ملف...

**Exceptions**

- None

**Warnings**

- None
