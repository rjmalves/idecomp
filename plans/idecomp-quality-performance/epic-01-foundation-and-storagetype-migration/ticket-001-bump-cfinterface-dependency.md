# ticket-001 Bump cfinterface dependency to >= 1.9.0

## Context

### Background

The idecomp package currently declares `"cfinterface>=1.8"` in `pyproject.toml`. cfinterface v1.9.0 has been released with StorageType enum, array-backed containers, optimized FloatField, schema versioning, and type-safe I/O dispatch. idecomp must be upgraded to use the new version as a prerequisite for all subsequent work in this plan.

### Relation to Epic

This is the first ticket in Epic 01 (Foundation and StorageType Migration). All other tickets depend on cfinterface >= 1.9.0 being declared and installable.

### Current State

- `pyproject.toml` line 9: `"cfinterface>=1.8"`
- cfinterface 1.9.0 is already installed locally at `/home/rogerio/git/cfinterface`
- The existing test suite runs against cfinterface 1.9.0 already (309 pass, 1 fail)
- No `[tool.uv.sources]` override exists in `pyproject.toml`

## Specification

### Requirements

1. Update the cfinterface dependency floor in `pyproject.toml` from `"cfinterface>=1.8"` to `"cfinterface>=1.9.0"`
2. Add a `[tool.uv.sources]` local path override pointing to `/home/rogerio/git/cfinterface` so development continues against the local copy while cfinterface 1.9.0 may or may not be on PyPI
3. Verify the package resolves correctly with `uv pip compile` or equivalent

### Inputs/Props

- File: `/home/rogerio/git/idecomp/pyproject.toml`

### Outputs/Behavior

- `pyproject.toml` `dependencies` list has `"cfinterface>=1.9.0"` instead of `"cfinterface>=1.8"`
- `pyproject.toml` has `[tool.uv.sources]` section with `cfinterface = { path = "/home/rogerio/git/cfinterface" }` for local development

### Error Handling

- If cfinterface 1.9.0 is not yet on PyPI, the `[tool.uv.sources]` override ensures local resolution. A comment must note that the override should be removed before release.

## Acceptance Criteria

- [ ] Given `pyproject.toml`, when searching for `cfinterface>=1.8`, then zero matches are found
- [ ] Given `pyproject.toml`, when searching for `cfinterface>=1.9.0`, then exactly one match is found in the `dependencies` list
- [ ] Given `pyproject.toml`, when searching for `[tool.uv.sources]`, then a section exists with `cfinterface` pointing to the local path
- [ ] Given the updated `pyproject.toml`, when running `python -c "import cfinterface; print(cfinterface.__version__)"`, then the output is `1.9.0` or higher
- [ ] Given the updated `pyproject.toml`, when running `pytest --co -q`, then all 310 tests are collected without import errors

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/pyproject.toml`
2. Change `"cfinterface>=1.8"` to `"cfinterface>=1.9.0"` in the `dependencies` list (line 9)
3. Add a `[tool.uv.sources]` section after the existing sections with a comment:
   ```toml
   # Remove this override once cfinterface 1.9.0 is published to PyPI
   [tool.uv.sources]
   cfinterface = { path = "/home/rogerio/git/cfinterface" }
   ```
4. Run `python -c "import cfinterface; print(cfinterface.__version__)"` to verify
5. Run `pytest --co -q` to verify test collection

### Key Files to Modify

- `/home/rogerio/git/idecomp/pyproject.toml` (lines 8-9 for dependency, new section at end for uv sources)

### Patterns to Follow

- Same pattern as inewave's `pyproject.toml`: `"cfinterface>=1.9.0"` with `[tool.uv.sources]` override. See `/home/rogerio/git/inewave/pyproject.toml` for reference.
- Use `>=` version bound, not `==` pin, because idecomp is a library.

### Pitfalls to Avoid

- Do NOT pin to exact version `"cfinterface==1.9.0"` -- this is a library, not an application
- Do NOT forget the `[tool.uv.sources]` comment about removing before release
- Do NOT modify any other dependencies in this ticket

## Testing Requirements

### Unit Tests

No new tests needed. This is a dependency change only.

### Integration Tests

- Run `pytest --co -q` to verify all 310 tests collect successfully
- Run `python -c "import cfinterface; print(cfinterface.__version__)"` to verify version

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: None (this is the first ticket)
- **Blocks**: ticket-002-migrate-storage-literals.md, ticket-003-fix-identity-test-verify-suite.md

## Effort Estimate

**Points**: 1
**Confidence**: High

## Out of Scope

- Migrating STORAGE string literals (ticket-002)
- Fixing failing tests (ticket-003)
- Any code changes beyond `pyproject.toml`
