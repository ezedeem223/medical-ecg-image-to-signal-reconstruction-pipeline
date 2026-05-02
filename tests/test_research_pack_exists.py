"""
Smoke tests verifying that all required research pack files exist.

These tests confirm that the ECG Research Workbench Seed documentation
is in place. They do not test content correctness — only file existence.
"""
from __future__ import annotations

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_RESEARCH_PACK_FILES = [
    "docs/research_pack/README.md",
    "docs/research_pack/PROJECT_BRIEF_KAUST.md",
    "docs/research_pack/FAILURE_MODE_ATLAS.md",
    "docs/research_pack/SYNTHETIC_BENCHMARK_PROTOCOL.md",
    "docs/research_pack/EVALUATION_PROTOCOL.md",
    "docs/research_pack/REPRODUCIBILITY_CHECKLIST.md",
]

REQUIRED_TOOL_FILES = [
    "tools/synthetic_benchmark/README.md",
    "tools/synthetic_benchmark/generate_cases.py",
    "tools/synthetic_benchmark/render_ecg.py",
    "tools/synthetic_benchmark/distortions.py",
    "tools/synthetic_benchmark/metadata.py",
    "tools/synthetic_benchmark/score_synthetic.py",
    "tools/quality/README.md",
    "tools/quality/checks.py",
    "tools/quality/generate_quality_report.py",
]

REQUIRED_BENCHMARK_FILES = [
    "benchmark_cases/seed/README.md",
]


@pytest.mark.parametrize("rel_path", REQUIRED_RESEARCH_PACK_FILES)
def test_research_pack_file_exists(rel_path):
    path = ROOT / rel_path
    assert path.exists(), f"Missing research pack file: {rel_path}"
    assert path.stat().st_size > 0, f"Research pack file is empty: {rel_path}"


@pytest.mark.parametrize("rel_path", REQUIRED_TOOL_FILES)
def test_tool_file_exists(rel_path):
    path = ROOT / rel_path
    assert path.exists(), f"Missing tool file: {rel_path}"
    assert path.stat().st_size > 0, f"Tool file is empty: {rel_path}"


@pytest.mark.parametrize("rel_path", REQUIRED_BENCHMARK_FILES)
def test_benchmark_structure_exists(rel_path):
    path = ROOT / rel_path
    assert path.exists(), f"Missing benchmark structure file: {rel_path}"


def test_kaust_brief_mentions_synthetic():
    path = ROOT / "docs/research_pack/PROJECT_BRIEF_KAUST.md"
    content = path.read_text(encoding="utf-8")
    assert "synthetic" in content.lower(), "KAUST brief must mention synthetic benchmark"


def test_kaust_brief_no_clinical_claims():
    path = ROOT / "docs/research_pack/PROJECT_BRIEF_KAUST.md"
    content = path.read_text(encoding="utf-8").lower()
    forbidden = ["clinical validation has been performed", "diagnos", "fda", "ce mark"]
    for term in forbidden:
        assert term not in content, (
            f"KAUST brief must not contain clinical claim: {term!r}"
        )


def test_failure_atlas_has_minimum_categories():
    path = ROOT / "docs/research_pack/FAILURE_MODE_ATLAS.md"
    content = path.read_text(encoding="utf-8")
    assert content.count("## Failure Mode") >= 5, (
        "Failure Mode Atlas must document at least 5 failure categories"
    )


def test_synthetic_protocol_exists_and_non_empty():
    path = ROOT / "docs/research_pack/SYNTHETIC_BENCHMARK_PROTOCOL.md"
    content = path.read_text(encoding="utf-8")
    assert len(content) > 500, "Synthetic benchmark protocol is suspiciously short"
    assert "cannot" in content.lower() or "limitation" in content.lower(), (
        "Protocol must state what synthetic cases cannot prove"
    )


def test_reproducibility_checklist_mentions_seed():
    path = ROOT / "docs/research_pack/REPRODUCIBILITY_CHECKLIST.md"
    content = path.read_text(encoding="utf-8")
    assert "--seed" in content or "seed" in content.lower(), (
        "Reproducibility checklist must mention the seed parameter"
    )


def test_manifest_image_references_exist():
    """Every image filename in synthetic_manifest.json must exist on disk.

    This test catches the PNG/PPM mismatch: if generate_cases records
    a .png name but the fallback writer produced a .ppm file, this test
    will fail with a clear error listing the missing paths.
    """
    import json
    manifest_path = ROOT / "benchmark_cases" / "seed" / "synthetic_manifest.json"
    if not manifest_path.exists():
        pytest.skip("Manifest not generated yet — run generate_cases.py first.")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    images_dir = ROOT / "benchmark_cases" / "seed" / "images"
    missing: list[str] = []
    for case in manifest["cases"]:
        for img_name in case["images"]:
            img_path = images_dir / img_name
            if not img_path.exists():
                missing.append(str(img_path.relative_to(ROOT)))
    assert not missing, (
        f"Manifest references {len(missing)} image file(s) that do not exist:\n"
        + "\n".join(f"  {p}" for p in missing)
    )


def test_manifest_waveform_and_metadata_references_exist():
    """Every waveform and metadata path in synthetic_manifest.json must exist."""
    import json
    manifest_path = ROOT / "benchmark_cases" / "seed" / "synthetic_manifest.json"
    if not manifest_path.exists():
        pytest.skip("Manifest not generated yet — run generate_cases.py first.")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    seed_dir = ROOT / "benchmark_cases" / "seed"
    missing: list[str] = []
    for case in manifest["cases"]:
        wf = seed_dir / case["waveform_csv"]
        if not wf.exists():
            missing.append(str(wf.relative_to(ROOT)))
        meta = seed_dir / case["metadata_json"]
        if not meta.exists():
            missing.append(str(meta.relative_to(ROOT)))
    assert not missing, (
        f"Manifest references {len(missing)} file(s) that do not exist:\n"
        + "\n".join(f"  {p}" for p in missing)
    )


def test_score_synthetic_has_disclaimer():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.synthetic_benchmark.score_synthetic import SYNTHETIC_DISCLAIMER
    assert len(SYNTHETIC_DISCLAIMER) > 50
    assert "clinical" in SYNTHETIC_DISCLAIMER.lower() or "synthetic" in SYNTHETIC_DISCLAIMER.lower()


def test_generate_cases_cli_importable():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.synthetic_benchmark.generate_cases import main
    assert callable(main)


def test_quality_checks_importable():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.quality.checks import run_all_checks
    assert callable(run_all_checks)
