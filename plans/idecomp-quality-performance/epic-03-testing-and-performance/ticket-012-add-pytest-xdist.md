# ticket-012 Add pytest-xdist and optimize test execution

## Context

### Background

Epic 03 includes parallelizing the test suite to reduce feedback time. The idecomp test suite currently has 310 tests that run sequentially in approximately 10 seconds. While 10 seconds is already fast, adding `pytest-xdist` enables `pytest -n auto` for parallel execution and establishes the infrastructure for when the test suite grows (ticket-010 adds more tests, and future development will continue adding tests).

From inewave learnings, `pytest-xdist` must be opt-in: the `-n auto` flag should NOT be set as a default in `[tool.pytest.ini_options]` because CI and some local workflows need deterministic sequential execution. The flag is only used when explicitly passed.

### Relation to Epic

This ticket addresses the "Add pytest-xdist for parallel test execution" goal of epic-03. It also configures `testpaths` and `filterwarnings` in the pytest config section, which benefits all future test work.

### Current State

- `/home/rogerio/git/idecomp/pyproject.toml` has dev dependencies: pytest, pytest-cov, ruff, mypy, sphinx-related packages. No pytest-xdist.
- No `[tool.pytest.ini_options]` section exists in pyproject.toml.
- No `conftest.py` exists at the test root (`tests/`).
- Test suite: 310 tests, ~10s sequential baseline.
- All tests use `mock_open` from `tests/mocks/mock_open.py` which uses module-level global state (`file_spec = None`). This is a potential issue under parallel execution because `file_spec` is set once per process, but since xdist forks separate processes (not threads), this is safe.

## Specification

### Requirements

1. Add `pytest-xdist` to the `[project.optional-dependencies] dev` list in `/home/rogerio/git/idecomp/pyproject.toml`.
2. Add a `[tool.pytest.ini_options]` section in `/home/rogerio/git/idecomp/pyproject.toml` with `testpaths = ["tests"]` and `filterwarnings = ["ignore::DeprecationWarning"]`.
3. Verify that `pytest -n auto` runs all tests without failures.

### Inputs/Props

No inputs -- this is a configuration-only change.

### Outputs/Behavior

- `pytest -n auto -q` runs all tests in parallel and all pass.
- `pytest -q` (without `-n`) still runs tests sequentially and all pass.
- The `[tool.pytest.ini_options]` section does NOT include `-n auto` as a default addopts value.

### Error Handling

If any test fails under parallel execution due to shared state, that test must be investigated and fixed (likely a test isolation issue, not a xdist issue).

### Out of Scope

- Creating a `conftest.py` with session-scoped fixtures -- not needed given the test patterns (all tests use local mock_open, no shared fixtures).
- Setting `-n auto` as a default in `addopts` -- parallel execution is opt-in only.
- Changing any test file content unless a test fails under `-n auto`.

## Acceptance Criteria

- [ ] Given `/home/rogerio/git/idecomp/pyproject.toml`, when the `[project.optional-dependencies] dev` list is inspected, then `"pytest-xdist"` is present.
- [ ] Given `/home/rogerio/git/idecomp/pyproject.toml`, when the `[tool.pytest.ini_options]` section is inspected, then `testpaths = ["tests"]` and a `filterwarnings` entry are present, and NO `addopts` with `-n` is present.
- [ ] Given `pytest-xdist` is installed, when `pytest -n auto -q` is run from the project root, then all 310+ tests pass.
- [ ] Given `pytest-xdist` is installed, when `pytest -q` is run without `-n`, then all 310+ tests pass sequentially.

## Implementation Guide

### Suggested Approach

1. Edit `/home/rogerio/git/idecomp/pyproject.toml`:
   - Add `"pytest-xdist"` to the `dev` optional-dependencies list (after `"pytest-cov"`).
   - Add a new `[tool.pytest.ini_options]` section with:
     ```toml
     [tool.pytest.ini_options]
     testpaths = ["tests"]
     filterwarnings = ["ignore::DeprecationWarning"]
     ```
2. Install the updated dev dependencies: `uv pip install -e ".[dev]"` or `pip install -e ".[dev]"`.
3. Run `pytest -n auto -q` and verify all tests pass.
4. Run `pytest -q` (sequential) to confirm no regression.

### Key Files to Modify

- `pyproject.toml` -- add pytest-xdist dependency and pytest config section

### Patterns to Follow

- Keep the dev dependency list alphabetically ordered or in the existing insertion order (the current list is: pytest, pytest-cov, ruff, mypy, sphinx-rtd-theme, sphinx-gallery, sphinx, numpydoc, plotly, matplotlib). Insert `pytest-xdist` right after `pytest-cov`.
- The `[tool.pytest.ini_options]` section should be placed after `[tool.ruff]` and before `[tool.mypy]`, following the existing tool section ordering convention.

### Pitfalls to Avoid

- Do NOT add `-n auto` to `addopts` in pytest config. Parallel execution is opt-in via CLI flag only.
- Do NOT create a root `conftest.py` unless a test actually fails under parallel execution. The existing test patterns use per-test mock isolation and do not need session fixtures.
- The `filterwarnings` should ignore DeprecationWarnings from third-party libraries (pandas, numpy) that generate noise during test runs.

## Testing Requirements

### Unit Tests

No new unit tests. The verification is running the existing suite under both parallel and sequential modes.

### Integration Tests

Not applicable.

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-003-fix-identity-test-verify-suite.md (all tests must be passing -- already completed)
- **Blocks**: None

## Effort Estimate

**Points**: 1
**Confidence**: High
