# ticket-015 Bump package version to 1.9.0

## Context

### Background

All production code changes (epics 01-03) and documentation (ticket-014) are complete. The final step is to update the version string from `1.8.1` to `1.9.0` in the single source-of-truth file `idecomp/__init__.py`. Hatchling reads the version from this file via `[tool.hatch.version] path = "idecomp/__init__.py"` in pyproject.toml, so no other version declaration needs updating.

### Relation to Epic

This is the second and final ticket in epic-04 (Documentation) and the last ticket in the entire plan. It must run after ticket-014 so that all documentation is finalized before the version is stamped.

### Current State

- `/home/rogerio/git/idecomp/idecomp/__init__.py` declares `__version__ = "1.8.1"` on line 9.
- `/home/rogerio/git/idecomp/pyproject.toml` contains `[tool.hatch.version] path = "idecomp/__init__.py"`, which reads the version dynamically. No version string exists in pyproject.toml itself.
- `/home/rogerio/git/idecomp/pyproject.toml` contains a `[tool.uv.sources]` override pointing cfinterface to a local path (`/home/rogerio/git/cfinterface`). cfinterface 1.9.0 is NOT published to PyPI (latest is 1.8.3 as of 2026-03-02). This override must remain until cfinterface 1.9.0 is published.

## Specification

### Requirements

1. Change the `__version__` string in `/home/rogerio/git/idecomp/idecomp/__init__.py` from `"1.8.1"` to `"1.9.0"`.
2. Do NOT remove the `[tool.uv.sources]` section from pyproject.toml -- cfinterface 1.9.0 is not on PyPI yet.
3. Do NOT create a git tag -- tagging is a release-management decision outside this plan's scope.

### Inputs/Props

None -- this is a single-line string replacement.

### Outputs/Behavior

After the change, `python -c "import idecomp; print(idecomp.__version__)"` prints `1.9.0`.

### Error Handling

Not applicable -- single-line edit with no runtime logic.

### Out of Scope

- Removing the `[tool.uv.sources]` local path override (cfinterface 1.9.0 is not on PyPI)
- Creating a git tag for the release
- Publishing to PyPI
- Modifying pyproject.toml version metadata (Hatchling reads from `__init__.py`)

## Acceptance Criteria

- [ ] Given `/home/rogerio/git/idecomp/idecomp/__init__.py`, when the file is read, then it contains `__version__ = "1.9.0"` and does NOT contain `__version__ = "1.8.1"`.
- [ ] Given `/home/rogerio/git/idecomp/pyproject.toml`, when the file is read, then the `[tool.uv.sources]` section with the cfinterface local path override is still present.
- [ ] Given a Python environment with idecomp installed, when `python -c "import idecomp; print(idecomp.__version__)"` is run, then the output is `1.9.0`.

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/idecomp/__init__.py`.
2. Replace `__version__ = "1.8.1"` with `__version__ = "1.9.0"` on line 9.
3. Verify no other files declare a version string (Hatchling uses the single source in `__init__.py`).

### Key Files to Modify

- `/home/rogerio/git/idecomp/idecomp/__init__.py` (line 9: version string)

### Patterns to Follow

- The version string format is a quoted string assigned to `__version__`. Match the existing format exactly: `__version__ = "1.9.0"`.

### Pitfalls to Avoid

- Do NOT edit `pyproject.toml` to add a static version. The project uses `dynamic = ["version"]` with Hatchling reading from `__init__.py`.
- Do NOT remove the `[tool.uv.sources]` override. A comment in pyproject.toml already says `# Remove this override once cfinterface 1.9.0 is published to PyPI`. This must stay until that condition is met.
- Do NOT create a git tag. Tagging is a separate release-management action.

## Testing Requirements

### Unit Tests

Not applicable -- version string change only.

### Integration Tests

Not applicable.

### E2E Tests

Not applicable.

### Verification

- `grep '__version__' /home/rogerio/git/idecomp/idecomp/__init__.py` outputs `__version__ = "1.9.0"`.
- `grep 'cfinterface.*path' /home/rogerio/git/idecomp/pyproject.toml` outputs the local path override line, confirming it was not removed.

## Dependencies

- **Blocked By**: ticket-014-write-migration-guide-changelog.md
- **Blocks**: None (final ticket in the plan)

## Effort Estimate

**Points**: 1
**Confidence**: High
