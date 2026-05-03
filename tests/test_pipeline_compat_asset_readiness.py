"""
Tests for tools/pipeline_compat/inspect_asset_readiness.py

Coverage:
- Missing files produce can_run_full_pipeline=false
- Report contains skip reasons
- No crash when files are absent
- JSON and Markdown reports are generated
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _import_inspect():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.pipeline_compat.inspect_asset_readiness import inspect
    return inspect


class TestAssetReadinessMissingFiles:
    def test_missing_all_returns_cannot_run(self, tmp_path):
        inspect = _import_inspect()
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        assert report["can_run_full_pipeline"] is False

    def test_missing_all_produces_skip_reasons(self, tmp_path):
        inspect = _import_inspect()
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        assert len(report["skip_reasons"]) > 0

    def test_skip_reasons_mention_missing_files(self, tmp_path):
        inspect = _import_inspect()
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        combined = " ".join(report["skip_reasons"])
        assert "configs/runtime.default.yaml" in combined or "Missing" in combined

    def test_no_crash_on_empty_root(self, tmp_path):
        inspect = _import_inspect()
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        assert "required_items" in report
        assert "checked_at_utc" in report

    def test_report_shape(self, tmp_path):
        inspect = _import_inspect()
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        required_keys = {
            "repository_root", "config_path", "models_registry_path",
            "checked_at_utc", "required_items", "can_run_full_pipeline",
            "skip_reasons", "warnings", "disclaimer",
        }
        assert required_keys <= set(report.keys())

    def test_disclaimer_present(self, tmp_path):
        inspect = _import_inspect()
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        assert "ECG reconstruction performance" in report["disclaimer"]
        assert "clinical utility" in report["disclaimer"]

    def test_required_items_all_have_path_kind_role_exists(self, tmp_path):
        inspect = _import_inspect()
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        for item in report["required_items"]:
            assert "path" in item
            assert "kind" in item
            assert "role" in item
            assert "exists" in item
            assert item["exists"] is False


class TestAssetReadinessPartialFiles:
    def test_one_existing_file_shows_exists_true(self, tmp_path):
        inspect = _import_inspect()
        (tmp_path / "configs").mkdir(parents=True)
        (tmp_path / "configs" / "runtime.default.yaml").write_text("paths:\n  data_root: data\n")
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        config_item = next(
            it for it in report["required_items"]
            if it["path"] == "configs/runtime.default.yaml"
        )
        assert config_item["exists"] is True
        assert "size_bytes" in config_item
        assert report["can_run_full_pipeline"] is False

    def test_empty_directory_produces_warning(self, tmp_path):
        inspect = _import_inspect()
        (tmp_path / "data" / "images").mkdir(parents=True)
        report = inspect(tmp_path, "configs/runtime.default.yaml")
        warnings_combined = " ".join(report["warnings"])
        assert "data/images" in warnings_combined or "empty" in warnings_combined.lower()


class TestAssetReadinessCLI:
    def test_cli_creates_json_report(self, tmp_path):
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.pipeline_compat.inspect_asset_readiness import main

        json_out = tmp_path / "asset_readiness_report.json"
        md_out = tmp_path / "asset_readiness_report.md"

        ret = main([
            "--root", str(tmp_path),
            "--output-json", str(json_out),
            "--output-md", str(md_out),
        ])
        assert ret == 0
        assert json_out.exists()
        report = json.loads(json_out.read_text())
        assert report["can_run_full_pipeline"] is False

    def test_cli_creates_md_report(self, tmp_path):
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.pipeline_compat.inspect_asset_readiness import main

        json_out = tmp_path / "report.json"
        md_out = tmp_path / "report.md"

        main([
            "--root", str(tmp_path),
            "--output-json", str(json_out),
            "--output-md", str(md_out),
        ])
        assert md_out.exists()
        md = md_out.read_text()
        assert "Asset Readiness Report" in md
        assert "Disclaimer" in md
