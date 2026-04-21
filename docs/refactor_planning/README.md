# Refactor Planning

This directory is the generated Phase 3 planning layer. It does not refactor code; it translates the Phase 1 audit and Phase 2 synthesis into a performance-aware refactor decision set.

## Key decisions

- Structural anchor: version 57 / `ecg-sim2real-datagenerator-mohamad-sabbagh (56).ipynb`
- Performance anchor: version 50 / `ecg-sim2real-datagenerator-mohamad-sabbagh (49).ipynb`
- Secondary performance reference: version 46 / `ecg-sim2real-datagenerator-mohamad-sabbagh (45).ipynb`
- Exception regression markers: v56, v57

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
