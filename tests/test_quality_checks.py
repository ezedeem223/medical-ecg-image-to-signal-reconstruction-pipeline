"""
Tests for the waveform quality-control checks module.

All tests use toy arrays — no real ECG data or model weights required.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.quality.checks import (  # noqa: E402
    SEVERITY_ERROR,
    SEVERITY_INFO,
    SEVERITY_OK,
    SEVERITY_WARNING,
    CheckResult,
    check_all_zero,
    check_amplitude_range,
    check_flatline,
    check_lead_count,
    check_lead_variance,
    check_length_consistency,
    check_nan_inf,
    overall_severity,
    run_all_checks,
)

LEAD_NAMES = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]


def _clean_leads(n_samples: int = 200) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(42)
    return {
        lead: (rng.standard_normal(n_samples) * 0.5).astype(np.float32)
        for lead in LEAD_NAMES
    }


class TestCheckNanInf:
    def test_clean_signal_passes(self):
        leads = _clean_leads()
        result = check_nan_inf(leads)
        assert result.passed is True
        assert result.severity == SEVERITY_OK

    def test_nan_detected(self):
        leads = _clean_leads()
        leads["I"] = np.array([float("nan"), 1.0, 2.0], dtype=np.float32)
        result = check_nan_inf(leads)
        assert result.passed is False
        assert result.severity == SEVERITY_ERROR
        assert "I" in result.message

    def test_inf_detected(self):
        leads = _clean_leads()
        leads["V1"] = np.array([float("inf"), 0.0], dtype=np.float32)
        result = check_nan_inf(leads)
        assert result.passed is False
        assert result.severity == SEVERITY_ERROR

    def test_multiple_affected_leads(self):
        leads = _clean_leads()
        leads["I"] = np.full(10, float("nan"), dtype=np.float32)
        leads["II"] = np.full(10, float("inf"), dtype=np.float32)
        result = check_nan_inf(leads)
        assert result.passed is False
        assert len(result.detail["affected_leads"]) == 2


class TestCheckAllZero:
    def test_clean_signal_passes(self):
        leads = _clean_leads()
        result = check_all_zero(leads)
        assert result.passed is True
        assert result.severity == SEVERITY_OK

    def test_all_zero_detected(self):
        leads = _clean_leads()
        leads["III"] = np.zeros(100, dtype=np.float32)
        result = check_all_zero(leads)
        assert result.passed is False
        assert result.severity == SEVERITY_ERROR
        assert "III" in result.detail["zero_leads"]

    def test_near_zero_not_flagged(self):
        leads = _clean_leads()
        leads["aVF"] = np.full(100, 1e-5, dtype=np.float32)
        result = check_all_zero(leads)
        assert result.passed is True


class TestCheckFlatline:
    def test_clean_signal_passes(self):
        leads = _clean_leads()
        result = check_flatline(leads)
        assert result.passed is True

    def test_constant_signal_flagged(self):
        leads = _clean_leads()
        leads["V2"] = np.full(100, 0.5, dtype=np.float32)
        result = check_flatline(leads)
        assert result.passed is False
        assert result.severity == SEVERITY_WARNING
        assert "V2" in result.detail["flatline_leads_variance"]

    def test_all_zero_not_double_flagged(self):
        leads = {"I": np.zeros(50, dtype=np.float32)}
        result = check_flatline(leads)
        assert result.passed is True


class TestCheckLengthConsistency:
    def test_consistent_passes(self):
        leads = {k: np.zeros(100, dtype=np.float32) for k in LEAD_NAMES}
        result = check_length_consistency(leads)
        assert result.passed is True
        assert result.severity == SEVERITY_OK

    def test_inconsistent_flagged(self):
        leads = {
            "I": np.zeros(100, dtype=np.float32),
            "II": np.zeros(90, dtype=np.float32),
        }
        result = check_length_consistency(leads)
        assert result.passed is False
        assert result.severity == SEVERITY_WARNING

    def test_empty_leads_flagged(self):
        result = check_length_consistency({})
        assert result.passed is False


class TestCheckAmplitudeRange:
    def test_in_range_passes(self):
        leads = {k: np.zeros(50, dtype=np.float32) for k in ["I", "II"]}
        result = check_amplitude_range(leads)
        assert result.passed is True

    def test_extreme_positive_flagged(self):
        leads = {"I": np.full(50, 15.0, dtype=np.float32)}
        result = check_amplitude_range(leads)
        assert result.passed is False
        assert "I" in result.detail["out_of_range_leads"]

    def test_extreme_negative_flagged(self):
        leads = {"II": np.full(50, -12.0, dtype=np.float32)}
        result = check_amplitude_range(leads)
        assert result.passed is False


class TestCheckLeadVariance:
    def test_returns_info(self):
        leads = _clean_leads()
        result = check_lead_variance(leads)
        assert result.severity == SEVERITY_INFO
        assert result.passed is True
        assert "per_lead_variance" in result.detail

    def test_all_leads_in_detail(self):
        leads = _clean_leads()
        result = check_lead_variance(leads)
        for lead in LEAD_NAMES:
            assert lead in result.detail["per_lead_variance"]


class TestCheckLeadCount:
    def test_12_leads_passes(self):
        leads = {k: np.zeros(10) for k in LEAD_NAMES}
        result = check_lead_count(leads)
        assert result.passed is True

    def test_fewer_leads_warning(self):
        leads = {"I": np.zeros(10), "II": np.zeros(10)}
        result = check_lead_count(leads)
        assert result.passed is False
        assert result.severity == SEVERITY_WARNING

    def test_zero_leads_error(self):
        result = check_lead_count({})
        assert result.passed is False
        assert result.severity == SEVERITY_ERROR


class TestOverallSeverity:
    def test_all_ok_returns_ok(self):
        results = [
            CheckResult("a", SEVERITY_OK, True, "ok"),
            CheckResult("b", SEVERITY_OK, True, "ok"),
        ]
        assert overall_severity(results) == SEVERITY_OK

    def test_single_error_dominates(self):
        results = [
            CheckResult("a", SEVERITY_OK, True, "ok"),
            CheckResult("b", SEVERITY_WARNING, False, "warn"),
            CheckResult("c", SEVERITY_ERROR, False, "err"),
        ]
        assert overall_severity(results) == SEVERITY_ERROR

    def test_empty_returns_ok(self):
        assert overall_severity([]) == SEVERITY_OK


class TestRunAllChecks:
    def test_clean_leads_all_pass(self):
        leads = _clean_leads()
        results = run_all_checks(leads)
        errors = [r for r in results if r.severity == SEVERITY_ERROR]
        assert len(errors) == 0

    def test_nan_lead_causes_error(self):
        leads = _clean_leads()
        leads["I"] = np.full(100, float("nan"), dtype=np.float32)
        results = run_all_checks(leads)
        errors = [r for r in results if r.severity == SEVERITY_ERROR]
        assert len(errors) >= 1

    def test_all_zero_causes_error(self):
        leads = {k: np.zeros(50, dtype=np.float32) for k in LEAD_NAMES}
        results = run_all_checks(leads)
        names = [r.name for r in results if r.severity == SEVERITY_ERROR]
        assert "all_zero" in names

    def test_returns_seven_checks(self):
        leads = _clean_leads()
        results = run_all_checks(leads)
        assert len(results) == 7


class TestQualityReportCLI:
    def test_cli_generates_report(self, tmp_path):
        import csv
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.quality.generate_quality_report import main

        csv_path = tmp_path / "wave.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["lead_name"] + list(range(100)))
            for lead in LEAD_NAMES:
                row = [lead] + ["0.1"] * 100
                writer.writerow(row)

        report_path = tmp_path / "report.md"
        ret = main(["--input", str(csv_path), "--output", str(report_path)])
        assert ret == 0
        assert report_path.exists()
        content = report_path.read_text()
        assert "DISCLAIMER" in content
        assert "quality" in content.lower() or "QC" in content or "Check" in content
