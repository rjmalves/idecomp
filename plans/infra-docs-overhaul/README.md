# Infrastructure & Documentation Overhaul (idecomp)

Modernize the idecomp Python package infrastructure, CI/CD pipelines, documentation theme/content, and repository polish. Replicates the successful overhaul from the inewave sibling project, adapted for idecomp's DECOMP-specific structure.

## Tech Stack

- Python 3.10+ / Hatchling build system
- GitHub Actions CI/CD
- Sphinx + Furo documentation theme
- ruff (linting/formatting) + mypy (type checking)
- pre-commit hooks

## Epics

| Epic | Name                            | Tickets | Detail Level | Phase     |
| ---- | ------------------------------- | ------- | ------------ | --------- |
| 1    | Packaging & CI Modernization    | 5       | Detailed     | completed |
| 2    | Sphinx Modernization            | 2       | Detailed     | completed |
| 3    | Documentation Content Expansion | 5       | Refined      | completed |
| 4    | Repository Polish               | 4       | Refined      | completed |

## Progress

| Ticket     | Title                                                    | Epic    | Status    | Detail Level | Readiness | Quality | Badge      |
| ---------- | -------------------------------------------------------- | ------- | --------- | ------------ | --------- | ------- | ---------- |
| ticket-001 | Modernize pyproject.toml Metadata and Dependency Groups  | epic-01 | completed | Detailed     | 1.00      | 1.00    | EXCELLENT  |
| ticket-002 | Restructure CI Workflow into Parallel Jobs               | epic-01 | completed | Detailed     | 1.00      | 1.00    | EXCELLENT  |
| ticket-003 | Migrate Docs Deployment to Official GitHub Pages Actions | epic-01 | completed | Detailed     | 1.00      | 1.00    | EXCELLENT  |
| ticket-004 | Create Tag-Triggered Release Workflow                    | epic-01 | completed | Detailed     | 1.00      | 1.00    | EXCELLENT  |
| ticket-005 | Add Pre-commit Hooks Configuration                       | epic-01 | completed | Detailed     | 1.00      | 1.00    | EXCELLENT  |
| ticket-006 | Migrate Sphinx Theme to Furo                             | epic-02 | completed | Detailed     | 1.00      | 0.85    | ACCEPTABLE |
| ticket-007 | Update Sphinx-Gallery Examples for Furo Compatibility    | epic-02 | completed | Detailed     | 0.94      | 1.00    | EXCELLENT  |
| ticket-008 | Create Architecture Documentation Page                   | epic-03 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |
| ticket-009 | Create FAQ Documentation Page                            | epic-03 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |
| ticket-010 | Create Performance Guide Page                            | epic-03 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |
| ticket-011 | Improve API Reference with Autosummary Blocks            | epic-03 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |
| ticket-012 | Update index.rst Toctree with Guias Section              | epic-03 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |
| ticket-013 | Expand README with Badges and Sections                   | epic-04 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |
| ticket-014 | Create CONTRIBUTING.md                                   | epic-04 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |
| ticket-015 | Reformat CHANGELOG to Keep a Changelog Standard          | epic-04 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |
| ticket-016 | Update Installation Documentation                        | epic-04 | completed | Refined      | 1.00      | 1.00    | EXCELLENT  |

## Dependency Graph

```
ticket-001 (pyproject.toml)
  |---> ticket-002 (CI restructure) ---> ticket-013 (README badges)
  |---> ticket-004 (release workflow)
  |---> ticket-005 (pre-commit) ---> ticket-014 (CONTRIBUTING)
  |---> ticket-006 (Furo theme)
            |---> ticket-007 (gallery examples)
            |---> ticket-008 (architecture page) --+
            |---> ticket-009 (FAQ page) -----------+--> ticket-012 (index toctree)
            |---> ticket-010 (performance page) ---+
            |---> ticket-011 (API autosummary)

ticket-003 (docs deployment) [independent]
ticket-015 (changelog) [independent]
ticket-016 (installation docs) [independent]
```

## Notes

- This is a **progressive plan**: Epics 1-2 have fully detailed tickets; Epics 3-4 have outline tickets that were refined with learnings from earlier epics
- All 4 epics have been **refined** and are ready for implementation
- All documentation content must be written in **Brazilian Portuguese** (pt_BR)
- Key learnings from the inewave overhaul are embedded in the detailed tickets (regex version extraction, mypy manual stage, cfinterface workarounds)
