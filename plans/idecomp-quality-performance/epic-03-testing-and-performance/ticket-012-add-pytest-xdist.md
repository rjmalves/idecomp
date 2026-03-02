# ticket-012 Add pytest-xdist and optimize test execution

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Add `pytest-xdist` to dev dependencies and verify that `pytest -n auto` runs all tests in parallel without failures. From inewave learnings, parallel execution is opt-in (NOT set as default in pytest config) and `-n auto` should NOT be in `[tool.pytest.ini_options]`. Also configure `testpaths` and `filterwarnings` in pytest config if not already present.

## Anticipated Scope

- **Files likely to be modified**: `pyproject.toml` (add pytest-xdist to dev deps, add pytest config section)
- **Key decisions needed**: Should DeprecationWarnings from inewave-style deprecated classes be filtered in conftest.py or pyproject.toml?
- **Open questions**:
  - Are there any tests with shared mutable state that would fail under parallel execution?
  - What is the current sequential test execution time baseline?
  - Should a `conftest.py` be created at the test root for session-scoped fixtures?

## Dependencies

- **Blocked By**: ticket-003-fix-identity-test-verify-suite.md (all tests must be passing)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
