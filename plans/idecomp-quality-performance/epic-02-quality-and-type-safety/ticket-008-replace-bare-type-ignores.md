# ticket-008 Replace bare type-ignore comments with specific error codes

## Context

### Background

idecomp currently has 123 bare `# type: ignore` comments (no error code specified). After tickets 006 and 007 enable mypy strict mode, some of these will have been replaced during annotation work. This ticket is a cleanup pass to ensure ALL remaining `# type: ignore` comments have specific error codes and explanations, following the inewave convention of zero bare ignores.

### Relation to Epic

This is a cleanup ticket that runs after the main strict-mode enablement (tickets 006, 007). It ensures the codebase meets the "zero bare ignores" quality standard.

### Current State

- 123 bare `# type: ignore` comments (counted via `grep -r "# type: ignore$" idecomp/ --include="*.py" | wc -l`)
- Most are on `import pandas as pd  # type: ignore` and `import numpy as np  # type: ignore` lines
- After tickets 006 and 007, many will already have codes; this ticket catches any remaining

## Specification

### Requirements

1. Scan all Python files in `idecomp/` for bare `# type: ignore` (without error code)
2. For each bare ignore, determine the specific mypy error code and add it with an inline explanation
3. After completion, `grep -r '# type: ignore$' idecomp/ --include="*.py"` returns zero matches
4. `mypy idecomp/` still passes with zero errors

### Inputs/Props

- All Python files in `idecomp/`

### Outputs/Behavior

- Zero bare `# type: ignore` comments remain
- Every `# type: ignore` has a specific error code like `[import-untyped]`, `[override]`, `[arg-type]`, etc.
- Every `# type: ignore` has an inline explanation (e.g., `# no pandas-stubs package`)

### Error Handling

Not applicable.

## Acceptance Criteria

- [ ] Given the command `grep -r '# type: ignore$' idecomp/ --include="*.py"`, when executed, then zero matches are found
- [ ] Given the command `grep -c 'type: ignore\[' idecomp/ -r --include="*.py"`, when executed, then a count is returned (showing all ignores have codes)
- [ ] Given the command `mypy idecomp/`, when executed, then zero errors are reported
- [ ] Given the command `pytest -v`, when executed, then all 310 tests pass

## Implementation Guide

### Suggested Approach

1. Run `grep -rn '# type: ignore$' idecomp/ --include="*.py"` to find all remaining bare ignores
2. For each line, run `mypy` on that specific file to determine what error code the ignore suppresses
3. Replace `# type: ignore` with `# type: ignore[error-code]  # brief explanation`

**Common replacements**:

- `import pandas as pd  # type: ignore` -> `import pandas as pd  # type: ignore[import-untyped]  # no pandas-stubs package`
- `import numpy as np  # type: ignore` -> `import numpy as np  # type: ignore[import-untyped]  # no numpy-stubs package`

4. After all replacements, verify `mypy idecomp/` still passes

### Key Files to Modify

All Python files in `idecomp/` that have bare `# type: ignore` comments. The exact list depends on what was already fixed in tickets 006 and 007.

### Patterns to Follow

- inewave convention: `# type: ignore[error-code]  # brief reason`
- Never use bare `# type: ignore` -- always include the specific error code
- Reference: `/home/rogerio/git/inewave/inewave/newave/modelos/dger.py` for annotated ignore patterns

### Pitfalls to Avoid

- Do NOT remove `# type: ignore` comments without checking if they are still needed -- removing a needed ignore will cause mypy to fail
- Do NOT add explanation comments that are longer than 60 characters -- keep them concise
- If a `# type: ignore` is no longer needed (the underlying issue was fixed), remove it entirely rather than adding a code

## Testing Requirements

### Unit Tests

No new tests.

### Integration Tests

- `mypy idecomp/` passes with zero errors
- `pytest -v` shows all 310 tests pass

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-006-enable-mypy-strict-decomp.md, ticket-007-enable-mypy-strict-libs.md
- **Blocks**: ticket-009-implement-lazy-imports-decomp.md

## Effort Estimate

**Points**: 3
**Confidence**: Medium (depends on how many bare ignores remain after tickets 006/007)

## Out of Scope

- Adding type stubs for pandas/numpy (they don't exist in a form mypy recognizes)
- Annotating test files
- Removing valid type-ignore comments
