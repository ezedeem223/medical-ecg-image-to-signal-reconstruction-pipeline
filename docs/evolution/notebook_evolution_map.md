# Notebook Evolution Map

This Phase 2 map synthesizes the Phase 1 audit bundle into a coherent lineage. It uses the archived file-audit reports as the factual base and the curated Phase 2 notes layer for ambiguous lineage decisions.

## Scope And Source Of Truth

- Notebook reports: [../../archive/provenance/file-audit/notebooks/](../../archive/provenance/file-audit/notebooks/)
- Manifest: [../../archive/provenance/file-audit/manifest.csv](../../archive/provenance/file-audit/manifest.csv)
- Checkpoint companion: [../../archive/provenance/file-audit/checkpoint-companion-summary.md](../../archive/provenance/file-audit/checkpoint-companion-summary.md)
- Phase 1 synthesis seed retained for terminology and era framing: [../../archive/provenance/final_synthesis_outline.md](../../archive/provenance/final_synthesis_outline.md)

## Mainline At A Glance

1. Early monolithic baseline
2. Compact proof-of-concept consolidation
3. Synthetic-to-real staged research branch
4. Architecture hardening and combat-detector era
5. Compact deployment and robustness iteration
6. Ensemble competitor branch
7. EfficientNet-B3 integration and modular finalization

## Path Classification

- Active final notebook candidate: `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`
- Dead-end benchmarking notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`
- Uncertain strategic notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`

## Milestone Notebooks

| Review order | Notebook | Phase label | Branch type | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | [`ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh.md) | `early-monolithic-baseline` | `baseline` | `superseded` | Original provenance notebook; conceptually the root of the whole project even though later notebooks split its responsibilities. |
| 2 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-1.md) | `compact-proof-of-concept` | `consolidation` | `superseded` | First successful compaction of the monolithic baseline into a rerunnable demonstration notebook. |
| 8 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-7.md) | `architecture-hardening-combat-detector` | `milestone` | `superseded` | Turns stronger segmentation architecture and combat-mode YOLO training into an explicit late-stage strategy. |
| 10 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-9.md) | `architecture-hardening-combat-detector` | `milestone` | `superseded` | Represents the last large single-model research notebook and the clearest phase-10 fine-tuning milestone. |
| 11 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-10.md) | `compact-deployment-robustness` | `milestone` | `superseded` | Collapses the research branch into a compact Kaggle runner and starts the long deployment-hardening era. |
| 32 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-31.md) | `compact-deployment-robustness` | `milestone` | `superseded` | Bridge notebook where the compact shell becomes helper-driven and more self-contained for no-internet Kaggle execution. |
| 43 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-42.md) | `ensemble-competitor-branch` | `branch` | `uncertain` | Reopens training after the compact era to create the phase-10, EfficientNet-B3, and DeepLabV3+ competitor bundle. Conceptual ancestor is notebook (9) even though the primary predecessor in review order is notebook (41). |
| 44 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-43.md) | `ensemble-competitor-branch` | `consolidation` | `superseded` | Packages notebook (42) into a compact runner so ensemble and benchmark variants can be compared quickly. |
| 50 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-49.md) | `effb3-integration-modular-finalization` | `milestone` | `superseded` | Promotes the EfficientNet-B3 branch from notebook (42) into the active compact deployment path. |
| 57 | [`ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-56.md) | `effb3-integration-modular-finalization` | `consolidation` | `active` | Final modular rewrite and the best candidate for the refactor starting point, although final checkpoint pairing still depends on runtime discovery. |

## Early monolithic baseline

- Review orders: 1 to 1
- Notebooks: [`ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh.md)
- Intent: Establish the original end-to-end thesis: synthetic ECG page rendering, segmentation training, Viterbi-style extraction, calibration, and Kaggle competition file handling all live in one notebook.
- Key surviving components:
  - Synthetic renderer as a controllable debug and data-generation surface.
  - Probability-map to waveform conversion through dynamic-programming / Viterbi-style extraction.
  - Competition-oriented calibration and submission formatting as explicit downstream goals.
- What was superseded:
  - One notebook owning every responsibility at once.
  - Heavy dependence on execution order rather than explicit boundaries between data generation, training, and inference.
- Confidence and uncertainty hotspots:
  - Some early branches are preserved only through outputs and code comments, not explicit project-level rationale.
- Primary predecessor outside era: None
- Primary successor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb`

## Compact proof-of-concept consolidation

- Review orders: 2 to 2
- Notebooks: [`ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-1.md)
- Intent: Compress the monolithic baseline into a rerunnable demonstration notebook that still exercises synthetic training, qualitative visualization, calibration, and real-image smoke testing.
- Key surviving components:
  - Visual quality control via stored plots and renderer outputs.
  - Synthetic-to-real bridging as an explicit goal rather than an accidental side effect of the large baseline notebook.
- What was superseded:
  - Most exploratory side branches from the original notebook.
- Confidence and uncertainty hotspots:
  - None called out beyond ordinary notebook lineage uncertainty.
- Primary predecessor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`
- Primary successor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb`

## Synthetic-to-real staged research branch

- Review orders: 3 to 7
- Notebooks: [`ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-2.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-3.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-4.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-5.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-6.md)
- Intent: Turn the proof-of-concept notebook into a staged research program with separate lanes for synthetic rendering, calibration, page-level localization, real-data tuning, and early detector preparation.
- Key surviving components:
  - Staged segmentation, calibration, and page-processing helpers.
  - The idea that detector support and geometric reasoning belong in the same workflow as segmentation.
  - Real-data adaptation as a persistent continuation of synthetic pretraining rather than a separate project.
- What was superseded:
  - The assumption that simple crop splitting is sufficient for page localization.
  - The early quality-boost factory as a final destination rather than a stepping stone toward a more disciplined pipeline.
- Confidence and uncertainty hotspots:
  - Checkpoint lineage from these research notebooks into the later compact deployment family is historically plausible but not always explicit.
- Primary predecessor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb`
- Primary successor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`

## Architecture hardening and combat-detector era

- Review orders: 8 to 10
- Notebooks: [`ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-7.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-8.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-9.md)
- Intent: Make architecture search, detector robustness, and harder real-image adaptation first-class concerns, culminating in phase-10 pseudo-label fine-tuning and the first explicit platinum final build.
- Key surviving components:
  - Combat-mode YOLO lead detector lineage.
  - ResNet50 plus scSE segmentation family and later phase-10 weights.
  - More explicit calibration, filtering, and adaptive extraction logic for difficult real pages.
- What was superseded:
  - Earlier baseline segmentation checkpoints as the only intended deployment path.
- Confidence and uncertainty hotspots:
  - The exact handoff from these large research notebooks into the later compact deployment notebooks remains partly historical.
- Primary predecessor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`
- Primary successor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb`

## Compact deployment and robustness iteration

- Review orders: 11 to 42
- Notebooks: [`ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-10.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-11.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-12.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-13.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-14.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (15).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-15.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (16).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-16.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (17).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-17.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (18).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-18.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-19.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (20).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-20.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (21).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-21.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (22).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-22.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (23).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-23.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (24).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-24.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (25).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-25.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (26).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-26.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (27).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-27.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (28).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-28.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (29).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-29.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-30.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-31.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (32).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-32.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (33).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-33.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (34).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-34.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (35).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-35.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-36.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-37.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (38).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-38.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (39).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-39.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-40.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-41.md)
- Intent: Collapse the large research notebooks into compact Kaggle runners, then iterate repeatedly on no-internet bootstrap strategy, runtime resilience, schema safety, identifier parsing, timing normalization, and self-contained helpers.
- Key surviving components:
  - Compact offline install/import shell.
  - Renderer retained as a debug and interpretation surface rather than as the main training engine.
  - YOLO plus segmentation inference, calibration, signal extraction, and submission validation.
- What was superseded:
  - In-notebook training as part of routine submission runs.
  - Assuming a stable Kaggle environment without custom wheel handling or defensive path logic.
- Confidence and uncertainty hotspots:
  - Not every compact notebook contributes a lasting idea; many are environment or robustness retries around the same engine core.
- Primary predecessor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- Primary successor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`

## Ensemble competitor branch

- Review orders: 43 to 49
- Notebooks: [`ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-42.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-43.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-44.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-45.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-46.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-47.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-48.md)
- Intent: Reopen the compact deployment story to train and benchmark multiple segmentation families, then package the resulting checkpoints into compact offline comparison notebooks.
- Key surviving components:
  - EfficientNet-B3 and DeepLabV3+ competitor checkpoints.
  - Evidence that the phase-10 branch became a baseline to compare against, not just a fixed final answer.
- What was superseded:
  - The assumption that one inherited segmentation model is the only serious deployment option.
- Confidence and uncertainty hotspots:
  - Phase 1 evidence does not fully resolve whether the full ensemble direction was a serious final target or mainly a benchmarking branch.
- Primary predecessor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`
- Primary successor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`

## EfficientNet-B3 integration and modular finalization

- Review orders: 50 to 57
- Notebooks: [`ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-49.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (50).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-50.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (51).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-51.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (52).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-52.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (53).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-53.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (54).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-54.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-55.md), [`ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`](../../archive/provenance/file-audit/notebooks/ecg-sim2real-datagenerator-mohamad-sabbagh-56.md)
- Intent: Promote the EfficientNet-B3 branch into the active deployment path, then harden path lookup, diagnostics, checkpoint selection, and finally modularize the whole compact engine.
- Key surviving components:
  - EfficientNet-B3 as a first-class deployed segmentation option.
  - Checkpoint selection and fallback logic as part of the runtime contract.
  - Explicit diagnostics, path resolution, and modular helper structure in the final notebook.
- What was superseded:
  - Pure ensemble benchmarking as the dominant late-stage theme.
  - Single giant inference cells with meaning encoded only in descriptive headings.
- Confidence and uncertainty hotspots:
  - The exact default checkpoint pairing in the final modular notebook can still depend on Kaggle input layout and discovered files.
- Primary predecessor outside era: `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`
- Primary successor outside era: None

## Terminology Note

Phase 2 keeps the terminology seeded in [../../archive/provenance/final_synthesis_outline.md](../../archive/provenance/final_synthesis_outline.md); this file focuses on lineage and milestone interpretation rather than re-defining the glossary.
