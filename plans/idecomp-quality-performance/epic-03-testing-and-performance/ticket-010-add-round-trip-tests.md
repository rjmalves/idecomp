# ticket-010 Add round-trip tests for decomp handlers

## Context

### Background

Epic 03 aims to improve test coverage and performance baselines for idecomp. The original outline for this ticket listed Hidr, Postos, Vazoes, Dadger, and Dadgnl as target handlers for round-trip tests. However, codebase inspection reveals that ALL five of those handlers already have `test_leitura_escrita_*` round-trip tests in their respective test files (added prior to this plan). The actual gap is in the two remaining writable handlers that lack round-trip tests: `Caso` (SectionFile, text) and `Arquivos` (SectionFile, text).

Additionally, the existing round-trip test for `Cortdeco` also exists. BlockFile handlers (Relato, Custos, Relgnl, Decomptim, Fcfnw, InviabUnic, DecEstatFpha) and the Mapcut SectionFile handler all raise `NotImplementedError` in their block/section `write()` methods and are therefore read-only -- they cannot have round-trip tests.

### Relation to Epic

This ticket covers the "round-trip tests for handlers that support write()" goal of epic-03. It closes the remaining write-test gap for all writable handlers in idecomp.

### Current State

Handlers with existing round-trip tests (`test_leitura_escrita_*`):

- `tests/decomp/test_hidr.py` -- `test_leitura_escrita_hidr`
- `tests/decomp/test_postos.py` -- `test_leitura_escrita_postos`, `test_leitura_escrita_editando_postos`
- `tests/decomp/test_vazoes.py` -- `test_leitura_escrita_vazoes`
- `tests/decomp/test_dadger.py` -- `test_leitura_escrita_dadger`
- `tests/decomp/test_dadgnl.py` -- `test_leitura_escrita_dadgnl`
- `tests/decomp/test_cortdeco.py` -- `test_leitura_escrita_cortdeco`

Handlers with write support but NO round-trip tests:

- `Caso` (SectionFile, text) -- `NomeCaso.write()` is implemented
- `Arquivos` (SectionFile, text) -- `BlocoNomesArquivos.write()` is implemented

## Specification

### Requirements

1. Add a `test_leitura_escrita_caso` function to `tests/decomp/test_caso.py` that reads a Caso file, writes it to a mock, re-reads from the written output, and asserts equality.
2. Add a `test_leitura_escrita_arquivos` function to `tests/decomp/test_arquivos.py` that reads an Arquivos file, writes it to a mock, re-reads from the written output, and asserts equality.

### Inputs/Props

- Mock data files: `tests/mocks/arquivos/caso.dat` (existing), and the mock data used by `test_arquivos.py` (existing mock strings in `tests/mocks/arquivos/arquivos.py`).
- The `tests/mocks/mock_open.py` utility for capturing written bytes/strings.

### Outputs/Behavior

- Each test reads a handler instance, writes to a `mock_open`, captures the written lines, creates a new `mock_open` with those lines as input, re-reads, and asserts the two instances are equal via `==`.
- Tests pass with `pytest tests/decomp/test_caso.py::test_leitura_escrita_caso` and `pytest tests/decomp/test_arquivos.py::test_leitura_escrita_arquivos`.

### Error Handling

No error handling changes. These are test-only additions.

### Out of Scope

- Adding round-trip tests for BlockFile handlers (Relato, Custos, Relgnl, etc.) -- their blocks raise `NotImplementedError` on write.
- Adding round-trip tests for Mapcut -- `SecaoDadosMapcut.write()` raises `NotImplementedError`.
- Modifying any handler source code.
- Adding round-trip tests for CSV (ArquivoCSV) handlers -- these are read-only output files.

## Acceptance Criteria

- [ ] Given `tests/decomp/test_caso.py` exists, when `pytest tests/decomp/test_caso.py::test_leitura_escrita_caso -v` is run, then the test passes and the re-read Caso instance equals the original.
- [ ] Given `tests/decomp/test_arquivos.py` exists, when `pytest tests/decomp/test_arquivos.py::test_leitura_escrita_arquivos -v` is run, then the test passes and the re-read Arquivos instance equals the original.
- [ ] Given the full test suite, when `pytest -x -q` is run, then all 312+ tests pass (310 existing + 2 new).

## Implementation Guide

### Suggested Approach

Follow the exact same pattern used in `test_leitura_escrita_dadgnl` (line 172 of `tests/decomp/test_dadgnl.py`) for text-based RegisterFile/SectionFile handlers:

1. Read the handler from mock data using `mock_open` and `patch("builtins.open", ...)`.
2. Write via `handler.write(path)` with a fresh `mock_open(read_data="")`.
3. Capture written lines from `m_escrita.mock_calls` -- extract `chamadas[i].args[0]` for `i in range(2, len(chamadas) - 1)` for text files (offset 2, not 1, because SectionFile/RegisterFile open calls differ from binary).
4. Create a re-read mock with `mock_open(read_data="".join(linhas_escritas))`.
5. Assert `d1 == d2`.

For `Caso`: the handler reads from a real file (`./tests/mocks/arquivos/caso.dat`), so use `Caso.read(ARQ_TEST)` directly (same pattern as `test_hidr.py`).

For `Arquivos`: the handler reads from mock string data (`MockArquivos` in `tests/mocks/arquivos/arquivos.py`), so use the mock_open + patch pattern (same as `test_dadgnl.py`).

### Key Files to Modify

- `tests/decomp/test_caso.py` -- add `test_leitura_escrita_caso` function
- `tests/decomp/test_arquivos.py` -- add `test_leitura_escrita_arquivos` function

### Patterns to Follow

- Use the `mock_open` from `tests/mocks/mock_open.py` (not stdlib `unittest.mock.mock_open`)
- Use `MagicMock` type annotation for mock variables: `m_escrita: MagicMock = mock_open(read_data="")`
- Match the `chamadas` extraction pattern from existing tests
- Use `assert h1 == h2` for equality (cfinterface implements `__eq__` on file objects)

### Pitfalls to Avoid

- The mock_calls offset differs between text and binary handlers. For text-mode SectionFile handlers that do NOT call `open()` with a mode argument, the offset in `chamadas` starts at index 2 (like dadgnl.py), not 1 (like hidr.py binary).
- Do NOT attempt round-trip tests on BlockFile or Mapcut handlers -- their write methods raise `NotImplementedError`.

## Testing Requirements

### Unit Tests

This ticket IS the test addition. The two new test functions are the deliverable.

### Integration Tests

Not applicable -- these are unit-level round-trip tests using mock I/O.

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-003-fix-identity-test-verify-suite.md (all tests must be passing -- already completed)
- **Blocks**: None

## Effort Estimate

**Points**: 1
**Confidence**: High
