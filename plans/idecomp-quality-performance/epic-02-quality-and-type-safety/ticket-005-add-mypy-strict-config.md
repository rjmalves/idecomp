# ticket-005 Add mypy strict configuration to pyproject.toml

## Context

### Background

idecomp has no mypy configuration in `pyproject.toml`. Running `mypy idecomp/ --strict` reports 1539 errors in 38 files. Before enabling strict mode per-module, a `[tool.mypy]` section must be added with global settings and per-module `[[tool.mypy.overrides]]` blocks. The inewave plan established proven patterns for this: `strict = true` per module with `warn_return_any = false` globally (because cfinterface's `Section.data` and `Block.data` are `Any`-typed).

### Relation to Epic

This ticket provides the mypy configuration infrastructure. Subsequent tickets (006, 007) will fix the actual type errors to make each module pass under strict mode.

### Current State

- `pyproject.toml` has no `[tool.mypy]` section
- `mypy idecomp/` passes with 0 errors (after ticket-004 fixes cortdeco.py)
- `mypy idecomp/ --strict` reports 1539 errors in 38 files
- cfinterface's `Block.data` and `Section.data` are `Any`-typed, which makes `warn_return_any` produce hundreds of meaningless errors

## Specification

### Requirements

1. Add a `[tool.mypy]` section to `/home/rogerio/git/idecomp/pyproject.toml` with `warn_return_any = false`
2. Add `[[tool.mypy.overrides]]` blocks for each production code module, all with `strict = true` and `warn_return_any = false`:
   - `idecomp.decomp.*`
   - `idecomp.decomp.modelos.*`
   - `idecomp.decomp.modelos.blocos.*`
   - `idecomp.decomp.modelos.arquivoscsv.*`
   - `idecomp.libs.*`
   - `idecomp.libs.modelos.*`
   - `idecomp.config`
3. Do NOT enable strict mode at the global level -- use per-module overrides only
4. After adding the configuration, `mypy idecomp/` should still run (it will report strict-mode errors, which will be fixed in ticket-006 and ticket-007)

### Inputs/Props

- File: `/home/rogerio/git/idecomp/pyproject.toml`

### Outputs/Behavior

- `pyproject.toml` has a `[tool.mypy]` section with `warn_return_any = false`
- `pyproject.toml` has at least 7 `[[tool.mypy.overrides]]` blocks

### Error Handling

Not applicable.

## Acceptance Criteria

- [ ] Given `pyproject.toml`, when searching for `[tool.mypy]`, then exactly one section is found
- [ ] Given `pyproject.toml`, when searching for `strict = true`, then at least 7 matches are found (one per override block)
- [ ] Given `pyproject.toml`, when searching for `warn_return_any = false`, then it appears in every override block
- [ ] Given the command `mypy idecomp/config.py`, when executed, then zero errors are reported (config.py is simple enough to pass strict immediately)
- [ ] Given the command `mypy idecomp/`, when executed (without --strict flag), then the mypy configuration is picked up from `pyproject.toml` and strict mode is applied per-module

## Implementation Guide

### Suggested Approach

Add the following configuration to the end of `pyproject.toml` (before any `[tool.uv.sources]` section if present):

```toml
[tool.mypy]
warn_return_any = false

[[tool.mypy.overrides]]
module = "idecomp.decomp.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idecomp.decomp.modelos.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idecomp.decomp.modelos.blocos.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idecomp.decomp.modelos.arquivoscsv.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idecomp.libs.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idecomp.libs.modelos.*"
strict = true
warn_return_any = false

[[tool.mypy.overrides]]
module = "idecomp.config"
strict = true
warn_return_any = false
```

### Key Files to Modify

- `/home/rogerio/git/idecomp/pyproject.toml`

### Patterns to Follow

- Exact same pattern as inewave's `pyproject.toml` `[tool.mypy]` section. See `/home/rogerio/git/inewave/pyproject.toml` for reference.
- `warn_return_any = false` is mandatory both globally and per-override because cfinterface's `Section.data`, `Block.data`, and `Register.data` are all `Any`-typed.

### Pitfalls to Avoid

- Do NOT set `strict = true` at the global `[tool.mypy]` level -- only in per-module overrides. Global strict breaks third-party imports.
- Do NOT omit `warn_return_any = false` from any override block -- this would produce hundreds of errors from cfinterface's `Any`-typed data attributes.
- Do NOT add overrides for test files -- tests are not production code and strict mode on tests is out of scope.

## Testing Requirements

### Unit Tests

No new tests.

### Integration Tests

- `mypy idecomp/config.py` passes with zero errors (config.py is trivially strict-compliant)
- `mypy idecomp/` runs without configuration errors

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-004-fix-mypy-error-cortdeco.md
- **Blocks**: ticket-006-enable-mypy-strict-decomp.md, ticket-007-enable-mypy-strict-libs.md

## Effort Estimate

**Points**: 2
**Confidence**: High

## Out of Scope

- Fixing type errors revealed by strict mode (ticket-006, ticket-007)
- Adding mypy overrides for test files
- Changing any Python source files
