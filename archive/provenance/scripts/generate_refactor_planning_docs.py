from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from refactor_planning_manual_notes import load_refactor_planning_notes


ROOT = Path(__file__).resolve().parents[1]
EVOLUTION_ROOT = ROOT / "docs" / "evolution"
REFACTOR_ROOT = ROOT / "docs" / "refactor_planning"
SOURCE_SCORE_PATH = REFACTOR_ROOT / "source_score_history.csv"

LINEAGE_PATH = EVOLUTION_ROOT / "notebook_lineage.csv"
CHECKPOINTS_PATH = EVOLUTION_ROOT / "checkpoint_inventory.csv"
COMPONENTS_PATH = EVOLUTION_ROOT / "component_inventory.csv"
ARCHITECTURE_PATH = EVOLUTION_ROOT / "final_architecture_synthesis.md"
OPEN_QUESTIONS_PATH = EVOLUTION_ROOT / "open_questions_remaining.md"

README_OUTPUT = REFACTOR_ROOT / "README.md"
SCORE_REGISTRY_OUTPUT = REFACTOR_ROOT / "score_registry.csv"
PERFORMANCE_LINEAGE_OUTPUT = REFACTOR_ROOT / "performance_lineage.md"
ARCHITECTURE_VS_PERFORMANCE_OUTPUT = REFACTOR_ROOT / "architecture_vs_performance_decision.md"
FINAL_RUNTIME_SCOPE_OUTPUT = REFACTOR_ROOT / "final_runtime_scope.md"
MODEL_SELECTION_OUTPUT = REFACTOR_ROOT / "model_selection_policy.md"
DEBUG_BOUNDARY_OUTPUT = REFACTOR_ROOT / "debug_boundary_decision.md"
TRAINING_SCOPE_OUTPUT = REFACTOR_ROOT / "training_scope_decision.md"
BLUEPRINT_OUTPUT = REFACTOR_ROOT / "refactor_blueprint.md"


def main() -> None:
    notes = load_refactor_planning_notes()
    lineage_rows = load_csv(LINEAGE_PATH)
    checkpoint_rows = load_csv(CHECKPOINTS_PATH)
    component_rows = load_csv(COMPONENTS_PATH)
    source_score_rows = load_csv(SOURCE_SCORE_PATH)
    architecture_text = ARCHITECTURE_PATH.read_text(encoding="utf-8")
    open_questions_text = OPEN_QUESTIONS_PATH.read_text(encoding="utf-8")

    lineage_by_name = {row["notebook_name"]: row for row in lineage_rows}
    validate_inputs(source_score_rows, lineage_by_name, notes, architecture_text, open_questions_text)
    score_registry_rows = build_score_registry(source_score_rows, lineage_by_name)
    top_versions = determine_top_versions(score_registry_rows, notes)
    checkpoint_summary = build_checkpoint_summary(checkpoint_rows)

    REFACTOR_ROOT.mkdir(parents=True, exist_ok=True)
    write_csv(
        SCORE_REGISTRY_OUTPUT,
        [
            "version",
            "notebook_name",
            "status",
            "public_score",
            "private_score",
            "branch_or_era",
            "milestone_group",
            "notes",
        ],
        score_registry_rows,
    )
    write_text(README_OUTPUT, render_readme(notes, top_versions))
    write_text(PERFORMANCE_LINEAGE_OUTPUT, render_performance_lineage(notes, score_registry_rows, top_versions))
    write_text(
        ARCHITECTURE_VS_PERFORMANCE_OUTPUT,
        render_architecture_vs_performance(notes, checkpoint_summary),
    )
    write_text(FINAL_RUNTIME_SCOPE_OUTPUT, render_final_runtime_scope(notes))
    write_text(MODEL_SELECTION_OUTPUT, render_model_selection_policy(notes, checkpoint_summary))
    write_text(DEBUG_BOUNDARY_OUTPUT, render_debug_boundary(notes))
    write_text(TRAINING_SCOPE_OUTPUT, render_training_scope(notes))
    write_text(BLUEPRINT_OUTPUT, render_refactor_blueprint(notes, checkpoint_summary, top_versions))

    validate_outputs(score_registry_rows, notes)

    print("Phase 3 refactor planning generated successfully.")
    print(f"- Score registry rows: {len(score_registry_rows)}")
    print(f"- Output root: {REFACTOR_ROOT}")


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


def validate_inputs(
    source_score_rows: list[dict[str, str]],
    lineage_by_name: dict[str, dict[str, str]],
    notes: dict[str, Any],
    architecture_text: str,
    open_questions_text: str,
) -> None:
    required_source_fields = ["version", "notebook_name", "status", "public_score", "private_score", "notes"]
    if not source_score_rows:
        raise SystemExit("source_score_history.csv is empty.")
    for field in required_source_fields:
        if field not in source_score_rows[0]:
            raise SystemExit(f"source_score_history.csv is missing required field: {field}")
    expected_versions = set(notes["source_score_versions"])
    actual_versions = {int(row["version"]) for row in source_score_rows}
    missing_versions = expected_versions - actual_versions
    if missing_versions:
        raise SystemExit(f"source_score_history.csv is missing versions: {sorted(missing_versions)}")
    for row in source_score_rows:
        if not row["version"] or not row["notebook_name"] or not row["status"]:
            raise SystemExit("Every source score row must include version, notebook_name, and status.")
        if row["notebook_name"] not in lineage_by_name:
            raise SystemExit(f"Unknown notebook in source score history: {row['notebook_name']}")
    if "## 12. Final likely architecture" not in architecture_text:
        raise SystemExit("Phase 2 final architecture synthesis is missing the required final architecture section.")
    if "Remaining Open Questions" not in open_questions_text:
        raise SystemExit("Phase 2 open questions file is missing.")


def build_score_registry(
    source_score_rows: list[dict[str, str]],
    lineage_by_name: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in sorted(source_score_rows, key=lambda item: int(item["version"])):
        lineage_row = lineage_by_name[row["notebook_name"]]
        rows.append(
            {
                "version": row["version"],
                "notebook_name": row["notebook_name"],
                "status": row["status"],
                "public_score": row["public_score"],
                "private_score": row["private_score"],
                "branch_or_era": lineage_row["phase_label"],
                "milestone_group": lineage_row["milestone_group"],
                "notes": row["notes"],
            }
        )
    return rows


def determine_top_versions(score_registry_rows: list[dict[str, str]], notes: dict[str, Any]) -> dict[str, Any]:
    performance = notes["performance_anchor"]
    primary = next(row for row in score_registry_rows if int(row["version"]) == performance["primary_version"])
    secondary = next(row for row in score_registry_rows if int(row["version"]) == performance["secondary_version"])
    return {
        "primary": primary,
        "secondary": secondary,
        "exceptions": [
            row for row in score_registry_rows if int(row["version"]) in set(performance["exception_versions"])
        ],
        "best_known": [
            row for row in score_registry_rows if int(row["version"]) in set(performance["best_known_versions"])
        ],
    }


def build_checkpoint_summary(checkpoint_rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row["canonical_name"]: row for row in checkpoint_rows}


def render_readme(notes: dict[str, Any], top_versions: dict[str, Any]) -> str:
    structural = notes["structural_anchor"]
    performance = notes["performance_anchor"]
    return f"""
# Refactor Planning

This directory is the generated Phase 3 planning layer. It does not refactor code; it translates the Phase 1 audit and Phase 2 synthesis into a performance-aware refactor decision set.

## Key decisions

- Structural anchor: version {structural["version"]} / `{structural["notebook_name"]}`
- Performance anchor: version {performance["primary_version"]} / `{performance["primary_notebook"]}`
- Secondary performance reference: version {performance["secondary_version"]} / `{performance["secondary_notebook"]}`
- Exception regression markers: {", ".join(f"v{row['version']}" for row in top_versions["exceptions"])}

## Files

- `source_score_history.csv`: authoritative raw score/planning input used in this phase.
- `score_registry.csv`: source score history enriched with era and milestone labels from Phase 2.
- `performance_lineage.md`: explains which lineage scored best and how it diverges from the structural endpoint.
- `architecture_vs_performance_decision.md`: explicit dual-anchor decision file with subsystem matrix.
- `final_runtime_scope.md`: classifies project pieces into core runtime, optional tooling, or archive.
- `model_selection_policy.md`: runtime model default and fallback policy.
- `debug_boundary_decision.md`: runtime vs tooling vs archive split for diagnostics and renderer behavior.
- `training_scope_decision.md`: defines how much training code belongs in the future repository.
- `refactor_blueprint.md`: final Phase 3 blueprint for Phase 4 construction.
"""


def render_performance_lineage(
    notes: dict[str, Any],
    score_registry_rows: list[dict[str, str]],
    top_versions: dict[str, Any],
) -> str:
    structural = notes["structural_anchor"]
    performance = notes["performance_anchor"]
    primary = top_versions["primary"]
    secondary = top_versions["secondary"]
    exceptions = top_versions["exceptions"]
    scored_versions = ", ".join(f"v{row['version']}" for row in score_registry_rows)
    exception_text = ", ".join(f"v{row['version']} ({row['notebook_name']})" for row in exceptions)
    return f"""
# Performance Lineage

## Evidence scope

- Observed facts:
  - The preserved score-history context identifies versions `46` and `50` as the best-known scoring tier.
  - Versions `56` and `57` are treated as exception regressions.
  - The structural endpoint is version `{structural["version"]}` / `{structural["notebook_name"]}`.
  - The scored versions represented in this phase are: {scored_versions}.
- Interpretation:
  - Peak score happened before the modular endpoint.
  - The best scoring lineage and the best structural lineage are related, but not identical.

## Best-scoring lineage

- Primary performance anchor: version {primary["version"]} / `{primary["notebook_name"]}`
  - Why: {performance["why_primary"]}
- Secondary performance reference: version {secondary["version"]} / `{secondary["notebook_name"]}`
  - Why: {performance["why_secondary"]}

## What the score history implies

- Observed facts:
  - Version {primary["version"]} belongs to the `{primary["branch_or_era"]}` era.
  - Version {secondary["version"]} belongs to the `{secondary["branch_or_era"]}` era.
  - Structural improvements continued into the final modular notebook, but the latest two tracked versions are exception rows: {exception_text}.
- Interpretation:
  - The project's best-known runtime behavior lives in the compact late deployment family, not in the final modular notebook run itself.
  - Later work improved maintainability, checkpoint management, and module separation, but did not preserve guaranteed peak runtime behavior automatically.

## Era-level interpretation

- Score-improving eras:
  - Late compact ensemble-to-EffB3 transition around versions 46 and 50.
  - Compact deployment hardening before full modularization.
- Maintainability-oriented eras:
  - The modular finalization notebooks culminating in version 57.
  - Late diagnostic and path-hardening revisions where clarity improved more than preserved score evidence.

## Final Phase 3 reading

- Structural anchor and performance anchor are intentionally separated.
- Performance decisions should borrow the runtime-critical behavior from version 50 first, version 46 second.
- Repository architecture decisions should still borrow from version 57.
- Confidence: `{performance["confidence"]}`
"""


def render_architecture_vs_performance(
    notes: dict[str, Any],
    checkpoint_summary: dict[str, dict[str, str]],
) -> str:
    structural = notes["structural_anchor"]
    performance = notes["performance_anchor"]
    shared = "\n".join(f"- {item['name']}: {item['why']}" for item in notes["shared_stable_components"])
    divergent = "\n".join(
        (
            f"### {item['name']}\n"
            f"- Structural anchor view: {item['structural_anchor_view']}\n"
            f"- Performance anchor view: {item['performance_anchor_view']}\n"
            f"- Adopted decision: {item['decision']}"
        )
        for item in notes["divergent_components"]
    )
    matrix_rows = "\n".join(
        f"| {item['subsystem']} | {item['adoption']} | {item['anchor']} | {item['policy']} | {item['core_scope']} |"
        for item in notes["decision_matrix"]
    )
    effb3 = checkpoint_summary["best_model_effb3_phase9_ddp"]
    phase10 = checkpoint_summary["best_model_phase10"]
    return f"""
# Architecture Vs Performance Decision

## Structural anchor

- Selected notebook: version {structural["version"]} / `{structural["notebook_name"]}`
- Reason:
  - {structural["why"]}
Limitations:
{chr(10).join(f"- {item}" for item in structural["limitations"])}

## Performance anchor

- Primary runtime reference: version {performance["primary_version"]} / `{performance["primary_notebook"]}`
- Secondary runtime reference: version {performance["secondary_version"]} / `{performance["secondary_notebook"]}`
- Reason:
  - {performance["why_primary"]}
  - {performance["why_secondary"]}

## Shared stable components

{shared}

## Divergent components

{divergent}

## Decision matrix

| Subsystem | Adopted follow rule | Anchor bias | Final planning policy | Scope |
| --- | --- | --- | --- | --- |
{matrix_rows}

## Final adopted planning policy

- Evidence:
  - `best.pt` remains active across the mature lineages.
  - `{effb3['checkpoint_name']}` is the late active primary candidate.
  - `{phase10['checkpoint_name']}` remains the trusted fallback-active checkpoint.
- Planning inference:
  - Final repository structure should follow the modular late notebook line.
  - Final runtime defaults should follow the best-known scoring compact line.
- Adopted policy:
  - Use a dual-anchor design.
  - Borrow structure from version {structural["version"]}.
  - Borrow runtime-critical behavior from version {performance["primary_version"]}, with version {performance["secondary_version"]} as a secondary score-proven reference.
  - Keep ensemble logic, renderer-heavy exploration, and temporary bootstrap artifacts out of the default runtime.
"""


def render_final_runtime_scope(notes: dict[str, Any]) -> str:
    scope = notes["runtime_scope"]
    return f"""
# Final Runtime Scope

## Core runtime

{chr(10).join(f"- {item}" for item in scope["core_runtime"])}

## Optional research/debug module

{chr(10).join(f"- {item}" for item in scope["optional_research_debug"])}

## Archive only

{chr(10).join(f"- {item}" for item in scope["archive_only"])}

## Subsystem callouts

- YOLO detection: `core runtime`
- EffB3 segmentation: `core runtime`
- Phase-10 segmentation fallback: `core runtime`
- Notebook (42) ensemble logic: `archive only` by default
- Renderer: `optional research/debug`
- Diagnostics: `optional research/debug`
- Bootstrap/environment logic: `core runtime`, but rewritten in modular form
- Training-only artifacts: `archive only` or `optional research`
- Temporary competitor checkpoints: `archive only`
- Validation/export logic: `core runtime`
"""


def render_model_selection_policy(
    notes: dict[str, Any],
    checkpoint_summary: dict[str, dict[str, str]],
) -> str:
    policy = notes["model_selection_policy"]
    effb3 = checkpoint_summary["best_model_effb3_phase9_ddp"]
    phase10 = checkpoint_summary["best_model_phase10"]
    return f"""
# Model Selection Policy

## Final policy

- Primary model: `{policy["primary_model"]}`
- Fallback model: `{policy["fallback_model"]}`
- Explicit selector required: `yes`
- Core runtime auto-discovery allowed: `no`

## Evidence

- Observed facts:
  - `{effb3['checkpoint_name']}` is marked `active` in the Phase 2 checkpoint inventory.
  - `{phase10['checkpoint_name']}` is marked `fallback-active`.
  - Version `50` is a best-known score-tier candidate and sits on the EffB3 integration line.
- Planning inference:
  - EffB3 is the best primary default for the future runtime because it matches the late-lineage direction and a top-scoring candidate lineage.
  - Phase-10 remains the safest explicit fallback because it is historically dominant, long-lived, and still paired with late compact notebooks.

## Selector behavior

- {policy["selector_policy"]}
- {policy["auto_discovery_policy"]}

## Rationale

{chr(10).join(f"- {item}" for item in policy["rationale"])}

## Confidence

- `{policy["confidence"]}`
"""


def render_debug_boundary(notes: dict[str, Any]) -> str:
    boundary = notes["debug_boundary"]
    return f"""
# Debug Boundary Decision

## Runtime

{chr(10).join(f"- {item}" for item in boundary["runtime"])}

## Debug/tooling

{chr(10).join(f"- {item}" for item in boundary["debug_tooling"])}

## Archive only

{chr(10).join(f"- {item}" for item in boundary["archive_only"])}

## Decision

- Renderer and visual diagnostics survive as opt-in tooling, not as mandatory runtime stages.
- Notebook-style sanity cells should be rewritten only if they become clean reusable tools; otherwise they stay archived.
"""


def render_training_scope(notes: dict[str, Any]) -> str:
    training = notes["training_scope"]
    return f"""
# Training Scope Decision

## Final decision

- Training code in the final repository: `{training['include_training_in_final_repo']}`
- Priority: `{training['priority']}`

## Policy

- {training["canonical_training_path"]}
- {training["competitor_branch_policy"]}
- {training["checkpoint_policy"]}

## Interpretation

- Phase 4 should prioritize a clean inference repository first.
- Training provenance may survive later, but only behind a single maintained path rather than the full notebook family.
"""


def render_refactor_blueprint(
    notes: dict[str, Any],
    checkpoint_summary: dict[str, dict[str, str]],
    top_versions: dict[str, Any],
) -> str:
    structural = notes["structural_anchor"]
    performance = notes["performance_anchor"]
    narrative = notes["narrative_guidance"]
    return f"""
# Refactor Blueprint

## 1. Final repository objective

- {narrative["repository_objective"]}

## 2. Structural anchor notebook(s)

- Primary structural anchor: version {structural["version"]} / `{structural["notebook_name"]}`

## 3. Performance anchor notebook(s)/versions

- Primary performance anchor: version {performance["primary_version"]} / `{performance["primary_notebook"]}`
- Secondary performance reference: version {performance["secondary_version"]} / `{performance["secondary_notebook"]}`
- Exception regressions excluded from anchor eligibility: {", ".join(f'v{row["version"]}' for row in top_versions["exceptions"])}

## 4. Final adopted runtime pipeline

- Config-driven bootstrap
- YOLO detection via `best.pt`
- EffB3 primary segmentation
- Phase-10 fallback segmentation
- Calibration and trace extraction
- Quality-aware postprocessing
- Validation and submission export

## 5. Modules to build

{chr(10).join(f"- `{item}`" for item in notes["modules_to_build"])}

## 6. Modules to archive

{chr(10).join(f"- `{item}`" for item in notes["modules_to_archive"])}

## 7. Expected repository structure

{chr(10).join(f"- `{item}`" for item in notes["expected_repo_structure"])}

## 8. Artifacts to preserve

{chr(10).join(f"- {item}" for item in notes["preserve_artifacts"])}

## 9. Artifacts to exclude

{chr(10).join(f"- {item}" for item in notes["exclude_artifacts"])}

## 10. Acceptable remaining ambiguities

{chr(10).join(f"- {item['question']} ({item['confidence']})" for item in notes["remaining_ambiguities"])}

## Final planning policy

- {narrative["final_policy"]}
"""


def validate_outputs(score_registry_rows: list[dict[str, str]], notes: dict[str, Any]) -> None:
    required_outputs = [
        README_OUTPUT,
        SCORE_REGISTRY_OUTPUT,
        PERFORMANCE_LINEAGE_OUTPUT,
        ARCHITECTURE_VS_PERFORMANCE_OUTPUT,
        FINAL_RUNTIME_SCOPE_OUTPUT,
        MODEL_SELECTION_OUTPUT,
        DEBUG_BOUNDARY_OUTPUT,
        TRAINING_SCOPE_OUTPUT,
        BLUEPRINT_OUTPUT,
    ]
    for path in required_outputs:
        if not path.exists():
            raise SystemExit(f"Missing generated output: {path}")
    if len(score_registry_rows) != len(notes["source_score_versions"]):
        raise SystemExit("score_registry.csv row count does not match the configured source versions.")
    registry_text = SCORE_REGISTRY_OUTPUT.read_text(encoding="utf-8")
    if "56," not in registry_text or "57," not in registry_text:
        raise SystemExit("score_registry.csv is missing the required exception versions.")
    blueprint_text = BLUEPRINT_OUTPUT.read_text(encoding="utf-8")
    required_sections = [
        "## 1. Final repository objective",
        "## 2. Structural anchor notebook(s)",
        "## 3. Performance anchor notebook(s)/versions",
        "## 4. Final adopted runtime pipeline",
        "## 5. Modules to build",
        "## 6. Modules to archive",
        "## 7. Expected repository structure",
        "## 8. Artifacts to preserve",
        "## 9. Artifacts to exclude",
        "## 10. Acceptable remaining ambiguities",
    ]
    for section in required_sections:
        if section not in blueprint_text:
            raise SystemExit(f"refactor_blueprint.md is missing required section: {section}")


if __name__ == "__main__":
    main()
