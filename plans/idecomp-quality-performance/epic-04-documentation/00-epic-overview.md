# Epic 04: Documentation

## Goals

1. Write a migration guide for downstream users (sintetizador-decomp) covering the cfinterface 1.9.0 upgrade
2. Update the changelog for v1.9.0
3. Bump the package version to 1.9.0

## Scope

- **In scope**: Migration guide, changelog, version bump
- **Out of scope**: Sphinx API documentation updates (autodoc handles those automatically), new tutorials

## Tickets

| Ticket     | Title                                                 | Points |
| ---------- | ----------------------------------------------------- | ------ |
| ticket-014 | Write migration guide and update changelog for v1.9.0 | 2      |
| ticket-015 | Bump package version to 1.9.0                         | 1      |

## Success Criteria

- `MIGRATION.md` exists at repo root with upgrade instructions
- `CHANGELOG.md` or changelog section exists with v1.9.0 entry
- `idecomp/__init__.py` declares `__version__ = "1.9.0"`
