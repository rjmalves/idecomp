# ticket-004 Fix existing mypy error in cortdeco.py

## Context

### Background

Running `mypy idecomp/` in non-strict mode reports 1 error in `idecomp/decomp/cortdeco.py` at line 53: `Incompatible return value type (got "SectionFile", expected "Cortdeco") [return-value]`. This is because the `read()` classmethod calls `super().read()` which returns `SectionFile`, but the type annotation declares the return type as `"Cortdeco"`. This must be fixed before enabling strict mode.

### Relation to Epic

This is the first ticket in Epic 02. It resolves the only existing mypy error, clearing the baseline for strict mode enablement in subsequent tickets.

### Current State

- `mypy idecomp/` reports: `Found 1 error in 1 file (checked 97 source files)`
- The error is at `/home/rogerio/git/idecomp/idecomp/decomp/cortdeco.py` line 53
- The `read()` classmethod overrides `SectionFile.read()` and calls `super().read()` which returns `SectionFile`, not `Cortdeco`

## Specification

### Requirements

1. Fix the return type annotation of `Cortdeco.read()` so mypy is satisfied
2. The fix must not change the runtime behavior -- `Cortdeco.read()` must still return a `Cortdeco` instance
3. After the fix, `mypy idecomp/` must report zero errors

### Inputs/Props

- File: `/home/rogerio/git/idecomp/idecomp/decomp/cortdeco.py` (line 53, the `return a` statement)

### Outputs/Behavior

- `mypy idecomp/` reports `Success: no issues found in 97 source files`

### Error Handling

Not applicable.

## Acceptance Criteria

- [ ] Given the command `mypy idecomp/`, when executed, then the output contains `Success: no issues found in 97 source files`
- [ ] Given the command `mypy idecomp/decomp/cortdeco.py`, when executed, then zero errors are reported
- [ ] Given `pytest tests/decomp/test_cortdeco.py -v`, when executed, then all cortdeco tests pass
- [ ] Given `Cortdeco.read(...)`, when called at runtime, then it returns a `Cortdeco` instance (not just `SectionFile`)

## Implementation Guide

### Suggested Approach

The issue is that `super().read()` returns `SectionFile` but the method signature says `-> "Cortdeco"`. The correct fix is to add a `cast()` on the return value:

```python
from typing import cast

class Cortdeco(SectionFile):
    @classmethod
    def read(cls, content, ...) -> "Cortdeco":
        a = super().read(content, ...)
        return cast("Cortdeco", a)
```

This is type-safe because `SectionFile.read()` called on a `Cortdeco` class will construct a `Cortdeco` instance at runtime -- the cast just tells mypy about this invariant.

### Key Files to Modify

- `/home/rogerio/git/idecomp/idecomp/decomp/cortdeco.py` (add `cast` import, wrap return value)

### Patterns to Follow

- `cast()` from `typing` is the standard way to narrow return types from base class methods. This pattern will be used elsewhere when enabling strict mode.

### Pitfalls to Avoid

- Do NOT change the runtime behavior of `read()` -- only add the cast
- Do NOT use `# type: ignore[return-value]` to suppress this -- it is better to fix it properly with `cast()`
- Do NOT add `assert isinstance(a, Cortdeco)` -- this adds a runtime check that is unnecessary

## Testing Requirements

### Unit Tests

No new tests. Existing cortdeco tests serve as regression.

### Integration Tests

- `mypy idecomp/` must pass with zero errors

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-003-fix-identity-test-verify-suite.md
- **Blocks**: ticket-005-add-mypy-strict-config.md

## Effort Estimate

**Points**: 1
**Confidence**: High

## Out of Scope

- Enabling mypy strict mode (ticket-005, ticket-006, ticket-007)
- Fixing other type annotation issues
- Modifying any file other than `cortdeco.py`
