"""
Tests for tools/pipeline_compat/convert_submission_to_waveforms.py

Coverage:
- Refuses ambiguous or unparseable IDs
- Converts well-formed synthetic IDs correctly
- Never fabricates missing leads
- Skips cleanly when submission file is absent
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LEAD_NAMES = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]


def _import_convert():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.pipeline_compat.convert_submission_to_waveforms import convert
    return convert


def _write_submission(path: Path, rows: list[tuple[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "value"])
        for row_id, value in rows:
            writer.writerow([row_id, value])


def _make_well_formed_submission(path: Path, case_id: str = "case_000", n: int = 5) -> None:
    rows = []
    for lead in LEAD_NAMES:
        for i in range(n):
            rows.append((f"{case_id}_{i}_{lead}", f"{float(i) * 0.01:.4f}"))
    _write_submission(path, rows)


class TestConversionRefusal:
    def test_missing_submission_skips(self, tmp_path):
        convert = _import_convert()
        result = convert(
            tmp_path / "nonexistent.csv", None,
            tmp_path / "out", tmp_path / "report.md",
        )
        assert result["status"] == "SKIPPED"
        assert result.get("skip_reason") is not None

    def test_ambiguous_ids_skips(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        _write_submission(sub, [("foo", "1.0"), ("bar", "2.0"), ("baz", "3.0")])
        result = convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        assert result["status"] in ("SKIPPED", "SKIPPED_NO_VALID_CASES")
        assert result["converted_cases"] == []

    def test_empty_submission_skips(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        sub.write_text("id,value\n")
        result = convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        assert result["status"] == "SKIPPED"

    def test_wrong_columns_skips(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        sub.write_text("case,signal\ncase_000,1.0\n")
        result = convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        assert result["status"] == "SKIPPED"
        assert "skip_reason" in result

    def test_missing_leads_refused(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        rows = []
        for i in range(5):
            rows.append((f"case_000_{i}_I", f"{i * 0.1:.4f}"))
        _write_submission(sub, rows)
        result = convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        assert result["converted_cases"] == []
        assert result["failed_cases"] or result["status"] != "CONVERTED"

    def test_no_fabrication_on_partial_leads(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        rows = [(f"case_000_{i}_I", f"{i * 0.01:.4f}") for i in range(5)]
        _write_submission(sub, rows)
        result = convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        assert result["converted_cases"] == []


class TestConversionSuccess:
    def test_well_formed_submission_converts(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        _make_well_formed_submission(sub, "case_000", n=5)
        result = convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        assert result["status"] == "CONVERTED"
        assert len(result["converted_cases"]) == 1

    def test_converted_file_has_all_leads(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        _make_well_formed_submission(sub, "case_000", n=5)
        convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        out_file = tmp_path / "out" / "case_000_predicted.csv"
        assert out_file.exists()
        with open(out_file, newline="") as f:
            reader = csv.reader(f)
            next(reader)
            lead_col = [row[0] for row in reader]
        assert lead_col == LEAD_NAMES

    def test_converted_file_has_correct_n_samples(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        n = 7
        _make_well_formed_submission(sub, "case_000", n=n)
        convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        out_file = tmp_path / "out" / "case_000_predicted.csv"
        with open(out_file, newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = list(reader)
        assert len(header) == n + 1
        assert rows[0][0] == "I"

    def test_report_written(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        _make_well_formed_submission(sub)
        report_path = tmp_path / "report.md"
        convert(sub, None, tmp_path / "out", report_path)
        assert report_path.exists()
        text = report_path.read_text()
        assert "Waveform Conversion Report" in text

    def test_result_has_synthetic_true(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        _make_well_formed_submission(sub)
        result = convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        assert result["synthetic"] is True
        assert result["compatibility_only"] is True

    def test_multiple_cases(self, tmp_path):
        convert = _import_convert()
        sub = tmp_path / "sub.csv"
        rows = []
        for cid in ["case_000", "case_001"]:
            for lead in LEAD_NAMES:
                for i in range(5):
                    rows.append((f"{cid}_{i}_{lead}", f"{i * 0.01:.4f}"))
        _write_submission(sub, rows)
        result = convert(sub, None, tmp_path / "out", tmp_path / "report.md")
        assert result["status"] == "CONVERTED"
        assert len(result["converted_cases"]) == 2
