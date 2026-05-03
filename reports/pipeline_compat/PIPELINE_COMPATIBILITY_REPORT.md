# ECG Pipeline Compatibility Report

**Generated:** 2026-05-03T05:47:04.410847+00:00
**Label:** `SYNTHETIC_COMPATIBILITY_ONLY`

> **Disclaimer:** This is a synthetic compatibility and engineering smoke-test report only. It does not establish clinical validity, real ECG reconstruction accuracy, or diagnostic performance.

---

## 1. Asset Readiness

**Can run full pipeline:** ❌ NO

**Missing assets:**
- Missing directory: data/images (input ECG page images)
- Missing file: data/test.csv (test manifest (id column, optional fs column))
- Missing file: data/sample_submission.parquet (submission template (id column, expected row order))

## 2. Input Compatibility

- Synthetic fixture cases prepared: **3**
- Submission template format: **csv_fallback**
- ⚠️  Parquet support unavailable (pandas/pyarrow not installed). CSV fallback generated. Full pipeline smoke test cannot run until parquet support exists or the runtime config is adapted.

## 3. Runtime Execution

**Smoke test status:** `SKIPPED_ASSETS_MISSING`
- ⏭️  Missing directory: data/images (input ECG page images)
- ⏭️  Missing file: data/test.csv (test manifest (id column, optional fs column))
- ⏭️  Missing file: data/sample_submission.parquet (submission template (id column, expected row order))

## 4. Output Validation

No output files generated.

## 5. Synthetic Scoring

_Synthetic score not available. Run score_synthetic.py on any predicted waveforms._

## 6. QC Inspection

_Run `tools/quality/generate_quality_report.py` on waveform CSVs for QC results._

## 7. Limitations

- All results are based on parametric synthetic waveforms — not real ECG recordings.
- Synthetic images may not match the spatial layout expected by the YOLO detector.
- Submission ID format must align exactly with the runtime template parser.
- Even a passing smoke test does not validate clinical or reconstruction accuracy.
- No published benchmark performance is claimed or implied.

## 8. Next Steps

- If assets are missing: obtain model checkpoints and real input data before retesting.
- If fixture format is incompatible: install pandas + pyarrow for parquet support.
- If smoke test fails: review `stderr_summary` in the smoke summary JSON.
- If smoke test passes: run `convert_submission_to_waveforms.py` then `score_synthetic.py`.
- Do not merge this branch to main until the full compatibility pass is reviewed.

---

> **Full disclaimer:** This is a synthetic compatibility and engineering smoke-test report only. It does not establish clinical validity, real ECG reconstruction accuracy, or diagnostic performance. All synthetic data is labeled SYNTHETIC_COMPATIBILITY_ONLY.


<!-- WARNING: Report may contain restricted phrase: diagnostic performance -->


<!-- WARNING: Report may contain restricted phrase: published benchmark -->
