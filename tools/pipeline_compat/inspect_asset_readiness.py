"""
Asset Readiness Inspector — ECG Pipeline Compatibility Layer

Checks whether the repository currently has all files required to attempt
full runtime execution. Generates JSON and Markdown reports.

SYNTHETIC COMPATIBILITY ONLY — this script checks engineering readiness only.
It does not validate ECG reconstruction performance, clinical utility, or
diagnostic correctness.

Usage:
    python tools/pipeline_compat/inspect_asset_readiness.py \\
        --config configs/runtime.default.yaml \\
        --output-json reports/pipeline_compat/asset_readiness_report.json \\
        --output-md  reports/pipeline_compat/asset_readiness_report.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.pipeline_compat.schemas import (  # noqa: E402
    ASSET_DISCLAIMER,
    LARGE_FILE_SHA256_THRESHOLD_BYTES,
    REQUIRED_ASSETS,
)


def _sha256(path: Path) -> tuple[str | None, str]:
    size = path.stat().st_size
    if size > LARGE_FILE_SHA256_THRESHOLD_BYTES:
        return None, f"skipped — file too large ({size // (1024 * 1024)} MB)"
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest(), "computed"


def _inspect_item(root: Path, asset: dict) -> dict:
    rel = asset["path"]
    p = root / rel
    result: dict = {
        "path": rel,
        "kind": asset["kind"],
        "role": asset["role"],
        "exists": p.exists(),
    }
    if p.exists() and p.is_file():
        size = p.stat().st_size
        result["size_bytes"] = size
        digest, status = _sha256(p)
        if digest is not None:
            result["sha256"] = digest
        else:
            result["sha256_status"] = status
    elif p.exists() and p.is_dir():
        files = list(p.iterdir())
        result["file_count"] = len(files)
    return result


def inspect(root: Path, config_path: str | None) -> dict:
    items = [_inspect_item(root, a) for a in REQUIRED_ASSETS]
    missing = [it["path"] for it in items if not it["exists"]]
    can_run = len(missing) == 0

    skip_reasons: list[str] = []
    warnings: list[str] = []

    for it in items:
        if not it["exists"]:
            skip_reasons.append(f"Missing {it['kind']}: {it['path']} ({it['role']})")
        elif it["kind"] == "directory" and it.get("file_count", 0) == 0:
            warnings.append(f"Directory exists but is empty: {it['path']}")

    return {
        "repository_root": str(root),
        "config_path": config_path or "configs/runtime.default.yaml",
        "models_registry_path": "configs/models.yaml",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "required_items": items,
        "can_run_full_pipeline": can_run,
        "skip_reasons": skip_reasons,
        "warnings": warnings,
        "disclaimer": ASSET_DISCLAIMER,
    }


def _md_report(report: dict) -> str:
    lines = [
        "# Asset Readiness Report",
        "",
        f"**Checked at:** {report['checked_at_utc']}",
        f"**Repository root:** `{report['repository_root']}`",
        "",
        f"**Can run full pipeline:** {'✅ YES' if report['can_run_full_pipeline'] else '❌ NO'}",
        "",
    ]

    if report["skip_reasons"]:
        lines += ["## Skip Reasons", ""]
        for r in report["skip_reasons"]:
            lines.append(f"- {r}")
        lines.append("")

    if report["warnings"]:
        lines += ["## Warnings", ""]
        for w in report["warnings"]:
            lines.append(f"- ⚠️  {w}")
        lines.append("")

    lines += ["## Asset Inventory", ""]
    lines.append("| Asset | Kind | Exists | Size / Files | Role |")
    lines.append("|-------|------|--------|--------------|------|")
    for it in report["required_items"]:
        exists = "✅" if it["exists"] else "❌"
        if it["exists"] and it["kind"] == "file":
            size_str = f"{it.get('size_bytes', '?'):,} bytes"
        elif it["exists"] and it["kind"] == "directory":
            size_str = f"{it.get('file_count', '?')} files"
        else:
            size_str = "—"
        lines.append(
            f"| `{it['path']}` | {it['kind']} | {exists} | {size_str} | {it['role']} |"
        )

    lines += [
        "",
        "---",
        "",
        f"> **Disclaimer:** {report['disclaimer']}",
        "",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Inspect asset readiness for ECG pipeline execution."
    )
    parser.add_argument(
        "--config", default="configs/runtime.default.yaml",
        help="Path to runtime config (used only to record in report; not parsed).",
    )
    parser.add_argument(
        "--root", default=str(ROOT),
        help="Repository root. Defaults to auto-detected project root.",
    )
    parser.add_argument(
        "--output-json",
        default="reports/pipeline_compat/asset_readiness_report.json",
    )
    parser.add_argument(
        "--output-md",
        default="reports/pipeline_compat/asset_readiness_report.md",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    report = inspect(root, args.config)

    json_path = root / args.output_json
    md_path = root / args.output_md
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(_md_report(report), encoding="utf-8")

    print(f"[asset_readiness] Checked {len(report['required_items'])} assets")
    print(f"[asset_readiness] Can run full pipeline: {report['can_run_full_pipeline']}")
    if report["skip_reasons"]:
        print("[asset_readiness] Skip reasons:")
        for r in report["skip_reasons"]:
            print(f"  - {r}")
    print(f"[asset_readiness] JSON → {json_path}")
    print(f"[asset_readiness] MD  → {md_path}")
    print(f"\n  DISCLAIMER: {ASSET_DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
