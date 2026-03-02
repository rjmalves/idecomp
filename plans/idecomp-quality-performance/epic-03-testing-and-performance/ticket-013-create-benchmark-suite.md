# ticket-013 Create benchmark suite for read performance

## Context

### Background

Epic 03 establishes performance baselines for idecomp. After ticket-009 implemented PEP 562 lazy imports for `idecomp.decomp.__init__.py` (reducing import overhead) and ticket-011 optimizes DataFrame concatenation, a benchmark suite is needed to document the current performance and enable regression detection in future releases.

The benchmark suite follows inewave conventions: stdlib-only (no pytest-benchmark dependency), `time.perf_counter` for timing, and the existing `tests/mocks/mock_open.py` utility for providing file data to handlers without disk I/O.

### Relation to Epic

This ticket addresses the "Create a benchmark baseline for read performance" goal of epic-03. It is the final ticket in the epic and should run after the DataFrame optimization in ticket-011 so that baselines reflect the optimized code.

### Current State

- No `benchmarks/` directory exists in the project.
- The `idecomp/decomp/__init__.py` uses PEP 562 lazy imports with 41 entries in `_LAZY_IMPORTS` (established in ticket-009).
- Mock data exists for all handlers in `tests/mocks/arquivos/` -- both binary files (`.dat`, `.rv0`, `.rv2`) and Python mock string modules.
- The `tests/mocks/mock_open.py` utility supports both text (`str`) and binary (`bytes`) read data.
- Representative handler classes by base type:
  - **RegisterFile**: `Dadger` (largest, text-based), `Hidr` (binary)
  - **SectionFile**: `Vazoes` (binary), `Cortdeco` (binary)
  - **BlockFile**: `Relato` (text, uses `__concatena_blocos`)
  - **ArquivoCSV**: `DecOperUsih` (CSV output)

## Specification

### Requirements

1. Create a `benchmarks/` directory at the project root.
2. Create `benchmarks/bench_read.py` that measures read performance for 4 representative handlers: Dadger (text RegisterFile), Hidr (binary RegisterFile), Vazoes (binary SectionFile), and DecOperUsih (CSV ArquivoCSV).
3. Create `benchmarks/bench_import.py` that measures import time for `idecomp.decomp` (to verify lazy import performance) and individual handler imports.
4. Create `benchmarks/run_benchmarks.py` as the entry point that runs all benchmarks and writes results to `benchmarks/benchmark_results.md`.

### Inputs/Props

- Mock data from `tests/mocks/arquivos/` for handler reading benchmarks.
- No external dependencies beyond stdlib (`time`, `importlib`, `statistics`, `sys`, `pathlib`).

### Outputs/Behavior

- `python benchmarks/run_benchmarks.py` executes all benchmarks and writes `benchmarks/benchmark_results.md` with a markdown table of results.
- Each benchmark function measures wall-clock time using `time.perf_counter`, runs multiple iterations (10 iterations for read benchmarks, 50 for import benchmarks), and reports mean and standard deviation.
- The results file includes: handler name, operation type (read/import), mean time (ms), std dev (ms), iterations count.

### Error Handling

If a handler fails to read during benchmarking, the benchmark reports `ERROR` for that handler and continues with the remaining handlers. The script does not abort on individual handler failures.

### Out of Scope

- Using pytest-benchmark or any third-party benchmarking framework.
- Benchmarking write operations (most handlers are read-only).
- Benchmarking with real DECOMP case files (only mock data is used).
- Automated CI integration of benchmarks (this establishes the baseline only).

## Acceptance Criteria

- [ ] Given the project root, when `ls benchmarks/` is run, then `bench_read.py`, `bench_import.py`, `run_benchmarks.py` are present.
- [ ] Given `benchmarks/run_benchmarks.py`, when `python benchmarks/run_benchmarks.py` is run from the project root, then it completes without error and writes `benchmarks/benchmark_results.md`.
- [ ] Given `benchmarks/benchmark_results.md`, when its content is inspected, then it contains a markdown table with rows for Dadger, Hidr, Vazoes, DecOperUsih read benchmarks and `idecomp.decomp` import benchmark, each with mean_ms and std_ms columns.
- [ ] Given the full test suite, when `pytest -x -q` is run, then all existing tests still pass (benchmark files are not collected by pytest since they are outside `tests/`).

## Implementation Guide

### Suggested Approach

**bench_read.py:**

```python
import time
import statistics
import sys
from pathlib import Path
from unittest.mock import patch

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from tests.mocks.mock_open import mock_open


def bench_handler_read(handler_cls, mock_data, n_iter=10, **read_kwargs):
    """Benchmark a handler's read() with mock data."""
    times = []
    for _ in range(n_iter):
        m = mock_open(read_data=mock_data)
        with patch("builtins.open", m):
            start = time.perf_counter()
            handler_cls.read("bench_file", **read_kwargs)
            elapsed = time.perf_counter() - start
        times.append(elapsed * 1000)  # ms
    return statistics.mean(times), statistics.stdev(times) if len(times) > 1 else 0.0
```

Then define functions that load each handler's mock data and call `bench_handler_read`:

- `bench_dadger()`: imports `MockDadger` from `tests/mocks/arquivos/dadger.py`, joins lines, benchmarks `Dadger.read()`
- `bench_hidr()`: reads `tests/mocks/arquivos/hidr.dat` as bytes, benchmarks `Hidr.read()`
- `bench_vazoes()`: reads `tests/mocks/arquivos/vazoes.rv0` as bytes, benchmarks `Vazoes.read()`
- `bench_dec_oper_usih()`: imports mock data from `tests/mocks/arquivos/dec_oper_usih.py`, benchmarks `DecOperUsih.read()`

**bench_import.py:**

```python
import time
import importlib
import statistics
import sys


def bench_import_decomp(n_iter=50):
    times = []
    for _ in range(n_iter):
        # Remove cached modules
        mods_to_remove = [k for k in sys.modules if k.startswith("idecomp")]
        for m in mods_to_remove:
            del sys.modules[m]
        start = time.perf_counter()
        importlib.import_module("idecomp.decomp")
        elapsed = time.perf_counter() - start
        times.append(elapsed * 1000)
    return statistics.mean(times), statistics.stdev(times)
```

**run_benchmarks.py:**

Orchestrates bench_read and bench_import, collects results, writes markdown table.

### Key Files to Modify

- `benchmarks/bench_read.py` -- new file
- `benchmarks/bench_import.py` -- new file
- `benchmarks/run_benchmarks.py` -- new file
- `benchmarks/benchmark_results.md` -- generated output (not committed, or committed as baseline)

### Patterns to Follow

- Use `time.perf_counter` (not `time.time`) for sub-second measurement accuracy.
- Use `statistics.mean` and `statistics.stdev` from stdlib.
- Use `tests/mocks/mock_open.py` (not stdlib mock_open) to support `seek()` and `tell()` needed by cfinterface handlers.
- Add `sys.path.insert(0, ...)` at the top of each benchmark file to ensure imports work when run from any directory.

### Pitfalls to Avoid

- Do NOT import handlers at module level in bench_import.py -- the benchmark measures import time itself.
- For binary handlers (Hidr, Vazoes), the mock data must be `bytes`, not `str`. Read the mock files with `open(path, "rb").read()`.
- For text handlers (Dadger, DecOperUsih), the mock data must be `str` (joined lines from mock modules).
- The `benchmarks/` directory is outside `testpaths = ["tests"]`, so pytest will not collect benchmark files. No `conftest.py` or `__init__.py` is needed in `benchmarks/`.

## Testing Requirements

### Unit Tests

No unit tests for benchmark code. The benchmark is validated by running it and checking that it produces valid output.

### Integration Tests

Not applicable.

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-009-implement-lazy-imports-decomp.md (lazy imports must be in place -- already completed), ticket-011-optimize-dataframe-concatenation.md (optimizations should be applied before establishing baseline)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: High
