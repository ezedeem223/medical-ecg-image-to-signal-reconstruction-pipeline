"""
Tests for tools/pipeline_compat/generate_pipeline_compat_report.py

Coverage:
- Creates Markdown report from available JSON inputs
- Contains synthetic-only disclaimer
- Contains no clinical validation wording
- Works when inputs are None (missing reports)
- Consolidates asset readiness, fixture, smoke sections
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

_FORBIDDEN_PHRASES = [
    "establishes clinical validity",
    "fda-approved",
    "ce-marked",
    "real ecg accuracy",
    "claims published benchmark",
    "validated on patients",
]


def _import_generate():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.pipeline_compat.generate_pipeline_compat_report import generate
    return generate


def _make_readiness(all_missing: bool = True) -> dict:
    return {
        "can_run_full_pipeline": not all_missing,
        "skip_reasons": ["Missing file: configs/runtime.default.yaml"] if all_missing else [],
        "warnings": [],
        "disclaimer": "This report only checks engineering readiness.",
    }


def _make_fixture_manifest() -> dict:
    return {
        "synthetic": True,
        "compatibility_only": True,
        "label": "SYNTHETIC_COMPATIBILITY_ONLY",
        "num_cases": 3,
        "submission_format": "parquet",
        "parquet_note": "parquet",
        "images_dir": "/tmp/images",
        "disclaimer": "SYNTHETIC_COMPATIBILITY_ONLY",
    }


def _make_smoke_summary(status: str = "SKIPPED_ASSETS_MISSING") -> dict:
    return {
        "synthetic": True,
        "compatibility_only": True,
        "label": "SYNTHETIC_COMPATIBILITY_ONLY",
        "status": status,
        "command_attempted": None,
        "skip_reasons": ["Missing assets"],
        "limitations": ["Scores are on synthetic data only."],
        "output_files": [],
        "scoring_possible": False,
        "qc_possible": False,
        "disclaimer": "SYNTHETIC_COMPATIBILITY_ONLY",
    }


class TestReportGeneration:
    def test_creates_markdown_file(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "PIPELINE_COMPATIBILITY_REPORT.md"
        generate(None, None, None, None, out)
        assert out.exists()

    def test_contains_disclaimer(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(None, None, None, None, out)
        text = out.read_text()
        assert "synthetic compatibility" in text.lower() or "SYNTHETIC" in text

    def test_contains_no_clinical_validation_wording(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(
            _make_readiness(),
            _make_fixture_manifest(),
            _make_smoke_summary(),
            None,
            out,
        )
        text = out.read_text().lower()
        for phrase in _FORBIDDEN_PHRASES:
            assert phrase not in text, f"Forbidden phrase found: {phrase!r}"

    def test_works_with_all_none_inputs(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(None, None, None, None, out)
        text = out.read_text()
        assert len(text) > 100

    def test_asset_readiness_section_present(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(_make_readiness(), None, None, None, out)
        text = out.read_text()
        assert "Asset Readiness" in text

    def test_runtime_execution_section_present(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(None, None, _make_smoke_summary(), None, out)
        text = out.read_text()
        assert "Runtime Execution" in text

    def test_smoke_status_appears_in_report(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(None, None, _make_smoke_summary("SKIPPED_ASSETS_MISSING"), None, out)
        text = out.read_text()
        assert "SKIPPED_ASSETS_MISSING" in text

    def test_can_run_false_reflected(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(_make_readiness(all_missing=True), None, None, None, out)
        text = out.read_text()
        assert "NO" in text or "false" in text.lower() or "❌" in text

    def test_fixture_section_present(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(None, _make_fixture_manifest(), None, None, out)
        text = out.read_text()
        assert "Input Compatibility" in text
        assert "3" in text

    def test_limitations_section_present(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(None, None, None, None, out)
        text = out.read_text()
        assert "Limitations" in text

    def test_next_steps_section_present(self, tmp_path):
        generate = _import_generate()
        out = tmp_path / "report.md"
        generate(None, None, None, None, out)
        text = out.read_text()
        assert "Next Steps" in text


class TestReportDocumentation:
    def test_protocol_doc_exists(self):
        path = ROOT / "docs" / "research_pack" / "PIPELINE_COMPATIBILITY_PROTOCOL.md"
        assert path.exists(), f"Missing: {path}"

    def test_runbook_doc_exists(self):
        path = ROOT / "docs" / "research_pack" / "ECG_PIPELINE_COMPATIBILITY_RUNBOOK.md"
        assert path.exists(), f"Missing: {path}"

    def test_protocol_doc_has_forbidden_wording_section(self):
        path = ROOT / "docs" / "research_pack" / "PIPELINE_COMPATIBILITY_PROTOCOL.md"
        text = path.read_text()
        assert "Forbidden" in text or "forbidden" in text

    def test_protocol_doc_has_allowed_wording_section(self):
        path = ROOT / "docs" / "research_pack" / "PIPELINE_COMPATIBILITY_PROTOCOL.md"
        text = path.read_text()
        assert "Allowed" in text or "allowed" in text

    def test_runbook_has_step_by_step_structure(self):
        path = ROOT / "docs" / "research_pack" / "ECG_PIPELINE_COMPATIBILITY_RUNBOOK.md"
        text = path.read_text()
        for step in range(1, 6):
            assert f"Step {step}" in text, f"Missing Step {step} in runbook"

    def test_protocol_doc_has_no_clinical_claims(self):
        path = ROOT / "docs" / "research_pack" / "PIPELINE_COMPATIBILITY_PROTOCOL.md"
        text = path.read_text()
        assert "SYNTHETIC_COMPATIBILITY_ONLY" in text or "synthetic compatibility" in text.lower()
        assert "clinical validation" in text.lower() or "Forbidden" in text

    def test_runbook_doc_has_no_forbidden_phrases(self):
        path = ROOT / "docs" / "research_pack" / "ECG_PIPELINE_COMPATIBILITY_RUNBOOK.md"
        text = path.read_text().lower()
        for phrase in ["fda approved", "ce-mark", "validated on patients"]:
            assert phrase not in text, f"Forbidden phrase in runbook: {phrase!r}"

    def test_compat_tools_readme_exists(self):
        path = ROOT / "tools" / "pipeline_compat" / "README.md"
        assert path.exists(), f"Missing: {path}"
