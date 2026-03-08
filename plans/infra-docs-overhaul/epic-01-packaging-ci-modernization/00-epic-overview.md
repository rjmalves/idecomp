# Epic 1: Packaging & CI Modernization

## Goal

Modernize the idecomp build metadata, CI/CD pipelines, and developer tooling to match the standards established in the inewave sibling project. After this epic, the CI will run 4 parallel jobs (lint, typecheck, test matrix, docs), the release workflow will be tag-triggered with version validation, and pre-commit hooks will enforce code quality locally.

## Scope

- Modernize `pyproject.toml` metadata, dependency groups, and tool configuration
- Restructure `main.yml` into 4 parallel CI jobs
- Migrate `docs.yml` to official GitHub Pages deployment actions
- Create tag-triggered `release.yml` with version validation
- Add `.pre-commit-config.yaml` with ruff and mypy hooks

## Tickets

| Order | Ticket     | Title                                                    | Points |
| ----- | ---------- | -------------------------------------------------------- | ------ |
| 1     | ticket-001 | Modernize pyproject.toml Metadata and Dependency Groups  | 3      |
| 2     | ticket-002 | Restructure CI Workflow into Parallel Jobs               | 3      |
| 3     | ticket-003 | Migrate Docs Deployment to Official GitHub Pages Actions | 2      |
| 4     | ticket-004 | Create Tag-Triggered Release Workflow                    | 3      |
| 5     | ticket-005 | Add Pre-commit Hooks Configuration                       | 2      |

## Dependencies

- ticket-002 depends on ticket-001 (needs dependency groups defined)
- ticket-003 is independent
- ticket-004 depends on ticket-001 (needs dependency groups)
- ticket-005 depends on ticket-001 (needs ruff/mypy config in pyproject.toml)

## Completion Criteria

- `uv sync --extra test` installs only test deps; `uv sync --extra lint` installs only lint deps
- `main.yml` runs 4 independent jobs that pass on PR
- `docs.yml` deploys using `actions/upload-pages-artifact@v3` and `actions/deploy-pages@v4`
- `release.yml` triggers on `v*` tags, validates version with regex, creates GitHub release
- `pre-commit run --all-files` executes ruff check + ruff format; `pre-commit run --hook-stage manual --all-files` runs mypy
