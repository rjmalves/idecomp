# ticket-003 Fix identity-based removal test and verify suite

## Context

### Background

cfinterface v1.9.0 changed `RegisterData._index_of()` from equality-based (`==`) to identity-based (`is`) object lookup. This means `data.remove(obj)` only works when `obj` is the exact same Python object instance stored in the container, not a copy or a separately-constructed equal object. The test `test_neq_restricoes` in `tests/libs/test_restricoes.py` fails because it constructs a `RegistroReHorizPer` object from a different file instance and passes it to `data.remove()`, which raises `ValueError: Register not found in container`.

Additionally, 9 test files in `tests/decomp/` use the deprecated `set_version()` API. These should be migrated to `read(version=...)` to eliminate DeprecationWarning.

### Relation to Epic

This is the final ticket in Epic 01, completing the foundation by ensuring all 310 tests pass with zero failures and zero deprecation warnings.

### Current State

- `tests/libs/test_restricoes.py::test_neq_restricoes` fails with `ValueError: Register not found in container`
- 9 test files use `set_version()` instead of `read(version=...)`:
  1. `tests/decomp/test_dec_oper_evap.py`
  2. `tests/decomp/test_dec_oper_gnl.py`
  3. `tests/decomp/test_dec_oper_interc.py`
  4. `tests/decomp/test_dec_oper_ree.py`
  5. `tests/decomp/test_dec_oper_rhesoft.py`
  6. `tests/decomp/test_dec_oper_sist.py`
  7. `tests/decomp/test_dec_oper_usie.py`
  8. `tests/decomp/test_dec_oper_usih.py`
  9. `tests/decomp/test_dec_oper_usit.py`
- Running `pytest` shows: 309 passed, 1 failed, 45 warnings (14 DeprecationWarnings)

## Specification

### Requirements

1. Fix `test_neq_restricoes` to use same-container objects when calling `data.remove()`. The test must fetch the register from the file's own data container (via accessor or `data.of_type()`) rather than constructing a separate object.
2. In all 9 test files, replace `set_version()` calls with `read(content, version="...")` pattern.
3. After all fixes, the full test suite must pass with zero failures.
4. After all fixes, running `pytest -W error::DeprecationWarning` must not raise errors from STORAGE strings or `set_version()` calls.

### Inputs/Props

- 10 test files (1 restricoes + 9 dec_oper)

### Outputs/Behavior

- All 310 tests pass
- No DeprecationWarning from STORAGE strings
- No DeprecationWarning from `set_version()` calls
- The `test_neq_restricoes` test correctly validates inequality behavior using identity-safe operations

### Error Handling

- If any test uses `data.remove()` with a cross-container object, it must be refactored to use same-container access patterns. Grep `tests/` for `.data.remove(` to identify all cases.

## Acceptance Criteria

- [ ] Given the command `pytest tests/libs/test_restricoes.py::test_neq_restricoes -v`, when executed, then the test passes
- [ ] Given the command `grep -r "set_version" tests/ --include="*.py"`, when executed, then zero matches are found
- [ ] Given the command `pytest -v`, when executed, then 310 tests pass and 0 tests fail
- [ ] Given the command `pytest -W error::DeprecationWarning 2>&1 | grep -c "DeprecationWarning"`, when executed, then the output is 0
- [ ] Given the 9 dec_oper test files, when opened, then each uses `Handler.read(content, version="31.0.2")` instead of `handler.set_version("31.0.2"); handler.read(content)`

## Implementation Guide

### Suggested Approach

**Step 1: Fix `test_neq_restricoes`**

Read the current test in `tests/libs/test_restricoes.py` to understand what `test_neq_restricoes` does. The issue is that it calls `data.remove(register)` where `register` was obtained from a different file instance. The fix is to fetch the register from the same file's data container.

Pattern from inewave learning: `cf.data.remove(cf.accessor()[0])` is valid because inewave accessors return the stored instance. Passing an object from a different file instance to `remove()` raises `ValueError` under cfinterface 1.9.0.

**Step 2: Migrate set_version() in 9 test files**

Each test file has a pattern like:

```python
handler = DecOperUsih()
handler.set_version("31.0.2")
handler.read(content)
```

Replace with:

```python
handler = DecOperUsih.read(content, version="31.0.2")
```

Reference: inewave test files `tests/nwlistop/test_cmarg.py` and `tests/nwlistop/test_pivarm.py` demonstrate this pattern.

**Step 3: Verify full suite**

Run `pytest -v` and `pytest -W error::DeprecationWarning` to confirm zero failures and zero deprecation warnings from STORAGE or set_version.

### Key Files to Modify

1. `/home/rogerio/git/idecomp/tests/libs/test_restricoes.py` -- fix identity-based removal
2. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_evap.py` -- set_version migration
3. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_gnl.py` -- set_version migration
4. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_interc.py` -- set_version migration
5. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_ree.py` -- set_version migration
6. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_rhesoft.py` -- set_version migration
7. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_sist.py` -- set_version migration
8. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_usie.py` -- set_version migration
9. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_usih.py` -- set_version migration
10. `/home/rogerio/git/idecomp/tests/decomp/test_dec_oper_usit.py` -- set_version migration

### Patterns to Follow

- **Identity-safe removal**: Always fetch the register from the file's own `data` container before calling `remove()`. Never pass a register from a different file instance.
- **read(version=...) convention**: `Handler.read(content, version="31.0.2")` instead of deprecated `handler.set_version("31.0.2"); handler.read(content)`.
- Reference: inewave's `tests/nwlistop/test_cmarg.py` for the version read pattern.

### Pitfalls to Avoid

- Do NOT suppress the identity-based removal failure with a try/except -- fix the root cause
- Do NOT change the test assertions, only the setup code (how objects are obtained)
- Do NOT change handler code -- all changes are in test files only
- Grep for `.data.remove(` in ALL test files to ensure no other identity-based removal issues exist beyond `test_neq_restricoes`

## Testing Requirements

### Unit Tests

The tests themselves are being fixed. Verification is done by running the full suite.

### Integration Tests

- `pytest -v` -- all 310 tests pass
- `pytest -W error::DeprecationWarning` -- no deprecation warnings from STORAGE or set_version

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-001-bump-cfinterface-dependency.md, ticket-002-migrate-storage-literals.md
- **Blocks**: All tickets in epic-02 and beyond

## Effort Estimate

**Points**: 2
**Confidence**: High

## Out of Scope

- Fixing mypy errors (epic-02)
- Adding new tests (epic-03)
- Changes to production code (only test files are modified)
- Adding DeprecationWarning to idecomp's own deprecated APIs (not applicable)
