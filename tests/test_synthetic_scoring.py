"""
Tests for the synthetic-only waveform scoring utility.

All tests use toy arrays — no real ECG data or model weights required.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.synthetic_benchmark.score_synthetic import (  # noqa: E402
    SYNTHETIC_DISCLAIMER,
    compute_mae,
    compute_rmse,
    compute_snr_proxy,
    load_waveform_csv,
    score_waveforms,
)


LEAD_NAMES = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]


def _toy_leads(n_samples: int = 100, n_leads: int = 12) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(0)
    return {
        LEAD_NAMES[i]: rng.standard_normal(n_samples).astype(np.float32)
        for i in range(n_leads)
    }


class TestComputeMAE:
    def test_identical_signals_zero(self):
        sig = np.array([1.0, 2.0, 3.0], dtype=np.float32)
        assert compute_mae(sig, sig) == pytest.approx(0.0)

    def test_constant_offset(self):
        gt = np.zeros(100, dtype=np.float32)
        pred = np.ones(100, dtype=np.float32)
        assert compute_mae(gt, pred) == pytest.approx(1.0)

    def test_length_mismatch_truncates(self):
        gt = np.ones(100, dtype=np.float32)
        pred = np.ones(80, dtype=np.float32)
        result = compute_mae(gt, pred)
        assert np.isfinite(result)


class TestComputeRMSE:
    def test_identical_signals_zero(self):
        sig = np.ones(50, dtype=np.float32)
        assert compute_rmse(sig, sig) == pytest.approx(0.0)

    def test_greater_than_mae_for_mixed_errors(self):
        gt = np.zeros(4, dtype=np.float32)
        pred = np.array([1.0, 0.0, 0.0, 3.0], dtype=np.float32)
        mae = compute_mae(gt, pred)
        rmse = compute_rmse(gt, pred)
        assert rmse >= mae


class TestComputeSnrProxy:
    def test_identical_signals_infinite(self):
        sig = np.sin(np.linspace(0, np.pi, 100)).astype(np.float32)
        result = compute_snr_proxy(sig, sig)
        assert result == float("inf") or result is None or result > 100.0

    def test_zero_signal_returns_none(self):
        gt = np.zeros(50, dtype=np.float32)
        pred = np.ones(50, dtype=np.float32)
        result = compute_snr_proxy(gt, pred)
        assert result is None

    def test_noisy_signal_positive(self):
        rng = np.random.default_rng(0)
        gt = np.sin(np.linspace(0, 4 * np.pi, 500)).astype(np.float32)
        pred = gt + rng.normal(0, 0.01, 500).astype(np.float32)
        result = compute_snr_proxy(gt, pred)
        assert result is not None and result > 0.0


class TestScoreWaveforms:
    def test_self_score_mae_zero(self):
        leads = _toy_leads()
        result = score_waveforms(leads, leads)
        assert result["aggregate"]["mean_mae"] == pytest.approx(0.0, abs=1e-6)

    def test_self_score_rmse_zero(self):
        leads = _toy_leads()
        result = score_waveforms(leads, leads)
        assert result["aggregate"]["mean_rmse"] == pytest.approx(0.0, abs=1e-6)

    def test_result_is_synthetic_labeled(self):
        leads = _toy_leads()
        result = score_waveforms(leads, leads)
        assert result["synthetic"] is True
        assert SYNTHETIC_DISCLAIMER in result["disclaimer"]

    def test_all_12_leads_scored(self):
        leads = _toy_leads()
        result = score_waveforms(leads, leads)
        assert result["aggregate"]["num_leads_scored"] == 12

    def test_per_lead_present(self):
        leads = _toy_leads()
        result = score_waveforms(leads, leads)
        for lead in LEAD_NAMES:
            assert lead in result["per_lead"]

    def test_missing_lead_detected(self):
        gt = _toy_leads()
        pred = {k: v for k, v in gt.items() if k != "V6"}
        result = score_waveforms(gt, pred)
        assert "V6" in result["missing_leads"]["in_prediction"]

    def test_noisy_prediction_higher_error(self):
        rng = np.random.default_rng(1)
        gt = _toy_leads()
        pred = {k: v + rng.normal(0, 0.1, len(v)).astype(np.float32) for k, v in gt.items()}
        result = score_waveforms(gt, pred)
        assert result["aggregate"]["mean_mae"] > 0.0

    def test_score_on_toy_csv(self, tmp_path):
        import csv
        leads = _toy_leads(n_samples=50)
        csv_path = tmp_path / "test.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["lead_name"] + list(range(50)))
            for name, sig in leads.items():
                writer.writerow([name] + [f"{v:.6f}" for v in sig.tolist()])

        loaded = load_waveform_csv(csv_path)
        assert set(loaded.keys()) == set(leads.keys())
        for name in leads:
            np.testing.assert_allclose(loaded[name], leads[name], atol=1e-5)


class TestScoreSyntheticCLI:
    """End-to-end test for score_synthetic.main() called as a library function."""

    def _write_waveform_csv(self, path: Path, n_samples: int = 50) -> None:
        import csv as csv_mod
        lead_names = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]
        rng = np.random.default_rng(0)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv_mod.writer(f)
            writer.writerow(["lead_name"] + [str(i) for i in range(n_samples)])
            for name in lead_names:
                row = [name] + [f"{v:.6f}" for v in rng.standard_normal(n_samples).tolist()]
                writer.writerow(row)

    def test_cli_returns_zero_on_valid_inputs(self, tmp_path):
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.synthetic_benchmark.score_synthetic import main
        gt_path = tmp_path / "gt.csv"
        pred_path = tmp_path / "pred.csv"
        out_path = tmp_path / "score.json"
        self._write_waveform_csv(gt_path)
        self._write_waveform_csv(pred_path)
        rc = main(["--ground-truth", str(gt_path), "--prediction", str(pred_path), "--output", str(out_path)])
        assert rc == 0

    def test_cli_writes_output_json(self, tmp_path):
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.synthetic_benchmark.score_synthetic import main
        gt_path = tmp_path / "gt.csv"
        pred_path = tmp_path / "pred.csv"
        out_path = tmp_path / "score.json"
        self._write_waveform_csv(gt_path)
        self._write_waveform_csv(pred_path)
        main(["--ground-truth", str(gt_path), "--prediction", str(pred_path), "--output", str(out_path)])
        assert out_path.exists(), "Output JSON was not written"

    def test_cli_output_has_synthetic_flag_and_disclaimer(self, tmp_path):
        import json as json_mod
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.synthetic_benchmark.score_synthetic import main
        gt_path = tmp_path / "gt.csv"
        pred_path = tmp_path / "pred.csv"
        out_path = tmp_path / "score.json"
        self._write_waveform_csv(gt_path)
        self._write_waveform_csv(pred_path)
        main(["--ground-truth", str(gt_path), "--prediction", str(pred_path), "--output", str(out_path)])
        result = json_mod.loads(out_path.read_text(encoding="utf-8"))
        assert result.get("synthetic") is True
        assert "disclaimer" in result
        assert "synthetic" in result["disclaimer"].lower()

    def test_cli_output_has_aggregate_metrics(self, tmp_path):
        import json as json_mod
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.synthetic_benchmark.score_synthetic import main
        gt_path = tmp_path / "gt.csv"
        pred_path = tmp_path / "pred.csv"
        out_path = tmp_path / "score.json"
        self._write_waveform_csv(gt_path)
        self._write_waveform_csv(pred_path)
        main(["--ground-truth", str(gt_path), "--prediction", str(pred_path), "--output", str(out_path)])
        result = json_mod.loads(out_path.read_text(encoding="utf-8"))
        agg = result.get("aggregate", {})
        assert "mean_mae" in agg
        assert "mean_rmse" in agg
        assert "num_leads_scored" in agg

    def test_cli_returns_nonzero_on_missing_gt(self, tmp_path):
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.synthetic_benchmark.score_synthetic import main
        rc = main(["--ground-truth", str(tmp_path / "missing.csv"),
                   "--prediction", str(tmp_path / "pred.csv"),
                   "--output", str(tmp_path / "out.json")])
        assert rc != 0


class TestLoadWaveformCsv:
    def test_loads_all_leads(self, tmp_path):
        import csv
        path = tmp_path / "wave.csv"
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["lead_name", "0", "1", "2"])
            writer.writerow(["I", "0.1", "0.2", "0.3"])
            writer.writerow(["II", "0.4", "0.5", "0.6"])
        leads = load_waveform_csv(path)
        assert "I" in leads
        assert "II" in leads
        np.testing.assert_allclose(leads["I"], [0.1, 0.2, 0.3], atol=1e-5)

    def test_raises_on_non_numeric(self, tmp_path):
        import csv
        path = tmp_path / "bad.csv"
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["lead_name", "0", "1"])
            writer.writerow(["I", "abc", "def"])
        with pytest.raises(ValueError):
            load_waveform_csv(path)
