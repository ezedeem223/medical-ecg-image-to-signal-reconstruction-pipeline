# Training Scope Decision

## Final decision

- Training code in the final repository: `optional_research_only`
- Priority: `runtime reproducibility over complete historical training reproduction`

## Policy

- If training survives at all, keep a single canonical training path centered on the mature segmentation branch rather than the full historical notebook zoo.
- Notebook (42) and its competitor training bundle remain optional research or archive material unless a future benchmark proves they belong in maintained code.
- Keep deployable checkpoints and one clear fallback in the maintained runtime plan; move temporary bootstrap and competitor warm-start artifacts to archive/provenance.

## Interpretation

- Phase 4 should prioritize a clean inference repository first.
- Training provenance may survive later, but only behind a single maintained path rather than the full notebook family.
