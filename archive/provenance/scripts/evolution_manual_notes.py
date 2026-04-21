from __future__ import annotations

from typing import Any


MAIN_NOTEBOOK = "ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb"


def _nb(number: int) -> str:
    return f"ecg-sim2real-datagenerator-mohamad-sabbagh ({number}).ipynb"


ERAS: list[dict[str, Any]] = [
    {
        "title": "Early monolithic baseline",
        "phase_label": "early-monolithic-baseline",
        "milestone_group": "baseline-origin",
        "start_order": 1,
        "end_order": 1,
        "default_branch_type": "baseline",
        "default_major_change_type": "monolithic-provenance",
        "default_status": "superseded",
        "default_confidence": "medium",
        "intent": (
            "Establish the original end-to-end thesis: synthetic ECG page rendering, "
            "segmentation training, Viterbi-style extraction, calibration, and Kaggle "
            "competition file handling all live in one notebook."
        ),
        "key_survivors": [
            "Synthetic renderer as a controllable debug and data-generation surface.",
            "Probability-map to waveform conversion through dynamic-programming / Viterbi-style extraction.",
            "Competition-oriented calibration and submission formatting as explicit downstream goals.",
        ],
        "superseded_elements": [
            "One notebook owning every responsibility at once.",
            "Heavy dependence on execution order rather than explicit boundaries between data generation, training, and inference.",
        ],
        "uncertainty_hotspots": [
            "Some early branches are preserved only through outputs and code comments, not explicit project-level rationale.",
        ],
    },
    {
        "title": "Compact proof-of-concept consolidation",
        "phase_label": "compact-proof-of-concept",
        "milestone_group": "proof-of-concept",
        "start_order": 2,
        "end_order": 2,
        "default_branch_type": "consolidation",
        "default_major_change_type": "proof-of-concept-compaction",
        "default_status": "superseded",
        "default_confidence": "high",
        "intent": (
            "Compress the monolithic baseline into a rerunnable demonstration notebook that still "
            "exercises synthetic training, qualitative visualization, calibration, and real-image smoke testing."
        ),
        "key_survivors": [
            "Visual quality control via stored plots and renderer outputs.",
            "Synthetic-to-real bridging as an explicit goal rather than an accidental side effect of the large baseline notebook.",
        ],
        "superseded_elements": [
            "Most exploratory side branches from the original notebook.",
        ],
        "uncertainty_hotspots": [],
    },
    {
        "title": "Synthetic-to-real staged research branch",
        "phase_label": "synthetic-to-real-staged-research",
        "milestone_group": "staged-research",
        "start_order": 3,
        "end_order": 7,
        "default_branch_type": "refinement",
        "default_major_change_type": "staged-research-expansion",
        "default_status": "superseded",
        "default_confidence": "medium",
        "intent": (
            "Turn the proof-of-concept notebook into a staged research program with separate lanes for "
            "synthetic rendering, calibration, page-level localization, real-data tuning, and early detector preparation."
        ),
        "key_survivors": [
            "Staged segmentation, calibration, and page-processing helpers.",
            "The idea that detector support and geometric reasoning belong in the same workflow as segmentation.",
            "Real-data adaptation as a persistent continuation of synthetic pretraining rather than a separate project.",
        ],
        "superseded_elements": [
            "The assumption that simple crop splitting is sufficient for page localization.",
            "The early quality-boost factory as a final destination rather than a stepping stone toward a more disciplined pipeline.",
        ],
        "uncertainty_hotspots": [
            "Checkpoint lineage from these research notebooks into the later compact deployment family is historically plausible but not always explicit.",
        ],
    },
    {
        "title": "Architecture hardening and combat-detector era",
        "phase_label": "architecture-hardening-combat-detector",
        "milestone_group": "combat-hardening",
        "start_order": 8,
        "end_order": 10,
        "default_branch_type": "refinement",
        "default_major_change_type": "architecture-hardening",
        "default_status": "superseded",
        "default_confidence": "medium",
        "intent": (
            "Make architecture search, detector robustness, and harder real-image adaptation first-class concerns, "
            "culminating in phase-10 pseudo-label fine-tuning and the first explicit platinum final build."
        ),
        "key_survivors": [
            "Combat-mode YOLO lead detector lineage.",
            "ResNet50 plus scSE segmentation family and later phase-10 weights.",
            "More explicit calibration, filtering, and adaptive extraction logic for difficult real pages.",
        ],
        "superseded_elements": [
            "Earlier baseline segmentation checkpoints as the only intended deployment path.",
        ],
        "uncertainty_hotspots": [
            "The exact handoff from these large research notebooks into the later compact deployment notebooks remains partly historical.",
        ],
    },
    {
        "title": "Compact deployment and robustness iteration",
        "phase_label": "compact-deployment-robustness",
        "milestone_group": "compact-deployment",
        "start_order": 11,
        "end_order": 42,
        "default_branch_type": "refinement",
        "default_major_change_type": "compact-deployment-hardening",
        "default_status": "superseded",
        "default_confidence": "high",
        "intent": (
            "Collapse the large research notebooks into compact Kaggle runners, then iterate repeatedly on no-internet "
            "bootstrap strategy, runtime resilience, schema safety, identifier parsing, timing normalization, and self-contained helpers."
        ),
        "key_survivors": [
            "Compact offline install/import shell.",
            "Renderer retained as a debug and interpretation surface rather than as the main training engine.",
            "YOLO plus segmentation inference, calibration, signal extraction, and submission validation.",
        ],
        "superseded_elements": [
            "In-notebook training as part of routine submission runs.",
            "Assuming a stable Kaggle environment without custom wheel handling or defensive path logic.",
        ],
        "uncertainty_hotspots": [
            "Not every compact notebook contributes a lasting idea; many are environment or robustness retries around the same engine core.",
        ],
    },
    {
        "title": "Ensemble competitor branch",
        "phase_label": "ensemble-competitor-branch",
        "milestone_group": "ensemble-branch",
        "start_order": 43,
        "end_order": 49,
        "default_branch_type": "refinement",
        "default_major_change_type": "ensemble-branch-packaging",
        "default_status": "superseded",
        "default_confidence": "high",
        "intent": (
            "Reopen the compact deployment story to train and benchmark multiple segmentation families, "
            "then package the resulting checkpoints into compact offline comparison notebooks."
        ),
        "key_survivors": [
            "EfficientNet-B3 and DeepLabV3+ competitor checkpoints.",
            "Evidence that the phase-10 branch became a baseline to compare against, not just a fixed final answer.",
        ],
        "superseded_elements": [
            "The assumption that one inherited segmentation model is the only serious deployment option.",
        ],
        "uncertainty_hotspots": [
            "Phase 1 evidence does not fully resolve whether the full ensemble direction was a serious final target or mainly a benchmarking branch.",
        ],
    },
    {
        "title": "EfficientNet-B3 integration and modular finalization",
        "phase_label": "effb3-integration-modular-finalization",
        "milestone_group": "effb3-finalization",
        "start_order": 50,
        "end_order": 57,
        "default_branch_type": "refinement",
        "default_major_change_type": "effb3-deployment-hardening",
        "default_status": "superseded",
        "default_confidence": "high",
        "intent": (
            "Promote the EfficientNet-B3 branch into the active deployment path, then harden path lookup, "
            "diagnostics, checkpoint selection, and finally modularize the whole compact engine."
        ),
        "key_survivors": [
            "EfficientNet-B3 as a first-class deployed segmentation option.",
            "Checkpoint selection and fallback logic as part of the runtime contract.",
            "Explicit diagnostics, path resolution, and modular helper structure in the final notebook.",
        ],
        "superseded_elements": [
            "Pure ensemble benchmarking as the dominant late-stage theme.",
            "Single giant inference cells with meaning encoded only in descriptive headings.",
        ],
        "uncertainty_hotspots": [
            "The exact default checkpoint pairing in the final modular notebook can still depend on Kaggle input layout and discovered files.",
        ],
    },
]


NOTEBOOK_OVERRIDES: dict[str, dict[str, Any]] = {
    MAIN_NOTEBOOK: {
        "notes": (
            "Original provenance notebook; conceptually the root of the whole project even though later notebooks split its responsibilities."
        ),
    },
    _nb(1): {
        "branch_type": "consolidation",
        "major_change_type": "proof-of-concept-compaction",
        "notes": "First successful compaction of the monolithic baseline into a rerunnable demonstration notebook.",
    },
    _nb(7): {
        "branch_type": "milestone",
        "major_change_type": "architecture-switch-and-combat-detector-hardening",
        "notes": (
            "Turns stronger segmentation architecture and combat-mode YOLO training into an explicit late-stage strategy."
        ),
    },
    _nb(9): {
        "branch_type": "milestone",
        "major_change_type": "real-image-pseudolabel-finetuning",
        "notes": (
            "Represents the last large single-model research notebook and the clearest phase-10 fine-tuning milestone."
        ),
    },
    _nb(10): {
        "branch_type": "milestone",
        "major_change_type": "compact-inference-collapse",
        "notes": (
            "Collapses the research branch into a compact Kaggle runner and starts the long deployment-hardening era."
        ),
    },
    _nb(31): {
        "branch_type": "milestone",
        "major_change_type": "self-contained-offline-refactor",
        "confidence": "medium",
        "notes": (
            "Bridge notebook where the compact shell becomes helper-driven and more self-contained for no-internet Kaggle execution."
        ),
    },
    _nb(42): {
        "branch_type": "branch",
        "major_change_type": "multi-checkpoint-ensemble-provenance",
        "status": "uncertain",
        "confidence": "medium",
        "notes": (
            "Reopens training after the compact era to create the phase-10, EfficientNet-B3, and DeepLabV3+ competitor bundle. "
            "Conceptual ancestor is notebook (9) even though the primary predecessor in review order is notebook (41)."
        ),
    },
    _nb(43): {
        "branch_type": "consolidation",
        "major_change_type": "ensemble-branch-packaging",
        "notes": "Packages notebook (42) into a compact runner so ensemble and benchmark variants can be compared quickly.",
    },
    _nb(44): {
        "branch_type": "dead-end",
        "major_change_type": "baseline-benchmark-detour",
        "notes": (
            "Intentional baseline-only detour used to measure the old single-model path after the ensemble branch opened."
        ),
    },
    _nb(47): {
        "branch_type": "refinement",
        "major_change_type": "winner-oriented-benchmarking",
        "notes": (
            "Shifts from hybridization toward benchmarking around the current ensemble-era winner rather than introducing a new architecture."
        ),
    },
    _nb(48): {
        "branch_type": "dead-end",
        "major_change_type": "benchmark-lock-in-rerun",
        "notes": (
            "Near-duplicate benchmark lock-in rerun that confirms a deployment shell but does not add a new long-term component."
        ),
    },
    _nb(49): {
        "branch_type": "milestone",
        "major_change_type": "effb3-integration",
        "notes": (
            "Promotes the EfficientNet-B3 branch from notebook (42) into the active compact deployment path."
        ),
    },
    _nb(54): {
        "branch_type": "refinement",
        "major_change_type": "diagnostic-coverage-check",
        "notes": (
            "Adds explicit pid-to-image coverage diagnostics before inference, making data-index confidence part of runtime behavior."
        ),
    },
    _nb(55): {
        "branch_type": "refinement",
        "major_change_type": "quality-gated-v42-engine",
        "notes": (
            "Replaces the repaired V41 engine with a more heavily quality-gated V42 inference path."
        ),
    },
    _nb(56): {
        "branch_type": "consolidation",
        "major_change_type": "modular-finalization",
        "status": "active",
        "confidence": "medium",
        "notes": (
            "Final modular rewrite and the best candidate for the refactor starting point, although final checkpoint pairing still depends on runtime discovery."
        ),
    },
}


TRANSITIONS: list[dict[str, Any]] = [
    {
        "title": "Monolithic baseline -> compact proof of concept",
        "from_notebooks": [MAIN_NOTEBOOK],
        "to_notebooks": [_nb(1)],
        "observed_change": [
            "The workflow contracts from a monolithic 15-cell research notebook into an 8-cell proof-of-concept.",
            "Synthetic training, calibration, renderer inspection, and real-image smoke tests remain, but most exploratory branches disappear.",
        ],
        "likely_motivation": [
            "Make the original idea rerunnable and inspectable without stepping through every early branch.",
        ],
        "pipeline_impact": [
            "Creates the first compact notebook that can serve as a readable demo and a reusable baseline for later staged research.",
        ],
        "retained_elements": [
            "Synthetic renderer.",
            "Segmentation training.",
            "Qualitative QC plots.",
            "Calibration and real-image testing.",
        ],
        "obsoleted_elements": [
            "Large mixed-responsibility notebook structure.",
            "Implicit dependence on exploratory side branches.",
        ],
        "confidence": "high",
    },
    {
        "title": "Compact proof of concept -> staged synthetic/real research pipeline",
        "from_notebooks": [_nb(1)],
        "to_notebooks": [_nb(2), _nb(3), _nb(4), _nb(5), _nb(6)],
        "observed_change": [
            "The notebook family expands back to long-form structure, but now with clearer stages for rendering, calibration, page-level processing, detector preparation, and real-data adaptation.",
            "Late cells begin to bridge segmentation research with page localization and competition ingestion rather than treating them as separate experiments.",
        ],
        "likely_motivation": [
            "Turn the proof-of-concept into a research program where components can evolve semi-independently before final recombination.",
        ],
        "pipeline_impact": [
            "Creates the first credible lineage for synthetic-to-real transfer and for later detector-assisted inference.",
        ],
        "retained_elements": [
            "Synthetic renderer and segmentation training backbone.",
            "Calibration and quality-control mindset from notebook (1).",
        ],
        "obsoleted_elements": [
            "The idea that a compact demonstration notebook is enough to answer the harder localization and real-domain questions.",
        ],
        "confidence": "high",
    },
    {
        "title": "Baseline segmentation -> geometry and calibration aware extraction",
        "from_notebooks": [_nb(4)],
        "to_notebooks": [_nb(5), _nb(6)],
        "observed_change": [
            "Geometry, calibration, and harder page conditions become explicit themes rather than background helper logic.",
            "The extractor evolves from a segmentation-centered decoder into a more coordinated system that reasons about page alignment and scale.",
        ],
        "likely_motivation": [
            "Simple crop-level extraction was not robust enough for realistic competition pages with skew, scale drift, and clutter.",
        ],
        "pipeline_impact": [
            "Sets up the later mature pipeline where segmentation output is never trusted without geometry and calibration context.",
        ],
        "retained_elements": [
            "Segmentation remains the core waveform-recovery mechanism.",
            "Synthetic-to-real staging remains intact.",
        ],
        "obsoleted_elements": [
            "Purely local extraction assumptions that ignore page geometry.",
        ],
        "confidence": "medium",
    },
    {
        "title": "Weak localization -> YOLO-assisted lead extraction",
        "from_notebooks": [_nb(2), _nb(3), _nb(4), _nb(5), _nb(6)],
        "to_notebooks": [_nb(7)],
        "observed_change": [
            "Notebook (7) makes combat-mode detector hardening explicit and couples it tightly to a stronger segmentation architecture.",
            "Detector checkpoints and YOLO model choices become visible, not just implied by helper code.",
        ],
        "likely_motivation": [
            "Fixed splits and weak localization were too brittle for full-page competition images, especially under skew and clutter.",
        ],
        "pipeline_impact": [
            "Lead detection becomes a dedicated stage of the pipeline and later survives into every compact deployment family.",
        ],
        "retained_elements": [
            "Segmentation-based waveform recovery.",
            "Calibration and page-processing logic from the staged research notebooks.",
        ],
        "obsoleted_elements": [
            "The assumption that page crops can be trusted without detector-assisted localization.",
        ],
        "confidence": "medium",
    },
    {
        "title": "Phase-7 architecture switch -> Phase-8 optimization retune",
        "from_notebooks": [_nb(7)],
        "to_notebooks": [_nb(8)],
        "observed_change": [
            "Notebook (7) changes architecture; notebook (8) keeps that harder detector-aware structure but retunes the segmentation objective and optimizer.",
            "Phase naming and checkpoint references make architecture search and optimization search look like separate consecutive decisions.",
        ],
        "likely_motivation": [
            "The author first validated that the new architecture mattered, then tested whether optimization alone could push the same structure further.",
        ],
        "pipeline_impact": [
            "Separates model-family choice from training-policy choice, which later helps phase-10 and competitor-branch reasoning.",
        ],
        "retained_elements": [
            "Combat YOLO branch.",
            "Stronger segmentation backbone.",
        ],
        "obsoleted_elements": [
            "Treating architecture and optimizer changes as one inseparable experiment.",
        ],
        "confidence": "medium",
    },
    {
        "title": "Synthetic-only emphasis -> phase-10 real-image pseudo-label fine-tuning",
        "from_notebooks": [_nb(8)],
        "to_notebooks": [_nb(9)],
        "observed_change": [
            "Notebook (9) explicitly introduces phase-10 real-world fine-tuning and the first platinum final build.",
            "New phase-10 checkpoint references replace the prior phase-8 emphasis.",
        ],
        "likely_motivation": [
            "Synthetic pretraining had reached its limit; the next gain needed better alignment with real competition pages.",
        ],
        "pipeline_impact": [
            "Phase-10 weights become the dominant single-model checkpoint lineage reused across later notebooks.",
        ],
        "retained_elements": [
            "Combat detector branch.",
            "Geometry and calibration hardening.",
            "Adaptive extraction logic.",
        ],
        "obsoleted_elements": [
            "The assumption that synthetic-only optimization is enough for the final deployment path.",
        ],
        "confidence": "high",
    },
    {
        "title": "Large research notebooks -> compact Kaggle submission runners",
        "from_notebooks": [_nb(9)],
        "to_notebooks": [_nb(10), _nb(11), _nb(12), _nb(13), _nb(14)],
        "observed_change": [
            "Notebook (10) removes in-notebook training and keeps only bootstrap, imports, renderer, final engine, and export validation.",
            "Subsequent compact notebooks stay inference-only and iterate mainly on bootstrap mechanics and schema-safe export.",
        ],
        "likely_motivation": [
            "Submission iteration on Kaggle required faster, smaller notebooks than the late research branch could provide.",
        ],
        "pipeline_impact": [
            "Creates the compact deployment mainline that dominates the middle of the notebook series.",
        ],
        "retained_elements": [
            "YOLO plus segmentation inference core.",
            "Renderer for qualitative inspection.",
            "Competition export validation.",
        ],
        "obsoleted_elements": [
            "Using the full research notebook as the routine submission vehicle.",
        ],
        "confidence": "high",
    },
    {
        "title": "Early compact runner -> self-contained robustness and helper-driven deployment",
        "from_notebooks": [_nb(14), _nb(19)],
        "to_notebooks": [_nb(31), _nb(32), _nb(33), _nb(34), _nb(35), _nb(36), _nb(37), _nb(38), _nb(39), _nb(40), _nb(41)],
        "observed_change": [
            "The compact era shifts from repeated install retries to helper-driven offline package discovery, safer runtime assumptions, and stricter validation.",
            "Per-lead timing, identifier parsing, and post-run sanity checks become recurring explicit concerns.",
        ],
        "likely_motivation": [
            "Real Kaggle failures moved from pure accuracy concerns toward operational issues: package availability, row formatting, path lookup, memory pressure, and silent output corruption.",
        ],
        "pipeline_impact": [
            "Transforms the compact notebook family into a deployment-hardening program rather than just a smaller version of the research branch.",
        ],
        "retained_elements": [
            "Same detector-plus-segmentation inference goal.",
            "Renderer and export validation shell.",
        ],
        "obsoleted_elements": [
            "Trusting the environment, IDs, and timing metadata without defensive checks.",
        ],
        "confidence": "high",
    },
    {
        "title": "Single-model path -> notebook (42) ensemble competitor branch",
        "from_notebooks": [_nb(41)],
        "to_notebooks": [_nb(42)],
        "observed_change": [
            "Notebook (42) expands from a compact six-cell runner into a 26-cell research notebook.",
            "The notebook trains or assembles a three-model competitor bundle: the phase-10 ResNet branch, EfficientNet-B3, and DeepLabV3+.",
        ],
        "likely_motivation": [
            "After long compact hardening, the author reopened research to test whether a broader checkpoint universe could outperform the single inherited winner.",
        ],
        "pipeline_impact": [
            "Creates the provenance source for the extra checkpoints later consumed by compact descendants and the EffB3 deployment branch.",
        ],
        "retained_elements": [
            "Phase-10 lineage.",
            "Combat detector and geometry logic.",
            "Compact-era understanding of difficult competition pages.",
        ],
        "obsoleted_elements": [
            "The assumption that only one segmentation checkpoint deserves deployment attention.",
        ],
        "confidence": "medium",
    },
    {
        "title": "Ensemble packaging -> benchmark detours and winner-oriented branch pruning",
        "from_notebooks": [_nb(42)],
        "to_notebooks": [_nb(43), _nb(44), _nb(45), _nb(46), _nb(47), _nb(48)],
        "observed_change": [
            "The compact descendants of notebook (42) alternate between ensemble, baseline-only, hybrid, and benchmark engines without returning to in-notebook training.",
            "Some notebooks are clear deployment experiments rather than lasting architecture steps.",
        ],
        "likely_motivation": [
            "The author needed quick offline runners to compare several candidate checkpoint mixes under competition conditions.",
        ],
        "pipeline_impact": [
            "Helps identify which competitor branch ideas survive and which become archive-only benchmark detours.",
        ],
        "retained_elements": [
            "Compact offline shell.",
            "Notebook (42) checkpoint bundle.",
        ],
        "obsoleted_elements": [
            "Treating every ensemble-era notebook as part of the final mainline; several are clearly evaluative side paths.",
        ],
        "confidence": "medium",
    },
    {
        "title": "Ensemble branch -> EfficientNet-B3 integration branch",
        "from_notebooks": [_nb(48)],
        "to_notebooks": [_nb(49)],
        "observed_change": [
            "Notebook (49) stops benchmarking around the notebook (42) bundle and explicitly attaches the new EffB3 checkpoint to the compact inference stack.",
            "Checkpoint routing and fallback behavior become part of the notebook contract.",
        ],
        "likely_motivation": [
            "The ensemble branch likely identified EfficientNet-B3 as worth promoting into the deployment mainline.",
        ],
        "pipeline_impact": [
            "Starts the final branch where model selection, fallback, and path resolution matter as much as raw inference logic.",
        ],
        "retained_elements": [
            "Compact no-internet shell.",
            "Phase-10 checkpoint as comparison or fallback.",
            "YOLO detector and submission pipeline.",
        ],
        "obsoleted_elements": [
            "Pure ensemble benchmarking as the main late-stage story.",
        ],
        "confidence": "high",
    },
    {
        "title": "Raw extraction -> quality-gated, calibration-aware compact engines",
        "from_notebooks": [_nb(19), _nb(30)],
        "to_notebooks": [_nb(40), _nb(55)],
        "observed_change": [
            "Across the compact era, signal extraction increasingly depends on timing metadata, gating rules, geometry repair, and explicit fallback behavior.",
            "By notebook (55), the V42 engine includes deskewing, trimming, model selection, and quality gating rather than a simple direct decode.",
        ],
        "likely_motivation": [
            "Competition pages exposed failure modes that could not be solved by raw segmentation output alone.",
        ],
        "pipeline_impact": [
            "Makes post-processing a first-class subsystem instead of a final cosmetic step.",
        ],
        "retained_elements": [
            "DP / Viterbi family extraction.",
            "Calibration and lead-wise reconstruction goals.",
        ],
        "obsoleted_elements": [
            "Trusting a single raw mask-to-wave pass without explicit quality control.",
        ],
        "confidence": "medium",
    },
    {
        "title": "Monolithic compact engine -> modular final notebook (56)",
        "from_notebooks": [_nb(55)],
        "to_notebooks": [_nb(56)],
        "observed_change": [
            "Notebook (56) abandons descriptive engine headings and decomposes the pipeline into install, config, indexing, model loading, utilities, formatting, validation, and debug blocks.",
            "The notebook keeps the detector-plus-segmentation submission goal but changes the operational shape dramatically.",
        ],
        "likely_motivation": [
            "Prepare the notebook family for synthesis and future refactor by exposing stable responsibilities instead of one opaque engine cell.",
        ],
        "pipeline_impact": [
            "Provides the cleanest direct bridge from notebooks to a future module-based repository layout.",
        ],
        "retained_elements": [
            "YOLO plus segmentation inference.",
            "Checkpoint selection and fallback logic.",
            "Submission validation and debug visibility.",
        ],
        "obsoleted_elements": [
            "Encoding most semantics only in notebook headings or a single monolithic inference block.",
        ],
        "confidence": "high",
    },
]


CHECKPOINT_ROWS: list[dict[str, Any]] = [
    {
        "checkpoint_name": "best.pt",
        "canonical_name": "best.pt",
        "aliases": ["best.pt"],
        "role": "Primary 12-class YOLO lead detector artifact used for page-level lead localization.",
        "development_phase": "lead-detector-deployment",
        "replaced_by": "",
        "final_status": "active",
        "confidence": "high",
        "notes": "Survives into the final compact pipeline and the modular notebook.",
    },
    {
        "checkpoint_name": "best_model.pth",
        "canonical_name": "best_model",
        "aliases": ["best_model.pth", "best_model.pt"],
        "role": "Earliest baseline segmentation checkpoint from the synthetic-only stage.",
        "development_phase": "baseline-synthetic-segmentation",
        "replaced_by": "best_model_real_data.pt; best_model_phase2.pt; best_model_phase10",
        "final_status": "superseded",
        "confidence": "medium",
        "notes": "Main notebook saves `best_model.pth`; later notebooks usually refer to a `.pt` variant or successor checkpoints instead.",
    },
    {
        "checkpoint_name": "best_model_real_data.pt",
        "canonical_name": "best_model_real_data",
        "aliases": ["best_model_real_data.pt", "best_model_real_data.pth"],
        "role": "Early real-data adaptation checkpoint bridging synthetic pretraining and later phase-labeled fine-tuning.",
        "development_phase": "early-real-data-adaptation",
        "replaced_by": "best_model_phase10",
        "final_status": "superseded",
        "confidence": "medium",
        "notes": "Referenced across early research notebooks and reused as historical context inside notebook (42).",
    },
    {
        "checkpoint_name": "best_model_phase2.pt",
        "canonical_name": "best_model_phase2",
        "aliases": ["best_model_phase2.pt", "best_model_phase2.pth"],
        "role": "Intermediate hardening-era segmentation checkpoint used in geometry and quality-boost experiments.",
        "development_phase": "phase-2-hardening",
        "replaced_by": "best_model_phase10",
        "final_status": "superseded",
        "confidence": "medium",
        "notes": "Important as a bridge checkpoint, but not part of the final likely architecture.",
    },
    {
        "checkpoint_name": "best_model_phase7.pt",
        "canonical_name": "best_model_phase7",
        "aliases": ["best_model_phase7.pt", "best_model_phase7.pth"],
        "role": "Architecture-hardening checkpoint from the phase-7 branch.",
        "development_phase": "phase-7-architecture-search",
        "replaced_by": "best_model_phase8.pt; best_model_phase10",
        "final_status": "superseded",
        "confidence": "low",
        "notes": "Only lightly evidenced in the audited corpus.",
    },
    {
        "checkpoint_name": "best_model_phase8.pt",
        "canonical_name": "best_model_phase8",
        "aliases": ["best_model_phase8.pt", "best_model_phase8.pth"],
        "role": "Optimization-retuned checkpoint from the phase-8 branch.",
        "development_phase": "phase-8-optimization",
        "replaced_by": "best_model_phase10",
        "final_status": "superseded",
        "confidence": "low",
        "notes": "Appears mainly as a handoff checkpoint before phase-10 fine-tuning takes over.",
    },
    {
        "checkpoint_name": "best_model_phase9.pt",
        "canonical_name": "best_model_phase9",
        "aliases": ["best_model_phase9.pt", "best_model_phase9.pth"],
        "role": "Late pre-phase-10 segmentation checkpoint retained as an alternate or predecessor reference.",
        "development_phase": "phase-9-bridge",
        "replaced_by": "best_model_phase10; best_model_effb3_phase9_ddp",
        "final_status": "superseded",
        "confidence": "medium",
        "notes": "Acts more as lineage evidence than as a clearly surviving deployed artifact.",
    },
    {
        "checkpoint_name": "best_model_phase10.pth",
        "canonical_name": "best_model_phase10",
        "aliases": ["best_model_phase10.pt", "best_model_phase10.pth"],
        "role": "Dominant phase-10 segmentation checkpoint from the real-image pseudo-label fine-tuning era.",
        "development_phase": "phase-10-real-image-finetuning",
        "replaced_by": "best_model_effb3_phase9_ddp (2).pth",
        "final_status": "fallback-active",
        "confidence": "high",
        "notes": "Remains a core fallback or comparison model even after the EffB3 branch becomes first-class.",
    },
    {
        "checkpoint_name": "best_model_deeplab_ph10.pth",
        "canonical_name": "best_model_deeplab_ph10",
        "aliases": ["best_model_deeplab_ph10.pt", "best_model_deeplab_ph10.pth", "temp_deeplab_base.pt"],
        "role": "DeepLabV3+ competitor branch checkpoint family created in the notebook (42) ensemble era.",
        "development_phase": "ensemble-competitor-branch",
        "replaced_by": "",
        "final_status": "archive-benchmark",
        "confidence": "medium",
        "notes": "Important competitor artifact, but Phase 1 evidence does not show it becoming the default final deployment path.",
    },
    {
        "checkpoint_name": "best_model_efficientnet_ph10.pth",
        "canonical_name": "best_model_efficientnet_ph10",
        "aliases": ["best_model_efficientnet_ph10.pt", "best_model_efficientnet_ph10.pth", "temp_effnet_base.pt"],
        "role": "EfficientNet competitor branch created during notebook (42) before the later dedicated EffB3 deployment lineage.",
        "development_phase": "ensemble-competitor-branch",
        "replaced_by": "best_model_effb3_phase9_ddp (2).pth",
        "final_status": "archive-benchmark",
        "confidence": "medium",
        "notes": "Serves as important evidence that EfficientNet-style encoders were being tested before the final EffB3 rollout.",
    },
    {
        "checkpoint_name": "best_model_effb3_phase9_ddp (2).pth",
        "canonical_name": "best_model_effb3_phase9_ddp",
        "aliases": ["best_model_effb3_phase9_ddp (2).pth", "best_model_effb3_phase9_ddp.pt"],
        "role": "Primary EfficientNet-B3 deployment checkpoint promoted into the late compact notebooks.",
        "development_phase": "phase-9-effb3-ddp",
        "replaced_by": "",
        "final_status": "active",
        "confidence": "medium",
        "notes": "Likely becomes the preferred primary segmentation branch in notebooks (49) through (56).",
    },
    {
        "checkpoint_name": "checkpoint_effb3_phase9_ddp (1) (1).pt",
        "canonical_name": "checkpoint_effb3_phase9_ddp_training_state",
        "aliases": ["checkpoint_effb3_phase9_ddp (1) (1).pt"],
        "role": "Full resumable training-state checkpoint for the EffB3 DDP branch.",
        "development_phase": "phase-9-effb3-ddp",
        "replaced_by": "best_model_effb3_phase9_ddp (2).pth",
        "final_status": "training-artifact",
        "confidence": "high",
        "notes": "Not referenced directly by notebooks in the bundle, but crucial for understanding the maturity of the EffB3 branch.",
    },
    {
        "checkpoint_name": "yolov8n.pt",
        "canonical_name": "yolov8n-pretrained",
        "aliases": ["yolov8n.pt"],
        "role": "Generic Ultralytics pretrained detector checkpoint used as a starting point for detector experiments.",
        "development_phase": "detector-bootstrap",
        "replaced_by": "best.pt",
        "final_status": "bootstrap-only",
        "confidence": "low",
        "notes": "Acts as upstream initialization rather than a project-specific final artifact.",
    },
    {
        "checkpoint_name": "yolov8l.pt",
        "canonical_name": "yolov8l-pretrained",
        "aliases": ["yolov8l.pt"],
        "role": "Larger pretrained YOLO variant used in detector experimentation.",
        "development_phase": "detector-bootstrap",
        "replaced_by": "best.pt",
        "final_status": "bootstrap-only",
        "confidence": "low",
        "notes": "Used to test detector scale choices before settling on project-specific detector artifacts.",
    },
    {
        "checkpoint_name": "yolov8m.pt",
        "canonical_name": "yolov8m-pretrained",
        "aliases": ["yolov8m.pt"],
        "role": "Medium pretrained YOLO variant used in detector experimentation.",
        "development_phase": "detector-bootstrap",
        "replaced_by": "best.pt",
        "final_status": "bootstrap-only",
        "confidence": "low",
        "notes": "Appears as an alternative detector initialization rather than a persistent project artifact.",
    },
    {
        "checkpoint_name": "yolov8x.pt",
        "canonical_name": "yolov8x-pretrained",
        "aliases": ["yolov8x.pt"],
        "role": "Large pretrained YOLO variant used in the combat detector branch and notebook (42) experiments.",
        "development_phase": "detector-bootstrap",
        "replaced_by": "best.pt",
        "final_status": "bootstrap-only",
        "confidence": "low",
        "notes": "Important as detector training provenance, not as the final deployed detector.",
    },
]


DATASET_ROWS: list[dict[str, Any]] = [
    {
        "dataset_name": "Synthetic renderer outputs",
        "canonical_identifier": "synthetic-rendered-ecg-pages",
        "path_or_reference": "synthetic_dataset/images; synthetic_dataset/masks; {OUTPUT_DIR}/images; {OUTPUT_DIR}/masks",
        "data_type": "synthetic",
        "patterns": [
            "synthetic_dataset/images",
            "synthetic_dataset/masks",
            "{output_dir}/images",
            "{output_dir}/masks",
        ],
        "role": "Synthetic supervision and debugging corpus generated inside notebooks for segmentation training and visual QC.",
        "replaced_by": "Supplemented by PhysioNet competition pages rather than fully replaced.",
        "confidence": "high",
        "notes": "Core to the early research branch and preserved conceptually as a debug renderer even after compact deployment takes over.",
    },
    {
        "dataset_name": "PhysioNet ECG digitization image corpus",
        "canonical_identifier": "physionet-ecg-image-digitization-pages",
        "path_or_reference": "/kaggle/input/physionet-ecg-image-digitization",
        "data_type": "real",
        "patterns": [
            "/kaggle/input/physionet-ecg-image-digitization",
            "image_dir",
        ],
        "role": "Primary real-image competition corpus for training, validation, smoke tests, and final inference.",
        "replaced_by": "",
        "confidence": "high",
        "notes": "This dataset remains central from the earliest real-image smoke tests through the final compact notebooks.",
    },
    {
        "dataset_name": "PhysioNet competition metadata tables",
        "canonical_identifier": "physionet-ecg-image-digitization-metadata",
        "path_or_reference": "train.csv; test.csv; sample_submission.parquet",
        "data_type": "metadata",
        "patterns": [
            "train.csv",
            "test.csv",
            "sample_submission.parquet",
            "submission.parquet",
        ],
        "role": "Competition metadata used for sample schema validation, per-record timing, and final export formatting.",
        "replaced_by": "",
        "confidence": "high",
        "notes": "Becomes increasingly important in the compact era as timing and schema correctness move into the center of the workflow.",
    },
    {
        "dataset_name": "PTB-XL waveform corpus",
        "canonical_identifier": "ptb-xl-waveforms",
        "path_or_reference": "PTB-XL; records100; wfdb.rdsamp",
        "data_type": "real",
        "patterns": [
            "ptb-xl",
            "records100",
            "wfdb.rdsamp",
            "db_dir",
        ],
        "role": "Waveform source used to drive synthetic rendering and later compact renderer-backed debugging flows.",
        "replaced_by": "",
        "confidence": "medium",
        "notes": "Phase 1 evidence clearly shows PTB-XL loading and fallback behavior, although exact coverage across compact notebooks varies.",
    },
    {
        "dataset_name": "Generated YOLO lead-detection dataset",
        "canonical_identifier": "generated-yolo-lead-dataset",
        "path_or_reference": "yolo_dataset/data.yaml; yolo_dataset/labels; {BASE_DIR}/images; {BASE_DIR}/labels",
        "data_type": "synthetic",
        "patterns": [
            "yolo_dataset/data.yaml",
            "yolo_dataset/labels/",
            "{base_dir}/images/train",
            "{base_dir}/labels/train",
            "{base_dir}/images/val",
            "{base_dir}/labels/val",
        ],
        "role": "Intermediate detector-training dataset generated inside notebooks to bootstrap and harden lead localization.",
        "replaced_by": "best.pt",
        "confidence": "medium",
        "notes": "Important as a generated training asset, even though the final repository should likely preserve only the generation logic rather than the transient files themselves.",
    },
    {
        "dataset_name": "Offline wheel bundle inputs",
        "canonical_identifier": "kaggle-offline-wheel-bundles",
        "path_or_reference": "/kaggle/input/**/*.whl",
        "data_type": "support",
        "patterns": [
            "/kaggle/input/**/*.whl",
            "/kaggle/input/**/**/*.whl",
            "/kaggle/input/**/*{wheel_hint}*.whl",
        ],
        "role": "No-internet dependency source used by compact deployment notebooks to repair Kaggle runtimes.",
        "replaced_by": "",
        "confidence": "high",
        "notes": "Operational support asset rather than model-training data, but central to the deployable notebook family.",
    },
]


COMPONENT_ROWS: list[dict[str, Any]] = [
    {
        "component_name": "Synthetic ECG renderer",
        "introduced_in": MAIN_NOTEBOOK,
        "matured_in": _nb(1),
        "deprecated_in": "",
        "role": "Generates synthetic ECG pages and later survives as a qualitative debug surface.",
        "final_architecture_included": "yes",
        "confidence": "high",
        "notes": "Starts as a data-generation engine and ends as an inspection tool for compact inference notebooks.",
    },
    {
        "component_name": "PTB-XL signal source",
        "introduced_in": _nb(10),
        "matured_in": _nb(19),
        "deprecated_in": "",
        "role": "Provides waveform primitives for synthetic or renderer-backed debug flows.",
        "final_architecture_included": "no",
        "confidence": "medium",
        "notes": "Important for research and debugging lineage, but not part of the final competition inference loop.",
    },
    {
        "component_name": "YOLO lead detector",
        "introduced_in": _nb(2),
        "matured_in": _nb(7),
        "deprecated_in": "",
        "role": "Localizes 12-lead regions on competition pages before segmentation and decoding.",
        "final_architecture_included": "yes",
        "confidence": "high",
        "notes": "Best represented by `best.pt` in the final likely architecture.",
    },
    {
        "component_name": "ResNet50 U-Net family",
        "introduced_in": _nb(7),
        "matured_in": _nb(9),
        "deprecated_in": "",
        "role": "Main segmentation family behind the dominant phase-10 checkpoint lineage.",
        "final_architecture_included": "yes",
        "confidence": "high",
        "notes": "Likely survives as the legacy or fallback segmentation path once EffB3 is integrated.",
    },
    {
        "component_name": "EfficientNet-B3 U-Net family",
        "introduced_in": _nb(42),
        "matured_in": _nb(49),
        "deprecated_in": "",
        "role": "Late competitor and then promoted deployment segmentation family.",
        "final_architecture_included": "yes",
        "confidence": "medium",
        "notes": "Appears to become the preferred primary segmentation branch in the final compact era.",
    },
    {
        "component_name": "DeepLabV3+ branch",
        "introduced_in": _nb(42),
        "matured_in": _nb(46),
        "deprecated_in": _nb(49),
        "role": "Competitor segmentation branch used for multi-checkpoint comparison and ensemble experiments.",
        "final_architecture_included": "no",
        "confidence": "medium",
        "notes": "Important as a benchmark and provenance branch, not as the final deployed default.",
    },
    {
        "component_name": "Pseudo-labeling on real competition images",
        "introduced_in": _nb(9),
        "matured_in": _nb(9),
        "deprecated_in": "",
        "role": "Bridges synthetic pretraining and real-page fine-tuning for the phase-10 model family.",
        "final_architecture_included": "no",
        "confidence": "high",
        "notes": "Training-stage component rather than a runtime component, but essential to the phase-10 lineage.",
    },
    {
        "component_name": "Viterbi trace extraction",
        "introduced_in": MAIN_NOTEBOOK,
        "matured_in": _nb(9),
        "deprecated_in": "",
        "role": "Converts segmentation probability maps into one-dimensional waveforms.",
        "final_architecture_included": "yes",
        "confidence": "high",
        "notes": "One of the clearest long-lived algorithmic survivors from the earliest notebooks to the final branch.",
    },
    {
        "component_name": "Adaptive extraction and quality gating",
        "introduced_in": _nb(9),
        "matured_in": _nb(55),
        "deprecated_in": "",
        "role": "Adds SNR-aware path selection, fallback behavior, and confidence-aware decoding.",
        "final_architecture_included": "yes",
        "confidence": "medium",
        "notes": "Becomes especially visible in the V42-style late compact engines.",
    },
    {
        "component_name": "Calibration",
        "introduced_in": MAIN_NOTEBOOK,
        "matured_in": _nb(5),
        "deprecated_in": "",
        "role": "Maps pixel-space traces back to plausible physical scale using grid spacing and geometry cues.",
        "final_architecture_included": "yes",
        "confidence": "high",
        "notes": "A core survivor; later notebooks only change how calibration is estimated and trusted.",
    },
    {
        "component_name": "Grid removal",
        "introduced_in": _nb(5),
        "matured_in": _nb(9),
        "deprecated_in": "",
        "role": "Suppresses ECG paper grid and background clutter before or during segmentation.",
        "final_architecture_included": "yes",
        "confidence": "medium",
        "notes": "Remains part of the mature inference logic even when exact implementations change.",
    },
    {
        "component_name": "Filtering",
        "introduced_in": _nb(9),
        "matured_in": _nb(9),
        "deprecated_in": _nb(56),
        "role": "Signal-domain cleanup such as high-pass removal of baseline wander and smoothing.",
        "final_architecture_included": "uncertain",
        "confidence": "medium",
        "notes": "Clearly important in the platinum research build, but not always explicit in the final modular notebook.",
    },
    {
        "component_name": "Resampling and timing normalization",
        "introduced_in": MAIN_NOTEBOOK,
        "matured_in": _nb(40),
        "deprecated_in": "",
        "role": "Normalizes lead lengths and sampling assumptions to match competition output expectations.",
        "final_architecture_included": "yes",
        "confidence": "high",
        "notes": "Becomes a defining theme of the compact deployment hardening era.",
    },
    {
        "component_name": "Submission validation",
        "introduced_in": MAIN_NOTEBOOK,
        "matured_in": _nb(41),
        "deprecated_in": "",
        "role": "Checks schema, row counts, IDs, and output formatting before submission export.",
        "final_architecture_included": "yes",
        "confidence": "high",
        "notes": "A persistent and increasingly explicit survivor across the notebook series.",
    },
    {
        "component_name": "Ensemble logic",
        "introduced_in": _nb(42),
        "matured_in": _nb(46),
        "deprecated_in": _nb(49),
        "role": "Combines or compares multiple segmentation families inside one inference path.",
        "final_architecture_included": "no",
        "confidence": "medium",
        "notes": "Valuable for experimentation and checkpoint selection, but not clearly the final operational default.",
    },
    {
        "component_name": "Modular final execution flow",
        "introduced_in": _nb(56),
        "matured_in": _nb(56),
        "deprecated_in": "",
        "role": "Separates bootstrap, config, indexing, model loading, utility logic, formatting, validation, and debugging.",
        "final_architecture_included": "yes",
        "confidence": "high",
        "notes": "This is the clearest direct bridge to a future refactor-ready repository structure.",
    },
]


ARCHITECTURE_SECTIONS: dict[str, dict[str, Any]] = {
    "project_objective": {
        "observed": [
            "The notebook family repeatedly targets competition-ready reconstruction from ECG images into long-format submission files.",
            "From the earliest notebook onward, segmentation output is treated as an intermediate representation that must be converted into 1D waveforms.",
        ],
        "synthesis": (
            "The project solves ECG image-to-signal reconstruction for the PhysioNet digitization competition. "
            "Its stable objective is not generic image segmentation, but recovering calibrated multi-lead waveforms from scanned or rendered ECG pages and writing competition-safe outputs."
        ),
    },
    "evolution_timeline": {
        "observed": [
            "The ordered notebook chain moves from monolithic research, to staged synthetic/real research, to compact deployment, to an ensemble competitor branch, and finally to EffB3 integration plus modular finalization.",
            "Milestone notebooks include the main notebook, notebook (1), notebook (9), notebook (10), notebook (42), notebook (49), and notebook (56).",
        ],
        "synthesis": (
            "The project evolved in discrete eras rather than as one smooth line. "
            "Each era answers a different question: can segmentation recover traces at all, can the pipeline survive real pages, can it run reliably on Kaggle, does a broader checkpoint family help, and which late-stage path should anchor a future refactor."
        ),
    },
    "renderer_evolution": {
        "observed": [
            "The renderer starts as a synthetic data factory in the earliest notebooks.",
            "Compact notebooks keep renderer cells even after training disappears, usually as a visual debugging or sanity-check surface.",
        ],
        "synthesis": (
            "The renderer survives because it does double duty. "
            "Early on it manufactures supervision; later it provides an interpretable surface for checking detector crops, predicted masks, and reconstructed traces. "
            "A refactor should preserve the renderer as a debug and evaluation utility even if synthetic training becomes a separate submodule."
        ),
    },
    "dataset_and_input_evolution": {
        "observed": [
            "Synthetic rendered images and masks dominate the earliest notebooks.",
            "PhysioNet competition files appear early and then remain present through the final modular notebook.",
            "PTB-XL loading appears explicitly in later research and compact notebooks as a waveform source.",
        ],
        "synthesis": (
            "The data strategy becomes progressively layered: synthetic data establishes the segmentation thesis, real competition pages expose domain gaps, "
            "and PTB-XL acts as a reusable waveform source that keeps the renderer grounded in realistic rhythms. "
            "By the end, the operational runtime depends on competition pages plus metadata, while synthetic and PTB-XL assets mainly support training and debugging."
        ),
    },
    "model_evolution": {
        "observed": [
            "Early notebooks train a baseline segmentation branch directly on synthetic assets.",
            "Notebook (7) upgrades the segmentation architecture and detector hardening together.",
            "Notebook (9) creates the dominant phase-10 checkpoint, while notebook (42) creates DeepLabV3+ and EfficientNet competitor branches.",
            "Notebooks (49) through (56) promote the EffB3 branch into active deployment decisions.",
        ],
        "synthesis": (
            "Model evolution follows a clear pattern: baseline synthetic segmentation, stronger architecture plus detector hardening, phase-10 real-image fine-tuning, "
            "competitor expansion, then EffB3-centered deployment. "
            "The final likely architecture is not a generic ensemble; it is a detector plus segmentation system where EffB3 appears primary and phase-10 remains a trusted fallback."
        ),
    },
    "checkpoint_evolution": {
        "observed": [
            "Checkpoint names progress from baseline and real-data variants to numbered phase checkpoints, then to competitor-specific names and EffB3 DDP artifacts.",
            "The companion summary shows `best.pt` and `best_model_phase10` as especially durable lineages, with later EffB3 artifacts becoming increasingly prominent.",
        ],
        "synthesis": (
            "Checkpoint naming mirrors project maturity. "
            "Early checkpoints encode experimentation, phase-10 marks the mature single-model branch, notebook (42) expands the candidate set, and EffB3 artifacts signal the late transition from research comparison to deployment selection."
        ),
    },
    "detection_and_cropping_evolution": {
        "observed": [
            "Detector preparation appears in early staged research notebooks.",
            "Notebook (7) makes combat detector training explicit, and compact notebooks thereafter assume a detector-backed lead localization stage.",
            "Late notebooks keep fallback split logic when YOLO or exact localization is unavailable.",
        ],
        "synthesis": (
            "Lead detection evolves from an auxiliary branch into a non-negotiable front end. "
            "The mature pipeline expects YOLO-backed crops first and only falls back to geometric splitting when the detector or page structure fails."
        ),
    },
    "segmentation_evolution": {
        "observed": [
            "Segmentation is present from the baseline notebook onward.",
            "The project later distinguishes between the phase-10 ResNet family, DeepLabV3+, and EfficientNet-B3 competitors.",
        ],
        "synthesis": (
            "Segmentation remains the central waveform-recovery mechanism, but the project learns that model-family choice matters. "
            "The final synthesis should treat segmentation as a pluggable stage with at least one primary model and one fallback-capable alternate lineage."
        ),
    },
    "trace_extraction_evolution": {
        "observed": [
            "Viterbi-style extraction is already present in the earliest notebook.",
            "Later notebooks introduce adaptive and quality-gated variants rather than abandoning the DP family.",
        ],
        "synthesis": (
            "Trace extraction is one of the strongest long-lived technical through-lines. "
            "The project never replaces Viterbi-style decoding outright; it progressively wraps it in calibration, adaptive weighting, and fallback logic."
        ),
    },
    "calibration_and_postprocessing_evolution": {
        "observed": [
            "Calibration helpers appear in the earliest notebooks and become more explicit in the geometry-heavy research branch.",
            "Notebook (9) adds signal-domain cleanup such as high-pass filtering and smarter post-processing.",
            "Late compact notebooks emphasize deskewing, trimming, gating, and per-lead timing normalization.",
        ],
        "synthesis": (
            "Post-processing grows from helper code into a major subsystem. "
            "The late notebooks show that segmentation alone is not sufficient; calibration, deskewing, gating, and sometimes filtering are necessary to produce competition-safe waveforms."
        ),
    },
    "submission_pipeline_evolution": {
        "observed": [
            "Submission writers exist from the earliest notebook.",
            "Compact notebooks repeatedly refine schema checks, row-count validation, ID formatting, and metadata-driven timing.",
        ],
        "synthesis": (
            "Submission generation becomes a serious engineering concern rather than a final line of code. "
            "By the compact era, the project treats export correctness as a first-class stage that deserves dedicated logic and diagnostics."
        ),
    },
    "final_likely_architecture": {
        "observed": [
            "Notebook (56) is the final modular rewrite.",
            "Notebooks (49) through (56) make EffB3 a first-class deployed checkpoint while preserving the older phase-10 path.",
            "The final compact notebooks still rely on YOLO detection, calibration-aware decoding, and submission validation.",
        ],
        "synthesis": (
            "The most likely final architecture is: offline Kaggle bootstrap and path resolution -> competition image indexing and diagnostics -> YOLO lead detection (`best.pt`) with fallback crop splitting -> "
            "primary EffB3 segmentation with phase-10 fallback or selector -> calibration, cleanup, and adaptive DP/Viterbi trace extraction -> per-lead timing normalization -> validated submission export. "
            "The renderer survives as an optional debug surface, not as the main runtime dependency."
        ),
    },
    "remaining_ambiguities": {
        "observed": [
            "Notebook (42) and its descendants do not make the long-term fate of the full ensemble branch fully explicit.",
            "Notebook (56) auto-discovers model paths and still includes a debug cell whose operational status is not fully resolved.",
        ],
        "synthesis": (
            "There are no major blind spots about the broad architecture, but there are still tactical ambiguities around default checkpoint selection, "
            "the archival status of the ensemble branch, and whether some diagnostic blocks should survive as operational components."
        ),
    },
    "refactor_implications": {
        "observed": [
            "Notebook (56) already splits the runtime into coherent blocks.",
            "The compact era stabilizes around detector, segmentation, extraction, formatting, and validation as durable responsibilities.",
        ],
        "synthesis": (
            "Phase 3 refactor planning should treat the final repository as a composition of durable modules: environment/bootstrap, data indexing, detector, segmentation model registry, "
            "geometry and calibration, trace extraction, output formatting, and validation. "
            "Archive candidates are duplicate bootstrap retries, isolated benchmark notebooks, and training-only checkpoint initialization details that do not survive into the final runtime."
        ),
    },
}


PROJECT_NARRATIVE: dict[str, Any] = {
    "overview": (
        "This project is a full ECG image-to-signal reconstruction program built through a long notebook lineage. "
        "Its goal is to recover calibrated multi-lead waveforms from ECG page images and export them in competition-ready long format."
    ),
    "why_it_matters": (
        "The work matters because it tackles the hard boundary between image understanding and signal recovery. "
        "It is not enough to segment traces visually; the pipeline must also preserve timing, amplitude, lead ordering, and submission integrity."
    ),
    "major_breakthroughs": [
        "Turning the original monolithic experiment into a staged synthetic-to-real research pipeline.",
        "Promoting YOLO lead localization into a durable front-end component.",
        "Moving from synthetic-only segmentation to phase-10 real-image pseudo-label fine-tuning.",
        "Hardening the project into compact no-internet Kaggle runners with strong validation and path logic.",
        "Using notebook (42) to open a competitor branch and then promoting EffB3 into the late deployment mainline.",
        "Ending with a modular final notebook that exposes the future repository boundaries directly.",
    ],
    "mature_pipeline_direction": (
        "The mature direction is a detector-plus-segmentation inference pipeline with strong calibration, adaptive extraction, "
        "timing normalization, and schema validation. "
        "EfficientNet-B3 appears to be the late preferred segmentation branch, while the phase-10 model remains the clearest fallback lineage."
    ),
    "preserve_in_final_repository": [
        "YOLO lead detector integration and fallback cropping logic.",
        "Phase-10 and EffB3 checkpoint integration with explicit model-selection behavior.",
        "Calibration, geometry repair, and adaptive DP/Viterbi extraction.",
        "Submission formatting, validation, and diagnostics.",
        "Renderer-backed debugging utilities.",
        "The modular responsibility split embodied by notebook (56).",
    ],
    "archive_only_candidates": [
        "Repeated brute-force offline install retries that do not change the runtime design.",
        "Benchmark-only ensemble descendants that do not survive into the final likely architecture.",
        "Temporary base checkpoints and training bootstrap details from the competitor branch.",
        "Near-duplicate compact runners whose only change is environment recovery rather than algorithmic behavior.",
    ],
}


OPEN_QUESTIONS: list[dict[str, str]] = [
    {
        "question": "Did the full notebook (42) ensemble path ever become the intended final runtime, or did it mainly serve as a checkpoint-generation and benchmarking branch?",
        "why_it_matters": "This determines whether ensemble logic belongs in the Phase 3 core design or only in archival experiment modules.",
        "affected_artifacts": f"{_nb(42)}; {_nb(43)}; {_nb(44)}; {_nb(45)}; {_nb(46)}; {_nb(47)}; {_nb(48)}; best_model_deeplab_ph10.pth; best_model_efficientnet_ph10.pth",
        "current_best_interpretation": (
            "The ensemble branch appears strategically important for generating and comparing competitor checkpoints, "
            "but the final likely deployment path narrows back toward detector plus one primary segmentation checkpoint with fallback."
        ),
        "confidence": "medium",
    },
    {
        "question": "In the final compact notebooks, is EfficientNet-B3 always the intended primary segmentation model, or is model selection meant to remain dynamic between EffB3 and phase-10 weights?",
        "why_it_matters": "Refactor planning needs a default inference contract and a clear story for fallback behavior.",
        "affected_artifacts": f"{_nb(49)}; {_nb(50)}; {_nb(51)}; {_nb(52)}; {_nb(53)}; {_nb(54)}; {_nb(55)}; {_nb(56)}; best_model_effb3_phase9_ddp (2).pth; best_model_phase10.pth",
        "current_best_interpretation": (
            "EffB3 looks like the preferred late-stage primary model, while phase-10 remains a trusted fallback or comparison branch."
        ),
        "confidence": "medium",
    },
    {
        "question": "How direct is the handoff from the large research notebooks into the first compact deployment notebook?",
        "why_it_matters": "This affects whether a future repository should preserve an explicit training-to-deployment export stage or infer it from notebook history.",
        "affected_artifacts": f"{_nb(7)}; {_nb(8)}; {_nb(9)}; {_nb(10)}; best_model_phase10.pth; best.pt",
        "current_best_interpretation": (
            "The handoff is conceptually clear but historically implicit: the compact notebook family packages the phase-10 and detector lineage rather than documenting a separate export notebook."
        ),
        "confidence": "medium",
    },
    {
        "question": "Should the renderer and late diagnostic cells be preserved as operational tools or moved into a debug-only package during refactor?",
        "why_it_matters": "This changes the shape of the final repository and whether visualization lives on the main inference path.",
        "affected_artifacts": f"{MAIN_NOTEBOOK}; {_nb(1)}; {_nb(10)}; {_nb(31)}; {_nb(54)}; {_nb(56)}",
        "current_best_interpretation": (
            "They should survive, but as opt-in debug and validation utilities rather than as mandatory runtime stages."
        ),
        "confidence": "high",
    },
    {
        "question": "What should be done with temporary competitor bootstrap checkpoints such as `temp_deeplab_base.pt` and `temp_effnet_base.pt`?",
        "why_it_matters": "They affect archive scope and whether competitor training provenance is reproducible enough for a cleaned repository.",
        "affected_artifacts": f"{_nb(42)}; temp_deeplab_base.pt; temp_effnet_base.pt",
        "current_best_interpretation": (
            "These artifacts look like branch-specific training initializers that belong in archive or provenance notes rather than the core runtime layout."
        ),
        "confidence": "medium",
    },
]


def load_evolution_notes() -> dict[str, Any]:
    return {
        "eras": ERAS,
        "notebook_overrides": NOTEBOOK_OVERRIDES,
        "transitions": TRANSITIONS,
        "checkpoint_rows": CHECKPOINT_ROWS,
        "dataset_rows": DATASET_ROWS,
        "component_rows": COMPONENT_ROWS,
        "architecture_sections": ARCHITECTURE_SECTIONS,
        "project_narrative": PROJECT_NARRATIVE,
        "open_questions": OPEN_QUESTIONS,
    }
