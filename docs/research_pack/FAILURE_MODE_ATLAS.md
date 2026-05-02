# Failure Mode Atlas — ECG Image Digitization Pipeline

**Scope:** Engineering and research reference only.
**Status:** Conceptual and synthetic failure modes — based on pipeline architecture
analysis and synthetic benchmark design. No real patient failure cases are documented here.

> All failure modes marked **[CONCEPTUAL]** are derived from architectural analysis
> and domain knowledge, not from observed real-data failures. All failure modes marked
> **[SYNTHETIC-SIMULATED]** can be reproduced using the synthetic benchmark distortion suite.

---

## Overview

| # | Failure Category | Severity | Synthetic Simulation |
|---|-----------------|----------|----------------------|
| 1 | Low contrast | High | Yes — `low_contrast` distortion |
| 2 | Rotation / perspective distortion | High | Yes — `rotation` distortion |
| 3 | Blur | Medium–High | Yes — `blur` distortion |
| 4 | Cropped sheet / margin loss | Medium | Yes — `cropped` distortion |
| 5 | Grid weakness / absence | High | Partial |
| 6 | Overlapping leads | High | Not yet |
| 7 | Flatline / all-zero extraction | Critical | Detectable via QC |
| 8 | Calibration ambiguity | High | Partial |

---

## Failure Mode 1: Low Contrast

**Tags:** [CONCEPTUAL] [SYNTHETIC-SIMULATED]

**Description:**
The ECG trace has low contrast relative to the ECG paper background, making it
difficult for the segmentation model to separate signal pixels from background.

**Likely Cause:**
- Poor scan quality or photocopied ECG sheets
- Faded thermal paper prints
- Over-exposed photography
- Automatic brightness normalization applied to the image before pipeline input

**Expected Reconstruction Impact:**
- Segmentation probability map has low peak values across the trace
- Viterbi trace extraction may follow background texture rather than true signal
- All-zero or near-zero lead output after threshold application
- QRS peaks may be partially detected while P and T waves are lost entirely

**Detection Signal:**
- Low mean probability in primary segmentation output
- QC: flatline or all-zero detection on extracted signal
- QC: amplitude range check shows values near zero across all samples

**Possible Mitigation:**
- CLAHE (contrast-limited adaptive histogram equalization) in preprocessing
- Adaptive thresholding before segmentation
- Lower segmentation threshold for low-confidence images
- Fallback model assist triggered more aggressively on low-contrast crops

**Synthetic Benchmark Simulation:**
Simulated via `apply_low_contrast(alpha=0.5, beta=40)` in `distortions.py`.
Alpha reduces dynamic range; beta shifts brightness toward mid-gray.

---

## Failure Mode 2: Rotation / Perspective Distortion

**Tags:** [CONCEPTUAL] [SYNTHETIC-SIMULATED]

**Description:**
The ECG sheet is rotated, skewed, or photographed at an angle, causing the
horizontal time axis of each lead to be misaligned with the image x-axis.

**Likely Cause:**
- Handheld photograph of a printed ECG sheet
- Scanner misalignment
- Document fed at an angle into a flatbed scanner
- Perspective distortion from a non-orthogonal camera angle

**Expected Reconstruction Impact:**
- YOLO lead detection may miss leads or produce incorrect crop boundaries
- Segmentation within a rotated crop assigns probability to the correct trace,
  but the Viterbi path follows the image x-axis — introducing systematic
  waveform distortion
- Time-axis compression or stretching if the rotation is asymmetric
- Einthoven relations may appear violated even when underlying signal is correct

**Detection Signal:**
- Unusual lead crop aspect ratios from the detector
- Asymmetric probability maps in the segmentation output
- Per-lead amplitude inconsistency across Einthoven leads (I, II, III)

**Possible Mitigation:**
- Pre-processing rotation correction using Hough line detection on grid lines
- Deskewing step before lead detection
- Perspective transform correction using detected corner points

**Synthetic Benchmark Simulation:**
Simulated via `apply_rotation(angle_deg=5.0)` in `distortions.py`.
Small angles (2–10°) are representative of real scan misalignment.

---

## Failure Mode 3: Blur

**Tags:** [CONCEPTUAL] [SYNTHETIC-SIMULATED]

**Description:**
The ECG image is blurred due to motion, out-of-focus photography, or
compression artifacts, causing the sharp ECG trace edges to spread into
the surrounding background.

**Likely Cause:**
- Camera shake during handheld ECG photography
- Low-resolution scan followed by upsampling
- JPEG compression at high compression ratios
- Thermal fax transmission artifacts

**Expected Reconstruction Impact:**
- Trace edges spread, increasing segmentation uncertainty
- QRS complex peaks (which are sharp and narrow) are most affected —
  peak height may be underestimated
- Narrow P and Q waves may merge into the baseline
- Viterbi trace may follow the blurred centroid, systematically smoothing
  the waveform and reducing high-frequency content

**Detection Signal:**
- Segmentation probability map has wide, diffuse peaks rather than sharp ridges
- Reconstructed QRS amplitude lower than expected
- High-frequency content in the extracted signal is attenuated

**Possible Mitigation:**
- Unsharp masking or edge-enhancement preprocessing
- Training segmentation model on blurred augmentation examples
- Multi-scale TTA (already implemented) partially compensates for blur

**Synthetic Benchmark Simulation:**
Simulated via `apply_blur(sigma=2.0)` in `distortions.py`.
Gaussian blur with sigma 1.5–3.0 covers the typical range of real blur severity.

---

## Failure Mode 4: Cropped Sheet / Margin Loss

**Tags:** [CONCEPTUAL] [SYNTHETIC-SIMULATED]

**Description:**
Part of the ECG sheet is outside the image frame, causing one or more leads
to be partially or fully absent from the image.

**Likely Cause:**
- Photograph taken without full sheet coverage
- Scanner bed smaller than the ECG form
- Binding margin in a medical record folder blocking part of the sheet
- ECG printout trimmed before scanning

**Expected Reconstruction Impact:**
- YOLO detector may fail to detect leads that are fully outside the crop
- Partially visible leads produce truncated waveforms
- Missing leads default to all-zero output in the submission
- Einthoven consistency checks may fail due to incomplete lead set

**Detection Signal:**
- Fewer than 12 leads detected by YOLO
- Detected lead bounding boxes close to the image boundary
- QC: lead count check reports fewer than 12 leads

**Possible Mitigation:**
- Image boundary padding before detection
- Confidence-weighted lead presence check
- Explicit flagging of missing leads in output metadata

**Synthetic Benchmark Simulation:**
Simulated via `apply_cropped(margin_frac=0.08)` in `distortions.py`.
Random margin trimming of up to 8% per edge.

---

## Failure Mode 5: Grid Weakness / Absence

**Tags:** [CONCEPTUAL]

**Description:**
The ECG paper grid is faint, absent, or has been digitally removed, making
grid-based calibration unreliable or impossible.

**Likely Cause:**
- Non-standard ECG paper without standard 1mm/5mm grid
- Grid removal applied as a preprocessing step by an upstream system
- Very faint thermal print with grid invisible at scan resolution
- Digital ECG screenshot without a rendered grid

**Expected Reconstruction Impact:**
- `estimate_grid_spacing_px` returns None or an incorrect estimate
- `choose_ppmv` falls back to a default pixels-per-millivolt value
- Amplitude calibration is incorrect — all leads scaled by the wrong factor
- Waveform amplitudes may be systematically too large or too small
- Timing normalization may also be affected if pixels-per-second estimation uses grid

**Detection Signal:**
- `estimate_grid_spacing_px` returns None or a very low confidence value
- QC: amplitude range check flags values far outside ±5 mV for a sinus rhythm

**Possible Mitigation:**
- Fallback to a configurable default calibration value
- Alternative calibration from known reference pulses on ECG paper
- Preprocessing grid detection with explicit confidence scoring

**Synthetic Benchmark Simulation:**
Partial — current synthetic render includes a grid; a grid-absent variant
could be added in a future benchmark iteration.

---

## Failure Mode 6: Overlapping Leads

**Tags:** [CONCEPTUAL]

**Description:**
Two or more lead strips are printed so close together or overlap in the image
that their waveforms intersect, causing the segmentation model to include
signal pixels from an adjacent lead.

**Likely Cause:**
- Unusual ECG printer layout with compressed vertical spacing
- High heart rate leading to tall QRS complexes that extend across lead rows
- Partial page crop causing two leads to appear in the same YOLO crop

**Expected Reconstruction Impact:**
- Segmentation probability map has two distinct ridges in a single crop
- Viterbi trace may jump between the two leads, producing a corrupted waveform
- Amplitude estimates are invalid for the mixed-lead signal

**Detection Signal:**
- Bimodal probability map in the y-axis (two parallel ridges)
- Viterbi trace with unusually high variance in y-position
- Einthoven relation violated for the affected leads

**Possible Mitigation:**
- YOLO lead detection with tighter crop boundaries
- Multi-peak detection in the segmentation output as a lead separation signal
- Post-detection validation of expected lead layout

**Synthetic Benchmark Simulation:**
Not yet implemented in the current seed. A future iteration could render
two leads in a single crop with overlapping amplitudes.

---

## Failure Mode 7: Flatline / All-Zero Extraction

**Tags:** [CONCEPTUAL] [DETECTABLE-VIA-QC]

**Description:**
The pipeline produces an all-zero or near-flatline signal for one or more leads,
even when the source image contains a visible waveform.

**Likely Cause:**
- Segmentation threshold set too high, rejecting all trace pixels
- Lead crop entirely outside the image (see Failure Mode 4)
- Grid-suppression preprocessing too aggressive, removing the trace itself
- Segmentation model produces very low probability everywhere on this crop
- YOLO crop bounding box captures only background or grid, not the actual trace

**Expected Reconstruction Impact:**
- Output is zero for all or most time points in the affected lead
- Submission CSV contains zeros for that lead's `id,value` pairs
- Einthoven relation violated if I or II is the affected lead

**Detection Signal:**
- QC: `check_all_zero` flags the lead
- QC: `check_flatline` flags near-zero variance
- Systematic pattern: same lead fails across multiple patients suggests
  a detector or layout issue, not a per-image issue

**Possible Mitigation:**
- Lower segmentation threshold or softer thresholding strategy
- Skeleton boost (already implemented) to reinforce thin traces
- Fallback model assist on all crops, not only low-confidence crops
- Detection of all-zero leads at runtime with explicit logging

**Synthetic Benchmark Simulation:**
Directly detectable by QC tooling. Can be introduced artificially by
zeroing a lead in the synthetic waveform CSV before scoring.

---

## Failure Mode 8: Calibration Ambiguity

**Tags:** [CONCEPTUAL]

**Description:**
The grid-spacing estimate is ambiguous — the image contains patterns
that could be interpreted as multiple valid grid spacings — leading to
an incorrect pixels-per-millivolt conversion factor.

**Likely Cause:**
- Image contains both 1mm minor grid and 5mm major grid with similar visual weight
- Scanner resolution causes aliasing between grid frequencies
- Non-standard paper with mixed grid spacings
- Handwritten annotations or sticker labels on the ECG grid

**Expected Reconstruction Impact:**
- All lead amplitudes are scaled by an incorrect constant factor
- Timing normalization may be affected if grid spacing is also used for
  pixels-per-second estimation
- The pattern is systematic across all leads for a given image — not random

**Detection Signal:**
- QC: amplitude range check shows all leads with amplitude uniformly too
  high or too low compared to expected sinus rhythm range
- Large deviation in Einthoven relation despite consistent sign pattern

**Possible Mitigation:**
- Multi-scale grid frequency detection to select the dominant grid period
- Sanity check on estimated pixels-per-millivolt against a prior distribution
- Explicit calibration confidence score in the pipeline output

**Synthetic Benchmark Simulation:**
Partial — the synthetic benchmark uses a fixed known grid spacing.
Calibration ambiguity could be tested by rendering images at different
effective grid spacings and scoring amplitude fidelity.

---

*This atlas is a living document. New failure modes should be added as they
are observed during evaluation on real ECG data or through controlled
synthetic experiments.*
