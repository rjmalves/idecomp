# ticket-007 Enable mypy strict mode for libs module

## Context

### Background

The `idecomp/libs/` module contains 2 handler files (`usinas_hidreletricas.py`, `restricoes.py`) and 2 model files with Register subclasses. These files need the same type annotation treatment as the decomp module to pass under mypy strict mode. The libs module is smaller (~2K LOC in models) but has more complex Register subclass patterns.

### Relation to Epic

This ticket parallels ticket-006 for the libs module. It can be done after or simultaneously with ticket-006, as both depend on ticket-005 (mypy config).

### Current State

- `idecomp/libs/modelos/restricoes.py` has 31 Register subclasses totaling ~1945 LOC
- `idecomp/libs/modelos/usinas_hidreletricas.py` has 5 Register subclasses totaling ~365 LOC
- `idecomp/libs/usinas_hidreletricas.py` is the handler (RegisterFile subclass)
- `idecomp/libs/restricoes.py` is the handler (RegisterFile subclass)
- All files have bare `# type: ignore` on pandas imports

## Specification

### Requirements

1. Add type annotations to all functions and methods in the libs module
2. Apply the same cfinterface annotation patterns as ticket-006
3. After fixes, `mypy idecomp/libs/` must pass under the strict configuration
4. All 310 tests must still pass

### Inputs/Props

- Files in `idecomp/libs/` and `idecomp/libs/modelos/`

### Outputs/Behavior

- `mypy idecomp/libs/` reports zero errors under strict mode
- All existing tests pass unchanged

### Error Handling

Not applicable.

## Acceptance Criteria

- [ ] Given the command `mypy idecomp/libs/`, when executed with the strict config from ticket-005, then zero errors are reported
- [ ] Given the command `grep -r '# type: ignore$' idecomp/libs/`, when executed, then zero bare type-ignore comments are found
- [ ] Given the command `pytest tests/libs/ -v`, when executed, then all libs tests pass

## Implementation Guide

### Suggested Approach

1. Run `mypy idecomp/libs/ 2>&1` to see all strict-mode errors
2. Apply the same fix patterns as ticket-006:
   - `IO[Any]` for read/write file parameters
   - `# type: ignore[override]` on read/write methods
   - `# type: ignore[import-untyped]` on pandas import
   - `Optional[Any]` for `__init__` parameters
   - `-> None` on all setters
   - `ClassVar` on class-level attributes
3. For the Register subclasses in `restricoes.py` (31 classes), the pattern is repetitive: each class has `__init__`, properties, and setters that need annotations
4. Run `mypy idecomp/libs/` after each batch of fixes to track progress

### Key Files to Modify

- `/home/rogerio/git/idecomp/idecomp/libs/usinas_hidreletricas.py`
- `/home/rogerio/git/idecomp/idecomp/libs/restricoes.py`
- `/home/rogerio/git/idecomp/idecomp/libs/modelos/usinas_hidreletricas.py`
- `/home/rogerio/git/idecomp/idecomp/libs/modelos/restricoes.py`
- `/home/rogerio/git/idecomp/idecomp/libs/__init__.py`

### Patterns to Follow

- Same patterns as ticket-006. Reference: `/home/rogerio/git/inewave/inewave/newave/modelos/dger.py` for annotation patterns.

### Pitfalls to Avoid

- `restricoes.py` has 31 Register subclasses -- do NOT add annotations one-by-one interactively. Batch the changes by pattern (all `__init__` first, then all properties, etc.)
- Do NOT change any runtime behavior in Register property getters/setters

## Testing Requirements

### Unit Tests

No new tests. Existing libs tests serve as regression.

### Integration Tests

- `mypy idecomp/libs/` passes with zero errors

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-005-add-mypy-strict-config.md
- **Blocks**: ticket-008-replace-bare-type-ignores.md

## Effort Estimate

**Points**: 2
**Confidence**: Medium

## Out of Scope

- Type annotations for decomp module (ticket-006)
- Bare type-ignore cleanup (ticket-008 verifies completeness)
- Changes to test files
