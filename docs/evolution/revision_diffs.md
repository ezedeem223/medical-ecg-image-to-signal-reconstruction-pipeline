# Revision Diffs

This file documents only milestone and architecture-significant transitions. It is not an all-pairs comparison matrix.

## 1. Monolithic baseline -> compact proof of concept

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb`

### Observed change
- The workflow contracts from a monolithic 15-cell research notebook into an 8-cell proof-of-concept.
- Synthetic training, calibration, renderer inspection, and real-image smoke tests remain, but most exploratory branches disappear.

### Likely motivation
- Make the original idea rerunnable and inspectable without stepping through every early branch.

### Pipeline impact
- Creates the first compact notebook that can serve as a readable demo and a reusable baseline for later staged research.

### Retained elements
- Synthetic renderer.
- Segmentation training.
- Qualitative QC plots.
- Calibration and real-image testing.

### Obsoleted or replaced elements
- Large mixed-responsibility notebook structure.
- Implicit dependence on exploratory side branches.

- Confidence: `high`

## 2. Compact proof of concept -> staged synthetic/real research pipeline

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (1).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`

### Observed change
- The notebook family expands back to long-form structure, but now with clearer stages for rendering, calibration, page-level processing, detector preparation, and real-data adaptation.
- Late cells begin to bridge segmentation research with page localization and competition ingestion rather than treating them as separate experiments.

### Likely motivation
- Turn the proof-of-concept into a research program where components can evolve semi-independently before final recombination.

### Pipeline impact
- Creates the first credible lineage for synthetic-to-real transfer and for later detector-assisted inference.

### Retained elements
- Synthetic renderer and segmentation training backbone.
- Calibration and quality-control mindset from notebook (1).

### Obsoleted or replaced elements
- The idea that a compact demonstration notebook is enough to answer the harder localization and real-domain questions.

- Confidence: `high`

## 3. Baseline segmentation -> geometry and calibration aware extraction

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`

### Observed change
- Geometry, calibration, and harder page conditions become explicit themes rather than background helper logic.
- The extractor evolves from a segmentation-centered decoder into a more coordinated system that reasons about page alignment and scale.

### Likely motivation
- Simple crop-level extraction was not robust enough for realistic competition pages with skew, scale drift, and clutter.

### Pipeline impact
- Sets up the later mature pipeline where segmentation output is never trusted without geometry and calibration context.

### Retained elements
- Segmentation remains the core waveform-recovery mechanism.
- Synthetic-to-real staging remains intact.

### Obsoleted or replaced elements
- Purely local extraction assumptions that ignore page geometry.

- Confidence: `medium`

## 4. Weak localization -> YOLO-assisted lead extraction

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (2).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (3).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (4).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (5).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (6).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`

### Observed change
- Notebook (7) makes combat-mode detector hardening explicit and couples it tightly to a stronger segmentation architecture.
- Detector checkpoints and YOLO model choices become visible, not just implied by helper code.

### Likely motivation
- Fixed splits and weak localization were too brittle for full-page competition images, especially under skew and clutter.

### Pipeline impact
- Lead detection becomes a dedicated stage of the pipeline and later survives into every compact deployment family.

### Retained elements
- Segmentation-based waveform recovery.
- Calibration and page-processing logic from the staged research notebooks.

### Obsoleted or replaced elements
- The assumption that page crops can be trusted without detector-assisted localization.

- Confidence: `medium`

## 5. Phase-7 architecture switch -> Phase-8 optimization retune

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (7).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`

### Observed change
- Notebook (7) changes architecture; notebook (8) keeps that harder detector-aware structure but retunes the segmentation objective and optimizer.
- Phase naming and checkpoint references make architecture search and optimization search look like separate consecutive decisions.

### Likely motivation
- The author first validated that the new architecture mattered, then tested whether optimization alone could push the same structure further.

### Pipeline impact
- Separates model-family choice from training-policy choice, which later helps phase-10 and competitor-branch reasoning.

### Retained elements
- Combat YOLO branch.
- Stronger segmentation backbone.

### Obsoleted or replaced elements
- Treating architecture and optimizer changes as one inseparable experiment.

- Confidence: `medium`

## 6. Synthetic-only emphasis -> phase-10 real-image pseudo-label fine-tuning

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (8).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`

### Observed change
- Notebook (9) explicitly introduces phase-10 real-world fine-tuning and the first platinum final build.
- New phase-10 checkpoint references replace the prior phase-8 emphasis.

### Likely motivation
- Synthetic pretraining had reached its limit; the next gain needed better alignment with real competition pages.

### Pipeline impact
- Phase-10 weights become the dominant single-model checkpoint lineage reused across later notebooks.

### Retained elements
- Combat detector branch.
- Geometry and calibration hardening.
- Adaptive extraction logic.

### Obsoleted or replaced elements
- The assumption that synthetic-only optimization is enough for the final deployment path.

- Confidence: `high`

## 7. Large research notebooks -> compact Kaggle submission runners

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (9).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (10).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (11).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (12).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (13).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb`

### Observed change
- Notebook (10) removes in-notebook training and keeps only bootstrap, imports, renderer, final engine, and export validation.
- Subsequent compact notebooks stay inference-only and iterate mainly on bootstrap mechanics and schema-safe export.

### Likely motivation
- Submission iteration on Kaggle required faster, smaller notebooks than the late research branch could provide.

### Pipeline impact
- Creates the compact deployment mainline that dominates the middle of the notebook series.

### Retained elements
- YOLO plus segmentation inference core.
- Renderer for qualitative inspection.
- Competition export validation.

### Obsoleted or replaced elements
- Using the full research notebook as the routine submission vehicle.

- Confidence: `high`

## 8. Early compact runner -> self-contained robustness and helper-driven deployment

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (14).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (31).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (32).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (33).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (34).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (35).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (36).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (37).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (38).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (39).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`

### Observed change
- The compact era shifts from repeated install retries to helper-driven offline package discovery, safer runtime assumptions, and stricter validation.
- Per-lead timing, identifier parsing, and post-run sanity checks become recurring explicit concerns.

### Likely motivation
- Real Kaggle failures moved from pure accuracy concerns toward operational issues: package availability, row formatting, path lookup, memory pressure, and silent output corruption.

### Pipeline impact
- Transforms the compact notebook family into a deployment-hardening program rather than just a smaller version of the research branch.

### Retained elements
- Same detector-plus-segmentation inference goal.
- Renderer and export validation shell.

### Obsoleted or replaced elements
- Trusting the environment, IDs, and timing metadata without defensive checks.

- Confidence: `high`

## 9. Single-model path -> notebook (42) ensemble competitor branch

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (41).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`

### Observed change
- Notebook (42) expands from a compact six-cell runner into a 26-cell research notebook.
- The notebook trains or assembles a three-model competitor bundle: the phase-10 ResNet branch, EfficientNet-B3, and DeepLabV3+.

### Likely motivation
- After long compact hardening, the author reopened research to test whether a broader checkpoint universe could outperform the single inherited winner.

### Pipeline impact
- Creates the provenance source for the extra checkpoints later consumed by compact descendants and the EffB3 deployment branch.

### Retained elements
- Phase-10 lineage.
- Combat detector and geometry logic.
- Compact-era understanding of difficult competition pages.

### Obsoleted or replaced elements
- The assumption that only one segmentation checkpoint deserves deployment attention.

- Confidence: `medium`

## 10. Ensemble packaging -> benchmark detours and winner-oriented branch pruning

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (42).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (43).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (44).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (46).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (47).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`

### Observed change
- The compact descendants of notebook (42) alternate between ensemble, baseline-only, hybrid, and benchmark engines without returning to in-notebook training.
- Some notebooks are clear deployment experiments rather than lasting architecture steps.

### Likely motivation
- The author needed quick offline runners to compare several candidate checkpoint mixes under competition conditions.

### Pipeline impact
- Helps identify which competitor branch ideas survive and which become archive-only benchmark detours.

### Retained elements
- Compact offline shell.
- Notebook (42) checkpoint bundle.

### Obsoleted or replaced elements
- Treating every ensemble-era notebook as part of the final mainline; several are clearly evaluative side paths.

- Confidence: `medium`

## 11. Ensemble branch -> EfficientNet-B3 integration branch

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (48).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`

### Observed change
- Notebook (49) stops benchmarking around the notebook (42) bundle and explicitly attaches the new EffB3 checkpoint to the compact inference stack.
- Checkpoint routing and fallback behavior become part of the notebook contract.

### Likely motivation
- The ensemble branch likely identified EfficientNet-B3 as worth promoting into the deployment mainline.

### Pipeline impact
- Starts the final branch where model selection, fallback, and path resolution matter as much as raw inference logic.

### Retained elements
- Compact no-internet shell.
- Phase-10 checkpoint as comparison or fallback.
- YOLO detector and submission pipeline.

### Obsoleted or replaced elements
- Pure ensemble benchmarking as the main late-stage story.

- Confidence: `high`

## 12. Raw extraction -> quality-gated, calibration-aware compact engines

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (19).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (30).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (40).ipynb`, `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`

### Observed change
- Across the compact era, signal extraction increasingly depends on timing metadata, gating rules, geometry repair, and explicit fallback behavior.
- By notebook (55), the V42 engine includes deskewing, trimming, model selection, and quality gating rather than a simple direct decode.

### Likely motivation
- Competition pages exposed failure modes that could not be solved by raw segmentation output alone.

### Pipeline impact
- Makes post-processing a first-class subsystem instead of a final cosmetic step.

### Retained elements
- DP / Viterbi family extraction.
- Calibration and lead-wise reconstruction goals.

### Obsoleted or replaced elements
- Trusting a single raw mask-to-wave pass without explicit quality control.

- Confidence: `medium`

## 13. Monolithic compact engine -> modular final notebook (56)

- From notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (55).ipynb`
- To notebooks: `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`

### Observed change
- Notebook (56) abandons descriptive engine headings and decomposes the pipeline into install, config, indexing, model loading, utilities, formatting, validation, and debug blocks.
- The notebook keeps the detector-plus-segmentation submission goal but changes the operational shape dramatically.

### Likely motivation
- Prepare the notebook family for synthesis and future refactor by exposing stable responsibilities instead of one opaque engine cell.

### Pipeline impact
- Provides the cleanest direct bridge from notebooks to a future module-based repository layout.

### Retained elements
- YOLO plus segmentation inference.
- Checkpoint selection and fallback logic.
- Submission validation and debug visibility.

### Obsoleted or replaced elements
- Encoding most semantics only in notebook headings or a single monolithic inference block.

- Confidence: `high`
