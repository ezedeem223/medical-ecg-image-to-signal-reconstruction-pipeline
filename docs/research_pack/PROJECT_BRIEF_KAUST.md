# Project Brief — ECG Image-to-Signal Reconstruction Pipeline

**Prepared for:** KAUST AI Research Portfolio Review
**Classification:** Research artifact — not a clinical or production system
**Status:** Active development — research workbench seed

---

## 1. Problem Statement

Electrocardiogram (ECG) recordings are one of the most widely used cardiac
assessment tools globally. However, a substantial portion of historical ECG
records exists only as paper printouts, scanned images, PDFs, or photographs —
not as structured digital waveforms. This creates a barrier for retrospective
research, large-scale dataset construction, and integration with modern
signal-processing and machine-learning pipelines.

The core problem is:
> Given a raster image of a 12-lead ECG sheet, recover a faithful numerical
> representation of the underlying waveform signals.

This is a non-trivial computer vision and signal processing challenge because
ECG sheet images vary in print quality, scanner resolution, lighting, orientation,
grid contrast, lead layout, and paper condition.

---

## 2. Motivation

**Research motivation:**
Digitizing legacy ECG archives enables retrospective cohort studies, longitudinal
waveform analysis, and downstream learning systems that require structured signal
data. It also supports migration from image-first clinical archives to structured
biomedical data repositories.

**Engineering motivation:**
Building a robust, modular, and reproducible digitization pipeline demonstrates
production-grade system design within a research context — explicitly separating
inference, calibration, extraction, and export stages.

**Portfolio motivation:**
This project serves as a flagship demonstration of applied AI engineering:
combining deep learning (YOLO, U-Net segmentation), classical signal processing
(Viterbi-based trace extraction, grid calibration), and rigorous software
architecture (typed configs, model registry, explicit selection policies).

---

## 3. Technical Pipeline

The maintained runtime follows a strict sequential inference pipeline:

### 3.1 Lead Detection (Verified)
- **Model:** YOLO-based detector (`best.pt`)
- **Role:** Localizes individual lead strips within the ECG page image
- **Output:** Per-lead bounding box crops

### 3.2 Primary Segmentation (Verified)
- **Model:** EfficientNet-B3 U-Net with SCSE decoder attention
  (`best_model_effb3_phase9_ddp (2).pth`)
- **Role:** Binary segmentation of the ECG trace within each lead crop
- **Augmentation:** Test-time augmentation (multi-scale, horizontal flip)

### 3.3 Fallback Segmentation (Verified)
- **Model:** ResNet50 U-Net with SCSE decoder attention (`best_model_phase10.pth`)
- **Role:** Assists or replaces primary segmentation when primary confidence is low
- **Policy:** Explicit config-driven selection — no automatic checkpoint discovery

### 3.4 Calibration (Verified in architecture)
- Grid spacing estimation from image texture
- Amplitude calibration via pixels-per-millivolt estimation
- Resize-scale correction applied to calibration

### 3.5 Trace Extraction (Verified in architecture)
- Viterbi-based dynamic programming trace along the probability mask
- Skeleton boost option for thin-trace recovery
- Morphological post-processing (erosion/dilation) to clean probability masks

### 3.6 Postprocessing and Export (Verified in architecture)
- High-pass filtering for baseline drift removal
- Signal resampling to target submission length
- Einthoven relation consistency fix (smart_einthoven_fix)
- Strict `id,value` CSV export with deterministic ordering

### 3.7 Model Selection Policy
- All model paths are config-driven and explicitly resolved
- Auto-discovery of checkpoints is forbidden in the core runtime
- Fallback escalation is logged and traceable

---

## 4. Contribution of This Work

This repository represents a production-oriented refactor of a competition-lineage
ECG digitization project. The key contributions are:

1. **Modular architecture:** Clear separation of detection, segmentation,
   calibration, extraction, postprocessing, and export into typed, testable modules.

2. **Explicit model governance:** A registry-based model selection system that
   makes checkpoint identity, role, and fallback policy fully auditable.

3. **Dual-anchor refactor strategy:** A documented methodology for preserving
   structural clarity (from a later notebook lineage) while freezing runtime
   behavior against the best-performing historical lineage — without conflating
   the two.

4. **ECG Research Workbench Seed (this addition):** A synthetic benchmark,
   scoring utility, quality-control framework, and failure mode atlas that begin
   converting the runtime pipeline into a research artifact.

---

## 5. What the Research Workbench Seed Adds

The workbench seed adds:

- **Parametric synthetic ECG-like benchmark:** 5–10 cases with 12-lead-like
  waveforms, ECG-paper-style image rendering, and six distortion variants
  (clean, blur, noise, low contrast, rotation, cropped).

- **Synthetic-only scoring utility:** MAE, RMSE, and an SNR-proxy score
  computed against known ground-truth waveforms. Strictly labeled as synthetic.

- **Engineering QC checks:** NaN/Inf detection, all-zero and flatline detection,
  amplitude range checks, length consistency, per-lead variance — all with
  severity ratings and Markdown report output.

- **Failure mode atlas:** Structured documentation of 8 failure categories with
  likely cause, reconstruction impact, detection signal, and mitigation paths.

- **Research documentation:** This brief, evaluation protocol, reproducibility
  checklist, and synthetic benchmark protocol.

---

## 6. Limitations

The following limitations apply to the current state of this project:

- **No real ECG validation:** The pipeline has not been evaluated against a
  labeled real ECG dataset in this repository. Synthetic benchmark scores
  reflect fidelity on parametric waveforms only.

- **No published score claims:** Historical competition performance values were
  not preserved in a verifiable form within this repository. No numeric
  performance claims are made.

- **Synthetic benchmark scope:** The current synthetic benchmark (5–10 cases)
  is a seed for methodology development, not a statistically meaningful
  evaluation corpus.

- **Runtime dependency on model weights:** Full pipeline inference requires
  three specific checkpoint files. The research tools (generation, scoring, QC)
  work independently of these weights.

- **Platform-specific assumptions:** The runtime assumes a competition-style
  `id,value` waveform export format. Generalization to other export targets
  requires adapter work.

---

## 7. Future Research Directions (KAUST-style)

The following directions are proposed for future research cycles:

### 7.1 Real ECG Evaluation
Evaluate the pipeline against a publicly available labeled ECG dataset
(e.g., PTB-XL, PhysioNet CinC challenge archives) to produce verifiable
per-lead reconstruction metrics.

### 7.2 Benchmark Corpus Expansion
Expand the synthetic benchmark to include pathology-like morphologies
(wide QRS, ST-elevation-like patterns, atrial flutter-like rates) to stress-test
segmentation and extraction robustness.

### 7.3 Failure Mode Simulation
Build a systematic distortion-to-failure mapping: quantify how each distortion
type and severity level degrades per-lead reconstruction quality.

### 7.4 Calibration Robustness
Develop a dedicated calibration evaluation protocol using synthetic ECG images
with known grid spacing and amplitude scaling, to isolate calibration error from
extraction error.

### 7.5 QRS-vs-Low-Amplitude Sensitivity Analysis
Characterize per-lead reconstruction accuracy separately for high-amplitude
(QRS complex) and low-amplitude (P wave, T wave) segments.

### 7.6 Cross-Pipeline Comparison
Compare the EffB3-primary / ResNet50-fallback architecture against
alternative segmentation backbones on a standardized synthetic benchmark
with known ground truth.

---

*This document is prepared for research portfolio purposes. It does not constitute
a clinical validation report, regulatory submission, or publication-ready manuscript.*
