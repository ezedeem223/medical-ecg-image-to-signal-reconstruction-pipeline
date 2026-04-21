from __future__ import annotations

from copy import deepcopy
from importlib.machinery import SourcelessFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path
import re
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
_LEGACY_NOTES_PATH = SCRIPT_DIR / "file_audit_manual_notes_legacy.pyc"

MAIN_NOTEBOOK = "ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb"

RENDERER_NOTE = (
    "Keeps the high-quality renderer in the notebook as a debugging surface, "
    "so predicted masks and extracted signals can still be inspected visually "
    "before submission export."
)
COMPACT_VALIDATION_NOTE = (
    "Validates the assembled dataframe against the sample-submission schema "
    "and writes the final CSV only after row count and column layout look "
    "consistent."
)
SAFE_LOGIC_CHECK_NOTE = (
    "Runs a stricter final logic check before writing the submission so "
    "schema drift, row-count mismatches, or malformed IDs are caught at the "
    "last stage."
)
SMART_OFFLINE_INSTALL_NOTE = (
    "Bootstraps the environment in smart offline mode by scanning local wheel "
    "sources first, reflecting the assumption that internet access may be "
    "unavailable on Kaggle."
)
SAFE_MINIMAL_INSTALL_NOTE = (
    "Uses the smallest safe offline install path, reducing package churn so "
    "the notebook can focus on inference rather than repeated environment "
    "repair."
)
IMPORT_FIX_NOTE = (
    "Imports the runtime stack and applies the notebook's path or package "
    "fixes immediately, so later cells can assume a stable offline inference "
    "environment."
)
NO_INTERNET_IMPORT_NOTE = (
    "Repairs imports and resolves local package paths explicitly for a "
    "no-internet Kaggle session, so the remaining cells can run without "
    "external downloads."
)
PATH_RESOLVER_NOTE = (
    "Imports the runtime stack and resolves model and data paths dynamically, "
    "making the notebook less dependent on one hard-coded Kaggle directory "
    "layout."
)
EFF_ATTACH_NOTE = (
    "Attaches the newer EfficientNet-B3 checkpoint to the inference stack and "
    "defines how it should replace or complement the older segmentation "
    "weights."
)
DIAGNOSTIC_PID_NOTE = (
    "Measures how many competition IDs can be matched to discovered image "
    "files, exposing mapping gaps before an expensive inference pass begins."
)


def _nb(number: int) -> str:
    return f"ecg-sim2real-datagenerator-mohamad-sabbagh ({number}).ipynb"


def _load_legacy_notes() -> dict[str, Any]:
    if not _LEGACY_NOTES_PATH.exists():
        raise FileNotFoundError(f"Missing legacy manual notes snapshot: {_LEGACY_NOTES_PATH}")
    loader = SourcelessFileLoader("file_audit_manual_notes_legacy", str(_LEGACY_NOTES_PATH))
    spec = spec_from_loader(loader.name, loader)
    if spec is None:
        raise ImportError(f"Could not create import spec for {_LEGACY_NOTES_PATH}")
    module = module_from_spec(spec)
    loader.exec_module(module)
    return deepcopy(module.load_manual_notes())


def _entry(
    notebook_summary: list[str],
    cell_notes: list[str],
    delta_notes: list[str],
    risk_overrides: list[str] | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "expected_cell_count": len(cell_notes),
        "notebook_summary": list(notebook_summary),
        "cell_notes": {index: note for index, note in enumerate(cell_notes, start=1)},
        "delta_notes": list(delta_notes),
    }
    if risk_overrides:
        payload["risk_overrides"] = list(risk_overrides)
    return payload


def _research_notes(training_note: str, tail: list[str], *, advanced_geometry: bool = False, corrected_manual: bool = False) -> list[str]:
    notes = [
        "Bootstraps the environment and prepares for a runtime restart, preserving the assumption that package installation happens inside the notebook rather than upstream.",
        "Loads the runtime stack, shared imports, and path configuration so the rest of the notebook can move between synthetic assets and Kaggle inputs without repeating setup logic.",
        "Keeps a reusable synthetic rendering and data-generation cell in the notebook, because every later training or detector branch still depends on controllable ECG imagery.",
        training_note,
        "Defines the mask-to-signal post-processing helpers, including the dynamic-programming and Viterbi-style logic that translates probability maps into one-dimensional traces.",
        "Executes a focused smoke test with stored outputs so the author can inspect whether the current model and decoder recover a plausible strip before moving to page-level logic.",
        "Wraps the strip decoder into a full-page or multi-lead processing helper, which is required before the notebook can touch real Kaggle pages.",
        "Introduces submission-oriented formatting helpers that reshape reconstructed leads into the schema expected by the competition files.",
        "Loads the official Kaggle metadata and image inventory, turning the notebook from a synthetic-only experiment into one that can address real evaluation inputs.",
        "Adds a real-image inference harness that points the current model stack at actual competition pages and exposes the remaining domain mismatch.",
        "Defines grid-detection and calibration helpers so waveform extraction can be normalized against paper spacing rather than raw pixels alone.",
        "Runs a calibration or visualization sanity pass, confirming whether the grid estimate and lead geometry look stable on representative samples.",
        "Adds a sliding-window or segmented decoding helper for long traces, reducing the chance that local failures corrupt the entire lead.",
        "Adjusts the waveform path solver and post-processing rules so sharp transitions can survive decoding instead of collapsing into an over-smoothed line.",
        "Introduces geometry-aware lead or strip normalization, correcting rotation and alignment assumptions before later detector-assisted versions.",
        "Adds cleanup logic that strips grid remnants or background clutter before the trace is decoded, improving robustness outside the synthetic domain.",
        "Provides a manual validation or crop-level helper used to inspect the current pipeline on chosen examples before the notebook expands into new branches.",
    ]
    if advanced_geometry:
        notes[14] = (
            "Expands the geometry subsystem into an explicit advanced engine "
            "that handles rotation, alignment, and spatial normalization more "
            "aggressively than earlier revisions."
        )
    if corrected_manual:
        notes[16] = (
            "Provides a corrected manual validation helper for chosen "
            "examples, indicating that earlier ad hoc tests were not reliable "
            "enough for later high-stakes inference cells."
        )
    return notes + list(tail)


def _build_notebook_editorial_data() -> dict[str, dict[str, Any]]:
    data: dict[str, dict[str, Any]] = {}

    data[MAIN_NOTEBOOK] = _entry(
        [
            "Initial monolithic research notebook that mixes synthetic data generation, baseline training, Viterbi decoding, Kaggle ingestion, and calibration experiments in one place.",
            "Later notebooks split these responsibilities, but this file remains the provenance source for the earliest end-to-end assumption that mask probabilities can be converted into 1D ECG signals.",
        ],
        [
            "Bootstraps the runtime by installing the full dependency set needed for data generation, CSV handling, model training, and image processing, assuming the environment can restart after package installation.",
            "Imports the core scientific stack, selects device and runtime globals, and establishes the shared configuration objects that every later stage in the notebook reuses.",
            "Builds the earliest synthetic ECG image factory, turning numeric signal templates into rasterized traces plus labels that can supervise a segmentation model.",
            "Defines and launches the baseline segmentation training loop, making this the first cell where synthetic ECG images become reusable trace-mask weights.",
            "Introduces Viterbi-style decoding from a probability map to a single waveform path, which is the conceptual bridge from segmentation output to signal reconstruction.",
            "Scales the same decoding idea from one strip to a full ECG page, coordinating per-strip processing and showing whether page segmentation can be stitched into usable lead-level signals.",
            "Packages the page-level decoder into submission-oriented output formatting, so this cell is the first attempt to align reconstructed signals with the competition deliverable.",
            "Switches from synthetic experiments to official Kaggle assets by mounting and reading the released metadata and sample files that define the real evaluation surface.",
            "Runs the current model on real stored images rather than synthetic renders, exposing the domain gap between clean training data and actual scanned ECG pages.",
            "Defines the first dedicated grid-detection and calibration subsystem, explicitly modeling paper scale so later extraction code can convert pixels into physiologically meaningful amplitudes and durations.",
            "Stress-tests the calibration helpers against representative examples and visual diagnostics, surfacing whether the grid estimate is reliable enough to support downstream measurement.",
            "Adds sliding-window inference for long or irregular strips, addressing the failure mode where a whole lead cannot be decoded robustly in one pass.",
            "Retunes the Viterbi transition logic to allow larger jumps, a direct attempt to preserve sharp QRS morphology instead of over-smoothing the recovered waveform.",
            "Rewrites processing around the images that actually exist on disk, replacing earlier assumed paths with file-driven discovery so inference no longer depends on guessed artifacts.",
            "Closes the notebook by running the image-driven extraction path end to end, making this cell the practical handoff from exploratory research to a file-based reconstruction workflow.",
        ],
        ["First notebook in review order; there is no earlier revision to diff against."],
    )

    data[_nb(1)] = _entry(
        [
            "Compact proof-of-concept rewrite of the monolithic notebook: it keeps synthetic training, visual QC, calibration, and real-image testing while dropping most exploratory branches.",
            "This file is the clearest early demonstration notebook because almost every major stage still emits plots for manual inspection.",
        ],
        [
            "Installs the required packages and expects a runtime restart, creating a clean environment for the compact eight-cell prototype.",
            "Loads the scientific stack, configures device and runtime defaults, and keeps only the globals needed for the reduced demonstration workflow.",
            "Defines the synthetic generator and training inputs that feed the prototype segmentation model, preserving the data-creation side of the original notebook.",
            "Runs model training and plots the learning outcomes, so this cell acts as the main quality checkpoint for the compact experiment.",
            "Packages the extraction algorithms and tests them visually on controlled examples, letting the author inspect whether the decoded signal follows the rendered trace.",
            "Adds calibration and grid-detection diagnostics with plotted overlays, checking whether page scale can be recovered before real-image inference.",
            "Applies the current stack to real ECG images with visual output, explicitly measuring the synthetic-to-real gap instead of assuming the model transfers cleanly.",
            "Saves the final model artifacts and any required outputs, turning the notebook from a pure demo into a reusable checkpoint-producing run.",
        ],
        [
            "Compared with the original notebook, this revision compresses the workflow into eight cells and emphasizes visual validation over exploratory side branches.",
        ],
    )

    data[_nb(2)] = _entry(
        [
            "First large split of the early research pipeline into reusable training, calibration, and detector-preparation stages.",
            "This notebook introduces the bridge from synthetic-only segmentation toward page-level localization and later real-data fine-tuning.",
        ],
        _research_notes(
            "Trains the baseline segmentation model on the synthetic ECG corpus, establishing the mask-prediction backbone that the rest of the notebook experiments with.",
            [
                "Creates synthetic full-page layouts and annotation assets for detector training, establishing the first page-localization dataset inside the notebook series.",
                "Coordinates export of those generated pages and labels to disk, so a detector or layout model can be trained outside the pure segmentation loop.",
                "Defines the first real-data fine-tuning dataset and training wrapper, moving the segmentation model closer to scanned ECG appearance instead of synthetic renderings only.",
                "Installs Ultralytics explicitly, showing that detector work becomes a first-class dependency rather than an optional side experiment.",
                "Loads or wires the newly introduced detector into the inference path, linking page localization to the earlier segmentation-based strip decoder.",
                "Builds the detector-aware inference scaffold that combines page localization, segmentation, and final export, even though the overall workflow is still exploratory.",
            ],
        ),
        [
            "Compared with notebook (1), this revision expands the compact demo into a 23-cell research pipeline with explicit Kaggle ingestion, calibration helpers, and the first YOLO-oriented tail.",
        ],
    )

    data[_nb(3)] = _entry(
        [
            "Second long-form research revision that tightens the page-localization branch and reduces some of the scaffolding duplication seen in notebook (2).",
            "The notebook is still training-oriented, but its late cells now concentrate on detector bootstrap, real-data tuning, and a more integrated inference path.",
        ],
        _research_notes(
            "Retrains the core segmentation backbone under the same synthetic objective, but in a cleaner notebook structure that is easier to extend with detector logic.",
            [
                "Creates the synthetic full-page factory and derived labels for YOLO-style localization, preserving the detector-training branch while reducing setup noise.",
                "Bootstraps detector training or configuration so page localization is no longer only a data-preparation idea.",
                "Runs the real-data fine-tuning branch that adapts the segmentation model toward scanned ECG appearance.",
                "Integrates detector output with the segmentation inference path, making this the first genuinely combined page-localization-plus-trace-reconstruction cell in the series.",
                "Performs the parquet and template validation step so the expanded inference path can still emit competition-shaped output.",
            ],
        ),
        [
            "Compared with notebook (2), this revision trims the YOLO branch into a tighter five-cell tail and makes the integrated inference story clearer.",
        ],
    )

    data[_nb(4)] = _entry(
        [
            "Research revision that keeps the long-form structure but pivots the ending toward an explicit quality-boost inference factory.",
            "The notebook still trains and fine-tunes models in place, yet its last cells now focus on how detector crops and phase-2 logic should be assembled for inference.",
        ],
        _research_notes(
            "Keeps the baseline segmentation-training role but treats it as the starting point for a more inference-focused late-stage pipeline.",
            [
                "Creates the synthetic page and YOLO-label factory used to keep localization training aligned with the current rendering assumptions.",
                "Bootstraps the detector branch around that generated dataset so page localization remains part of the end-to-end plan.",
                "Runs the real-data fine-tuning branch that adapts segmentation weights toward scanned competition pages.",
                "Adds glue code that reconciles page orientation, detector crops, and segmentation input formatting before the final inference factory runs.",
                "Defines the phase-2 quality-boost inference factory, an explicit attempt to increase reconstruction fidelity without reopening the whole training stack.",
                "Validates the phase-2 factory against the expected parquet and template layout before treating it as submission-ready.",
            ],
        ),
        [
            "Compared with notebook (3), this revision keeps the same research skeleton but turns the ending into a deliberate quality-boost inference experiment.",
        ],
    )

    data[_nb(5)] = _entry(
        [
            "Long-form research notebook that upgrades the geometry side of the pipeline and hardens training for more difficult page conditions.",
            "This is the first revision where geometric reasoning, detector support, and phase-2 segmentation tuning are presented as one coordinated system.",
        ],
        _research_notes(
            "Keeps the main segmentation-training branch alive while preparing the notebook for later geometry-aware and hardening-era inference.",
            [
                "Builds the synthetic page and detector-label factory again, now under the stronger geometry assumptions introduced earlier in the notebook.",
                "Bootstraps detector training around that geometry-aware dataset so localization and segmentation can share the same revised coordinate model.",
                "Launches the phase-2 hardening training pass, explicitly fine-tuning the segmentation model for more difficult or noisier cases.",
                "Adds the helper glue that joins detector crops, geometric normalization, and hardening-era segmentation weights into one inference path.",
                "Defines the physics-aware phase-2 inference factory, combining improved calibration logic with the hardened weights to stabilize amplitude and timing reconstruction.",
                "Performs the final parquet and template validation so the geometry-heavy phase-2 engine can still emit competition-compliant output.",
            ],
            advanced_geometry=True,
        ),
        [
            "Compared with notebook (4), this revision makes geometry explicit and adds a dedicated hardening phase instead of relying only on the previous quality-boost factory.",
        ],
    )

    data[_nb(6)] = _entry(
        [
            "Continuation of the geometry-aware branch that promotes the phase-2 work into a higher-fidelity phase-3 inference engine.",
            "The notebook still retrains and validates in place, but the intended deliverable is now a cleaner final extractor rather than just another training snapshot.",
        ],
        _research_notes(
            "Keeps the segmentation-training role from the previous revision while preserving compatibility with the upgraded geometry engine.",
            [
                "Rebuilds the synthetic page and localization dataset pipeline so the detector branch stays consistent with the new geometry assumptions.",
                "Bootstraps detector training or loading around that revised dataset, keeping localization aligned with the latest rendering logic.",
                "Runs the hardening fine-tuning phase again so difficult pages remain covered even as the inference engine changes.",
                "Adds the bridge code that passes detector crops and geometry metadata into the high-fidelity inference path.",
                "Promotes the pipeline to a phase-3 high-fidelity inference engine, emphasizing cleaner lead alignment and more trustworthy reconstructed strip morphology.",
                "Checks the resulting output against parquet and sample expectations before treating the new engine as ready for submission use.",
            ],
            advanced_geometry=True,
            corrected_manual=True,
        ),
        [
            "Compared with notebook (5), this revision keeps the same branches but replaces the phase-2 finale with a more ambitious phase-3 extractor.",
        ],
    )

    data[_nb(7)] = _entry(
        [
            "Late-stage research notebook that swaps in a stronger ResNet50 plus scSE segmentation architecture while keeping the combat YOLO branch alive.",
            "This file marks the point where architecture search, detector robustness, and hardened inference are all treated as parts of the same submission strategy.",
        ],
        _research_notes(
            "Trains the phase-7 ResNet50 plus scSE segmentation architecture, testing whether a stronger encoder and attention stack improve trace-mask quality.",
            [
                "Prepares a more aggressive combat-mode YOLO dataset with harder augmentations and clutter, aiming to make lead localization survive messy page layouts.",
                "Trains the combat YOLOv8x detector on that harsher dataset so detector robustness stops being the bottleneck for the final submission engine.",
                "Keeps the phase-2 hardening segmentation branch in the workflow as a fallback or complementary weight set for difficult pages.",
                "Adds the integration helpers that translate detector crops, calibration metadata, and segmentation outputs into a common inference contract.",
                "Defines the final phase-7 inference engine, now centered on the ResNet50 plus scSE weights rather than the earlier baseline checkpoint.",
                "Performs the final parquet and template validation step to ensure the generated submission still matches competition schema constraints.",
            ],
            advanced_geometry=True,
            corrected_manual=True,
        ),
        [
            "Compared with notebook (6), this revision changes the segmentation architecture itself and makes detector hardening an explicit combat-mode branch.",
        ],
    )

    data[_nb(8)] = _entry(
        [
            "Optimization-focused follow-up to notebook (7) that keeps the same overall structure but retunes the segmentation branch with hybrid loss and AdamW.",
            "The core question here is whether better optimization can beat the architecture-only gain from the previous revision.",
        ],
        _research_notes(
            "Trains the phase-8 variant with hybrid loss and AdamW, focusing on optimization stability and better contour fidelity rather than a new detector design.",
            [
                "Prepares the combat-mode YOLO dataset again so localization remains stress-tested under the same difficult page conditions.",
                "Retrains the combat detector to preserve parity between the localization branch and the new segmentation optimization settings.",
                "Keeps the phase-2 hardening branch available for hard pages, rather than trusting the new optimizer alone.",
                "Adds the same detector-to-segmentation bridge layer so the updated phase-8 weights can be evaluated in the full pipeline.",
                "Defines the final phase-8 inference engine, now explicitly consuming the hybrid-loss segmentation weights.",
                "Revalidates output shape and schema against the parquet and template expectation before exporting results.",
            ],
            advanced_geometry=True,
            corrected_manual=True,
        ),
        [
            "Compared with notebook (7), this revision keeps the detector scaffolding but swaps the segmentation-training objective and optimizer strategy.",
        ],
    )

    data[_nb(9)] = _entry(
        [
            "Phase-10 research notebook that fine-tunes toward real-world competition pages while retaining the combat detector and hardening branches.",
            "This is the last large single-model research notebook before the series collapses into compact submission-only variants.",
        ],
        _research_notes(
            "Fine-tunes the segmentation stack on real or pseudo-labeled competition data, explicitly targeting the synthetic-to-real gap instead of only improving synthetic training.",
            [
                "Prepares the combat-mode localization dataset once more so page detection can keep pace with the new phase-10 segmentation branch.",
                "Retrains or refreshes the combat YOLO detector, preserving robust lead localization as part of the final build recipe.",
                "Maintains the phase-2 hardening branch as a fallback path for difficult pages and noisy scans.",
                "Adds the integration helpers that let detector outputs, calibration data, and segmentation masks flow into a single final engine contract.",
                "Defines the platinum final build that combines later signal-processing ideas and test-time augmentation on top of the phase-10 weights.",
                "Runs the parquet and sample validation pass so the new platinum engine can be treated as a submission candidate rather than only a research artifact.",
            ],
            advanced_geometry=True,
            corrected_manual=True,
        ),
        [
            "Compared with notebook (8), this revision turns the main segmentation branch toward real-world fine-tuning and produces the first explicit platinum final build.",
        ],
    )

    compact_summary = [
        "Compact submission-focused notebook that keeps only environment bootstrap, imports, renderer, final engine, and export validation.",
        "The training and exploratory branches are removed so the notebook can act as a fast Kaggle inference run rather than a research diary.",
    ]

    data[_nb(10)] = _entry(
        list(compact_summary),
        [
            "Installs the dependencies and forces a runtime restart so the notebook can run from a fresh Kaggle session without carrying earlier state.",
            "Imports the reduced runtime stack and resolves the few globals the compact inference path still needs.",
            RENDERER_NOTE,
            "Deploys the first compact phase-14 and phase-15 final engine with permanent paths, turning the large notebook logic into a five-cell submission runner.",
            COMPACT_VALIDATION_NOTE,
        ],
        [
            "Compared with notebook (9), this revision discards in-notebook training and keeps only the minimal scaffold required to run the platinum inference path.",
        ],
    )

    data[_nb(11)] = _entry(
        list(compact_summary),
        [
            "Repeats the compact environment bootstrap so the same final engine can be rerun from a clean session.",
            "Reloads the reduced inference stack and confirms the compact notebook still has the required globals after restart.",
            RENDERER_NOTE,
            "Reuses the same compact phase-14 and phase-15 engine as notebook (10), indicating this revision is primarily a cleanup and rerun pass.",
            COMPACT_VALIDATION_NOTE,
        ],
        [
            "Compared with notebook (10), this is a near-duplicate cleanup pass that preserves the same compact engine while retesting the minimal scaffold.",
        ],
    )

    data[_nb(12)] = _entry(
        list(compact_summary),
        [
            "Bootstraps the environment again for another compact inference-only run.",
            "Imports the trimmed inference stack and resolves the runtime state needed by the repaired engine cell.",
            RENDERER_NOTE,
            "Applies another fixed-build edit to the phase-14 and phase-15 engine, targeting remaining path or runtime issues while keeping the compact form.",
            COMPACT_VALIDATION_NOTE,
        ],
        [
            "Compared with notebook (11), the main change is a repaired final engine cell rather than a new workflow shape.",
        ],
    )

    data[_nb(13)] = _entry(
        list(compact_summary),
        [
            "Bootstraps the compact submission environment one more time before running the fixed final build.",
            "Reloads the reduced import stack and runtime configuration for the corrected export path.",
            RENDERER_NOTE,
            "Keeps the fixed final-build engine but treats it as a stable baseline that now needs export-path validation more than architectural changes.",
            "Makes the final verification explicitly CSV-aware, so output correctness is checked against the actual submission file contract rather than only dataframe shape.",
        ],
        [
            "Compared with notebook (12), the export cell becomes explicitly CSV-aware so validation follows the real submission schema.",
        ],
    )

    for number, install_note, delta_note in [
        (
            14,
            "Installs libraries from user-uploaded wheel files in a smart offline mode, assuming Kaggle internet is unavailable but curated wheels are present.",
            "Compared with notebook (13), this revision changes the bootstrap strategy to depend on uploaded offline wheels rather than a standard restart and install path.",
        ),
        (
            15,
            "Uses a nuclear direct-install strategy that aggressively forces package availability when the gentler offline approach proves unreliable.",
            "Compared with notebook (14), this revision keeps the same engine but escalates installation into a direct, forceful recovery path.",
        ),
        (
            16,
            "Uses a brute-force installation sweep to make the offline runtime usable even when package state is inconsistent.",
            "Compared with notebook (15), the engine stays stable while the install cell is rewritten as a broader brute-force repair pass.",
        ),
        (
            17,
            "Repeats the brute-force installation strategy as another environment-repair iteration for the same compact engine.",
            "Compared with notebook (16), this is another retry of the same compact inference stack under a slightly different brute-force bootstrap.",
        ),
        (
            18,
            "Runs yet another brute-force offline installation pass, showing that environment reliability remained the main issue rather than engine logic.",
            "Compared with notebook (17), the notebook remains engine-identical and focuses again on making the runtime install actually stick.",
        ),
    ]:
        data[_nb(number)] = _entry(
            [
                "Compact offline deployment notebook that preserves the fixed final engine while experimenting with different bootstrap tactics.",
                "The notebook is inference-only; the only moving part between revisions is how aggressively it repairs the environment before running the submission path.",
            ],
            [
                install_note,
                "Imports the runtime stack and prepares the compact inference environment after the chosen offline installation strategy completes.",
                RENDERER_NOTE,
                "Keeps the fixed phase-14 and phase-15 final engine as the stable inference core while the surrounding bootstrap strategy changes.",
                "Performs the updated CSV-aware validation and writes the submission file once the compact engine completes.",
            ],
            [delta_note],
        )

    compact_engine_deltas = {
        19: (
            "Deploys a GPU-batched version of the platinum engine, prioritizing throughput while still assuming rows and IDs are well-behaved.",
            "Compared with notebook (18), this revision returns to a smart offline install and pivots the engine toward GPU-batched throughput.",
        ),
        20: (
            "Corrects the GPU-batched engine so batching and memory management do not break the earlier final-build logic.",
            "Compared with notebook (19), the main change is a corrected batch-oriented engine rather than a new workflow shape.",
        ),
        21: (
            "Rewrites the engine into a streaming memory-safe variant, trading raw speed for survival on constrained Kaggle sessions.",
            "Compared with notebook (20), this revision sacrifices throughput to reduce OOM and long-run instability.",
        ),
        22: (
            "Focuses the engine on formatting and ID sanitization, showing that submission schema mismatches had become a significant failure mode.",
            "Compared with notebook (21), the emphasis moves from memory safety to row formatting and identifier cleanup.",
        ),
        23: (
            "Tightens formatting and ID rules further and pairs them with a safer verification path so malformed rows cannot slip into the final CSV.",
            "Compared with notebook (22), this revision doubles down on schema safety and stricter verification.",
        ),
        24: (
            "Fixes scoring errors by hardening the ID parser and row-alignment assumptions against the official metadata files.",
            "Compared with notebook (23), this revision targets observed scoring failures rather than raw runtime stability.",
        ),
        25: (
            "Brands the engine as version 26 and consolidates the robust ID and scoring-safe logic into a more stable final path.",
            "Compared with notebook (24), the fixes are consolidated into a more clearly versioned final engine.",
        ),
        26: (
            "Adds strict row matching so output ordering and row cardinality track the official template exactly.",
            "Compared with notebook (25), the engine becomes stricter about row identity and ordering.",
        ),
        27: (
            "Introduces universal column finding, making the engine tolerant to small schema or naming shifts in upstream metadata.",
            "Compared with notebook (26), the notebook becomes more defensive about upstream column names.",
        ),
        28: (
            "Forces integer ID normalization before lookup and export, preventing string-formatting quirks from breaking joins.",
            "Compared with notebook (27), the major change is forced integer handling for IDs.",
        ),
        29: (
            "Fixes read-only system interactions so the engine works in restricted Kaggle directories without trying to write where it cannot.",
            "Compared with notebook (28), this revision focuses on filesystem restrictions rather than schema parsing.",
        ),
        30: (
            "Enforces literal ID matching and more robust length handling, reflecting the last refinements before the codebase is refactored again.",
            "Compared with notebook (29), the engine tightens ID equality and signal-length handling before the later refactor series.",
        ),
    }

    for number, (engine_note, delta_note) in compact_engine_deltas.items():
        validation_note = SAFE_LOGIC_CHECK_NOTE if number >= 23 else COMPACT_VALIDATION_NOTE
        data[_nb(number)] = _entry(
            [
                "Compact offline inference notebook built to run on Kaggle without internet access.",
                "The workflow is stable by this point; the notebook series now iterates mainly on the central inference engine and its validation rules.",
            ],
            [
                SMART_OFFLINE_INSTALL_NOTE,
                IMPORT_FIX_NOTE,
                RENDERER_NOTE,
                engine_note,
                validation_note,
            ],
            [delta_note],
        )

    data[_nb(31)] = _entry(
        [
            "Self-contained compact inference notebook that replaces repeated phase-14 and phase-15 boilerplate with helper-driven offline installation and a consolidated engine.",
            "This file is the clearest compact bridge between the earlier research notebooks and the later packaged deployment notebooks.",
        ],
        [
            "Scans local wheel directories and installs what is needed, so package bootstrap becomes data-driven instead of hard-coded.",
            "Defines helper functions that filter wheels by Python and platform compatibility and execute the offline installer pipeline.",
            RENDERER_NOTE,
            "Builds a consolidated inference engine around `/kaggle/input/ecg-final-models/best.pt` and `best_model_phase10.pth`, using the detector for lead localization and the segmentation model for trace recovery.",
            "Performs submission integrity checks on the assembled dataframe before writing it, treating row count and column layout as first-class invariants.",
        ],
        [
            "Compared with notebook (30), this revision internalizes package discovery and collapses the engine into a helper-driven compact deployment block.",
        ],
    )

    compact_v32_to_40 = {
        32: (
            "Deploys a merged ultra-safe engine that explicitly prioritizes crash resistance, parquet handling, and streaming over elegance.",
            "Compared with notebook (31), the workflow simplifies again and the engine becomes explicitly safety-first.",
        ),
        33: (
            "Adds dynamic lead-length handling and preserves the original calibration logic, making temporal normalization a first-class concern.",
            "Compared with notebook (32), this revision keeps the compact shell but rebalances the engine around dynamic lengths and original-scale calibration.",
        ),
        34: (
            "Packages lead mapping, safe YOLO use, adaptive DP-Viterbi decoding, and more robust calibration into a single heavy-duty inference cell.",
            "Compared with notebook (33), the engine becomes broader and more explicit about localization, mapping, and calibration robustness.",
        ),
        35: (
            "Refines the engine into a lighter safe variant with a smart grid hypothesis, suggesting calibration uncertainty had become a dominant failure mode.",
            "Compared with notebook (34), the engine is trimmed and reframed around smarter grid reasoning.",
        ),
        36: (
            "Adds test-time augmentation and per-lead gating, making the engine more selective about which recovered traces it trusts.",
            "Compared with notebook (35), this revision turns quality control and augmentation into key engine behaviors.",
        ),
        37: (
            "Refactors the same V43-family engine into a generic-titled block; the code still serves as the main inference engine even though the heading no longer says so.",
            "Compared with notebook (36), the core engine is refactored into a title-less cell rather than replaced outright.",
        ),
        38: (
            "Introduces a more balanced engine built around template lengths, lighter gating, and restrained test-time augmentation instead of maximum defensive complexity.",
            "Compared with notebook (37), the engine is deliberately rebalanced for pragmatism rather than pure safety.",
        ),
        39: (
            "Extends the balanced V46 idea with safer sampling-frequency recovery from `test.csv`, tightening temporal assumptions against the official metadata.",
            "Compared with notebook (38), the main delta is safer use of `test.csv` to recover timing information.",
        ),
        40: (
            "Uses per-lead length and sampling-frequency information from `test.csv`, plus confidence gates and linear-phase resampling, to make timing normalization much more explicit.",
            "Compared with notebook (39), this revision leans heavily into per-lead timing control and resampling discipline.",
        ),
    }

    for number, (engine_note, delta_note) in compact_v32_to_40.items():
        data[_nb(number)] = _entry(
            [
                "Compact no-internet deployment notebook that keeps only the offline bootstrap, renderer, final engine, and schema check.",
                "By this stage the notebook family is primarily an engine-tuning series, with each revision swapping one inference policy for another inside the same shell.",
            ],
            [
                SMART_OFFLINE_INSTALL_NOTE,
                NO_INTERNET_IMPORT_NOTE,
                RENDERER_NOTE,
                engine_note,
                SAFE_LOGIC_CHECK_NOTE,
            ],
            [delta_note],
        )

    data[_nb(41)] = _entry(
        [
            "Compact no-internet deployment notebook that adds one more explicit sanity cell after the usual five-cell inference flow.",
            "The extra cell shows that row count and ID uniqueness had become important enough to warrant a dedicated post-run check.",
        ],
        [
            SMART_OFFLINE_INSTALL_NOTE,
            NO_INTERNET_IMPORT_NOTE,
            RENDERER_NOTE,
            "Runs a V42-style engine that derives per-lead lengths and sampling frequencies while applying safe gating before export.",
            SAFE_LOGIC_CHECK_NOTE,
            "Prints final row-count and unique-ID statistics as an extra sanity check, making silent duplication or truncation easier to catch.",
        ],
        [
            "Compared with notebook (40), this revision adds a dedicated final sanity cell instead of relying only on inline validation inside the engine and export path.",
        ],
    )

    data[_nb(42)] = _entry(
        [
            "Largest late-stage research notebook; it extends the phase-10 branch into a three-model ensemble consisting of the ResNet-based phase-10 model, an EfficientNet-B3 competitor, and a DeepLabV3+ competitor.",
            "This file is the provenance notebook for the extra competition checkpoints that later compact notebooks consume directly.",
        ],
        [
            "Bootstraps the full research environment again, because this notebook reopens training rather than staying in submission-only mode.",
            "Loads the updated import stack and runtime configuration shared by the ensemble experiments.",
            "Keeps the renderer and synthetic ECG utilities available for qualitative debugging and data generation across all ensemble branches.",
            "Fine-tunes the phase-10 segmentation branch on real or pseudo-labeled data, preserving the main ResNet-style path from notebook (9).",
            "Replaces and expands the phase-10 helper definitions with stronger losses, richer pseudo-label dataset handling, and safer training utilities that the ensemble branches can reuse.",
            "Trains the EfficientNet-B3 competitor model, creating the lighter segmentation checkpoint that later notebooks can compare or ensemble against the ResNet branch.",
            "Trains the DeepLabV3+ competitor model, giving the notebook a third segmentation family with a different decoder bias.",
            "Reintroduces the mask-to-signal decoding helpers so all three segmentation branches can be evaluated under the same waveform-reconstruction logic.",
            "Runs a focused smoke test that checks whether the revised helpers still produce sensible outputs after the ensemble-related refactor.",
            "Wraps the decoder into a page-level processing helper so real Kaggle pages can be passed through the revised reconstruction stack.",
            "Keeps the submission-formatting helper in place so ensemble results can still be shaped into the competition schema.",
            "Loads the official Kaggle metadata and page inventory, giving the ensemble notebook direct access to the true evaluation surface.",
            "Adds a real-image inference harness so the multiple segmentation branches can be compared on actual scanned pages rather than only synthetic examples.",
            "Defines grid-detection and calibration helpers for the ensemble era, ensuring all candidate models share the same measurement assumptions.",
            "Runs calibration validation on representative examples so errors in paper-scale estimation are not mistaken for model-quality differences.",
            "Keeps the sliding-window decoder available for long or awkward strips, preventing whole-lead failures when a single pass is unreliable.",
            "Preserves the tuned high-jump waveform solver so sharp ECG deflections can survive decoding across all ensemble candidates.",
            "Carries forward the advanced geometry engine, which remains necessary for consistent detector crops and lead alignment.",
            "Adds the cleanup helper that removes grid and background clutter before segmentation and decoding.",
            "Provides a corrected manual test helper for carefully inspecting selected examples under the new ensemble setup.",
            "Builds the combat-mode YOLO training dataset again so detector robustness stays aligned with the new segmentation experiments.",
            "Trains or refreshes the combat YOLO detector that later compact notebooks use for lead localization.",
            "Keeps the phase-2 hardening segmentation branch alive as an additional robustness path in case the ensemble alone is not enough.",
            "Adds the integration helpers that let detector outputs, calibration data, and multiple segmentation predictions share one inference contract.",
            "Defines the final ensemble inference engine that combines YOLO localization with the phase-10 ResNet weights, the EfficientNet-B3 competitor, and the DeepLabV3+ competitor.",
            "Validates the ensemble output against the parquet and template expectation before treating the notebook as the provenance run for later deployment notebooks.",
        ],
        [
            "Compared with notebook (41), this revision leaves the compact submission format entirely and reopens training to build a multi-checkpoint ensemble.",
        ],
    )

    ensemble_compact = {
        43: (
            "Deploys the full notebook (42) ensemble directly, treating the combined ResNet, EffNet, and DeepLab predictions as the preferred inference recipe.",
            "Compared with notebook (42), this revision packages the ensemble as a compact offline deployment notebook.",
        ),
        44: (
            "Runs a ResNet50-only baseline check so the new ensemble can be compared against the legacy single-model path under the same offline shell.",
            "Compared with notebook (43), this revision deliberately drops the extra ensemble members to measure the old baseline cleanly.",
        ),
        45: (
            "Reverts to a robust single-model V39-style engine, suggesting the ensemble did not eliminate the need for a dependable fallback path.",
            "Compared with notebook (44), this notebook restores a tougher single-model engine instead of a pure baseline check.",
        ),
        46: (
            "Builds a hybrid ensemble with fixed calibration, combining multiple model families while explicitly controlling the measurement stage.",
            "Compared with notebook (45), the notebook reintroduces multiple models but keeps calibration logic more disciplined.",
        ),
        47: (
            "Packages a benchmarking engine built from the earlier winning configuration, treating the notebook as a comparative reference point for later fixes.",
            "Compared with notebook (46), the goal shifts from hybridization to benchmarking around the current winner.",
        ),
        48: (
            "Locks in the same benchmarking engine again, implying this revision is mainly a stabilization or rerun of the benchmark path.",
            "Compared with notebook (47), the workflow stays almost identical and serves as a lock-in rerun of the benchmark engine.",
        ),
    }

    for number, (engine_note, delta_note) in ensemble_compact.items():
        data[_nb(number)] = _entry(
            [
                "Compact offline deployment notebook that consumes the notebook (42) model bundle rather than training in place.",
                "The shell stays minimal while the main engine cell swaps between ensemble, baseline, or benchmark variants.",
            ],
            [
                SMART_OFFLINE_INSTALL_NOTE,
                NO_INTERNET_IMPORT_NOTE,
                RENDERER_NOTE,
                engine_note,
                SAFE_LOGIC_CHECK_NOTE,
            ],
            [delta_note],
        )

    for number, summary_line, engine_note, delta_note in [
        (
            49,
            "Inference notebook that introduces the new EfficientNet-B3 checkpoint into the compact offline pipeline.",
            "Introduces the new EfficientNet-B3 segmentation checkpoint as the preferred inference model while still keeping the older model path as an optional fallback.",
            "Compared with notebook (48), this revision pivots from ensemble benchmarking toward integrating the newly trained EffB3 checkpoint.",
        ),
        (
            50,
            "EffB3-focused inference notebook that also makes runtime warnings and timing decisions more explicit.",
            "Builds on the EffB3-first engine with frequency-aware length selection, quieter warning handling, and explicit debug counters for pipeline visibility.",
            "Compared with notebook (49), the EffB3 branch stays primary while timing logic and debug visibility are improved.",
        ),
        (
            51,
            "EffB3-focused inference notebook that hardens ID parsing and path resolution around the new checkpoint.",
            "Hardens the same dual-model engine with a more robust ID parser and safer calibration choices so mismatched paths do not poison the submission.",
            "Compared with notebook (50), the emphasis moves from counters and warnings to safer identifier and path handling.",
        ),
        (
            52,
            "EffB3-focused inference notebook that promotes the branch to a more explicit V40 final engine.",
            "Promotes the branch to a V40 final engine with `test.csv` path mapping, ImageNet normalization, a NEW and OLD ensemble choice, and stronger dynamic-programming recovery.",
            "Compared with notebook (51), this revision rebrands the EffB3 branch as a more complete V40-style final engine.",
        ),
        (
            53,
            "EffB3-focused inference notebook that repairs the pid-to-image lookup layer without abandoning the V40 core.",
            "Adds a smart pid-to-image path index and sanity checks, fixing the fragile lookup layer while keeping the V40-style inference core.",
            "Compared with notebook (52), the primary change is safer mapping from competition IDs to actual image paths.",
        ),
    ]:
        install_note = SAFE_MINIMAL_INSTALL_NOTE if number >= 52 else SMART_OFFLINE_INSTALL_NOTE
        data[_nb(number)] = _entry(
            [
                summary_line,
                "These notebooks keep the same compact shell but make the new EffB3 checkpoint a first-class participant in inference decisions.",
            ],
            [
                install_note,
                PATH_RESOLVER_NOTE,
                EFF_ATTACH_NOTE,
                RENDERER_NOTE,
                engine_note,
                SAFE_LOGIC_CHECK_NOTE,
            ],
            [delta_note],
        )

    data[_nb(54)] = _entry(
        [
            "EffB3 deployment notebook that inserts an explicit diagnostic step before running the repaired V41 inference engine.",
            "The goal is to expose mapping coverage problems early instead of discovering them only after inference finishes.",
        ],
        [
            SAFE_MINIMAL_INSTALL_NOTE,
            PATH_RESOLVER_NOTE,
            EFF_ATTACH_NOTE,
            RENDERER_NOTE,
            DIAGNOSTIC_PID_NOTE,
            "Keeps the V41 fix engine centered on smarter pid-to-image lookup and the V40 inference core, but now runs it only after the diagnostic coverage check.",
            SAFE_LOGIC_CHECK_NOTE,
        ],
        [
            "Compared with notebook (53), this revision inserts a dedicated diagnostic cell before inference to measure path-index coverage explicitly.",
        ],
    )

    data[_nb(55)] = _entry(
        [
            "EffB3 deployment notebook that replaces the earlier V41 fix with a more explicitly robust V42 inference engine.",
            "The notebook still values mapping diagnostics, but the main change is a stronger final engine with deskewing, trimming, model selection, and quality gating.",
        ],
        [
            SAFE_MINIMAL_INSTALL_NOTE,
            PATH_RESOLVER_NOTE,
            EFF_ATTACH_NOTE,
            RENDERER_NOTE,
            DIAGNOSTIC_PID_NOTE,
            "Replaces the prior V41 path with a V42 robust inference engine that explicitly deskews the image, trims strips, selects between models, and quality-gates the recovered signal before export.",
            SAFE_LOGIC_CHECK_NOTE,
        ],
        [
            "Compared with notebook (54), the diagnostic cell stays in place but the main engine is replaced by a more heavily quality-gated V42 path.",
        ],
    )

    data[_nb(56)] = _entry(
        [
            "Final modular rewrite that abandons descriptive headings and decomposes the pipeline into install, config, indexing, model loading, utility, formatting, validation, and debug blocks.",
            "This notebook is structurally cleaner than the earlier compact series, but its generic headings make manual editorial notes essential for readability.",
        ],
        [
            "Implements a minimal offline wheel installer with a small helper wrapper, making dependency bootstrap explicit but intentionally lightweight.",
            "Loads imports, runtime configuration, and path-discovery logic for the new UNet checkpoint, the old fallback UNet checkpoint, and the YOLO detector bundle.",
            "Indexes discovered test images and checks coverage against competition IDs, ensuring the pipeline knows which files are actually available before loading models.",
            "Builds the model-loading layer: it unwraps checkpoint state dicts, guesses encoder families from key patterns, constructs the UNet, and loads YOLO for lead localization.",
            "Defines the crop-extraction and waveform utility functions that convert detector boxes and segmentation masks into per-lead numeric traces.",
            "Formats reconstructed outputs against the sample-submission contract so the modular helper stack can still emit the required competition schema.",
            "Runs validation and writes `submission.csv`, making this the main execution cell that turns the modular helpers into a real deliverable.",
            "Provides an optional one-ID debug path for focused troubleshooting, useful when the main execution succeeds structurally but a particular record still looks wrong.",
        ],
        [
            "Compared with notebook (55), this revision fully decomposes the pipeline into modular helpers and abandons descriptive headings; the editorial notes restore the missing semantics.",
        ],
        risk_overrides=[
            "Because model paths are auto-discovered in this notebook, a wrong match could silently swap checkpoints unless the discovered filenames are reviewed carefully.",
        ],
    )

    if len(data) != 57:
        raise ValueError(f"Expected editorial data for 57 notebooks, found {len(data)}")
    return data


def _notebook_chain_index(notebook_name: str) -> int:
    if notebook_name == MAIN_NOTEBOOK:
        return 1
    match = re.fullmatch(r"ecg-sim2real-datagenerator-mohamad-sabbagh \((\d+)\)\.ipynb", notebook_name)
    if not match:
        raise ValueError(f"Unexpected notebook name: {notebook_name}")
    return int(match.group(1)) + 1


def _strengthen_delta_notes(notebook_name: str, raw_delta_notes: list[str]) -> list[str]:
    chain_index = _notebook_chain_index(notebook_name)
    if chain_index == 1:
        return list(raw_delta_notes)

    primary_change = raw_delta_notes[0] if raw_delta_notes else "Compared with the prior notebook, this revision changes the active workflow."
    if chain_index == 2:
        context = {
            "why": "The apparent motivation is to compress the monolithic exploratory notebook into a smaller proof-of-concept that can be rerun and visually checked without stepping through every research branch.",
            "retained": "It retains the core synthetic training, calibration, and real-image smoke-test ideas from the first notebook instead of throwing away the earlier pipeline entirely.",
            "effect": "The workflow effect is a much clearer demonstration notebook whose stored plots are easier to interpret as a single run rather than as an interleaved lab notebook.",
            "obsolete": "What becomes less central is the sprawling mix of side experiments from the original notebook; this revision treats them as background rather than as the main interface.",
        }
    elif 3 <= chain_index <= 7:
        context = {
            "why": "The apparent motivation is to turn the early prototype into a staged research pipeline that can separately evolve segmentation, calibration, detector preparation, and real-image adaptation.",
            "retained": "It retains the synthetic renderer, segmentation backbone, Viterbi-style decoding, and Kaggle-facing ingestion path from the earlier notebooks.",
            "effect": "The workflow effect is a broader experiment surface: later cells can now feed detector work, real-data tuning, and more deliberate page-level inference rather than only strip-level demos.",
            "obsolete": "What becomes less central is the purely compact visual-demo framing from notebook (1); the notebook now behaves like a research branch with durable intermediate stages.",
        }
    elif 8 <= chain_index <= 10:
        context = {
            "why": "The apparent motivation is to improve final reconstruction quality through architecture search, harder detector training, and eventually real-image pseudo-label fine-tuning.",
            "retained": "It retains the late-stage geometry, combat-detector, and hardening ideas from the immediately preceding research notebooks instead of restarting the pipeline from scratch.",
            "effect": "The workflow effect is that the notebook becomes a late-stage model-selection and final-build source, not just another intermediate research checkpoint.",
            "obsolete": "What starts to become obsolete is the assumption that the older baseline segmentation branch alone is the intended deployment path; newer architecture and fine-tuning branches take over.",
        }
    elif 11 <= chain_index <= 19:
        context = {
            "why": "The apparent motivation is to collapse the large research notebooks into a compact Kaggle runner that can be executed quickly during submission iteration.",
            "retained": "It retains the renderer, the current best final engine, and the export-validation pattern from the prior final-build notebook family.",
            "effect": "The workflow effect is shorter rerun time and less hidden dependency on earlier cells, which is valuable once the focus shifts from training to deployment reliability.",
            "obsolete": "What becomes obsolete is in-notebook training and most exploratory branch work; those remain part of provenance, not part of the active submission path.",
        }
    elif 20 <= chain_index <= 31:
        context = {
            "why": "The apparent motivation is to harden the compact deployment flow against concrete Kaggle failures such as schema mismatches, identifier parsing problems, memory pressure, and filesystem restrictions.",
            "retained": "It retains the five-cell compact shell and the renderer-to-engine-to-validation cadence established in the previous compact notebooks.",
            "effect": "The workflow effect is cumulative robustness: each revision tunes the same basic submission runner so it survives more edge cases without reopening training.",
            "obsolete": "What becomes obsolete is the earlier, more fragile assumption that IDs, lengths, row ordering, and writable paths will behave perfectly by default.",
        }
    elif 32 <= chain_index <= 42:
        context = {
            "why": "The apparent motivation is to refactor the compact deployment notebooks into more helper-driven and self-contained offline runners that behave predictably in no-internet Kaggle sessions.",
            "retained": "It retains the offline-deployment focus, the qualitative renderer, and the idea that one dominant engine cell should still drive submission export.",
            "effect": "The workflow effect is less boilerplate duplication and a clearer separation between environment repair, helper setup, inference, and export sanity checks.",
            "obsolete": "What becomes obsolete is the earlier pattern of repeating large inline engine scaffolds and ad hoc install logic across many nearly identical notebooks.",
        }
    elif chain_index == 43:
        context = {
            "why": "The apparent motivation is to reopen the now-compact deployment story and test whether a broader multi-checkpoint ensemble can outperform the single-model final builds.",
            "retained": "It retains the phase-10 lineage, the detector branch, the geometry logic, and the hardening-era understanding of difficult pages from the preceding notebooks.",
            "effect": "The workflow effect is a major expansion of the checkpoint universe: later notebooks can now benchmark or deploy multiple segmentation families rather than only one inherited winner.",
            "obsolete": "What becomes less final is the single-model-only assumption that dominated notebooks (10) through (41); from this point onward, ensemble and competitor checkpoints become first-class options.",
        }
    elif 44 <= chain_index <= 49:
        context = {
            "why": "The apparent motivation is to package the notebook (42) checkpoint branch into compact offline runners that can compare ensemble, baseline, hybrid, and benchmark behavior quickly.",
            "retained": "It retains the compact no-internet shell that had already proved useful for Kaggle deployment, as well as the renderer plus final-validation pattern.",
            "effect": "The workflow effect is faster comparison across model strategies without rerunning the heavy training notebook, which is exactly what Phase 1 needs before synthesis.",
            "obsolete": "What becomes obsolete is the need to keep the ensemble notebook itself open for every comparison; the compact descendants become the operational interface.",
        }
    elif 50 <= chain_index <= 56:
        context = {
            "why": "The apparent motivation is to bring the EfficientNet-B3 branch into the active deployment flow and determine whether it should replace or complement the older segmentation weights.",
            "retained": "It retains the compact no-internet runner, the renderer, and the final validation shell from the prior deployment families.",
            "effect": "The workflow effect is a new inference-routing era where the notebook must decide between old and new checkpoints instead of assuming one inherited phase-10 default.",
            "obsolete": "What becomes obsolete is the assumption that the older single-model path is sufficient on its own; checkpoint selection and fallback logic become part of the deployment contract.",
        }
    else:
        context = {
            "why": "The apparent motivation is to modularize the final notebook so install, configuration, loading, execution, and debugging can be understood as separate responsibilities before later synthesis work.",
            "retained": "It retains the same detector-plus-segmentation submission goal as the preceding deployment notebooks even though the code layout changes dramatically.",
            "effect": "The workflow effect is a cleaner operational shape that is easier to map into a future synthesis, because the notebook is no longer a single large opaque engine cell.",
            "obsolete": "What becomes obsolete is the old habit of encoding meaning only in descriptive cell headings or one monolithic inference cell; the logic is now spread across modular blocks.",
        }

    return [primary_change, context["why"], context["retained"], context["effect"], context["obsolete"]]


def _open_questions_for_notebook(notebook_name: str) -> list[str]:
    chain_index = _notebook_chain_index(notebook_name)
    if chain_index == 1:
        return [
            "Because this notebook mixes synthetic training, Viterbi decoding, Kaggle ingestion, and calibration in one file, some behavior may still depend on execution order rather than explicit interfaces.",
            "Several stored outputs in this notebook document visible reconstruction failures; it remains unclear which early branches were considered dead ends versus reusable prototypes.",
        ]
    if 3 <= chain_index <= 7:
        return [
            "These notebooks introduce detector preparation and real-data fine-tuning, but the exact checkpoint lineage from these branches into later compact deployment notebooks is not always explicit.",
        ]
    if 8 <= chain_index <= 10:
        return [
            "The late research notebooks clearly evolve toward a final build, but the exact handoff from these in-notebook training runs to the later compact deployment notebooks is still partly historical rather than explicit.",
        ]
    if chain_index == 32:
        return [
            "This helper-driven offline refactor is clearly important, but it is not fully explicit whether the later no-internet notebooks inherit the helpers themselves or only the engine ideas.",
        ]
    if chain_index == 43:
        return [
            "The ensemble direction is well defined technically, but Phase 1 evidence does not fully resolve whether it became the long-term preferred path or remained a benchmarking branch.",
            "Notebook evidence references temporary base checkpoints for the EfficientNet and DeepLab branches, and those base artifacts are not present in the audited bundle.",
        ]
    if chain_index == 57:
        return [
            "This notebook auto-discovers model paths, so the intended final checkpoint pairing may still depend on the exact Kaggle input layout present at execution time.",
            "The debug cell is clearly useful, but it is not entirely certain whether it was meant as a permanent operational step or only as a troubleshooting convenience.",
        ]
    return []


def _confidence_for_notebook(notebook_name: str) -> str:
    chain_index = _notebook_chain_index(notebook_name)
    if chain_index in {1, 3, 4, 5, 6, 7, 8, 9, 10, 32, 43, 57}:
        return "medium"
    return "high"


def load_manual_notes() -> dict[str, Any]:
    notes = _load_legacy_notes()
    notebooks = notes.setdefault("notebooks", {})

    for notebook_name, payload in _build_notebook_editorial_data().items():
        entry = notebooks.setdefault(notebook_name, {})
        expected = int(payload["expected_cell_count"])
        cell_notes = dict(payload["cell_notes"])
        if len(cell_notes) != expected:
            raise ValueError(f"{notebook_name}: expected {expected} cell notes, found {len(cell_notes)}")
        entry["notebook_summary"] = list(payload["notebook_summary"])
        entry["cell_notes"] = deepcopy(cell_notes)
        entry["delta_notes"] = _strengthen_delta_notes(notebook_name, list(payload["delta_notes"]))
        entry["open_questions"] = _open_questions_for_notebook(notebook_name)
        entry["confidence"] = _confidence_for_notebook(notebook_name)
        if payload.get("risk_overrides"):
            entry["risk_overrides"] = list(payload["risk_overrides"])
        elif "risk_overrides" in entry:
            del entry["risk_overrides"]

    return notes
