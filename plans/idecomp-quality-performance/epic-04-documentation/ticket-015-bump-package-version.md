# ticket-015 Bump package version to 1.9.0

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Update the package version from `1.8.1` to `1.9.0` in `idecomp/__init__.py` and remove the `[tool.uv.sources]` local path override from `pyproject.toml` (if cfinterface 1.9.0 is available on PyPI by this point). This is the final release preparation ticket.

## Anticipated Scope

- **Files likely to be modified**: `idecomp/__init__.py` (version string), `pyproject.toml` (remove uv sources override)
- **Key decisions needed**: Is cfinterface 1.9.0 on PyPI yet? If not, the uv.sources override must stay.
- **Open questions**:
  - Should the version be 1.9.0 (matching cfinterface) or follow idecomp's own versioning scheme?
  - Should a git tag be created for the release?

## Dependencies

- **Blocked By**: ticket-014-write-migration-guide-changelog.md
- **Blocks**: None (final ticket in the plan)

## Effort Estimate

**Points**: 1
**Confidence**: Low (will be re-estimated during refinement)
