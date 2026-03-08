# ticket-005 Add Pre-commit Hooks Configuration

## Context

### Background

idecomp has no `.pre-commit-config.yaml`. Developers must manually run ruff and mypy before committing. The inewave overhaul added pre-commit hooks for ruff (check + format) and mypy (manual stage due to cfinterface issues), and idecomp should adopt the same configuration.

### Relation to Epic

Fifth and final ticket of Epic 1. Depends on ticket-001 for ruff and mypy configuration in `pyproject.toml`.

### Current State

- No `.pre-commit-config.yaml` exists in the repository
- ruff and mypy are listed as dev dependencies (will be in `lint` group after ticket-001)
- mypy has known issues with cfinterface (missing type stubs, `warn_return_any` conflicts)

## Specification

### Requirements

1. Create `.pre-commit-config.yaml` at repository root with:
   - **ruff-pre-commit** hooks (from `https://github.com/astral-sh/ruff-pre-commit`):
     - `ruff` hook (linting/check)
     - `ruff-format` hook (formatting)
   - **mypy** hook as a local hook:
     - `language: system` (uses the project's installed mypy, not a separate venv)
     - `entry: uv run mypy ./idecomp`
     - `pass_filenames: false` (runs on entire package)
     - `stages: [manual]` (not run on every commit due to cfinterface import issues; invoked explicitly with `pre-commit run --hook-stage manual`)
2. Use a recent ruff-pre-commit rev (e.g., `v0.8.6` or latest stable)

### Inputs/Props

- No existing file to modify; creating new file at `/home/rogerio/git/idecomp/.pre-commit-config.yaml`

### Outputs/Behavior

- `pre-commit run --all-files` executes ruff check and ruff format on all files
- `pre-commit run --hook-stage manual --all-files` additionally runs mypy
- ruff hooks use the pre-commit framework's own ruff installation (fast, isolated)
- mypy hook uses the system/project-installed mypy via `uv run`

### Error Handling

- If ruff finds formatting issues, the hook auto-fixes them and fails the commit (user re-stages and re-commits)
- If mypy fails due to cfinterface issues, it only affects manual runs, not regular commits

## Acceptance Criteria

- [ ] Given the repository root, when listing files, then `.pre-commit-config.yaml` exists at `/home/rogerio/git/idecomp/.pre-commit-config.yaml`
- [ ] Given the `.pre-commit-config.yaml`, when inspecting the ruff-pre-commit repo entry, then it contains hooks with ids `ruff` and `ruff-format`
- [ ] Given the `.pre-commit-config.yaml`, when inspecting the local hooks, then there is a hook with `id: mypy`, `language: system`, `entry: uv run mypy ./idecomp`, `pass_filenames: false`, and `stages: [manual]`
- [ ] Given a clean checkout with pre-commit installed, when running `pre-commit run --all-files`, then the ruff and ruff-format hooks execute (mypy does not execute because it is manual stage)

## Implementation Guide

### Suggested Approach

1. Create `/home/rogerio/git/idecomp/.pre-commit-config.yaml` with the following structure:

   ```yaml
   repos:
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: v0.8.6
       hooks:
         - id: ruff
           args: [--fix]
         - id: ruff-format

     - repo: local
       hooks:
         - id: mypy
           name: mypy
           entry: uv run mypy ./idecomp
           language: system
           types: [python]
           pass_filenames: false
           stages: [manual]
   ```

2. Verify the file is valid YAML

### Key Files to Modify

- `/home/rogerio/git/idecomp/.pre-commit-config.yaml` (new file)

### Patterns to Follow

- Match the inewave `.pre-commit-config.yaml` structure exactly
- Use `language: system` for mypy to avoid installing it in an isolated venv (it needs access to project deps)
- Use `stages: [manual]` to prevent mypy from running on every commit

### Pitfalls to Avoid

- Do NOT set mypy stages to `[pre-commit]` or omit stages -- cfinterface issues will cause every commit to fail
- Do NOT use `language: python` for mypy -- it installs mypy in an isolated venv without project deps
- Do NOT forget `pass_filenames: false` for mypy -- it should type-check the whole package, not individual files
- Do NOT forget `args: [--fix]` on the ruff hook -- without it, ruff only reports but does not fix issues

## Testing Requirements

### Unit Tests

- Not applicable (configuration file)

### Integration Tests

- Validate YAML syntax of the new file
- Run `pre-commit run --all-files` and verify ruff hooks execute

### E2E Tests

- Not applicable

## Dependencies

- **Blocked By**: ticket-001-modernize-pyproject-toml.md
- **Blocks**: ticket-014-create-contributing.md (CONTRIBUTING references pre-commit setup)

## Effort Estimate

**Points**: 2
**Confidence**: High
