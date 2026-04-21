from __future__ import annotations

from ecg_digitizer.io import build_image_index, parse_template_id, resolve_image_path


def test_parse_template_id_handles_lead_suffix() -> None:
    pid, point_index, lead = parse_template_id("123_42_aVR")
    assert pid == "123"
    assert point_index == 42
    assert lead == "aVR"


def test_image_index_and_resolution(repo_fixture) -> None:
    image_path = repo_fixture["image_root"] / "patientA.png"
    image_path.write_bytes(b"fake")

    index = build_image_index(repo_fixture["image_root"], (".png", ".jpg"))
    resolved = resolve_image_path("patientA", index)

    assert index["patientA"] == image_path
    assert resolved == image_path
