# Version Mapping

This repository preserves both Kaggle version numbers and notebook filenames. They are not identical, and the mapping is frozen here to avoid future ambiguity.

## Mapping Rule

- Kaggle version `1` maps to the unnumbered notebook:
  - `ecg-sim2real-datagenerator-mohamad-sabbagh.ipynb`
- Kaggle version `N > 1` maps to notebook `(N-1)`:
  - `version 2` -> notebook `(1)`
  - `version 3` -> notebook `(2)`
  - and so on

## Required Examples

- version `46` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`
- version `50` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`
- version `57` -> `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`

## Why This Matters

The Phase 4 build uses a dual-anchor refactor:

- structure comes from version `57`
- runtime behavior is frozen against version `50`
- version `46` remains the secondary performance reference

Without this mapping note, the repository would make those freezes appear inconsistent even though they are historically correct.
