from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Any

from evolution_manual_notes import load_evolution_notes


ROOT = Path(__file__).resolve().parents[1]
FILE_AUDIT_ROOT = ROOT / "docs" / "file-audit"
EVOLUTION_ROOT = ROOT / "docs" / "evolution"
MANIFEST_PATH = FILE_AUDIT_ROOT / "manifest.csv"
CHECKPOINT_COMPANION_PATH = FILE_AUDIT_ROOT / "checkpoint-companion-summary.md"
SYNTHESIS_SEED_PATH = ROOT / "docs" / "final_synthesis_outline.md"

LINEAGE_OUTPUT = EVOLUTION_ROOT / "notebook_lineage.csv"
EVOLUTION_MAP_OUTPUT = EVOLUTION_ROOT / "notebook_evolution_map.md"
REVISION_DIFFS_OUTPUT = EVOLUTION_ROOT / "revision_diffs.md"
CHECKPOINT_INVENTORY_OUTPUT = EVOLUTION_ROOT / "checkpoint_inventory.csv"
DATASET_INVENTORY_OUTPUT = EVOLUTION_ROOT / "dataset_inventory.csv"
COMPONENT_INVENTORY_OUTPUT = EVOLUTION_ROOT / "component_inventory.csv"
ARCHITECTURE_OUTPUT = EVOLUTION_ROOT / "final_architecture_synthesis.md"
NARRATIVE_OUTPUT = EVOLUTION_ROOT / "project_narrative_final.md"
OPEN_QUESTIONS_OUTPUT = EVOLUTION_ROOT / "open_questions_remaining.md"
README_OUTPUT = EVOLUTION_ROOT / "README.md"

REQUIRED_ARCHITECTURE_SECTIONS = [
    "## 1. Project objective",
    "## 2. Evolution timeline",
    "## 3. Renderer evolution",
    "## 4. Dataset and input evolution",
    "## 5. Model evolution",
    "## 6. Checkpoint evolution",
    "## 7. Detection and cropping evolution",
    "## 8. Segmentation evolution",
    "## 9. Trace extraction evolution",
    "## 10. Calibration and post-processing evolution",
    "## 11. Submission pipeline evolution",
    "## 12. Final likely architecture",
    "## 13. Remaining ambiguities",
    "## 14. Refactor implications",
]


def main() -> None:
    notes = load_evolution_notes()
    manifest_rows = load_manifest_rows()
    notebook_rows = sorted(
        [row for row in manifest_rows if row["entry_type"] == "notebook"],
        key=lambda row: int(row["review_order"]),
    )
    model_rows = sorted(
        [row for row in manifest_rows if row["entry_type"] == "model"],
        key=lambda row: int(row["review_order"]),
    )
    if len(notebook_rows) != 57:
        raise SystemExit(f"Expected 57 notebook rows in manifest, found {len(notebook_rows)}")
    if len(model_rows) != 6:
        raise SystemExit(f"Expected 6 model rows in manifest, found {len(model_rows)}")

    synthesis_seed_text = SYNTHESIS_SEED_PATH.read_text(encoding="utf-8")
    notebook_data = [parse_notebook_report(row) for row in notebook_rows]
    notebook_by_name = {entry["source_name"]: entry for entry in notebook_data}
    companion_entries = parse_checkpoint_companion(CHECKPOINT_COMPANION_PATH.read_text(encoding="utf-8"))

    EVOLUTION_ROOT.mkdir(parents=True, exist_ok=True)

    lineage_rows = build_lineage_rows(notebook_data, notes)
    checkpoint_rows = build_checkpoint_inventory_rows(notebook_data, companion_entries, notes)
    dataset_rows = build_dataset_inventory_rows(notebook_data, notes)
    component_rows = build_component_inventory_rows(notes)

    write_csv(
        LINEAGE_OUTPUT,
        [
            "review_order",
            "notebook_name",
            "phase_label",
            "predecessor",
            "successor",
            "branch_type",
            "major_change_type",
            "status",
            "confidence",
            "milestone_group",
            "notes",
        ],
        lineage_rows,
    )
    write_text(EVOLUTION_MAP_OUTPUT, render_notebook_evolution_map(notebook_data, lineage_rows, notes, synthesis_seed_text))
    write_text(REVISION_DIFFS_OUTPUT, render_revision_diffs(notes))
    write_csv(
        CHECKPOINT_INVENTORY_OUTPUT,
        [
            "checkpoint_name",
            "canonical_name",
            "first_appearance",
            "last_appearance",
            "training_notebooks",
            "inference_notebooks",
            "role",
            "development_phase",
            "replaced_by",
            "final_status",
            "confidence",
            "notes",
        ],
        checkpoint_rows,
    )
    write_csv(
        DATASET_INVENTORY_OUTPUT,
        [
            "dataset_name",
            "canonical_identifier",
            "path_or_reference",
            "data_type",
            "first_use",
            "last_use",
            "role",
            "linked_notebooks",
            "replaced_by",
            "confidence",
            "notes",
        ],
        dataset_rows,
    )
    write_csv(
        COMPONENT_INVENTORY_OUTPUT,
        [
            "component_name",
            "introduced_in",
            "matured_in",
            "deprecated_in",
            "role",
            "final_architecture_included",
            "confidence",
            "notes",
        ],
        component_rows,
    )
    write_text(ARCHITECTURE_OUTPUT, render_architecture_synthesis(notes))
    write_text(NARRATIVE_OUTPUT, render_project_narrative(notes))
    write_text(OPEN_QUESTIONS_OUTPUT, render_open_questions(notes))
    write_text(README_OUTPUT, render_evolution_readme(synthesis_seed_text))

    validate_outputs(notebook_rows, model_rows, lineage_rows, checkpoint_rows, dataset_rows, component_rows, companion_entries)

    print("Phase 2 synthesis generated successfully.")
    print(f"- Notebook lineage rows: {len(lineage_rows)}")
    print(f"- Checkpoint inventory rows: {len(checkpoint_rows)}")
    print(f"- Dataset inventory rows: {len(dataset_rows)}")
    print(f"- Component inventory rows: {len(component_rows)}")
    print(f"- Output root: {EVOLUTION_ROOT}")


def load_manifest_rows() -> list[dict[str, str]]:
    with MANIFEST_PATH.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_notebook_report(manifest_row: dict[str, str]) -> dict[str, Any]:
    report_path = FILE_AUDIT_ROOT / manifest_row["report_path"]
    text = report_path.read_text(encoding="utf-8")
    return {
        "source_name": manifest_row["source_name"],
        "review_order": int(manifest_row["review_order"]),
        "report_path": manifest_row["report_path"],
        "report_link": f"../file-audit/{manifest_row['report_path']}",
        "text": text,
        "lower_text": text.lower(),
        "inferred_role": extract_table_value(text, "Inferred role"),
        "confidence": manifest_row["confidence"],
        "open_questions_count": int(manifest_row["open_questions_count"]),
        "notebook_summary": extract_bullets(text, "Notebook summary"),
        "delta_notes": extract_bullets(text, "Delta notes"),
        "open_questions": extract_bullets(text, "Open questions"),
        "referenced_checkpoints": extract_bullets(text, "Referenced checkpoints"),
        "referenced_datasets": extract_bullets(text, "Referenced datasets"),
        "external_files": extract_bullets(text, "External files"),
        "runtime_assumptions": extract_bullets(text, "Required runtime assumptions"),
        "outputs_created": extract_bullets(text, "Outputs created or updated"),
    }


def extract_table_value(text: str, field: str) -> str:
    match = re.search(rf"\| {re.escape(field)} \| (.*?) \|", text)
    return match.group(1).strip() if match else ""


def extract_bullets(text: str, label: str) -> list[str]:
    match = re.search(rf"\*\*{re.escape(label)}\*\*\s*\n\s*((?:- .*(?:\n|$))+)", text)
    if not match:
        return []
    items = []
    for line in match.group(1).splitlines():
        if not line.startswith("- "):
            continue
        item = line[2:].strip()
        if item.lower() == "none":
            continue
        items.append(item)
    return items


def parse_checkpoint_companion(text: str) -> dict[str, dict[str, Any]]:
    parts = re.split(r"^## `(.*?)`\s*$", text, flags=re.M)
    entries: dict[str, dict[str, Any]] = {}
    for index in range(1, len(parts), 2):
        name = parts[index]
        body = parts[index + 1]
        references_line = find_prefixed_line(body, "Referencing notebooks")
        entries[name] = {
            "name": name,
            "audited": find_prefixed_line(body, "Audited artifact in bundle") == "yes",
            "references": [] if references_line in {"", "None"} else re.findall(r"`([^`]+)`", references_line),
            "role": find_prefixed_line(body, "Interpreted role"),
            "development_phase": find_prefixed_line(body, "Development phase"),
            "confidence": find_prefixed_line(body, "Interpretation confidence"),
        }
    return entries


def find_prefixed_line(body: str, prefix: str) -> str:
    match = re.search(rf"^- {re.escape(prefix)}: (.*)$", body, flags=re.M)
    return match.group(1).strip() if match else ""


def build_lineage_rows(notebooks: list[dict[str, Any]], notes: dict[str, Any]) -> list[dict[str, str]]:
    overrides = notes["notebook_overrides"]
    eras = notes["eras"]
    total = len(notebooks)
    rows: list[dict[str, str]] = []
    for index, notebook in enumerate(notebooks):
        era = era_for_order(notebook["review_order"], eras)
        override = overrides.get(notebook["source_name"], {})
        predecessor = override.get("predecessor", notebooks[index - 1]["source_name"] if index > 0 else "")
        successor = override.get("successor", notebooks[index + 1]["source_name"] if index < total - 1 else "")
        branch_type = override.get("branch_type", era["default_branch_type"])
        major_change_type = override.get("major_change_type", era["default_major_change_type"])
        status = override.get("status", "active" if index == total - 1 else era["default_status"])
        confidence = override.get("confidence", notebook["confidence"] or era["default_confidence"])
        milestone_group = override.get("milestone_group", era["milestone_group"])
        notes_text = override.get("notes") or first_nonempty(notebook["notebook_summary"], notebook["delta_notes"], notebook["inferred_role"])
        rows.append(
            {
                "review_order": str(notebook["review_order"]),
                "notebook_name": notebook["source_name"],
                "phase_label": override.get("phase_label", era["phase_label"]),
                "predecessor": predecessor,
                "successor": successor,
                "branch_type": branch_type,
                "major_change_type": major_change_type,
                "status": status,
                "confidence": confidence,
                "milestone_group": milestone_group,
                "notes": notes_text,
            }
        )
    return rows


def era_for_order(review_order: int, eras: list[dict[str, Any]]) -> dict[str, Any]:
    for era in eras:
        if era["start_order"] <= review_order <= era["end_order"]:
            return era
    raise KeyError(f"No era covers review order {review_order}")


def first_nonempty(*groups: Any) -> str:
    for group in groups:
        if isinstance(group, list) and group:
            return group[0]
        if isinstance(group, str) and group.strip():
            return group.strip()
    return ""


def build_checkpoint_inventory_rows(
    notebooks: list[dict[str, Any]],
    companion_entries: dict[str, dict[str, Any]],
    notes: dict[str, Any],
) -> list[dict[str, str]]:
    notebook_order = {entry["source_name"]: entry["review_order"] for entry in notebooks}
    rows: list[dict[str, str]] = []
    for checkpoint in notes["checkpoint_rows"]:
        aliases = checkpoint.get("aliases", [checkpoint["checkpoint_name"]])
        referenced_notebooks: list[str] = []
        for alias in aliases:
            referenced_notebooks.extend(companion_entries.get(alias, {}).get("references", []))
        referenced_notebooks = unique_sorted(referenced_notebooks, key=lambda name: notebook_order.get(name, 10**9))
        first_appearance = referenced_notebooks[0] if referenced_notebooks else ""
        last_appearance = referenced_notebooks[-1] if referenced_notebooks else ""
        training_notebooks = [
            name
            for name in referenced_notebooks
            if notebook_order.get(name, 0) <= 10 or notebook_order.get(name, 0) == 43
        ]
        inference_notebooks = [name for name in referenced_notebooks if name not in training_notebooks]
        alias_note = f"Aliases normalized under `{checkpoint['canonical_name']}`: {', '.join(aliases)}."
        notes_text = checkpoint["notes"]
        if notes_text:
            notes_text = f"{notes_text} {alias_note}"
        else:
            notes_text = alias_note
        rows.append(
            {
                "checkpoint_name": checkpoint["checkpoint_name"],
                "canonical_name": checkpoint["canonical_name"],
                "first_appearance": first_appearance,
                "last_appearance": last_appearance,
                "training_notebooks": "; ".join(training_notebooks),
                "inference_notebooks": "; ".join(inference_notebooks),
                "role": checkpoint["role"],
                "development_phase": checkpoint["development_phase"],
                "replaced_by": checkpoint["replaced_by"],
                "final_status": checkpoint["final_status"],
                "confidence": checkpoint["confidence"],
                "notes": notes_text,
            }
        )
    return rows


def unique_sorted(values: list[str], key: Any) -> list[str]:
    seen: set[str] = set()
    unique_values = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        unique_values.append(value)
    return sorted(unique_values, key=key)


def build_dataset_inventory_rows(notebooks: list[dict[str, Any]], notes: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for dataset in notes["dataset_rows"]:
        matched = [
            notebook["source_name"]
            for notebook in notebooks
            if any(pattern.lower() in notebook["lower_text"] for pattern in dataset["patterns"])
        ]
        matched = unique_sorted(matched, key=lambda name: next(entry["review_order"] for entry in notebooks if entry["source_name"] == name))
        first_use = matched[0] if matched else ""
        last_use = matched[-1] if matched else ""
        rows.append(
            {
                "dataset_name": dataset["dataset_name"],
                "canonical_identifier": dataset["canonical_identifier"],
                "path_or_reference": dataset["path_or_reference"],
                "data_type": dataset["data_type"],
                "first_use": first_use,
                "last_use": last_use,
                "role": dataset["role"],
                "linked_notebooks": "; ".join(matched),
                "replaced_by": dataset["replaced_by"],
                "confidence": dataset["confidence"],
                "notes": dataset["notes"],
            }
        )
    return rows


def build_component_inventory_rows(notes: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for component in notes["component_rows"]:
        rows.append(
            {
                "component_name": component["component_name"],
                "introduced_in": component["introduced_in"],
                "matured_in": component["matured_in"],
                "deprecated_in": component["deprecated_in"],
                "role": component["role"],
                "final_architecture_included": component["final_architecture_included"],
                "confidence": component["confidence"],
                "notes": component["notes"],
            }
        )
    return rows


def render_notebook_evolution_map(
    notebooks: list[dict[str, Any]],
    lineage_rows: list[dict[str, str]],
    notes: dict[str, Any],
    synthesis_seed_text: str,
) -> str:
    notebooks_by_order = {entry["review_order"]: entry for entry in notebooks}
    lineage_by_name = {entry["notebook_name"]: entry for entry in lineage_rows}
    dead_end_notebooks = [row["notebook_name"] for row in lineage_rows if row["branch_type"] == "dead-end"]
    uncertain_notebooks = [row["notebook_name"] for row in lineage_rows if row["status"] == "uncertain"]
    milestone_rows = [
        row
        for row in lineage_rows
        if row["branch_type"] in {"baseline", "consolidation", "milestone", "branch"} or row["status"] == "active"
    ]
    lines = [
        "# Notebook Evolution Map",
        "",
        "This Phase 2 map synthesizes the Phase 1 audit bundle into a coherent lineage. It uses the file-audit reports as the factual base and the curated Phase 2 notes layer for ambiguous lineage decisions.",
        "",
        "## Scope And Source Of Truth",
        "",
        f"- Notebook reports: [../file-audit/notebooks/](../file-audit/notebooks/)",
        f"- Manifest: [../file-audit/manifest.csv](../file-audit/manifest.csv)",
        f"- Checkpoint companion: [../file-audit/checkpoint-companion-summary.md](../file-audit/checkpoint-companion-summary.md)",
        f"- Phase 1 synthesis seed retained for terminology and era framing: [../final_synthesis_outline.md](../final_synthesis_outline.md)",
        "",
        "## Mainline At A Glance",
        "",
        "1. Early monolithic baseline",
        "2. Compact proof-of-concept consolidation",
        "3. Synthetic-to-real staged research branch",
        "4. Architecture hardening and combat-detector era",
        "5. Compact deployment and robustness iteration",
        "6. Ensemble competitor branch",
        "7. EfficientNet-B3 integration and modular finalization",
        "",
        "## Path Classification",
        "",
        f"- Active final notebook candidate: `{lineage_rows[-1]['notebook_name']}`",
        f"- Dead-end benchmarking notebooks: {', '.join(f'`{name}`' for name in dead_end_notebooks) if dead_end_notebooks else 'None'}",
        f"- Uncertain strategic notebooks: {', '.join(f'`{name}`' for name in uncertain_notebooks) if uncertain_notebooks else 'None'}",
        "",
        "## Milestone Notebooks",
        "",
        "| Review order | Notebook | Phase label | Branch type | Status | Notes |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in milestone_rows:
        notebook = next(entry for entry in notebooks if entry["source_name"] == row["notebook_name"])
        link = f"[`{row['notebook_name']}`]({notebook['report_link']})"
        lines.append(
            f"| {row['review_order']} | {link} | `{row['phase_label']}` | `{row['branch_type']}` | `{row['status']}` | {row['notes']} |"
        )
    for era in notes["eras"]:
        era_notebooks = [
            notebooks_by_order[order]
            for order in range(era["start_order"], era["end_order"] + 1)
            if order in notebooks_by_order
        ]
        if not era_notebooks:
            continue
        lines.extend(
            [
                "",
                f"## {era['title']}",
                "",
                f"- Review orders: {era['start_order']} to {era['end_order']}",
                f"- Notebooks: {', '.join(f'[`{entry['source_name']}`]({entry['report_link']})' for entry in era_notebooks)}",
                f"- Intent: {era['intent']}",
                "- Key surviving components:",
            ]
        )
        lines.extend([f"  - {item}" for item in era["key_survivors"]])
        lines.append("- What was superseded:")
        lines.extend([f"  - {item}" for item in era["superseded_elements"]])
        if era["uncertainty_hotspots"]:
            lines.append("- Confidence and uncertainty hotspots:")
            lines.extend([f"  - {item}" for item in era["uncertainty_hotspots"]])
        else:
            lines.append("- Confidence and uncertainty hotspots:")
            lines.append("  - None called out beyond ordinary notebook lineage uncertainty.")
        primary_head = lineage_by_name[era_notebooks[0]["source_name"]]["predecessor"]
        primary_tail = lineage_by_name[era_notebooks[-1]["source_name"]]["successor"]
        lines.append(f"- Primary predecessor outside era: `{primary_head}`" if primary_head else "- Primary predecessor outside era: None")
        lines.append(f"- Primary successor outside era: `{primary_tail}`" if primary_tail else "- Primary successor outside era: None")
    if "Terminology Glossary Seed" in synthesis_seed_text:
        lines.extend(
            [
                "",
                "## Terminology Note",
                "",
                "Phase 2 keeps the terminology seeded in [../final_synthesis_outline.md](../final_synthesis_outline.md); this file focuses on lineage and milestone interpretation rather than re-defining the glossary.",
            ]
        )
    return "\n".join(lines) + "\n"


def render_revision_diffs(notes: dict[str, Any]) -> str:
    lines = [
        "# Revision Diffs",
        "",
        "This file documents only milestone and architecture-significant transitions. It is not an all-pairs comparison matrix.",
    ]
    for index, transition in enumerate(notes["transitions"], start=1):
        lines.extend(
            [
                "",
                f"## {index}. {transition['title']}",
                "",
                f"- From notebooks: {', '.join(f'`{name}`' for name in transition['from_notebooks'])}",
                f"- To notebooks: {', '.join(f'`{name}`' for name in transition['to_notebooks'])}",
                "",
                "### Observed change",
            ]
        )
        lines.extend([f"- {item}" for item in transition["observed_change"]])
        lines.extend(["", "### Likely motivation"])
        lines.extend([f"- {item}" for item in transition["likely_motivation"]])
        lines.extend(["", "### Pipeline impact"])
        lines.extend([f"- {item}" for item in transition["pipeline_impact"]])
        lines.extend(["", "### Retained elements"])
        lines.extend([f"- {item}" for item in transition["retained_elements"]])
        lines.extend(["", "### Obsoleted or replaced elements"])
        lines.extend([f"- {item}" for item in transition["obsoleted_elements"]])
        lines.extend(["", f"- Confidence: `{transition['confidence']}`"])
    return "\n".join(lines) + "\n"


def render_architecture_synthesis(notes: dict[str, Any]) -> str:
    ordered_sections = [
        ("1. Project objective", "project_objective"),
        ("2. Evolution timeline", "evolution_timeline"),
        ("3. Renderer evolution", "renderer_evolution"),
        ("4. Dataset and input evolution", "dataset_and_input_evolution"),
        ("5. Model evolution", "model_evolution"),
        ("6. Checkpoint evolution", "checkpoint_evolution"),
        ("7. Detection and cropping evolution", "detection_and_cropping_evolution"),
        ("8. Segmentation evolution", "segmentation_evolution"),
        ("9. Trace extraction evolution", "trace_extraction_evolution"),
        ("10. Calibration and post-processing evolution", "calibration_and_postprocessing_evolution"),
        ("11. Submission pipeline evolution", "submission_pipeline_evolution"),
        ("12. Final likely architecture", "final_likely_architecture"),
        ("13. Remaining ambiguities", "remaining_ambiguities"),
        ("14. Refactor implications", "refactor_implications"),
    ]
    lines = [
        "# Final Architecture Synthesis",
        "",
        "This synthesis uses Phase 1 structural facts and Phase 2 curated interpretation. The bullets under **Observed evidence** are factual summaries; the paragraph under **Synthesis** is the project-level inference.",
    ]
    for title, key in ordered_sections:
        section = notes["architecture_sections"][key]
        lines.extend(
            [
                "",
                f"## {title}",
                "",
                "**Observed evidence**",
            ]
        )
        lines.extend([f"- {item}" for item in section["observed"]])
        lines.extend(["", "**Synthesis**", "", section["synthesis"]])
    return "\n".join(lines) + "\n"


def render_project_narrative(notes: dict[str, Any]) -> str:
    narrative = notes["project_narrative"]
    lines = [
        "# Final Project Narrative",
        "",
        narrative["overview"],
        "",
        "## Why it matters",
        "",
        narrative["why_it_matters"],
        "",
        "## Major breakthroughs",
        "",
    ]
    lines.extend([f"- {item}" for item in narrative["major_breakthroughs"]])
    lines.extend(
        [
            "",
            "## Mature pipeline direction",
            "",
            narrative["mature_pipeline_direction"],
            "",
            "## Preserve in the final repository",
            "",
        ]
    )
    lines.extend([f"- {item}" for item in narrative["preserve_in_final_repository"]])
    lines.extend(["", "## Archive-only candidates", ""])
    lines.extend([f"- {item}" for item in narrative["archive_only_candidates"]])
    return "\n".join(lines) + "\n"


def render_open_questions(notes: dict[str, Any]) -> str:
    lines = [
        "# Remaining Open Questions",
        "",
        "Only refactor-relevant unresolved questions are listed here. These are not a dump of all Phase 1 ambiguities.",
    ]
    for index, item in enumerate(notes["open_questions"], start=1):
        lines.extend(
            [
                "",
                f"## {index}. {item['question']}",
                "",
                f"- Why it matters: {item['why_it_matters']}",
                f"- Affected notebooks or checkpoints: {item['affected_artifacts']}",
                f"- Current best interpretation: {item['current_best_interpretation']}",
                f"- Confidence: `{item['confidence']}`",
            ]
        )
    return "\n".join(lines) + "\n"


def render_evolution_readme(synthesis_seed_text: str) -> str:
    seed_note = "present" if "Phase 2 Synthesis Seed" in synthesis_seed_text else "not parsed"
    return "\n".join(
        [
            "# Evolution Docs",
            "",
            "This directory is the generated Phase 2 synthesis layer. It is built from the completed Phase 1 audit bundle and the curated Phase 2 notes layer.",
            "",
            "## Files",
            "",
            "- [notebook_evolution_map.md](notebook_evolution_map.md)",
            "- [notebook_lineage.csv](notebook_lineage.csv)",
            "- [revision_diffs.md](revision_diffs.md)",
            "- [checkpoint_inventory.csv](checkpoint_inventory.csv)",
            "- [dataset_inventory.csv](dataset_inventory.csv)",
            "- [component_inventory.csv](component_inventory.csv)",
            "- [final_architecture_synthesis.md](final_architecture_synthesis.md)",
            "- [project_narrative_final.md](project_narrative_final.md)",
            "- [open_questions_remaining.md](open_questions_remaining.md)",
            "",
            "## Upstream Inputs",
            "",
            "- [../file-audit/manifest.csv](../file-audit/manifest.csv)",
            "- [../file-audit/checkpoint-companion-summary.md](../file-audit/checkpoint-companion-summary.md)",
            "- [../file-audit/notebooks/](../file-audit/notebooks/)",
            f"- [../final_synthesis_outline.md](../final_synthesis_outline.md) ({seed_note})",
            "",
            "## Generation Rule",
            "",
            "Only `scripts/generate_evolution_docs.py` writes this directory. Handwritten synthesis prose lives in `scripts/evolution_manual_notes.py`.",
        ]
    ) + "\n"


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def validate_outputs(
    notebook_rows: list[dict[str, str]],
    model_rows: list[dict[str, str]],
    lineage_rows: list[dict[str, str]],
    checkpoint_rows: list[dict[str, str]],
    dataset_rows: list[dict[str, str]],
    component_rows: list[dict[str, str]],
    companion_entries: dict[str, dict[str, Any]],
) -> None:
    errors: list[str] = []
    required_paths = [
        LINEAGE_OUTPUT,
        EVOLUTION_MAP_OUTPUT,
        REVISION_DIFFS_OUTPUT,
        CHECKPOINT_INVENTORY_OUTPUT,
        DATASET_INVENTORY_OUTPUT,
        COMPONENT_INVENTORY_OUTPUT,
        ARCHITECTURE_OUTPUT,
        NARRATIVE_OUTPUT,
        OPEN_QUESTIONS_OUTPUT,
        README_OUTPUT,
    ]
    for path in required_paths:
        if not path.exists():
            errors.append(f"Missing required output: {path}")
    notebook_names = {row["source_name"] for row in notebook_rows}
    lineage_names = {row["notebook_name"] for row in lineage_rows}
    if len(lineage_rows) != 57:
        errors.append(f"Expected 57 lineage rows, found {len(lineage_rows)}")
    if notebook_names != lineage_names:
        errors.append("Lineage notebook set does not match manifest notebook set.")
    allowed_confidence = {"high", "medium", "low"}
    if any(row["confidence"] not in allowed_confidence for row in lineage_rows):
        errors.append("Lineage CSV contains invalid confidence values.")
    bundled_model_names = {row["source_name"] for row in model_rows}
    checkpoint_inventory_names = {row["checkpoint_name"] for row in checkpoint_rows}
    missing_bundled_models = sorted(bundled_model_names - checkpoint_inventory_names)
    if missing_bundled_models:
        errors.append(f"Bundled checkpoints missing from checkpoint inventory: {missing_bundled_models}")
    architecture_text = ARCHITECTURE_OUTPUT.read_text(encoding="utf-8") if ARCHITECTURE_OUTPUT.exists() else ""
    for heading in REQUIRED_ARCHITECTURE_SECTIONS:
        if heading not in architecture_text:
            errors.append(f"Missing architecture synthesis section: {heading}")
    revision_text = REVISION_DIFFS_OUTPUT.read_text(encoding="utf-8") if REVISION_DIFFS_OUTPUT.exists() else ""
    required_transition_markers = [
        "Monolithic baseline -> compact proof of concept",
        "Compact proof of concept -> staged synthetic/real research pipeline",
        "Baseline segmentation -> geometry and calibration aware extraction",
        "Weak localization -> YOLO-assisted lead extraction",
        "Synthetic-only emphasis -> phase-10 real-image pseudo-label fine-tuning",
        "Phase-7 architecture switch -> Phase-8 optimization retune",
        "Large research notebooks -> compact Kaggle submission runners",
        "Early compact runner -> self-contained robustness and helper-driven deployment",
        "Single-model path -> notebook (42) ensemble competitor branch",
        "Ensemble branch -> EfficientNet-B3 integration branch",
        "Monolithic compact engine -> modular final notebook (56)",
    ]
    for marker in required_transition_markers:
        if marker not in revision_text:
            errors.append(f"Missing revision-diff transition: {marker}")
    milestone_notebooks = {
        "ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb",
        "ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb",
        "ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb",
        "ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb",
    }
    if not milestone_notebooks.issubset(lineage_names):
        errors.append("One or more milestone notebooks are missing from notebook_lineage.csv.")
    if any(not row["dataset_name"].strip() for row in dataset_rows):
        errors.append("Dataset inventory contains unnamed rows.")
    if any(not row["component_name"].strip() for row in component_rows):
        errors.append("Component inventory contains unnamed rows.")
    if any(not row["checkpoint_name"].strip() for row in checkpoint_rows):
        errors.append("Checkpoint inventory contains unnamed rows.")
    if not companion_entries:
        errors.append("Checkpoint companion summary could not be parsed.")
    if errors:
        raise SystemExit("\n".join(errors))


if __name__ == "__main__":
    main()
