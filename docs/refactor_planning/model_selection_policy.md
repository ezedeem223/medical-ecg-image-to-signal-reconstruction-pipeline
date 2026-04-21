# Model Selection Policy

## Final policy

- Primary model: `best_model_effb3_phase9_ddp (2).pth`
- Fallback model: `best_model_phase10.pth`
- Explicit selector required: `yes`
- Core runtime auto-discovery allowed: `no`

## Evidence

- Observed facts:
  - `best_model_effb3_phase9_ddp (2).pth` is marked `active` in the Phase 2 checkpoint inventory.
  - `best_model_phase10.pth` is marked `fallback-active`.
  - Version `50` is a best-known score-tier candidate and sits on the EffB3 integration line.
- Planning inference:
  - EffB3 is the best primary default for the future runtime because it matches the late-lineage direction and a top-scoring candidate lineage.
  - Phase-10 remains the safest explicit fallback because it is historically dominant, long-lived, and still paired with late compact notebooks.

## Selector behavior

- Core runtime must use an explicit, config-driven selector. The selector chooses the primary model by default and can switch to the fallback by configuration or controlled failover.
- Notebook-style auto-discovery of whatever checkpoint happens to exist on Kaggle input mounts is forbidden in core runtime. Discovery may survive only in debug/tooling modules.

## Rationale

- EffB3 is the best fit for the late architectural direction and for the best-known score lineage candidate at version 50.
- Phase-10 remains the strongest historically trusted fallback and is already paired with late compact notebooks.

## Confidence

- `medium`
