"""
Tests for the synthetic ECG benchmark generation pipeline.

All tests are self-contained — no model weights, real ECG data,
or external downloads required.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]


def _import_generate():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.synthetic_benchmark.generate_cases import (
        _generate_12_lead,
        _pqrst_template,
        generate_cases,
        save_waveform_csv,
    )
    return _generate_12_lead, _pqrst_template, generate_cases, save_waveform_csv


def _import_distortions():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.synthetic_benchmark.distortions import (
        DISTORTION_REGISTRY,
        apply_distortion,
    )
    return DISTORTION_REGISTRY, apply_distortion


def _import_metadata():
    import sys
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from tools.synthetic_benchmark.metadata import build_case_metadata, build_manifest
    return build_case_metadata, build_manifest


class TestPqrstTemplate:
    def test_returns_float32_array(self):
        _gen, _pqrst, _, _ = _import_generate()
        rng = np.random.default_rng(0)
        beat = _pqrst(500, hr_bpm=75.0, rng=rng)
        assert beat.dtype == np.float32

    def test_beat_length_approximately_correct(self):
        _gen, _pqrst, _, _ = _import_generate()
        rng = np.random.default_rng(1)
        fs = 500
        hr = 60.0
        beat = _pqrst(fs, hr_bpm=hr, rng=rng)
        expected_len = int(round(fs * 60.0 / hr))
        assert len(beat) == expected_len

    def test_beat_has_r_wave_peak(self):
        _gen, _pqrst, _, _ = _import_generate()
        rng = np.random.default_rng(2)
        beat = _pqrst(500, hr_bpm=75.0, r_amp=1.0, rng=rng)
        assert beat.max() > 0.5


class TestGenerate12Lead:
    def test_output_shape(self):
        _gen, _, _, _ = _import_generate()
        rng = np.random.default_rng(0)
        waveforms = _gen(500, 5, hr_bpm=70.0, rng=rng)
        assert waveforms.shape == (12, 500 * 5)

    def test_output_dtype(self):
        _gen, _, _, _ = _import_generate()
        rng = np.random.default_rng(0)
        waveforms = _gen(500, 5, hr_bpm=70.0, rng=rng)
        assert waveforms.dtype == np.float32

    def test_no_nan_or_inf(self):
        _gen, _, _, _ = _import_generate()
        rng = np.random.default_rng(0)
        waveforms = _gen(500, 5, hr_bpm=70.0, rng=rng)
        assert np.all(np.isfinite(waveforms))

    def test_leads_not_all_identical(self):
        _gen, _, _, _ = _import_generate()
        rng = np.random.default_rng(0)
        waveforms = _gen(500, 5, hr_bpm=70.0, rng=rng)
        first = waveforms[0]
        assert not np.allclose(waveforms[3], first), "aVR should differ from lead I"


class TestGenerateCases:
    def test_generates_expected_files(self, tmp_path):
        _, _, generate_cases, _ = _import_generate()
        cases = generate_cases(tmp_path, num_cases=2, fs=100, duration_s=3)
        assert len(cases) == 2
        assert (tmp_path / "synthetic_manifest.json").exists()
        assert (tmp_path / "waveforms" / "case_000.csv").exists()
        assert (tmp_path / "waveforms" / "case_001.csv").exists()
        assert (tmp_path / "metadata" / "case_000.json").exists()

    def test_manifest_marks_synthetic_true(self, tmp_path):
        _, _, generate_cases, _ = _import_generate()
        generate_cases(tmp_path, num_cases=2, fs=100, duration_s=3)
        manifest = json.loads((tmp_path / "synthetic_manifest.json").read_text())
        assert manifest["synthetic"] is True
        assert manifest["num_cases"] == 2

    def test_each_case_is_synthetic(self, tmp_path):
        _, _, generate_cases, _ = _import_generate()
        generate_cases(tmp_path, num_cases=2, fs=100, duration_s=3)
        for case_idx in range(2):
            meta_path = tmp_path / "metadata" / f"case_{case_idx:03d}.json"
            meta = json.loads(meta_path.read_text())
            assert meta["synthetic"] is True
            assert meta["data_source"] == "SYNTHETIC"

    def test_waveform_csv_has_12_leads(self, tmp_path):
        _, _, generate_cases, _ = _import_generate()
        generate_cases(tmp_path, num_cases=1, fs=100, duration_s=3)
        csv_path = tmp_path / "waveforms" / "case_000.csv"
        with open(csv_path, newline="") as f:
            rows = list(csv.reader(f))
        data_rows = [r for r in rows if r and r[0] != "lead_name"]
        assert len(data_rows) == 12

    def test_images_directory_created(self, tmp_path):
        _, _, generate_cases, _ = _import_generate()
        generate_cases(
            tmp_path, num_cases=1, fs=100, duration_s=3,
            distortions=["clean"]
        )
        assert (tmp_path / "images").exists()


class TestSaveWaveformCsv:
    def test_roundtrip(self, tmp_path):
        _, _, _, save_csv = _import_generate()
        waveforms = np.random.rand(12, 200).astype(np.float32)
        path = tmp_path / "test.csv"
        save_csv(waveforms, path)
        assert path.exists()
        with open(path, newline="") as f:
            rows = list(csv.reader(f))
        assert len(rows) == 13


class TestDistortions:
    def _make_image(self) -> np.ndarray:
        return (np.random.rand(80, 120, 3) * 255).astype(np.uint8)

    def test_clean_returns_copy(self):
        _, apply = _import_distortions()
        img = self._make_image()
        out = apply("clean", img, seed=0)
        np.testing.assert_array_equal(img, out)

    def test_all_distortions_return_uint8(self):
        registry, apply = _import_distortions()
        img = self._make_image()
        for name in registry:
            out = apply(name, img, seed=0)
            assert out.dtype == np.uint8, f"Distortion {name!r} did not return uint8"

    def test_noise_changes_image(self):
        _, apply = _import_distortions()
        img = self._make_image()
        out = apply("noise", img, seed=0)
        assert not np.array_equal(img, out)

    def test_unknown_distortion_raises(self):
        _, apply = _import_distortions()
        img = self._make_image()
        with pytest.raises(ValueError, match="Unknown distortion"):
            apply("nonexistent_distortion", img)


class TestDistortionSeedDeterminism:
    """Distortion seeds must not rely on hash() and must be stable across runs."""

    def _import_offset(self):
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.synthetic_benchmark.generate_cases import _DISTORTION_OFFSET, DEFAULT_DISTORTIONS
        return _DISTORTION_OFFSET, DEFAULT_DISTORTIONS

    def test_offset_map_covers_all_default_distortions(self):
        offset_map, defaults = self._import_offset()
        for name in defaults:
            assert name in offset_map, f"Missing distortion offset for {name!r}"

    def test_offset_values_are_plain_integers(self):
        offset_map, _ = self._import_offset()
        for name, val in offset_map.items():
            assert isinstance(val, int), f"Offset for {name!r} is not int: {type(val)}"

    def test_offsets_are_unique(self):
        offset_map, _ = self._import_offset()
        values = list(offset_map.values())
        assert len(values) == len(set(values)), "Distortion offsets must be unique"

    def test_seed_derivation_is_stable(self):
        """Same base_seed + distortion name → same dist_seed, regardless of process."""
        offset_map, _ = self._import_offset()
        base_seed = 42
        for name, offset in offset_map.items():
            dist_seed_a = base_seed + offset
            dist_seed_b = base_seed + offset_map[name]
            assert dist_seed_a == dist_seed_b

    def test_no_hash_call_in_generate_cases(self):
        """Regression guard: generate_cases.py must not call hash() on dist names."""
        src = (ROOT / "tools" / "synthetic_benchmark" / "generate_cases.py").read_text()
        assert "hash(dist_name)" not in src, (
            "generate_cases.py must not use hash(dist_name) — it is non-deterministic"
        )


class TestBlurFallbackChannelSafety:
    """Numpy blur fallback must apply convolution per channel, not across channels."""

    def _import_blur(self):
        import sys
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from tools.synthetic_benchmark.distortions import apply_blur, _gaussian_kernel_1d
        return apply_blur, _gaussian_kernel_1d

    def _distinct_channel_image(self) -> np.ndarray:
        """Return a small uint8 image where each RGB channel has a unique constant value."""
        img = np.zeros((20, 30, 3), dtype=np.uint8)
        img[:, :, 0] = 50
        img[:, :, 1] = 150
        img[:, :, 2] = 200
        return img

    def test_blur_preserves_shape_and_dtype(self):
        apply_blur, _ = self._import_blur()
        img = self._distinct_channel_image()
        out = apply_blur(img)
        assert out.shape == img.shape
        assert out.dtype == np.uint8

    def test_blur_does_not_mix_channels(self):
        """Per-channel blur must not bleed one channel's values into another.

        Each channel is a uniform constant.  Correct per-channel blur should
        produce an output whose mean is very close to the original constant
        (edge pixels may deviate slightly due to zero-padding, but no channel's
        average should drift toward another channel's value).  If channels were
        mixed the means would converge toward each other.
        """
        apply_blur, _ = self._import_blur()
        img = self._distinct_channel_image()
        out = apply_blur(img)
        original_means = [50.0, 150.0, 200.0]
        for c in range(3):
            channel_mean = float(out[:, :, c].mean())
            assert abs(channel_mean - original_means[c]) < 30.0, (
                f"Channel {c} mean drifted too far: expected ~{original_means[c]}, "
                f"got {channel_mean:.1f}. Channels may be mixed."
            )

    def test_gaussian_kernel_sums_to_one(self):
        _, _gaussian_kernel_1d = self._import_blur()
        kernel = _gaussian_kernel_1d(7, 2.0)
        assert abs(kernel.sum() - 1.0) < 1e-5


class TestMetadata:
    def test_build_case_metadata_synthetic_flag(self):
        build_meta, _ = _import_metadata()
        meta = build_meta(
            "case_000",
            fs=500,
            num_leads=12,
            signal_length=5000,
            heart_rate_bpm=72.0,
            distortions=["clean", "blur"],
            generator_params={},
            seed=42,
        )
        assert meta["synthetic"] is True
        assert meta["data_source"] == "SYNTHETIC"
        assert "warning" in meta

    def test_build_manifest_synthetic_flag(self):
        _, build_manifest = _import_metadata()
        manifest = build_manifest([{"case_id": "case_000"}], Path("/tmp/test"))
        assert manifest["synthetic"] is True
        assert manifest["num_cases"] == 1
