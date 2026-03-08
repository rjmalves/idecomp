# ticket-002 Restructure CI Workflow into Parallel Jobs

## Context

### Background

The current `main.yml` workflow runs a single job that sequentially executes pytest, mypy, ruff, and sphinx-build for each Python version in the matrix. This wastes CI time because a linting failure only surfaces after tests complete. The inewave overhaul split this into 4 parallel jobs, and idecomp should follow the same pattern.

### Relation to Epic

Second ticket in Epic 1. Depends on ticket-001 for the dependency group split (each job installs only its required extras).

### Current State

File: `/home/rogerio/git/idecomp/.github/workflows/main.yml`

- Workflow name: `tests`
- Triggers: push/PR to `main`
- Single `test` job with matrix `python-version: ["3.10", "3.11", "3.12"]`
- Steps: checkout, install uv, install python, `uv sync --all-extras --dev`, pytest with coverage, codecov upload, mypy, ruff check, sphinx-build
- All 7 steps run sequentially in each matrix entry

## Specification

### Requirements

1. Replace the single `test` job with 4 independent jobs:
   - **lint**: Runs `ruff check ./idecomp` and `ruff format --check ./idecomp`. Single Python version (3.12). Installs `--extra lint`.
   - **typecheck**: Runs `uv run mypy ./idecomp`. Single Python version (3.12). Installs `--extra lint`.
   - **test**: Runs `uv run pytest --cov-report=xml --cov=idecomp ./tests` with codecov upload. Matrix: 3.10, 3.11, 3.12. Installs `--extra test`.
   - **docs**: Runs `uv run sphinx-build -M html docs/source docs/build`. Single Python version (3.12). Installs `--extra docs`.
2. Keep the workflow name as `tests` (badge URLs reference this name)
3. Keep triggers as push/PR to `main`
4. Each job: checkout, install uv, install python, `uv sync --extra <group>`, run tool
5. The `test` job keeps the codecov upload step with the existing token reference

### Inputs/Props

- Current file: `/home/rogerio/git/idecomp/.github/workflows/main.yml` (46 lines)

### Outputs/Behavior

- 4 jobs appear in the GitHub Actions UI, running in parallel
- Each job fails independently without blocking others
- Total CI wall-clock time is reduced to the longest single job

### Error Handling

- Each job fails independently; a lint failure does not prevent test results from appearing
- Codecov token is only referenced in the test job

## Acceptance Criteria

- [ ] Given the updated `main.yml`, when parsing the YAML, then exactly 4 top-level keys exist under `jobs`: `lint`, `typecheck`, `test`, `docs`
- [ ] Given the `lint` job definition, when inspecting its steps, then it runs `uv sync --extra lint` (not `--all-extras`) and executes both `uv run ruff check ./idecomp` and `uv run ruff format --check ./idecomp`
- [ ] Given the `typecheck` job definition, when inspecting its steps, then it runs `uv sync --extra lint` and executes `uv run mypy ./idecomp`
- [ ] Given the `test` job definition, when inspecting its matrix, then `python-version` includes `["3.10", "3.11", "3.12"]` and the job runs `uv sync --extra test` and includes the codecov upload step
- [ ] Given the `docs` job definition, when inspecting its steps, then it runs `uv sync --extra docs` and executes `uv run sphinx-build -M html docs/source docs/build`

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/.github/workflows/main.yml`
2. Remove the existing `test` job entirely
3. Add 4 new jobs: `lint`, `typecheck`, `test`, `docs`
4. For each job, use the common preamble: `actions/checkout@v4`, `astral-sh/setup-uv@v3`, `uv python install <version>`, `uv sync --extra <group>`
5. The `test` job gets the matrix strategy and codecov step from the old job
6. The `lint` and `typecheck` jobs use Python 3.12 (no matrix)
7. The `docs` job uses Python 3.12 (no matrix)

### Key Files to Modify

- `/home/rogerio/git/idecomp/.github/workflows/main.yml`

### Patterns to Follow

- Match the inewave `main.yml` 4-job structure
- Use `uv sync --extra <group>` instead of `--all-extras --dev` for each job

### Pitfalls to Avoid

- Do NOT rename the workflow from `tests` (the README badge URL references `actions/workflows/main.yml/badge.svg`)
- Do NOT remove the codecov token secret reference; it must stay in the `test` job
- Do NOT add job dependencies between the 4 jobs; they must run in parallel
- The docs job needs `--extra docs` which pulls in sphinx, furo, sphinx-gallery, etc. -- it does NOT need test or lint deps

## Testing Requirements

### Unit Tests

- Not applicable (YAML configuration)

### Integration Tests

- Validate the YAML structure is valid (no syntax errors)
- Verify each job references the correct extras group

### E2E Tests

- Push a PR and verify 4 separate jobs appear in the GitHub Actions UI

## Dependencies

- **Blocked By**: ticket-001-modernize-pyproject-toml.md
- **Blocks**: ticket-013-expand-readme.md (needs final workflow name for badge URL)

## Effort Estimate

**Points**: 3
**Confidence**: High
