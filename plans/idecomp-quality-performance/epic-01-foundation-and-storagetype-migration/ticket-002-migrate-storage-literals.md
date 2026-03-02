# ticket-002 Migrate STORAGE string literals to StorageType enum

## Context

### Background

cfinterface v1.9.0 introduced the `StorageType` enum to replace string literals `"BINARY"` and `"TEXT"`. Using the old string literals emits `DeprecationWarning`. idecomp has 5 files that declare `STORAGE = "BINARY"` and must be migrated to `STORAGE = StorageType.BINARY`.

### Relation to Epic

This is the second ticket in Epic 01. It requires cfinterface >= 1.9.0 (ticket-001) and is a prerequisite for the test verification in ticket-003.

### Current State

Five files in `idecomp/decomp/` contain `STORAGE = "BINARY"`:

1. `/home/rogerio/git/idecomp/idecomp/decomp/vazoes.py` (line 19) -- SectionFile subclass
2. `/home/rogerio/git/idecomp/idecomp/decomp/postos.py` (line 19) -- RegisterFile subclass
3. `/home/rogerio/git/idecomp/idecomp/decomp/cortdeco.py` (line 17) -- SectionFile subclass
4. `/home/rogerio/git/idecomp/idecomp/decomp/hidr.py` (line 19) -- RegisterFile subclass
5. `/home/rogerio/git/idecomp/idecomp/decomp/mapcut.py` (line 20) -- SectionFile subclass

No files use `STORAGE = "TEXT"` -- all other handlers inherit the default `StorageType.TEXT` from their base classes.

## Specification

### Requirements

1. In each of the 5 files, replace `STORAGE = "BINARY"` with `STORAGE = StorageType.BINARY`
2. In each of the 5 files, add `from cfinterface.storage import StorageType` to the cfinterface import group
3. The import must be placed adjacent to existing cfinterface imports (before idecomp local imports)
4. No other code changes in these files

### Inputs/Props

- 5 handler files listed in Current State section

### Outputs/Behavior

- Each file has `STORAGE = StorageType.BINARY` instead of `STORAGE = "BINARY"`
- Each file imports `StorageType` from `cfinterface.storage`

### Error Handling

Not applicable -- this is a static code change.

## Acceptance Criteria

- [ ] Given the command `grep -r 'STORAGE = "BINARY"' idecomp/`, when executed after migration, then zero matches are found
- [ ] Given the command `grep -r 'StorageType.BINARY' idecomp/`, when executed after migration, then exactly 5 matches are found (one per file)
- [ ] Given the command `grep -r 'from cfinterface.storage import StorageType' idecomp/`, when executed after migration, then exactly 5 matches are found (one per file)
- [ ] Given `/home/rogerio/git/idecomp/idecomp/decomp/vazoes.py`, when opened, then `from cfinterface.storage import StorageType` appears in the cfinterface import group before idecomp imports
- [ ] Given the command `pytest tests/decomp/test_vazoes.py tests/decomp/test_postos.py tests/decomp/test_cortdeco.py tests/decomp/test_hidr.py tests/decomp/test_mapcut.py -v`, when executed, then all tests in these 5 files pass

## Implementation Guide

### Suggested Approach

For each of the 5 files, apply the same transformation:

1. Add `from cfinterface.storage import StorageType` adjacent to existing cfinterface imports
2. Replace `STORAGE = "BINARY"` with `STORAGE = StorageType.BINARY`

**Example for `hidr.py`**:

Before:

```python
from cfinterface.files.registerfile import RegisterFile
from idecomp.decomp.modelos.hidr import RegistroUHEHidr
...

class Hidr(RegisterFile):
    ...
    STORAGE = "BINARY"
```

After:

```python
from cfinterface.files.registerfile import RegisterFile
from cfinterface.storage import StorageType
from idecomp.decomp.modelos.hidr import RegistroUHEHidr
...

class Hidr(RegisterFile):
    ...
    STORAGE = StorageType.BINARY
```

### Key Files to Modify

1. `/home/rogerio/git/idecomp/idecomp/decomp/vazoes.py`
2. `/home/rogerio/git/idecomp/idecomp/decomp/postos.py`
3. `/home/rogerio/git/idecomp/idecomp/decomp/cortdeco.py`
4. `/home/rogerio/git/idecomp/idecomp/decomp/hidr.py`
5. `/home/rogerio/git/idecomp/idecomp/decomp/mapcut.py`

### Patterns to Follow

- Follow the inewave pattern: `from cfinterface.storage import StorageType` in the cfinterface import group, before idecomp local imports. See `/home/rogerio/git/inewave/inewave/newave/hidr.py` for reference.
- Import ordering convention: cfinterface imports first (all adjacent), then idecomp imports, then typing imports last.

### Pitfalls to Avoid

- Do NOT add `STORAGE = StorageType.TEXT` to files that don't currently have a STORAGE attribute -- they inherit TEXT from their base class and must not be given a redundant attribute (inewave learning)
- Do NOT change any other code in these files -- the ticket scope is strictly the STORAGE attribute and its import
- Do NOT reorder other imports while adding the StorageType import

## Testing Requirements

### Unit Tests

No new tests needed. Existing tests for these 5 handlers serve as regression tests.

### Integration Tests

- Run the relevant test files to confirm no regressions
- Run `pytest -W error::DeprecationWarning` to confirm no STORAGE-related deprecation warnings

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-001-bump-cfinterface-dependency.md
- **Blocks**: ticket-003-fix-identity-test-verify-suite.md

## Effort Estimate

**Points**: 2
**Confidence**: High

## Out of Scope

- Fixing the failing `test_neq_restricoes` test (ticket-003)
- Adding StorageType to files that don't currently have STORAGE attributes
- Any changes to the model files under `modelos/`
