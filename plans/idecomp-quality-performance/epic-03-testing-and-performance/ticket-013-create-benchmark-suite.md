# ticket-013 Create benchmark suite for read performance

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Create a minimal benchmark suite under `benchmarks/` that measures read performance for representative handlers (Dadger, Relato, DecOperUsih, Vazoes) and import time for the idecomp package. The benchmark produces a `benchmark_results.md` file for regression detection. Follow the inewave benchmark patterns: stdlib-only (no pytest-benchmark), `importlib.import_module` for handler loading, and mock-open for file reading.

## Anticipated Scope

- **Files likely to be modified**: New files under `benchmarks/` directory: `bench_read.py`, `bench_import.py`, `run_benchmarks.py`, `benchmark_results.md`
- **Key decisions needed**: Which handlers are most representative for benchmarking? How many iterations for stable timing?
- **Open questions**:
  - Should the benchmark measure the lazy import improvement from ticket-009?
  - Does idecomp have mock_open support equivalent to inewave's `tests/mocks/mock_open.py`?
  - What is the target set of handlers to benchmark (representative of each base class type)?

## Dependencies

- **Blocked By**: ticket-009-implement-lazy-imports-decomp.md, ticket-011-optimize-dataframe-concatenation.md
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
