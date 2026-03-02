# ticket-006 Enable mypy strict mode for decomp handlers and models

## Context

### Background

With the mypy strict configuration in place (ticket-005), running `mypy idecomp/` will report strict-mode errors across all production code. The decomp module is the largest module (~95% of production code) and will have the most errors. The inewave plan established proven annotation patterns for cfinterface subclasses: `IO[Any]` for read/write, `# type: ignore[override]` for return type mismatches, `Optional[Any]` for `__init__` parameters, and `# type: ignore[import-untyped]` for pandas/numpy.

### Relation to Epic

This is the largest ticket in Epic 02. It fixes all strict-mode errors in the decomp module (handlers, models, blocos, arquivoscsv). After this ticket, `mypy idecomp/decomp/` passes under strict mode.

### Current State

- `mypy idecomp/ --strict` reports ~1500+ errors across the decomp module
- Common error categories (from inewave experience):
  - `[no-untyped-def]`: Functions missing type annotations for parameters or return types
  - `[override]`: Subclass read/write methods returning `None` instead of `bool`
  - `[import-untyped]`: pandas and numpy lack type stubs
  - `[arg-type]`: `IO[str]` vs `IO[Any]` mismatches at cfinterface boundary
  - `[assignment]`: Missing ClassVar annotations on class attributes

## Specification

### Requirements

1. Add type annotations to all functions and methods in the decomp module that lack them
2. Add `# type: ignore[override]` with explanation comments on all Block/Section/Register `read()` and `write()` methods that override cfinterface base return types
3. Add `# type: ignore[import-untyped]` on all `import pandas as pd` and `import numpy as np` lines
4. Use `IO[Any]` for all `read()` and `write()` file parameter types
5. Use `Optional[Any]` for cfinterface `__init__` parameter types (`previous`, `next`, `data`)
6. After all fixes, `mypy idecomp/decomp/` must pass under the strict configuration
7. All 310 tests must still pass

### Inputs/Props

- All Python files in `idecomp/decomp/` and `idecomp/decomp/modelos/`

### Outputs/Behavior

- `mypy idecomp/decomp/` reports zero errors under strict mode configuration from ticket-005
- All existing tests pass unchanged

### Error Handling

Not applicable -- this is a type annotation change with no runtime impact.

## Acceptance Criteria

- [ ] Given the command `mypy idecomp/decomp/`, when executed with the strict config from ticket-005, then zero errors are reported
- [ ] Given the command `grep -r '# type: ignore$' idecomp/decomp/`, when executed, then zero bare type-ignore comments are found (all have specific error codes)
- [ ] Given the command `pytest -v`, when executed, then all 310 tests pass
- [ ] Given any `read()` or `write()` method in a Block/Section/Register subclass, when inspected, then the file parameter is typed as `IO[Any]` and the method has `# type: ignore[override]` with an explanation

## Implementation Guide

### Suggested Approach

Work through the errors module by module. Run `mypy idecomp/decomp/ 2>&1 | head -50` to see the first batch, fix them, then iterate until zero errors.

**Common fix patterns** (from inewave epic-05 learnings):

1. **Missing return type on `__init__`**:

   ```python
   def __init__(self, data=...) -> None:
   ```

2. **Missing parameter annotations**:

   ```python
   def __init__(self, previous: Optional[Any] = None,
                next: Optional[Any] = None,
                data: Optional[Any] = None) -> None:
   ```

3. **read/write override**:

   ```python
   def read(self, file: IO[Any], *args: Any, **kwargs: Any) -> None:  # type: ignore[override]  # cfinterface base returns bool
   ```

4. **pandas/numpy imports**:

   ```python
   import pandas as pd  # type: ignore[import-untyped]  # no pandas-stubs package
   import numpy as np  # type: ignore[import-untyped]  # no numpy-stubs package
   ```

5. **Property setter return type**:

   ```python
   @property_name.setter
   def property_name(self, value: pd.DataFrame) -> None:
   ```

6. **Class variable annotations** (for BLOCKS, SECTIONS, REGISTERS, COLUMN_NAMES, etc.):
   ```python
   from typing import ClassVar, List, Type
   BLOCKS: ClassVar[List[Type[Block]]] = [...]
   COLUMN_NAMES: ClassVar[List[str]] = [...]
   ```

### Key Files to Modify

All Python files under:

- `/home/rogerio/git/idecomp/idecomp/decomp/*.py` (~43 handler files)
- `/home/rogerio/git/idecomp/idecomp/decomp/modelos/*.py` (~25 model files)
- `/home/rogerio/git/idecomp/idecomp/decomp/modelos/blocos/*.py` (3 files)
- `/home/rogerio/git/idecomp/idecomp/decomp/modelos/arquivoscsv/*.py` (2 files)

### Patterns to Follow

- Follow inewave's annotation patterns exactly. Reference file: `/home/rogerio/git/inewave/inewave/newave/modelos/dger.py` for Section subclass annotations.
- `# type: ignore` always has specific code AND inline explanation. Zero bare ignores.
- `IO[Any]` over `IO[str]` for ALL read/write overrides (inewave learning: `Line.write()` returns `Union[str, bytes]`).

### Pitfalls to Avoid

- Do NOT use `IO[str]` -- this caused 193 errors in inewave due to `Line.write()` returning `Union[str, bytes]`
- Do NOT remove `# type: ignore` comments without checking if they are still needed -- some are needed even under strict
- Do NOT add `warn_return_any = true` -- this would produce 500+ meaningless errors from cfinterface's `Any`-typed data
- Do NOT annotate test files -- they are out of scope for strict mode
- Do NOT change any runtime behavior -- only type annotations and ignore comments

## Testing Requirements

### Unit Tests

No new tests. All 310 existing tests must pass.

### Integration Tests

- `mypy idecomp/decomp/` passes with zero errors

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-005-add-mypy-strict-config.md
- **Blocks**: ticket-008-replace-bare-type-ignores.md

## Effort Estimate

**Points**: 3
**Confidence**: Medium (error count is high but patterns are well-established from inewave)

## Out of Scope

- Fixing type errors in `idecomp/libs/` (ticket-007)
- Replacing bare type-ignore comments that may already have codes (ticket-008 verifies completeness)
- Adding type stubs for pandas/numpy
- Changing any runtime behavior
