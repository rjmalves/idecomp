# ticket-001 Modernize pyproject.toml Metadata and Dependency Groups

## Context

### Background

The idecomp `pyproject.toml` has sparse metadata (description is just "idecomp", only Python 3.10 classifier), flat dev dependencies in a single group, and no tool configuration for mypy. This ticket brings it to parity with the inewave sibling project's modernized `pyproject.toml`.

### Relation to Epic

This is the foundational ticket of Epic 1. All other CI and tooling tickets depend on the dependency groups and tool configuration defined here.

### Current State

File: `/home/rogerio/git/idecomp/pyproject.toml`

- `description = "idecomp"` (should be descriptive, in Portuguese)
- Classifiers: only `Python :: 3.10`, missing 3.11/3.12 and `Typing :: Typed`
- Single `[project.optional-dependencies] dev` group with all deps mixed together: pytest, pytest-cov, ruff, mypy, sphinx-rtd-theme, sphinx-gallery, sphinx, numpydoc, plotly, matplotlib
- `[tool.ruff]` has only `line-length = 80`
- No `[tool.mypy]` section
- No `[tool.ruff.lint]` section
- `py.typed` marker already exists at `/home/rogerio/git/idecomp/idecomp/py.typed`
- Wheel include already covers `idecomp/` (which includes `py.typed`)

## Specification

### Requirements

1. Update `description` to `"Pacote para manipulacao dos arquivos do DECOMP"` (matching the README's Portuguese description)
2. Add classifiers: `Programming Language :: Python :: 3.11`, `Programming Language :: Python :: 3.12`, `Typing :: Typed`
3. Split `[project.optional-dependencies]` into 4 groups:
   - `test = ["pytest", "pytest-cov"]`
   - `lint = ["ruff", "mypy"]`
   - `docs = ["sphinx", "furo", "sphinx-gallery", "numpydoc", "plotly", "matplotlib"]`
   - `dev = ["idecomp[test,lint,docs]"]` (self-referencing alias)
4. Note: `furo` replaces `sphinx-rtd-theme` in the docs group (theme migration happens in ticket-006, but the dependency is set here)
5. Add `[tool.mypy]` section with strict settings and cfinterface override:

   ```toml
   [tool.mypy]
   python_version = "3.10"
   warn_return_any = false
   warn_unused_configs = true
   disallow_untyped_defs = true
   disallow_incomplete_defs = true
   check_untyped_defs = true
   no_implicit_optional = true
   warn_redundant_casts = true
   warn_unused_ignores = true
   strict = true

   [[tool.mypy.overrides]]
   module = "cfinterface.*"
   ignore_missing_imports = true
   warn_return_any = false
   ```

6. Expand `[tool.ruff.lint]` with select rules:
   ```toml
   [tool.ruff.lint]
   select = ["E", "F", "I", "UP"]
   ```
7. Verify `py.typed` is present and included in wheel build (no changes needed, just verify)

### Inputs/Props

- Current file: `/home/rogerio/git/idecomp/pyproject.toml` (57 lines)

### Outputs/Behavior

- Updated `pyproject.toml` with all changes above
- `uv sync --extra test` installs only pytest + pytest-cov
- `uv sync --extra lint` installs only ruff + mypy
- `uv sync --extra docs` installs only sphinx + furo + sphinx-gallery + numpydoc + plotly + matplotlib
- `uv sync --extra dev` installs all of the above

### Error Handling

- If the self-referencing `dev` extra causes resolution issues, fall back to listing all deps explicitly in the dev group
- The cfinterface pin `>=1.8,<=1.8.3` must remain unchanged

## Acceptance Criteria

- [ ] Given the updated `pyproject.toml`, when running `uv sync --extra test`, then only `pytest` and `pytest-cov` are installed as extras (verify with `uv pip list | grep -i pytest`)
- [ ] Given the updated `pyproject.toml`, when inspecting the `[project]` section, then `description` equals `"Pacote para manipulacao dos arquivos do DECOMP"` and classifiers include `Programming Language :: Python :: 3.11`, `Programming Language :: Python :: 3.12`, and `Typing :: Typed`
- [ ] Given the updated `pyproject.toml`, when inspecting `[tool.mypy]`, then `strict = true` is set and `[[tool.mypy.overrides]]` for `cfinterface.*` has `ignore_missing_imports = true` and `warn_return_any = false`
- [ ] Given the updated `pyproject.toml`, when inspecting `[tool.ruff.lint]`, then `select = ["E", "F", "I", "UP"]` is present
- [ ] Given the file `/home/rogerio/git/idecomp/idecomp/py.typed`, when inspecting the wheel build config `[tool.hatch.build.targets.wheel]`, then the include pattern `"idecomp/"` covers the `py.typed` marker file

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/pyproject.toml`
2. Update the `description` field in `[project]`
3. Add missing classifiers to the `classifiers` list
4. Replace the single `dev` group in `[project.optional-dependencies]` with 4 groups: `test`, `lint`, `docs`, `dev`
5. Add `[tool.mypy]` section after the existing `[tool.ruff]` section
6. Add `[tool.ruff.lint]` section after `[tool.ruff]`
7. Verify `idecomp/py.typed` exists and the wheel include covers it (read-only check)

### Key Files to Modify

- `/home/rogerio/git/idecomp/pyproject.toml` (the only file modified)

### Patterns to Follow

- Match the inewave pyproject.toml structure for consistency across sibling projects
- Use self-referencing extras syntax: `"idecomp[test,lint,docs]"`

### Pitfalls to Avoid

- Do NOT remove the `cfinterface>=1.8,<=1.8.3` pin from `[project] dependencies`
- Do NOT add `sphinx-rtd-theme` to the docs group (it is being replaced by `furo`)
- Do NOT use `exec()` anywhere for version extraction (the Hatchling `path` config handles this)
- The `warn_return_any = false` must appear both at the top-level `[tool.mypy]` AND in the `[[tool.mypy.overrides]]` for cfinterface because `strict = true` re-enables it

## Testing Requirements

### Unit Tests

- No code changes; no unit tests needed

### Integration Tests

- Run `uv sync --extra test` and verify pytest is available
- Run `uv sync --extra lint` and verify ruff and mypy are available
- Run `uv sync --extra docs` and verify sphinx and furo are available
- Run `uv sync --extra dev` and verify all tools are available

### E2E Tests

- Not applicable

## Dependencies

- **Blocked By**: None (first ticket in the plan)
- **Blocks**: ticket-002-restructure-ci-workflow.md, ticket-004-create-release-workflow.md, ticket-005-add-pre-commit-hooks.md, ticket-006-migrate-sphinx-theme-to-furo.md

## Effort Estimate

**Points**: 3
**Confidence**: High
