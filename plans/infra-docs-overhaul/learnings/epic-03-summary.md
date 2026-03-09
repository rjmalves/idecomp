# Accumulated Learnings: Epics 01-03

**Plan**: infra-docs-overhaul
**Last updated**: 2026-03-09
**Covers**: epic-01-packaging-ci-modernization, epic-02-sphinx-modernization, epic-03-documentation-content

---

## Dependency & Packaging Conventions

- `pyproject.toml` uses 4 extras: `test`, `lint`, `docs`, `dev`; `docs` includes `furo` (not `sphinx-rtd-theme`). File: `/home/rogerio/git/idecomp/pyproject.toml` lines 32-43.
- `cfinterface` pin `>=1.8,<=1.8.3` is immutable — do not widen or remove. File: `/home/rogerio/git/idecomp/pyproject.toml` line 9.
- CI installs only the minimal required extra per job via `uv sync --extra <group>`. Never use `--all-extras` in CI.
- All tool invocations in CI use `uv run <tool>` — never bare `ruff`, `pytest`, or `sphinx-build`.

## CI Workflow Patterns

- `main.yml` runs 4 independent parallel jobs: `lint`, `typecheck`, `test`, `docs`. No `needs:` dependencies. File: `/home/rogerio/git/idecomp/.github/workflows/main.yml`.
- `docs.yml` uses the official 2-job Pages pattern: `build` (sphinx-build + `upload-pages-artifact@v3`) then `deploy` (`deploy-pages@v4`). Concurrency group `"pages"` with `cancel-in-progress: false` is mandatory. File: `/home/rogerio/git/idecomp/.github/workflows/docs.yml`.
- `release.yml` triggers on `push: tags: ["v*"]`. Version extracted via `grep -oP` from `idecomp/__init__.py` — never via Python import or `exec()`. File: `/home/rogerio/git/idecomp/.github/workflows/release.yml`.
- `main.yml` workflow `name:` is `tests` — badge URLs reference this filename. Do not rename.

## Pre-commit Hook Conventions

- mypy hook uses `stages: [manual]` to prevent cfinterface import errors from blocking commits. Run with `pre-commit run --hook-stage manual --all-files`. File: `/home/rogerio/git/idecomp/.pre-commit-config.yaml`.
- ruff hook uses `args: [--fix]` for auto-correction. Without this flag it only reports and requires manual re-run.

## mypy Configuration

- `strict = true` replaces all explicit strict flags — do not repeat `disallow_untyped_defs` etc. alongside it.
- `warn_return_any = false` must appear in `[tool.mypy]` to override what `strict = true` enables. File: `/home/rogerio/git/idecomp/pyproject.toml`.

## Sphinx / Furo Theme Conventions

- `html_theme = "furo"` is the only required theme setting; Furo must NOT appear in `extensions`. File: `/home/rogerio/git/idecomp/docs/source/conf.py` line 43.
- Dual pygments settings required: `pygments_style = "friendly"` (light) and `pygments_dark_style = "monokai"` (dark). File: `/home/rogerio/git/idecomp/docs/source/conf.py` lines 39-40.
- Brand colors: `#2962ff` (light) / `#5c8aff` (dark), matching inewave sibling project verbatim.
- `"sidebar_hide_name": True` prevents duplicate project name display when `html_logo` is set.
- `sphinx.ext.githubpages` must remain in `extensions` regardless of theme — creates `.nojekyll` for GitHub Pages.
- `pio.renderers.default = "sphinx_gallery"` at the top of `conf.py` is required for plotly charts — do not remove.
- Local build: `uv sync --extra docs && uv run sphinx-build -M html docs/source docs/build`.

## Sphinx Gallery Structure

- 4 example scripts in `/home/rogerio/git/idecomp/examples/`: `plot_dadger.py`, `plot_dec_oper_sist.py`, `plot_edit_dadger.py`, `plot_relato.py`.
- Mock data at `/home/rogerio/git/idecomp/examples/decomp/`. New examples must add mock data here.
- `sphinx_gallery_conf` paths must not change. File: `/home/rogerio/git/idecomp/docs/source/conf.py` lines 72-76.
- All examples use class-based API (`ClassName.read()`). No deprecated `le_arquivo`/`escreve_arquivo` patterns exist.
- Gallery files use `:orphan:` directive — `examples/index.rst` and `sg_execution_times.rst` are sphinx-gallery-generated and must not be added to a toctree manually.

## Documentation Content Conventions

- Use explicit `.. code-block:: python` in all RST pages — Furo's monokai dark style only applies to syntax-highlighted blocks, not anonymous `::` blocks. Files: `/home/rogerio/git/idecomp/docs/source/guias/`.
- RST heading hierarchy: `=` underline for page title, `-` underline for sections, `^` underline for subsections (questions in FAQ). Reference file: `/home/rogerio/git/idecomp/docs/source/geral/tutorial.rst`.
- All prose is in Brazilian Portuguese (pt_BR). All new guide pages follow this convention.
- Guide pages live in `docs/source/guias/` — three files created: `arquitetura.rst`, `faq.rst`, `desempenho.rst`. Each is 178-374 lines; the ticket size estimates (80-200 lines) were conservative.
- Do NOT add guide pages to `index.rst` in the same ticket that creates them. The toctree update is always a separate, dependent ticket (ticket-012 pattern).
- `docs/source/index.rst` toctree order: Apresentacao → Geral → Guias → Referencia. The "Guias" section uses `:maxdepth: 2` and no `.rst` extension in entries (matching "Geral" convention, not "Referencia" convention).

## Autosummary Conventions

- `autosummary_generate = True` is already set in `conf.py` line 30. Do not change.
- Use `.. autosummary:: :nosignatures:` (no `:toctree:` option) — individual class pages already exist via the toctree; `:toctree:` would generate duplicate stub pages.
- Autosummary entries must use fully qualified module paths (e.g., `idecomp.decomp.dadger.Dadger`), not re-exported paths from `__init__.py`.
- The autosummary block goes before the existing `.. toctree::` block in each index file.
- The default autosummary templates are sufficient — do NOT create custom templates in `docs/source/_templates/autosummary/`. Files: `/home/rogerio/git/idecomp/docs/source/referencia/decomp/index.rst`, `/home/rogerio/git/idecomp/docs/source/referencia/libs/index.rst`.

## Documentation Structure: :orphan: Directive Pattern

- Pages not linked from any toctree produce Sphinx warnings about unreferenced documents. The `:orphan:` directive suppresses this warning.
- sphinx-gallery auto-generates `examples/index.rst` and `sg_execution_times.rst` with `:orphan:` already set; these files must NOT be manually managed or added to toctrees.
- New guide pages (in `guias/`) must NOT use `:orphan:` — they are properly linked via the "Guias" toctree in `index.rst`. Using `:orphan:` on linked pages is an error.
- If a page needs to exist without being in a toctree (e.g., a draft or a utility page), place `:orphan:` on line 1, before the title underline.

## API & Codebase Reference Facts

- `idecomp` exports 41 DECOMP file classes via `idecomp.decomp` (eager import of all 41 in `__init__.py`).
- `idecomp.libs` exports 2 auxiliary classes: `Restricoes` and `UsinasHidreletricas`.
- Three base class types: `RegisterFile` (line-oriented, e.g., Dadger), `BlockFile` (section-oriented, e.g., Relato), `ArquivoCSV` (CSV outputs, e.g., DecOperSist).
- Output files (Relato, DecOperSist, etc.) have no `write` method — they are read-only.
- Properties returning tabular data return `pd.DataFrame`; scalar properties return typed values; missing data returns `None`.
- intersphinx for cfinterface is configured at `conf.py` line 69: `"cfinterface": ("https://rjmalves.github.io/cfinterface/", None)`.

## Release & Version Conventions (Epic 4)

- Pushing a `v*` tag triggers `release.yml` and attempts PyPI publication. Coordinate version bumps and tag pushes explicitly.
- CONTRIBUTING.md must document: `pip install pre-commit && pre-commit install` for hooks, and `pre-commit run --hook-stage manual --all-files` for mypy. Explain the `stages: [manual]` design decision.
- Badge URL: `[![Tests](https://github.com/rjmalves/idecomp/actions/workflows/main.yml/badge.svg)](...)` — references `main.yml` by filename, not display name.
- `publish.yml` was renamed to `release.yml`. Any README or CONTRIBUTING docs referencing `publish.yml` must be updated.
