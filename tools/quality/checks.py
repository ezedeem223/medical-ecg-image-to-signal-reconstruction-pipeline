"""
Basic quality-control checks for waveform arrays or CSV-like outputs.

These checks are designed for engineering and research inspection support only.
They are NOT clinical validation tools and must not be used for diagnostic purposes.

Each check returns a CheckResult with:
  - name: check identifier
  - severity: "ok", "info", "warning", or "error"
  - passed: bool
  - message: human-readable description
  - detail: optional dict with per-lead or per-check detail
"""
from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np


SEVERITY_OK = "ok"
SEVERITY_INFO = "info"
SEVERITY_WARNING = "warning"
SEVERITY_ERROR = "error"

SEVERITY_ORDER = {SEVERITY_OK: 0, SEVERITY_INFO: 1, SEVERITY_WARNING: 2, SEVERITY_ERROR: 3}

ENGINEERING_DISCLAIMER = (
    "These QC checks are for engineering and research inspection only. "
    "They do not constitute clinical ECG quality assessment or validation."
)


@dataclass
class CheckResult:
    name: str
    severity: str
    passed: bool
    message: str
    detail: dict[str, Any] = field(default_factory=dict)

    @property
    def severity_rank(self) -> int:
        return SEVERITY_ORDER.get(self.severity, 0)


def load_waveform_csv(path: Path) -> tuple[dict[str, np.ndarray], list[str]]:
    leads: dict[str, np.ndarray] = {}
    warnings_list: list[str] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            warnings_list.append("CSV file is empty.")
            return leads, warnings_list
        for row in reader:
            if not row:
                continue
            lead_name = row[0].strip()
            try:
                values = np.array([float(v) for v in row[1:]], dtype=np.float32)
                leads[lead_name] = values
            except ValueError as exc:
                warnings_list.append(f"Could not parse lead {lead_name!r}: {exc}")
    return leads, warnings_list


def check_nan_inf(leads: dict[str, np.ndarray]) -> CheckResult:
    affected: dict[str, dict[str, int]] = {}
    for name, signal in leads.items():
        n_nan = int(np.sum(np.isnan(signal)))
        n_inf = int(np.sum(np.isinf(signal)))
        if n_nan > 0 or n_inf > 0:
            affected[name] = {"nan_count": n_nan, "inf_count": n_inf}
    if affected:
        return CheckResult(
            name="nan_inf",
            severity=SEVERITY_ERROR,
            passed=False,
            message=f"NaN or Inf values detected in {len(affected)} lead(s): {sorted(affected)}",
            detail={"affected_leads": affected},
        )
    return CheckResult(
        name="nan_inf",
        severity=SEVERITY_OK,
        passed=True,
        message="No NaN or Inf values detected.",
    )


def check_all_zero(leads: dict[str, np.ndarray]) -> CheckResult:
    zero_leads: list[str] = []
    for name, signal in leads.items():
        if np.all(signal == 0.0):
            zero_leads.append(name)
    if zero_leads:
        return CheckResult(
            name="all_zero",
            severity=SEVERITY_ERROR,
            passed=False,
            message=f"All-zero signal detected in {len(zero_leads)} lead(s): {zero_leads}",
            detail={"zero_leads": zero_leads},
        )
    return CheckResult(
        name="all_zero",
        severity=SEVERITY_OK,
        passed=True,
        message="No all-zero signals detected.",
    )


def check_flatline(
    leads: dict[str, np.ndarray], *, variance_threshold: float = 1e-6
) -> CheckResult:
    flatline_leads: dict[str, float] = {}
    for name, signal in leads.items():
        if np.all(signal == 0.0):
            continue
        variance = float(np.var(signal))
        if variance < variance_threshold:
            flatline_leads[name] = round(variance, 10)
    if flatline_leads:
        return CheckResult(
            name="flatline",
            severity=SEVERITY_WARNING,
            passed=False,
            message=(
                f"Near-flatline (variance < {variance_threshold}) in "
                f"{len(flatline_leads)} lead(s): {sorted(flatline_leads)}"
            ),
            detail={"flatline_leads_variance": flatline_leads},
        )
    return CheckResult(
        name="flatline",
        severity=SEVERITY_OK,
        passed=True,
        message="No flatline signals detected.",
    )


def check_length_consistency(leads: dict[str, np.ndarray]) -> CheckResult:
    if not leads:
        return CheckResult(
            name="length_consistency",
            severity=SEVERITY_WARNING,
            passed=False,
            message="No leads found.",
        )
    lengths = {name: len(signal) for name, signal in leads.items()}
    unique_lengths = set(lengths.values())
    if len(unique_lengths) > 1:
        return CheckResult(
            name="length_consistency",
            severity=SEVERITY_WARNING,
            passed=False,
            message=f"Inconsistent lead lengths detected: {sorted(unique_lengths)}",
            detail={"per_lead_lengths": lengths},
        )
    return CheckResult(
        name="length_consistency",
        severity=SEVERITY_OK,
        passed=True,
        message=f"All {len(leads)} leads have consistent length: {next(iter(unique_lengths))}",
        detail={"length": next(iter(unique_lengths))},
    )


def check_amplitude_range(
    leads: dict[str, np.ndarray],
    *,
    min_mv: float = -10.0,
    max_mv: float = 10.0,
) -> CheckResult:
    out_of_range: dict[str, dict[str, float]] = {}
    for name, signal in leads.items():
        finite = signal[np.isfinite(signal)]
        if len(finite) == 0:
            continue
        sig_min = float(finite.min())
        sig_max = float(finite.max())
        if sig_min < min_mv or sig_max > max_mv:
            out_of_range[name] = {"min": round(sig_min, 4), "max": round(sig_max, 4)}
    if out_of_range:
        return CheckResult(
            name="amplitude_range",
            severity=SEVERITY_WARNING,
            passed=False,
            message=(
                f"Amplitude outside [{min_mv}, {max_mv}] mV in "
                f"{len(out_of_range)} lead(s): {sorted(out_of_range)}"
            ),
            detail={"out_of_range_leads": out_of_range, "expected_range_mv": [min_mv, max_mv]},
        )
    return CheckResult(
        name="amplitude_range",
        severity=SEVERITY_OK,
        passed=True,
        message=f"All lead amplitudes within [{min_mv}, {max_mv}] mV.",
    )


def check_lead_variance(leads: dict[str, np.ndarray]) -> CheckResult:
    per_lead: dict[str, float] = {}
    for name, signal in leads.items():
        finite = signal[np.isfinite(signal)]
        per_lead[name] = round(float(np.var(finite)) if len(finite) > 0 else 0.0, 8)
    return CheckResult(
        name="lead_variance",
        severity=SEVERITY_INFO,
        passed=True,
        message=f"Per-lead variance computed for {len(per_lead)} leads.",
        detail={"per_lead_variance": per_lead},
    )


def check_lead_count(leads: dict[str, np.ndarray], *, expected: int = 12) -> CheckResult:
    n = len(leads)
    if n == expected:
        return CheckResult(
            name="lead_count",
            severity=SEVERITY_OK,
            passed=True,
            message=f"Lead count matches expected: {n}/{expected}.",
            detail={"found": n, "expected": expected, "lead_names": sorted(leads)},
        )
    sev = SEVERITY_WARNING if n > 0 else SEVERITY_ERROR
    return CheckResult(
        name="lead_count",
        severity=sev,
        passed=False,
        message=f"Lead count mismatch: found {n}, expected {expected}.",
        detail={"found": n, "expected": expected, "lead_names": sorted(leads)},
    )


def run_all_checks(leads: dict[str, np.ndarray]) -> list[CheckResult]:
    return [
        check_nan_inf(leads),
        check_all_zero(leads),
        check_flatline(leads),
        check_length_consistency(leads),
        check_amplitude_range(leads),
        check_lead_variance(leads),
        check_lead_count(leads),
    ]


def overall_severity(results: list[CheckResult]) -> str:
    if not results:
        return SEVERITY_OK
    return max(results, key=lambda r: r.severity_rank).severity
