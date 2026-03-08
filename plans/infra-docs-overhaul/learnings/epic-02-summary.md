# Accumulated Learnings: Epics 01-02

**Plan**: infra-docs-overhaul
**Last updated**: 2026-03-08
**Covers**: epic-01-packaging-ci-modernization, epic-02-sphinx-modernization

---

## Dependency & Packaging Conventions

- `pyproject.toml` uses 4 extras: `test`, `lint`, `docs`, `dev`; `docs` includes `furo` (not `sphinx-rtd-theme`). File: `/home/rogerio/git/idecomp/pyproject.toml` lines 32-43.
- `cfinterface` pin `>=1.8,<=1.8.3` is immutable — do not widen or remove. File: `/home/rogerio/git/idecomp/pyproject.toml` line 9.
- CI installs only the minimal required extra per job via `uv sync --extra <group>`. Never use `--all-extras` in CI.
- All tool invocations in CI use `uv run <tool>` — never bare `ruff`, `pytest`, or `sphinx-build`.

## CI Workflow Patterns

- `main.yml` runs 4 independent parallel jobs: `lint`, `typecheck`, `test`, `docs`. No `needs:` dependencies between them. File: `/home/rogerio/git/idecomp/.github/workflows/main.yml`.
- `docs.yml` uses the official 2-job Pages pattern: `build` job (sphinx-build + `upload-pages-artifact@v3`) then `deploy` job (`deploy-pages@v4`). Concurrency group `"pages"` with `cancel-in-progress: false` is mandatory. File: `/home/rogerio/git/idecomp/.github/workflows/docs.yml`.
- `release.yml` triggers on `push: tags: ["v*"]`. Version extracted via `grep -oP` from `idecomp/__init__.py` — never via Python import or `exec()`. File: `/home/rogerio/git/idecomp/.github/workflows/release.yml`.
- `main.yml` workflow `name:` is `tests` — badge URLs reference this. Do not rename.
- `publish.yml` was renamed to `release.yml` via `git mv`. Any docs referencing `publish.yml` must be updated.

## Pre-commit Hook Conventions

- mypy hook uses `stages: [manual]` to prevent cfinterface import errors from blocking commits. Run with `pre-commit run --hook-stage manual --all-files`. File: `/home/rogerio/git/idecomp/.pre-commit-config.yaml`.
- ruff hook uses `args: [--fix]` for auto-correction. Without this flag it only reports and requires manual re-run.

## mypy Configuration

- `strict = true` replaces all explicit strict flags — do not repeat `disallow_untyped_defs` etc. alongside it.
- `warn_return_any = false` must appear in `[tool.mypy]` to override what `strict = true` enables. File: `/home/rogerio/git/idecomp/pyproject.toml`.

## Sphinx / Furo Theme Conventions

- `html_theme = "furo"` is the only required theme setting; Furo must NOT appear in `extensions`. Adding it to extensions causes a warning. File: `/home/rogerio/git/idecomp/docs/source/conf.py` line 43.
- Dual pygments settings are required for Furo: `pygments_style = "friendly"` (light) and `pygments_dark_style = "monokai"` (dark). A single setting leaves dark mode unstyled. File: `/home/rogerio/git/idecomp/docs/source/conf.py` lines 39-40.
- `html_theme_options` must be a complete replacement when switching themes — no RTD keys are reusable with Furo.
- Brand colors match inewave sibling project verbatim: `#2962ff` (light) / `#5c8aff` (dark). Do not change without consulting inewave `conf.py`.
- `"sidebar_hide_name": True` prevents duplicate project name display when `html_logo` is set.
- `sphinx.ext.githubpages` must remain in `extensions` regardless of theme — it creates the `.nojekyll` file required by GitHub Pages.
- `pio.renderers.default = "sphinx_gallery"` at the top of `conf.py` is required for plotly charts in the gallery — do not remove.

## Documentation Build Command

- Local build: `uv sync --extra docs && uv run sphinx-build -M html docs/source docs/build`
- Built output: `docs/build/html/index.html`
- Gallery examples are cached after first build in `docs/source/examples/` — subsequent builds are faster.

## Sphinx Gallery Structure

- 4 example scripts in `/home/rogerio/git/idecomp/examples/`: `plot_dadger.py`, `plot_dec_oper_sist.py`, `plot_edit_dadger.py`, `plot_relato.py`.
- Mock data lives at `/home/rogerio/git/idecomp/examples/decomp/` (`dadger.rv0`, `dec_oper_sist.csv`, `relato.rv0`). New examples must add their mock data here.
- `sphinx_gallery_conf` paths (`examples_dirs`, `gallery_dirs`, `backreferences_dir`) must not be changed. File: `/home/rogerio/git/idecomp/docs/source/conf.py` lines 72-76.
- `abort_on_example_error = False` was anticipated as a cfinterface fallback but was NOT needed — all 4 examples run cleanly with the existing mock data.
- All examples use the current class-based API (`ClassName.read()`). No deprecated `le_arquivo`/`escreve_arquivo` patterns exist.

## Documentation Content Conventions (for Epic 3)

- Use explicit `.. code-block:: python` in RST pages — Furo's monokai dark style only applies to syntax-highlighted blocks, not anonymous `::` blocks.
- `autosummary_generate = True` auto-generates stub pages. Templates at `docs/source/_templates/autosummary/`. File: `/home/rogerio/git/idecomp/docs/source/conf.py` line 30.
- `numpydoc_show_class_members = False` suppresses member tables in class pages — adjust if ticket-011 should show members inline.
- intersphinx includes cfinterface at `https://rjmalves.github.io/cfinterface/` — cross-references to cfinterface types will resolve without explicit declarations.

## Release & Version Conventions (for Epic 4)

- Pushing a `v*` tag triggers `release.yml` and attempts PyPI publication. Coordinate version bumps and tag pushes explicitly.
- CONTRIBUTING.md must document: `pip install pre-commit && pre-commit install` for hooks, and `pre-commit run --hook-stage manual --all-files` for mypy. Explain the `stages: [manual]` design decision.
- Badge URL: `[![Tests](https://github.com/rjmalves/idecomp/actions/workflows/main.yml/badge.svg)](...)` — references `main.yml` by filename, not display name.
