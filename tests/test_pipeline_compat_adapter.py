"""
Tests for tools/pipeline_compat/prepare_synthetic_runtime_inputs.py

Coverage:
- Creates isolated fixture directory (not data/images/)
- Manifest contains synthetic=true and compatibility_only=true
- Does not overwrite real data directories
- CSV fallback when parquet unavailable
- Graceful handling of missing source manifest
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _import_prepare():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.pipeline_compat.prepare_synthetic_runtime_inputs import prepare
    return prepare


def _make_minimal_synthetic_root(tmp_path: Path, n_cases: int = 2) -> Path:
    src = tmp_path / "synthetic"
    src.mkdir()
    images_dir = src / "images"
    images_dir.mkdir()
    waveforms_dir = src / "waveforms"
    waveforms_dir.mkdir()
    metadata_dir = src / "metadata"
    metadata_dir.mkdir()

    cases = []
    for i in range(n_cases):
        cid = f"case_{i:03d}"
        wf = waveforms_dir / f"{cid}.csv"
        wf.write_text("lead_name,0,1\nI,0.1,0.2\nII,0.3,0.4\n")
        meta = metadata_dir / f"{cid}.json"
        meta.write_text(json.dumps({"case_id": cid, "hr_bpm": 75.0}))
        (images_dir / f"{cid}_clean.ppm").write_bytes(b"P6\n1 1\n255\n\xff\xff\xff")
        cases.append({
            "case_id": cid,
            "waveform_csv": f"waveforms/{cid}.csv",
            "metadata_json": f"metadata/{cid}.json",
            "images": [f"{cid}_clean"],
        })

    manifest = {
        "label": "SYNTHETIC_COMPATIBILITY_ONLY",
        "cases": cases,
    }
    (src / "synthetic_manifest.json").write_text(json.dumps(manifest))
    return src


class TestSyntheticAdapter:
    def test_creates_isolated_output_dir(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        prepare(src, out, max_cases=2)
        assert out.exists()
        assert out.is_dir()

    def test_does_not_write_into_data_images(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        data_images = tmp_path / "data" / "images"
        data_images.mkdir(parents=True)
        out = tmp_path / "runtime_compat"
        prepare(src, out, max_cases=2)
        assert not any(data_images.iterdir()), "Should not write into data/images/"

    def test_manifest_has_synthetic_true(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        result = prepare(src, out, max_cases=2)
        assert result.get("synthetic") is True

    def test_manifest_has_compatibility_only_true(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        result = prepare(src, out, max_cases=2)
        assert result.get("compatibility_only") is True

    def test_manifest_written_to_disk(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        prepare(src, out, max_cases=2)
        manifest_path = out / "synthetic_runtime_input_manifest.json"
        assert manifest_path.exists()
        manifest = json.loads(manifest_path.read_text())
        assert manifest["synthetic"] is True
        assert manifest["compatibility_only"] is True

    def test_manifest_label_field(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        result = prepare(src, out, max_cases=2)
        assert result.get("label") == "SYNTHETIC_COMPATIBILITY_ONLY"

    def test_test_csv_created(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        prepare(src, out, max_cases=2)
        test_csv = out / "test.csv"
        assert test_csv.exists()
        with open(test_csv, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert len(rows) > 0
        assert "id" in rows[0]

    def test_max_cases_respected(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path, n_cases=4)
        out = tmp_path / "runtime_compat"
        result = prepare(src, out, max_cases=2)
        assert result.get("num_cases") == 2

    def test_readme_created(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        prepare(src, out, max_cases=2)
        readme = out / "README.md"
        assert readme.exists()
        text = readme.read_text()
        assert "SYNTHETIC" in text

    def test_missing_source_manifest_returns_error_dict(self, tmp_path):
        prepare = _import_prepare()
        src = tmp_path / "empty_source"
        src.mkdir()
        out = tmp_path / "runtime_compat"
        result = prepare(src, out, max_cases=2)
        assert result.get("success") is False
        assert "error" in result

    def test_submission_template_created(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        result = prepare(src, out, max_cases=2)
        fmt = result.get("submission_format")
        assert fmt in ("parquet", "csv_fallback")
        submission_path = Path(result["submission_template"])
        assert submission_path.exists()

    def test_case_entries_have_required_fields(self, tmp_path):
        prepare = _import_prepare()
        src = _make_minimal_synthetic_root(tmp_path)
        out = tmp_path / "runtime_compat"
        result = prepare(src, out, max_cases=2)
        for case in result.get("cases", []):
            assert "case_id" in case
            assert "waveform_ground_truth_path" in case
            assert "metadata_path" in case
            assert case["synthetic"] is True
            assert case["compatibility_only"] is True
            assert "notes" in case
