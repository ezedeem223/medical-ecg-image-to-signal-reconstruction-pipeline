# Evaluation Protocol — ECG Waveform Reconstruction

**Status:** Research framework — not a clinical evaluation standard
**Scope:** Defines how reconstruction fidelity should be measured and reported
          for both synthetic and (future) real ECG evaluation.

---

## 1. Objectives

This protocol establishes:
- Which metrics to use for waveform fidelity assessment
- How to report per-lead vs aggregate results
- How to distinguish synthetic from real evaluation
- What limitations must be stated in any evaluation report

---

## 2. Waveform Fidelity Metrics

### 2.1 Primary Metrics

| Metric | Formula | Unit | Notes |
|--------|---------|------|-------|
| MAE | `mean(|gt - pred|)` | signal units | Robust to individual outliers |
| RMSE | `sqrt(mean((gt - pred)²))` | signal units | Sensitive to large deviations |

These metrics are computed per-lead, then aggregated as mean across leads.

### 2.2 Secondary Metrics (Optional)

| Metric | Description | Applicability |
|--------|-------------|---------------|
| SNR proxy | `10 * log10(signal_power / noise_power)` in dB | Synthetic only — requires clean ground truth |
| Pearson correlation | Per-lead correlation between gt and pred | Supplementary shape fidelity measure |
| DTW distance | Dynamic time warping distance | Future — for timing-misaligned comparison |

### 2.3 Signal Alignment

Before computing metrics, signals are aligned to a common length by truncating
to `min(len(gt), len(pred))`. Any length mismatch must be reported in the
evaluation output.

---

## 3. Per-Lead Reporting

All evaluation reports must include per-lead results in addition to aggregate
statistics. This is essential because:

- Different leads have different morphological complexity and amplitude ranges
- Failure modes (e.g., cropping, lead overlap) often affect specific leads
- Aggregate metrics may mask total failure in individual leads

Required per-lead fields:
- `mae`: float
- `rmse`: float
- `gt_length`: int (ground-truth sample count)
- `pred_length`: int (prediction sample count)
- `aligned_length`: int (samples used in metric computation)
- `length_match`: bool

---

## 4. Alignment Sensitivity

The reconstruction is time-indexed: each output sample corresponds to a specific
time point in the original signal. Alignment errors (time shift, rate mismatch)
produce inflated MAE and RMSE even when the waveform shape is correct.

For synthetic benchmark evaluation, alignment is exact (same sample count, same
time grid). For real ECG evaluation, the following alignment checks must be
performed:

- Verify that predicted and ground-truth signals have the same sampling rate
- Verify that the start time of both signals is aligned to the same reference
- Report `length_match: false` and `aligned_length` whenever truncation occurs

---

## 5. QRS vs Low-Amplitude Segment Sensitivity

**Current status:** Future research direction.

QRS complexes (R waves) have high amplitude and are typically easier for
segmentation models to detect. P waves and T waves have lower amplitude and
are more sensitive to:
- Segmentation threshold settings
- Blur and noise
- Low contrast

A future evaluation should decompose per-lead error into:
- QRS-region MAE (samples within ±50ms of detected R-peak)
- Non-QRS MAE (all other samples)

This decomposition requires R-peak detection on the ground-truth signal,
which is not implemented in the current seed.

---

## 6. Synthetic vs Real Evaluation Distinction

Every evaluation report must clearly state which data type was used:

| Field | Synthetic | Real |
|-------|-----------|------|
| `data_source` | `"SYNTHETIC"` | dataset name + version |
| `ground_truth_origin` | `"parametric_generator"` | labeling method |
| `clinical_relevance` | `"none"` | depends on dataset |
| `num_cases` | integer | integer |

**Synthetic evaluation** supports:
- Tooling verification
- Distortion sensitivity analysis
- Regression testing

**Real evaluation** is required for:
- Research claims about pipeline performance
- Any comparison to published systems
- Portfolio-level credibility statements

---

## 7. Limitations

The following limitations apply to all evaluation results produced by this framework:

1. **Synthetic benchmark is not a proxy for real performance.** Scores on
   parametric waveforms do not predict performance on scanned clinical ECGs.

2. **No inter-rater reliability estimate.** The ground truth for real ECG
   digitization depends on the reference system used; this protocol does not
   address inter-rater agreement.

3. **No statistical testing framework.** With 5–10 synthetic cases, no
   confidence intervals or hypothesis tests are valid. Future iterations
   should expand the corpus before reporting statistical measures.

4. **Amplitude units are signal units, not verified millivolts.** The
   synthetic benchmark uses mV-equivalent units derived from the parametric
   generator. Real pipeline output depends on calibration accuracy.

5. **This protocol does not cover clinical efficacy.** It covers engineering
   fidelity of waveform reconstruction only.
