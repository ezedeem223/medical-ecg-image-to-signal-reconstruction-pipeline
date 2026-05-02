"""
Parametric Synthetic ECG-like Benchmark Case Generator.

Generates a small number of synthetic 12-lead-like ECG cases for use as
a research benchmark seed. All outputs are clearly labeled SYNTHETIC.

No real ECG data, PhysioNet, PTB-XL, or patient data is used.

Usage:
    python tools/synthetic_benchmark/generate_cases.py \\
        --output benchmark_cases/seed \\
        --num-cases 5
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.synthetic_benchmark.distortions import apply_distortion  # noqa: E402
from tools.synthetic_benchmark.metadata import (  # noqa: E402
    build_case_metadata,
    build_manifest,
    save_manifest,
    save_metadata,
)
from tools.synthetic_benchmark.render_ecg import render_ecg_image, save_image  # noqa: E402

LEAD_NAMES = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]
DEFAULT_FS = 500
DEFAULT_DURATION_S = 10
DEFAULT_DISTORTIONS = ["clean", "blur", "noise", "low_contrast", "rotation", "cropped"]


def _pqrst_template(
    fs: int,
    *,
    hr_bpm: float,
    p_amp: float = 0.15,
    q_amp: float = -0.1,
    r_amp: float = 1.0,
    s_amp: float = -0.2,
    t_amp: float = 0.3,
    noise_std: float = 0.02,
    rng: np.random.Generator,
) -> np.ndarray:
    beat_len = int(round(fs * 60.0 / hr_bpm))
    t = np.linspace(0, 1, beat_len)

    def _gauss(center: float, width: float, amp: float) -> np.ndarray:
        return amp * np.exp(-((t - center) ** 2) / (2 * width ** 2))

    beat = (
        _gauss(0.15, 0.03, p_amp)
        + _gauss(0.35, 0.008, q_amp)
        + _gauss(0.38, 0.012, r_amp)
        + _gauss(0.41, 0.008, s_amp)
        + _gauss(0.65, 0.06, t_amp)
    )
    baseline_drift = 0.03 * np.sin(2 * np.pi * t * 0.5)
    beat = beat + baseline_drift
    noise = rng.normal(0.0, noise_std, size=beat_len).astype(np.float32)
    return (beat + noise).astype(np.float32)


def _generate_12_lead(
    fs: int,
    duration_s: int,
    *,
    hr_bpm: float,
    rng: np.random.Generator,
    morphology_seed: dict[str, float] | None = None,
) -> np.ndarray:
    n_samples = fs * duration_s
    beat_template = _pqrst_template(fs, hr_bpm=hr_bpm, rng=rng)
    beat_len = len(beat_template)

    full_signal = np.zeros(n_samples, dtype=np.float32)
    offset = int(rng.integers(0, max(1, beat_len // 4)))
    pos = offset
    while pos + beat_len < n_samples:
        full_signal[pos: pos + beat_len] += beat_template
        jitter = int(rng.integers(-int(fs * 0.02), int(fs * 0.02) + 1))
        pos += beat_len + jitter

    if morphology_seed is None:
        morphology_seed = {}

    lead_scales = {
        "I":   morphology_seed.get("I",   1.0),
        "II":  morphology_seed.get("II",  1.2),
        "III": morphology_seed.get("III", 0.8),
        "aVR": morphology_seed.get("aVR", -0.9),
        "aVL": morphology_seed.get("aVL", 0.4),
        "aVF": morphology_seed.get("aVF", 0.9),
        "V1":  morphology_seed.get("V1",  0.5),
        "V2":  morphology_seed.get("V2",  0.7),
        "V3":  morphology_seed.get("V3",  1.1),
        "V4":  morphology_seed.get("V4",  1.3),
        "V5":  morphology_seed.get("V5",  1.2),
        "V6":  morphology_seed.get("V6",  0.9),
    }

    waveforms = np.zeros((12, n_samples), dtype=np.float32)
    for idx, lead in enumerate(LEAD_NAMES):
        scale = lead_scales[lead]
        noise = rng.normal(0.0, 0.015, size=n_samples).astype(np.float32)
        waveforms[idx] = full_signal * scale + noise

    return waveforms


def _random_morphology(rng: np.random.Generator) -> dict[str, float]:
    base = {
        "I":   float(rng.uniform(0.7, 1.3)),
        "II":  float(rng.uniform(0.9, 1.5)),
        "III": float(rng.uniform(0.4, 1.0)),
        "aVR": float(rng.uniform(-1.2, -0.6)),
        "aVL": float(rng.uniform(0.2, 0.6)),
        "aVF": float(rng.uniform(0.7, 1.1)),
        "V1":  float(rng.uniform(0.3, 0.7)),
        "V2":  float(rng.uniform(0.5, 0.9)),
        "V3":  float(rng.uniform(0.9, 1.3)),
        "V4":  float(rng.uniform(1.1, 1.5)),
        "V5":  float(rng.uniform(1.0, 1.4)),
        "V6":  float(rng.uniform(0.7, 1.1)),
    }
    return base


def save_waveform_csv(waveforms: np.ndarray, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    n_leads, n_samples = waveforms.shape
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["lead_name"] + [str(i) for i in range(n_samples)])
        for idx in range(n_leads):
            row = [LEAD_NAMES[idx]] + [f"{v:.6f}" for v in waveforms[idx].tolist()]
            writer.writerow(row)


def generate_cases(
    output_dir: Path,
    num_cases: int = 5,
    fs: int = DEFAULT_FS,
    duration_s: int = DEFAULT_DURATION_S,
    distortions: list[str] | None = None,
    base_seed: int = 42,
) -> list[dict]:
    if distortions is None:
        distortions = DEFAULT_DISTORTIONS

    output_dir = Path(output_dir)
    (output_dir / "images").mkdir(parents=True, exist_ok=True)
    (output_dir / "waveforms").mkdir(parents=True, exist_ok=True)
    (output_dir / "metadata").mkdir(parents=True, exist_ok=True)

    manifest_cases = []

    for case_idx in range(num_cases):
        seed = base_seed + case_idx
        rng = np.random.default_rng(seed)
        case_id = f"case_{case_idx:03d}"

        hr_bpm = float(rng.uniform(55.0, 100.0))
        morphology = _random_morphology(rng)

        print(f"  Generating {case_id}  HR={hr_bpm:.1f} bpm  seed={seed}")
        waveforms = _generate_12_lead(
            fs, duration_s, hr_bpm=hr_bpm, rng=rng, morphology_seed=morphology
        )

        waveform_path = output_dir / "waveforms" / f"{case_id}.csv"
        save_waveform_csv(waveforms, waveform_path)

        image = render_ecg_image(waveforms, fs=fs)
        image_files: list[str] = []
        for dist_name in distortions:
            dist_seed = seed + hash(dist_name) % 1000
            dist_image = apply_distortion(dist_name, image, seed=dist_seed)
            img_filename = f"{case_id}_{dist_name}.png"
            img_path = output_dir / "images" / img_filename
            save_image(dist_image, img_path)
            image_files.append(img_filename)

        generator_params = {
            "fs": fs,
            "duration_s": duration_s,
            "heart_rate_bpm": hr_bpm,
            "morphology_scales": morphology,
        }

        meta = build_case_metadata(
            case_id,
            fs=fs,
            num_leads=12,
            signal_length=fs * duration_s,
            heart_rate_bpm=hr_bpm,
            distortions=distortions,
            generator_params=generator_params,
            seed=seed,
        )
        meta_path = output_dir / "metadata" / f"{case_id}.json"
        save_metadata(meta, meta_path)

        manifest_cases.append(
            {
                "case_id": case_id,
                "synthetic": True,
                "seed": seed,
                "heart_rate_bpm": hr_bpm,
                "waveform_csv": str(waveform_path.relative_to(output_dir)),
                "metadata_json": str(meta_path.relative_to(output_dir)),
                "images": image_files,
            }
        )

    manifest = build_manifest(manifest_cases, output_dir)
    manifest_path = output_dir / "synthetic_manifest.json"
    save_manifest(manifest, manifest_path)

    readme = output_dir / "README.md"
    readme.write_text(
        "# Synthetic ECG Benchmark Seed\n\n"
        "**SYNTHETIC DATA — NOT REAL PATIENT DATA**\n\n"
        f"Generated: {num_cases} cases  |  "
        f"Sampling rate: {fs} Hz  |  Duration: {duration_s}s  |  Leads: 12\n\n"
        "All waveforms are parametrically generated. "
        "See `synthetic_manifest.json` for case index.\n",
        encoding="utf-8",
    )

    return manifest_cases


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate synthetic ECG-like benchmark cases (SYNTHETIC only)."
    )
    parser.add_argument(
        "--output",
        default="benchmark_cases/seed",
        help="Output directory for generated cases.",
    )
    parser.add_argument(
        "--num-cases",
        type=int,
        default=5,
        help="Number of synthetic cases to generate (default: 5, max recommended: 10).",
    )
    parser.add_argument(
        "--fs",
        type=int,
        default=DEFAULT_FS,
        help=f"Sampling rate in Hz (default: {DEFAULT_FS}).",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=DEFAULT_DURATION_S,
        help=f"Signal duration in seconds (default: {DEFAULT_DURATION_S}).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Base random seed for reproducibility (default: 42).",
    )
    args = parser.parse_args(argv)

    if args.num_cases > 10:
        print(
            f"WARNING: num-cases={args.num_cases} exceeds recommended maximum of 10 "
            "for this seed pass. Proceeding anyway.",
            file=sys.stderr,
        )

    print(f"[synthetic_benchmark] Generating {args.num_cases} SYNTHETIC cases")
    print(f"  Output: {args.output}")
    print(f"  FS={args.fs} Hz  duration={args.duration}s  seed={args.seed}")
    print("  WARNING: All output is SYNTHETIC — not real ECG data.")

    cases = generate_cases(
        output_dir=Path(args.output),
        num_cases=args.num_cases,
        fs=args.fs,
        duration_s=args.duration,
        base_seed=args.seed,
    )

    print(f"\n[synthetic_benchmark] Done. Generated {len(cases)} cases.")
    print(f"  Manifest: {args.output}/synthetic_manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
