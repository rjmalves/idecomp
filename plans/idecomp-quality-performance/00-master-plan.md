# Master Plan: idecomp Quality and Performance Upgrade

## Executive Summary

Upgrade the idecomp package (v1.8.1, 192 Python files, ~23K LOC) to fully leverage cfinterface v1.9.0, applying the patterns and learnings from the completed inewave overhaul. This plan covers four epics: foundation upgrade with StorageType migration and critical bug fix, quality and type safety improvements, testing and performance enhancements, and documentation updates.

## Goals and Non-Goals

### Goals

1. **Eliminate deprecation warnings**: Replace all 5 `STORAGE = "BINARY"` string literals with `StorageType.BINARY` and bump cfinterface dependency to >= 1.9.0
2. **Fix the existing failing test**: The `test_neq_restricoes` test fails due to cfinterface 1.9.0's identity-based `_index_of()` -- fix the test to use same-container objects
3. **Migrate deprecated API usage**: Replace 9 test files using `set_version()` with `read(version=...)` pattern
4. **Strengthen type safety**: Move toward mypy strict mode, replace 123 bare `# type: ignore` comments with specific error codes, fix the 1 existing mypy error
5. **Implement lazy imports**: Convert the `idecomp/decomp/__init__.py` eager imports (43 entries) to PEP 562 lazy imports
6. **Improve test quality**: Add round-trip tests where write() is implemented, optimize test execution with pytest-xdist
7. **Update documentation**: Migration guide for downstream users, changelog for v1.9.0

### Non-Goals

- Changing the public API surface (all changes must be backward-compatible)
- Rewriting the decomp module's Block/Section classes from scratch
- Adding TabularSection adoption -- idecomp's TabelaCSV pattern is already schema-driven and does not benefit from migration (unlike inewave's nwlistop)
- Adding async file I/O support
- Dropping Python 3.10 support
- Removing pandas as a dependency (idecomp legitimately depends on DataFrames)
- Adding new VERSIONS dictionaries -- the 9 existing VERSIONS files already cover known DECOMP format differences

## Architecture Overview

### Current State

```
idecomp/
  decomp/          # 43 handlers (25 ArquivoCSV, 5 BlockFile, 5 SectionFile, 4 RegisterFile) + models
    modelos/
      blocos/      # 2 base block types (TabelaCSV, VersaoModelo)
      arquivoscsv/ # 1 base archive (ArquivoCSV)
      *.py         # ~25 model files for individual handlers
  libs/            # 2 handler files (UsinasHidreletricas, Restricoes) + models
  config.py        # Constants (MAX_PATAMARES, MESES, etc.)
```

**Key patterns**:

- `STORAGE = "BINARY"` used as string literal in 5 files: vazoes.py, postos.py, cortdeco.py, hidr.py, mapcut.py
- 25 ArquivoCSV subclasses use the TabelaCSV pattern with LINE_MODEL + COLUMN_NAMES -- already schema-driven, no need for TabularSection migration
- 9 handlers have VERSIONS dictionaries for DECOMP v31.0.2 vs v31.1.2 format differences
- Tests use mock data via `tests/mocks/` with `unittest.mock.patch` on `builtins.open`
- 123 bare `# type: ignore` comments (no error code specified)
- 1 mypy error in non-strict mode (cortdeco.py return type)
- 1 failing test (test_neq_restricoes -- cfinterface identity-based removal)
- 9 test files use deprecated `set_version()` instead of `read(version=...)`
- `idecomp/decomp/__init__.py` has 43 eager imports
- No mypy configuration in pyproject.toml
- 310 tests, 309 passing, 1 failing, 45 warnings

### Target State

```
idecomp/
  decomp/          # Same structure, STORAGE = StorageType.BINARY, lazy imports
    modelos/       # Same files, improved type annotations
      blocos/      # Same
      arquivoscsv/ # Same
  libs/            # Same, fixed identity-based removal test
  config.py        # Unchanged
```

**Key improvements**:

- All `STORAGE` attributes use `StorageType` enum
- cfinterface dependency >= 1.9.0
- All tests passing (310/310), including fixed identity test
- Tests use `read(version=...)` instead of deprecated `set_version()`
- mypy strict mode passing on all production code
- Lazy imports for decomp module
- pytest-xdist for parallel test execution
- Round-trip tests for handlers with write() support
- Migration guide and changelog for downstream users

### Key Design Decisions

1. **No TabularSection migration needed**: Unlike inewave's nwlistop module (162 files with boilerplate `ValoresSerie`/`ValoresSeriePatamar` blocks), idecomp's `TabelaCSV` pattern is already clean and schema-driven. Each subclass defines `LINE_MODEL`, `COLUMN_NAMES`, and `BEGIN_PATTERN` -- this IS the schema-driven approach. Migrating to TabularSection would add complexity without reducing boilerplate.
2. **No new VERSIONS needed**: idecomp already has 9 handler files with VERSIONS for DECOMP v31.0.2/v31.1.2. No other format differences are known.
3. **Smaller epic count**: idecomp is ~7K prod LOC vs inewave's ~18K LOC. The inewave plan had 7 epics and 33 tickets; idecomp needs only 4 epics and ~16 tickets.
4. **Foundation epic critical path**: The identity-based removal bug in the test must be fixed immediately because it proves cfinterface 1.9.0 breaking changes affect idecomp.
5. **Combined quality+performance epic**: Since idecomp is small, quality (mypy strict) and performance (lazy imports) can share an epic, unlike inewave which split them.

## Technical Approach

### Tech Stack

- **Language**: Python 3.10+
- **Dependencies**: cfinterface >= 1.9.0, numpy >= 2.0, pandas >= 2.2
- **Build**: Hatchling
- **CI**: pytest + coverage, mypy, ruff
- **Quality**: ruff (80 char line length), mypy, pytest + coverage, sphinx

### Component/Module Breakdown

| Module      | Files                   | Migration Scope                                         |
| ----------- | ----------------------- | ------------------------------------------------------- |
| `decomp/`   | 43 handlers, ~25 models | 5 STORAGE migrations, 9 set_version test updates, types |
| `libs/`     | 2 handlers, 2 models    | Fix identity test, type annotations                     |
| `config.py` | 1 file                  | Unchanged                                               |

### Handler File Distribution by Base Class

| Base Class   | Count  | Has VERSIONS? | Notes                             |
| ------------ | ------ | ------------- | --------------------------------- |
| ArquivoCSV   | 25     | 9 of 25       | TabelaCSV subclass per handler    |
| BlockFile    | 5      | 0             | relato, custos, relgnl, etc.      |
| SectionFile  | 5      | 0             | vazoes, cortdeco, mapcut, etc.    |
| RegisterFile | 4      | 0             | dadger, dadgnl, hidr, postos      |
| **Total**    | **39** |               | Plus 2 libs RegisterFile handlers |

### Data Flow

```
File on disk
    |
    v
cfinterface BlockFile/SectionFile/RegisterFile.read()
    |
    v
Block.read() / Section.read() / Register.read()
    |
    v
Handler properties (.tabela, .cadastro, etc.) -- convert to pd.DataFrame
    |
    v
User code (downstream consumers like sintetizador-decomp)
```

### Testing Strategy

- **Regression tests**: All 310 existing tests must pass (including the currently-failing one after fix)
- **Round-trip tests**: Add for handlers where write() is implemented (hidr, postos, vazoes, dadger, dadgnl)
- **Version tests**: Migrate 9 test files from set_version() to read(version=...)
- **Parallel execution**: Add pytest-xdist for development speed

## Phases and Milestones

| Epic | Name                                 | Scope                                             | Duration Estimate |
| ---- | ------------------------------------ | ------------------------------------------------- | ----------------- |
| 1    | Foundation and StorageType Migration | Bump cfinterface, migrate 5 STORAGE literals, fix | 1 week            |
| 2    | Quality and Type Safety              | mypy strict, type annotations, lazy imports       | 2-3 weeks         |
| 3    | Testing and Performance              | Round-trip tests, version test migration, xdist   | 1-2 weeks         |
| 4    | Documentation                        | Migration guide, changelog, version bump          | 1 week            |

## Risk Analysis

| Risk                                                 | Probability | Impact | Mitigation                                                                                      |
| ---------------------------------------------------- | ----------- | ------ | ----------------------------------------------------------------------------------------------- |
| cfinterface identity-based removal affects more code | Medium      | Medium | Grep for `.data.remove(` in all tests before starting; the one known case is already identified |
| mypy strict reveals many cfinterface boundary issues | High        | Medium | Apply inewave's proven patterns: `IO[Any]`, `# type: ignore[override]`, `Optional[Any]`         |
| Downstream breakage (sintetizador-decomp)            | Low         | High   | Preserve all public property signatures and DataFrame column names; version bump with changelog |
| Test mock data incompatible after changes            | Low         | Low    | Existing tests are the primary regression gate; mock data format is not changing                |

## Success Metrics

1. Zero `STORAGE = "BINARY"` string literals remaining
2. cfinterface dependency bumped to >= 1.9.0
3. All 310+ tests pass (0 failures, 0 skips)
4. mypy strict mode passes on all production modules
5. Zero bare `# type: ignore` comments (all have specific error codes)
6. Lazy imports for `idecomp/decomp/__init__.py`
7. Documented migration guide for downstream users
8. No performance regression
