# Epic 01: Foundation and StorageType Migration

## Goals

1. Bump cfinterface dependency from >= 1.8 to >= 1.9.0
2. Replace all 5 `STORAGE = "BINARY"` string literals with `StorageType.BINARY`
3. Fix the identity-based removal bug in `test_neq_restricoes`
4. Verify the full test suite passes with zero failures and zero deprecation warnings from STORAGE strings

## Scope

- **In scope**: pyproject.toml dependency bump, 5 handler file STORAGE migrations, 1 test fix, full test suite verification
- **Out of scope**: mypy strict mode, lazy imports, new VERSIONS, TabularSection adoption

## Tickets

| Ticket     | Title                                               | Points |
| ---------- | --------------------------------------------------- | ------ |
| ticket-001 | Bump cfinterface dependency to >= 1.9.0             | 1      |
| ticket-002 | Migrate STORAGE string literals to StorageType enum | 2      |
| ticket-003 | Fix identity-based removal test and verify suite    | 2      |

## Success Criteria

- `grep -r 'STORAGE = "BINARY"' idecomp/` returns zero matches
- `pyproject.toml` declares `"cfinterface>=1.9.0"`
- `pytest` shows 310 tests passed, 0 failed
- No `DeprecationWarning` from STORAGE string usage in test output
