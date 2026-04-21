from __future__ import annotations

from typing import Any


def _nb(number: int) -> str:
    return f"ecg-sim2real-datagenerator-mohamad-sabbagh ({number}).ipynb"


SOURCE_SCORE_VERSIONS = [
    33,
    34,
    35,
    36,
    38,
    40,
    41,
    42,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
]


STRUCTURAL_ANCHOR = {
    "version": 57,
    "notebook_name": _nb(56),
    "confidence": "high",
    "why": (
        "Notebook (56) is the clearest refactor origin because it separates bootstrap, "
        "path resolution, model loading, inference helpers, formatting, validation, and "
        "diagnostic cells into a modular late-stage execution flow."
    ),
    "limitations": [
        "It depends on runtime path discovery more than a future repository should.",
        "Its observed notebook run ended in an import exception, so it is not the best direct runtime anchor.",
    ],
}


PERFORMANCE_ANCHOR = {
    "primary_version": 50,
    "primary_notebook": _nb(49),
    "secondary_version": 46,
    "secondary_notebook": _nb(45),
    "confidence": "medium",
    "metric": (
        "Best-known score tier from the currently preserved competition history context, "
        "using private score as the preferred metric when numeric values are later backfilled."
    ),
    "why_primary": (
        "Version 50 sits on the late EfficientNet-B3 deployment line while still looking like a "
        "successful compact Kaggle runner, making it the strongest available runtime anchor that also "
        "aligns with the late architectural direction."
    ),
    "why_secondary": (
        "Version 46 is an earlier score-proven compact runtime reference that keeps the detector "
        "plus phase-10 lineage intact and serves as a fallback design check when late EffB3 behavior diverges."
    ),
    "best_known_versions": [46, 50],
    "exception_versions": [56, 57],
}


SHARED_STABLE_COMPONENTS = [
    {
        "name": "YOLO detector with `best.pt`",
        "why": "Present across the mature compact eras and still referenced by the modular late notebooks.",
    },
    {
        "name": "Compact offline Kaggle bootstrap shell",
        "why": "Both anchors assume a self-contained runner that can load local wheels and ship `submission.csv`.",
    },
    {
        "name": "Calibration, trace extraction, and submission formatting core",
        "why": "These remain non-negotiable survivors across the score-proven and structurally mature lineages.",
    },
    {
        "name": "Explicit schema and submission validation",
        "why": "Late compact notebooks and the modular rewrite both preserve validation as part of runtime correctness.",
    },
]


DIVERGENT_COMPONENTS = [
    {
        "name": "Segmentation default",
        "structural_anchor_view": "Late modular notebooks promote EffB3-aware loading and dual-path logic.",
        "performance_anchor_view": "Score-proven behavior peaks before the final modular rewrite and still keeps phase-10 as an active companion.",
        "decision": "Hybrid: EffB3 primary, phase-10 explicit fallback.",
    },
    {
        "name": "Bootstrap and model path resolution",
        "structural_anchor_view": "Generalized discovery and modular helpers.",
        "performance_anchor_view": "Compact hard-coded Kaggle paths that were already score-proven.",
        "decision": "Structural anchor for module design, but with explicit config instead of notebook-style auto-discovery.",
    },
    {
        "name": "Diagnostics and debug cells",
        "structural_anchor_view": "Late notebooks surface diagnostics more clearly.",
        "performance_anchor_view": "Best-known score lineages do not require them on the hot path.",
        "decision": "Keep as opt-in tooling only.",
    },
    {
        "name": "Ensemble/competitor logic from notebook (42)",
        "structural_anchor_view": "Useful provenance but not central to the modular final engine.",
        "performance_anchor_view": "No preserved evidence that full ensemble execution beat the compact single-primary runtime line.",
        "decision": "Research/archive, not core runtime.",
    },
]


DECISION_MATRIX = [
    {
        "subsystem": "detector",
        "adoption": "hybrid adoption",
        "anchor": "shared stable component",
        "policy": "Keep the project-specific YOLO detector as a core runtime module, exposed through the structural anchor layout.",
        "core_scope": "core runtime",
    },
    {
        "subsystem": "segmentation",
        "adoption": "hybrid adoption",
        "anchor": "performance anchor for behavior, structural anchor for loading shape",
        "policy": "Use EffB3 as the default runtime segmentation path and preserve the phase-10 branch as an explicit fallback.",
        "core_scope": "core runtime",
    },
    {
        "subsystem": "fallback selection",
        "adoption": "hybrid adoption",
        "anchor": "hybrid",
        "policy": "Replace implicit notebook branching with an explicit selector that can choose primary or fallback checkpoints deterministically.",
        "core_scope": "core runtime",
    },
    {
        "subsystem": "calibration",
        "adoption": "hybrid adoption",
        "anchor": "performance anchor behavior inside structural modules",
        "policy": "Preserve the score-proven calibration behavior while expressing it as a dedicated module.",
        "core_scope": "core runtime",
    },
    {
        "subsystem": "extraction",
        "adoption": "hybrid adoption",
        "anchor": "performance anchor behavior inside structural modules",
        "policy": "Keep Viterbi/adaptive extraction logic as a first-class runtime subsystem.",
        "core_scope": "core runtime",
    },
    {
        "subsystem": "filtering",
        "adoption": "hybrid adoption",
        "anchor": "performance anchor",
        "policy": "Retain only the filtering steps that were clearly part of the score-proven late compact behavior; treat extra signal polishing as optional.",
        "core_scope": "core runtime",
    },
    {
        "subsystem": "validation",
        "adoption": "structural anchor",
        "anchor": "structural anchor",
        "policy": "Promote validation/export into a clean module that always runs before submission emission.",
        "core_scope": "core runtime",
    },
    {
        "subsystem": "bootstrap",
        "adoption": "structural anchor",
        "anchor": "structural anchor",
        "policy": "Use the modular late-lineage bootstrap shape, but freeze model paths and wheel handling behind config rather than ad hoc notebook discovery.",
        "core_scope": "core runtime",
    },
    {
        "subsystem": "debug utilities",
        "adoption": "optional only",
        "anchor": "structural anchor",
        "policy": "Retain renderer, visual diagnostics, and notebook-style checks as tooling outside the default inference path.",
        "core_scope": "optional research/debug",
    },
]


RUNTIME_SCOPE = {
    "core_runtime": [
        "YOLO detection via `best.pt`.",
        "EffB3 segmentation as the primary path.",
        "Phase-10 segmentation as the explicit fallback path.",
        "Checkpoint selector, calibration, trace extraction, timing normalization, and submission validation/export.",
        "Config-driven bootstrap and deterministic path resolution.",
    ],
    "optional_research_debug": [
        "Synthetic renderer as a debug/inspection tool.",
        "Visual diagnostics, coverage checks, and notebook-style sanity plots.",
        "Model comparison helpers and controlled fallback benchmarking.",
    ],
    "archive_only": [
        "Full ensemble execution logic from notebook (42) and its compact packaging branch.",
        "Temporary competitor bootstrap checkpoints such as `temp_deeplab_base.pt` and `temp_effnet_base.pt`.",
        "Historical environment-repair retries that existed only to keep Kaggle notebooks alive.",
    ],
}


MODEL_SELECTION_POLICY = {
    "primary_model": "best_model_effb3_phase9_ddp (2).pth",
    "primary_alias": "EffB3 primary segmentation path",
    "fallback_model": "best_model_phase10.pth",
    "fallback_alias": "phase-10 fallback segmentation path",
    "selector_policy": (
        "Core runtime must use an explicit, config-driven selector. The selector chooses the primary model by default "
        "and can switch to the fallback by configuration or controlled failover."
    ),
    "auto_discovery_policy": (
        "Notebook-style auto-discovery of whatever checkpoint happens to exist on Kaggle input mounts is forbidden in core runtime. "
        "Discovery may survive only in debug/tooling modules."
    ),
    "rationale": [
        "EffB3 is the best fit for the late architectural direction and for the best-known score lineage candidate at version 50.",
        "Phase-10 remains the strongest historically trusted fallback and is already paired with late compact notebooks.",
    ],
    "confidence": "medium",
}


DEBUG_BOUNDARY = {
    "runtime": [
        "Minimal logging needed for deterministic inference, checkpoint selection, and export validation.",
    ],
    "debug_tooling": [
        "Renderer-backed qualitative inspection.",
        "Visual lead crops, waveform overlays, and pid coverage diagnostics.",
        "Ad hoc comparison helpers for primary vs fallback segmentation behavior.",
    ],
    "archive_only": [
        "Notebook-only sanity cells that exist purely as interactive exploration without clean function boundaries.",
    ],
}


TRAINING_SCOPE = {
    "include_training_in_final_repo": "optional_research_only",
    "canonical_training_path": (
        "If training survives at all, keep a single canonical training path centered on the mature segmentation branch rather than the full historical notebook zoo."
    ),
    "competitor_branch_policy": (
        "Notebook (42) and its competitor training bundle remain optional research or archive material unless a future benchmark proves they belong in maintained code."
    ),
    "checkpoint_policy": (
        "Keep deployable checkpoints and one clear fallback in the maintained runtime plan; move temporary bootstrap and competitor warm-start artifacts to archive/provenance."
    ),
    "priority": "runtime reproducibility over complete historical training reproduction",
}


REMAINING_AMBIGUITIES = [
    {
        "question": "Whether version 46 or version 50 should be treated as the long-term gold runtime reference once exact score values are backfilled.",
        "why_it_is_acceptable": "Both sit in the best-known score tier, and the adopted policy already names version 50 primary and version 46 secondary.",
        "confidence": "medium",
    },
    {
        "question": "How much of the late filtering stack belongs in the default runtime versus optional signal-polish utilities.",
        "why_it_is_acceptable": "The blueprint already keeps the score-proven filtering core and leaves extra polishing outside the mandatory path.",
        "confidence": "medium",
    },
]


MODULES_TO_BUILD = [
    "config",
    "bootstrap",
    "io/indexing",
    "detector",
    "segmentation",
    "checkpoint_selection",
    "preprocessing",
    "extraction",
    "calibration",
    "postprocessing",
    "validation",
    "submission_export",
]


MODULES_TO_ARCHIVE = [
    "ensemble_experiments",
    "historical_training_notebooks",
    "temporary_bootstrap_checkpoints",
    "interactive_debug_cells",
]


EXPECTED_REPO_STRUCTURE = [
    "src/ecg_digitizer/config/",
    "src/ecg_digitizer/runtime/",
    "src/ecg_digitizer/models/",
    "src/ecg_digitizer/validation/",
    "tools/debug/",
    "research/training/",
    "archive/notebooks/",
    "archive/checkpoints/",
]


PRESERVE_ARTIFACTS = [
    "best.pt",
    "best_model_effb3_phase9_ddp (2).pth",
    "best_model_phase10.pth",
    "sample submission schema checks",
    "late compact inference logic around calibration and extraction",
]


EXCLUDE_ARTIFACTS = [
    "Temporary competitor bootstrap weights (`temp_deeplab_base.pt`, `temp_effnet_base.pt`).",
    "Notebook-only package repair cells that have no clean production equivalent.",
    "Full ensemble runtime path unless later evidence reopens it.",
]


NARRATIVE_GUIDANCE = {
    "repository_objective": (
        "Build a maintainable ECG image digitization repository whose structure comes from the modular late notebook line, "
        "while its runtime-critical behavior stays aligned with the best-known scoring compact line."
    ),
    "final_policy": (
        "Use a dual-anchor refactor: structural modules inherit from notebook (56), but runtime defaults inherit from the version-50 score-proven compact path, "
        "with version 46 retained as a secondary behavioral reference."
    ),
}


def load_refactor_planning_notes() -> dict[str, Any]:
    return {
        "source_score_versions": SOURCE_SCORE_VERSIONS,
        "structural_anchor": STRUCTURAL_ANCHOR,
        "performance_anchor": PERFORMANCE_ANCHOR,
        "shared_stable_components": SHARED_STABLE_COMPONENTS,
        "divergent_components": DIVERGENT_COMPONENTS,
        "decision_matrix": DECISION_MATRIX,
        "runtime_scope": RUNTIME_SCOPE,
        "model_selection_policy": MODEL_SELECTION_POLICY,
        "debug_boundary": DEBUG_BOUNDARY,
        "training_scope": TRAINING_SCOPE,
        "remaining_ambiguities": REMAINING_AMBIGUITIES,
        "modules_to_build": MODULES_TO_BUILD,
        "modules_to_archive": MODULES_TO_ARCHIVE,
        "expected_repo_structure": EXPECTED_REPO_STRUCTURE,
        "preserve_artifacts": PRESERVE_ARTIFACTS,
        "exclude_artifacts": EXCLUDE_ARTIFACTS,
        "narrative_guidance": NARRATIVE_GUIDANCE,
    }
