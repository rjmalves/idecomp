# Epic 02: Quality and Type Safety

## Goals

1. Enable mypy strict mode on all production code modules
2. Replace all 123 bare `# type: ignore` comments with specific error codes and explanations
3. Fix the 1 existing mypy error (cortdeco.py return type)
4. Add mypy configuration to `pyproject.toml` with per-module strict overrides
5. Implement lazy imports for `idecomp/decomp/__init__.py` (43 eager imports)
6. Reduce code duplication in `__concatena_blocos` pattern (3 files)

## Scope

- **In scope**: mypy strict configuration, type annotation fixes, bare type-ignore cleanup, lazy imports for decomp, deduplication of concatenation pattern
- **Out of scope**: New tests (epic-03), documentation (epic-04), changes to public API

## Tickets

| Ticket     | Title                                              | Points |
| ---------- | -------------------------------------------------- | ------ |
| ticket-004 | Fix existing mypy error in cortdeco.py             | 1      |
| ticket-005 | Add mypy strict configuration to pyproject.toml    | 2      |
| ticket-006 | Enable mypy strict for decomp handlers and models  | 3      |
| ticket-007 | Enable mypy strict for libs module                 | 2      |
| ticket-008 | Replace bare type-ignore comments with error codes | 3      |
| ticket-009 | Implement lazy imports for decomp module           | 2      |

## Success Criteria

- `mypy idecomp/ --strict` passes with zero errors (per-module overrides in `pyproject.toml`)
- `grep -r '# type: ignore$' idecomp/` returns zero matches
- `idecomp/decomp/__init__.py` uses PEP 562 `__getattr__` lazy import pattern
- All 310 tests continue to pass
