# idecomp Quality and Performance Upgrade

## Overview

Progressive plan to upgrade idecomp (v1.8.1 -> v1.9.0) to leverage cfinterface v1.9.0 features: StorageType enum, optimized FloatField, type-safe I/O dispatch, and lazy imports. Adapted from the completed inewave 7-epic plan, scaled down to idecomp's smaller codebase (192 files, ~23K LOC, ~7K production LOC).

## Tech Stack

- Python 3.10+
- cfinterface >= 1.9.0
- numpy >= 2.0, pandas >= 2.2
- Build: Hatchling
- Quality: ruff (80 char), mypy, pytest + coverage, sphinx

## Epics

| Epic | Name                                 | Tickets      | Status    |
| ---- | ------------------------------------ | ------------ | --------- |
| 01   | Foundation and StorageType Migration | 3 (detailed) | completed |
| 02   | Quality and Type Safety              | 6 (detailed) | pending   |
| 03   | Testing and Performance              | 4 (outline)  | pending   |
| 04   | Documentation                        | 2 (outline)  | pending   |

## Progress Tracking

| Ticket     | Title                                                  | Epic    | Status    | Detail Level | Readiness | Quality | Badge |
| ---------- | ------------------------------------------------------ | ------- | --------- | ------------ | --------- | ------- | ----- |
| ticket-001 | Bump cfinterface dependency to >= 1.9.0                | epic-01 | completed | Detailed     | 1.00      | --      | --    |
| ticket-002 | Migrate STORAGE string literals to StorageType enum    | epic-01 | completed | Detailed     | 0.98      | --      | --    |
| ticket-003 | Fix identity-based removal test and verify suite       | epic-01 | completed | Detailed     | 0.96      | --      | --    |
| ticket-004 | Fix existing mypy error in cortdeco.py                 | epic-02 | completed | Detailed     | 1.00      | --      | --    |
| ticket-005 | Add mypy strict configuration to pyproject.toml        | epic-02 | completed | Detailed     | 1.00      | --      | --    |
| ticket-006 | Enable mypy strict mode for decomp handlers and models | epic-02 | completed | Detailed     | 0.92      | --      | --    |
| ticket-007 | Enable mypy strict mode for libs module                | epic-02 | pending   | Detailed     | 0.98      | --      | --    |
| ticket-008 | Replace bare type-ignore comments with error codes     | epic-02 | pending   | Detailed     | 0.92      | --      | --    |
| ticket-009 | Implement lazy imports for decomp module               | epic-02 | pending   | Detailed     | 1.00      | --      | --    |
| ticket-010 | Add round-trip tests for decomp handlers               | epic-03 | pending   | Outline      | --        | --      | --    |
| ticket-011 | Optimize DataFrame concatenation in BlockFile handlers | epic-03 | pending   | Outline      | --        | --      | --    |
| ticket-012 | Add pytest-xdist and optimize test execution           | epic-03 | pending   | Outline      | --        | --      | --    |
| ticket-013 | Create benchmark suite for read performance            | epic-03 | pending   | Outline      | --        | --      | --    |
| ticket-014 | Write migration guide and update changelog for v1.9.0  | epic-04 | pending   | Outline      | --        | --      | --    |
| ticket-015 | Bump package version to 1.9.0                          | epic-04 | pending   | Outline      | --        | --      | --    |

## Key Differences from inewave Plan

1. **No TabularSection migration**: idecomp's TabelaCSV is already schema-driven (LINE_MODEL + COLUMN_NAMES); no nwlistop-style boilerplate to eliminate
2. **No schema versioning epic**: idecomp already has 9 VERSIONS dictionaries covering known DECOMP format differences
3. **4 epics / 15 tickets** vs inewave's 7 epics / 33 tickets -- proportional to ~7K vs ~18K production LOC
4. **Combined quality+performance epic**: idecomp's smaller scale allows merging quality and performance work
