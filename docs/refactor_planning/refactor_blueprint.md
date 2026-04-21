# Refactor Blueprint

## 1. Final repository objective

- Build a maintainable ECG image digitization repository whose structure comes from the modular late notebook line, while its runtime-critical behavior stays aligned with the best-known scoring compact line.

## 2. Structural anchor notebook(s)

- Primary structural anchor: version 57 / `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`

## 3. Performance anchor notebook(s)/versions

- Primary performance anchor: version 50 / `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`
- Secondary performance reference: version 46 / `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`
- Exception regressions excluded from anchor eligibility: v56, v57

## 4. Final adopted runtime pipeline

- Config-driven bootstrap
- YOLO detection via `best.pt`
- EffB3 primary segmentation
- Phase-10 fallback segmentation
- Calibration and trace extraction
- Quality-aware postprocessing
- Validation and submission export

## 5. Modules to build

- `config`
- `bootstrap`
- `io/indexing`
- `detector`
- `segmentation`
- `checkpoint_selection`
- `preprocessing`
- `extraction`
- `calibration`
- `postprocessing`
- `validation`
- `submission_export`

## 6. Modules to archive

- `ensemble_experiments`
- `historical_training_notebooks`
- `temporary_bootstrap_checkpoints`
- `interactive_debug_cells`

## 7. Expected repository structure

- `src/ecg_digitizer/config/`
- `src/ecg_digitizer/runtime/`
- `src/ecg_digitizer/models/`
- `src/ecg_digitizer/validation/`
- `tools/debug/`
- `research/training/`
- `archive/notebooks/`
- `archive/checkpoints/`

## 8. Artifacts to preserve

- best.pt
- best_model_effb3_phase9_ddp (2).pth
- best_model_phase10.pth
- sample submission schema checks
- late compact inference logic around calibration and extraction

## 9. Artifacts to exclude

- Temporary competitor bootstrap weights (`temp_deeplab_base.pt`, `temp_effnet_base.pt`).
- Notebook-only package repair cells that have no clean production equivalent.
- Full ensemble runtime path unless later evidence reopens it.

## 10. Acceptable remaining ambiguities

- Whether version 46 or version 50 should be treated as the long-term gold runtime reference once exact score values are backfilled. (medium)
- How much of the late filtering stack belongs in the default runtime versus optional signal-polish utilities. (medium)

## Final planning policy

- Use a dual-anchor refactor: structural modules inherit from notebook (56), but runtime defaults inherit from the version-50 score-proven compact path, with version 46 retained as a secondary behavioral reference.
