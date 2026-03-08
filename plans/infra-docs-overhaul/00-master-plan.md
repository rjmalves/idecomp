# Master Plan: Infrastructure & Documentation Overhaul (idecomp)

## Executive Summary

This plan modernizes the idecomp Python package infrastructure, CI/CD pipelines, documentation theme, content, and repository polish. It replicates the successful overhaul completed for the sibling inewave package, adapted for idecomp's DECOMP-specific structure (the `idecomp/decomp/` and `idecomp/libs/` modules, DECOMP file formats, and existing `py.typed` marker).

The plan is organized into 4 epics with 16 tickets, following the same proven structure from the inewave overhaul.

## Goals & Non-Goals

### Goals

- Modernize `pyproject.toml` with proper metadata, dependency groups, and tool configuration
- Split the monolithic CI workflow into parallel, focused jobs (lint, typecheck, test matrix, docs)
- Migrate docs deployment from deprecated `peaceiris/actions-gh-pages@v3` to official GitHub Pages actions
- Create a tag-triggered release workflow with version validation (regex, not exec)
- Add pre-commit hooks for ruff and mypy
- Migrate Sphinx theme from sphinx-rtd-theme to Furo with dark mode
- Expand documentation with architecture, FAQ, and performance pages (all in Brazilian Portuguese)
- Improve API reference with autosummary
- Polish repository with expanded README, CONTRIBUTING.md, reformatted CHANGELOG

### Non-Goals

- Changing the idecomp public API or data models
- Adding new DECOMP file support
- Migrating away from cfinterface
- Changing the test suite logic (only CI pipeline changes)
- Translating any content to English

## Architecture Overview

### Current State

- **Build**: Hatchling, version in `idecomp/__init__.py`, `py.typed` present
- **pyproject.toml**: Flat dev deps, minimal ruff config, no mypy config, sparse classifiers, description is just "idecomp"
- **CI**: Single `main.yml` job running lint/typecheck/test/docs sequentially per matrix entry; separate `docs.yml` using deprecated peaceiris action; `publish.yml` triggered on GitHub release events
- **Docs**: sphinx-rtd-theme, pt_BR, extensions include autosummary/autodoc/intersphinx/viewcode/sphinx-gallery/numpydoc; sections for apresentacao, geral (instalacao/tutorial/contribuicao), referencia (decomp + libs)
- **Repo**: Minimal README (36 lines), no CONTRIBUTING.md, no .pre-commit-config.yaml, no mypy config, CHANGELOG in ad-hoc format

### Target State

- **pyproject.toml**: Full Portuguese description, Python 3.10/3.11/3.12 classifiers, `Typing :: Typed`, split dep groups (test/lint/docs/dev), mypy and ruff config sections
- **CI**: 4 parallel jobs in main.yml (lint, typecheck, test matrix, docs); docs.yml using official `upload-pages-artifact@v3` + `deploy-pages@v4`; release.yml with tag trigger and version validation
- **Docs**: Furo theme with dark mode (monokai), updated sphinx-gallery examples, new pages (arquitetura, faq, desempenho), improved autosummary, updated index.rst toctree
- **Repo**: Expanded README with badges, CONTRIBUTING.md, Keep a Changelog format, updated installation docs, .pre-commit-config.yaml

### Key Design Decisions

1. **Regex for version extraction** in release workflow (never `exec()` with relative imports)
2. **mypy hook at `stages: [manual]`** due to cfinterface compatibility issues
3. **All documentation in Brazilian Portuguese** (pt_BR)
4. **`uv run` prefix** for all tool invocations in CI and docs
5. **Furo theme** replaces sphinx-rtd-theme (dark mode with monokai pygments)
6. **Keep a Changelog** format for CHANGELOG.md with Portuguese category names

## Technical Approach

### Tech Stack

- Python 3.10+ with Hatchling build system
- GitHub Actions for CI/CD
- Sphinx with Furo theme for documentation
- ruff for linting/formatting, mypy for type checking
- pre-commit for local hooks

### Component/Module Breakdown

| Component               | Current                       | Target                                        |
| ----------------------- | ----------------------------- | --------------------------------------------- |
| pyproject.toml          | Flat deps, sparse metadata    | Split groups, full metadata, tool configs     |
| main.yml                | 1 sequential job              | 4 parallel jobs                               |
| docs.yml                | peaceiris/actions-gh-pages@v3 | upload-pages-artifact@v3 + deploy-pages@v4    |
| publish.yml             | Release trigger               | Tag trigger + version validation + GH release |
| .pre-commit-config.yaml | N/A                           | ruff + mypy hooks                             |
| docs/source/conf.py     | sphinx-rtd-theme              | Furo                                          |
| docs content            | 3 pages                       | 3 + 3 new guide pages                         |
| README.md               | 36 lines                      | Full with badges                              |
| CONTRIBUTING.md         | N/A                           | Full contributor guide                        |
| CHANGELOG.md            | Ad-hoc format                 | Keep a Changelog                              |

### Data Flow

No runtime data flow changes. This plan affects only build/CI/docs/repo infrastructure.

### Testing Strategy

- Verify CI workflows with dry-run analysis (YAML structure validation)
- Verify Sphinx builds successfully with Furo theme
- Verify pre-commit hooks run correctly
- No changes to the existing test suite

## Phases & Milestones

| Epic | Name                            | Tickets | Estimated Duration | Milestone                                               |
| ---- | ------------------------------- | ------- | ------------------ | ------------------------------------------------------- |
| 1    | Packaging & CI Modernization    | 5       | 1-2 weeks          | CI pipeline fully parallel, pre-commit hooks active     |
| 2    | Sphinx Modernization            | 2       | 3-5 days           | Furo theme live, gallery working                        |
| 3    | Documentation Content Expansion | 5       | 2-3 weeks          | 3 new guide pages, improved API ref, updated toctree    |
| 4    | Repository Polish               | 4       | 1-2 weeks          | Full README, CONTRIBUTING, CHANGELOG, installation docs |

## Risk Analysis

| Risk                                            | Likelihood | Impact | Mitigation                                                                     |
| ----------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------------ |
| cfinterface import errors in sphinx-gallery     | Medium     | Medium | Known from inewave; test gallery build early in Epic 2                         |
| mypy strict + cfinterface conflicts             | Medium     | Low    | Known fix: manual stage for pre-commit hook, `warn_return_any: false` override |
| ruff auto-format changes many files             | High       | Low    | Run ruff format once, commit separately before other changes                   |
| GitHub Pages action migration breaks deployment | Low        | High   | Test in PR before merging; keep old workflow as fallback                       |

## Success Metrics

- All 4 CI jobs pass independently on PR
- Sphinx builds with Furo theme without warnings
- Pre-commit hooks catch formatting/linting issues locally
- Documentation site has architecture, FAQ, and performance pages
- README displays all badges correctly
- Release workflow creates GitHub release and publishes to PyPI on tag push
