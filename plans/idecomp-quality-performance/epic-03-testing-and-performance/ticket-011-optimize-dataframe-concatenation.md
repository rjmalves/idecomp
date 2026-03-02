# ticket-011 Optimize DataFrame concatenation in BlockFile handlers

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Replace the O(n^2) `pd.concat([df, b.data])` loop in `__concatena_blocos` (found in `relato.py`, `custos.py`, `relgnl.py`) with the collect-then-concat pattern: collect DataFrames into a list, then call `pd.concat(dfs, ignore_index=True)` once. This is the same optimization applied to inewave's archive base classes in epic-02/epic-04, which eliminates quadratic behavior when many blocks exist.

## Anticipated Scope

- **Files likely to be modified**: `idecomp/decomp/relato.py`, `idecomp/decomp/custos.py`, `idecomp/decomp/relgnl.py`
- **Key decisions needed**: Should the three `__concatena_blocos` implementations be deduplicated into a shared helper, or kept as separate per-file methods?
- **Open questions**:
  - How many blocks does a typical relato.rvx file contain? (determines the practical impact of this optimization)
  - Is there any handler that uses `pd.concat` in a loop outside of `__concatena_blocos`?

## Dependencies

- **Blocked By**: ticket-006-enable-mypy-strict-decomp.md (type annotations must be in place)
- **Blocks**: ticket-013-create-benchmark-suite.md

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
