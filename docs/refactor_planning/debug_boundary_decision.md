# Debug Boundary Decision

## Runtime

- Minimal logging needed for deterministic inference, checkpoint selection, and export validation.

## Debug/tooling

- Renderer-backed qualitative inspection.
- Visual lead crops, waveform overlays, and pid coverage diagnostics.
- Ad hoc comparison helpers for primary vs fallback segmentation behavior.

## Archive only

- Notebook-only sanity cells that exist purely as interactive exploration without clean function boundaries.

## Decision

- Renderer and visual diagnostics survive as opt-in tooling, not as mandatory runtime stages.
- Notebook-style sanity cells should be rewritten only if they become clean reusable tools; otherwise they stay archived.
