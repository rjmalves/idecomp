# ticket-014 Write migration guide and update changelog for v1.9.0

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Write a user-facing migration guide (`MIGRATION.md` at repo root) in Portuguese documenting all changes from v1.8.1 to v1.9.0 for downstream consumers (sintetizador-decomp). Also create or update `CHANGELOG.md` with a v1.9.0 entry listing all changes. Follow inewave's documentation patterns: audience-based language split (user-facing in Portuguese), MIGRATION.md as standalone repo-root document, section ordering prioritizing user actions first.

## Anticipated Scope

- **Files likely to be modified**: New `MIGRATION.md` at repo root, new or updated `CHANGELOG.md` at repo root
- **Key decisions needed**: Does idecomp already have a CHANGELOG.md? What format should it follow?
- **Open questions**:
  - Are there any breaking changes for downstream users? (StorageType migration is internal, but `read(version=...)` vs `set_version()` may affect users)
  - Should the migration guide document the `set_version()` deprecation even though idecomp's public API doesn't expose it?
  - What language should be used for technical terms (e.g., "lazy imports")?

## Dependencies

- **Blocked By**: All tickets in epics 01-03 (documentation must reflect completed work)
- **Blocks**: ticket-015-bump-package-version.md

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
