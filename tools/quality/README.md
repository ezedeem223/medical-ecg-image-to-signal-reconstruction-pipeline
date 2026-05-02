# Waveform Quality-Control Checks

This directory contains engineering QC tools for inspecting waveform arrays and
CSV outputs produced by the ECG digitization pipeline.

## Purpose

These checks support **research and engineering inspection only** — not clinical
validation. They detect common failure modes in reconstructed or synthetic waveform
data so researchers can identify issues early.

## What It Is Not

- Not a clinical diagnostic tool
- Not a replacement for medical-grade ECG quality assessment
- Not a safety-critical validator

## Files

| File | Purpose |
|------|---------|
| `checks.py` | Individual QC check functions with severity ratings |
| `generate_quality_report.py` | CLI to run all checks and produce a Markdown report |

## Quick Start

```bash
# Generate a QC report for a waveform CSV
python tools/quality/generate_quality_report.py \
    --input benchmark_cases/seed/waveforms/case_000.csv \
    --output reports/quality_report.md
```

## Checks Implemented

| Check | Severity | Description |
|-------|----------|-------------|
| `nan_inf` | ERROR | Detects NaN or Inf values |
| `all_zero` | ERROR | Detects all-zero leads |
| `flatline` | WARNING | Detects near-zero variance flatlines |
| `length_consistency` | WARNING | Checks all leads have same length |
| `amplitude_range` | WARNING | Flags extreme amplitudes outside ±10 mV |
| `lead_variance` | INFO | Reports per-lead variance |
| `lead_count` | INFO | Reports number of leads found |

## Report Format

The generated Markdown report includes:
- Summary table of all checks with pass/warn/fail status
- Per-lead detail where relevant
- Engineering disclaimer
