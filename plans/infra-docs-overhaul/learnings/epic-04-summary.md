# Accumulated Learnings: Epics 01-04 (Full Plan)

**Plan**: infra-docs-overhaul
**Last updated**: 2026-03-09
**Covers**: epic-01 through epic-04 — complete plan retrospective

---

## Dependency & Packaging Conventions

- `pyproject.toml` uses 4 extras: `test`, `lint`, `docs`, `dev`; `dev` self-references the other three. File: `/home/rogerio/git/idecomp/pyproject.toml` lines 32-43.
- `cfinterface` pin `>=1.8,<=1.8.3` is immutable — do not widen or remove. File: `/home/rogerio/git/idecomp/pyproject.toml` line 9.
- CI installs only the minimal required extra per job via `uv sync --extra <group>`. Never use `--all-extras` in CI.
- All tool invocations in CI and contributor docs use `uv run <tool>` — never bare `ruff`, `pytest`, or `sphinx-build`.
- Python minimum requirement is `>= 3.10` — stated in `pyproject.toml`, `README.md`, and `instalacao.rst`. All three must be kept in sync.

## CI Workflow Patterns

- `main.yml` runs 4 independent parallel jobs: `lint`, `typecheck`, `test`, `docs`. No `needs:` dependencies. File: `/home/rogerio/git/idecomp/.github/workflows/main.yml`.
- `docs.yml` uses the official 2-job Pages pattern: `build` then `deploy`. Concurrency group `"pages"` with `cancel-in-progress: false` is mandatory. File: `/home/rogerio/git/idecomp/.github/workflows/docs.yml`.
- `release.yml` triggers on `push: tags: ["v*"]`. Version extracted via `grep -oP` — never via Python import or `exec()`. File: `/home/rogerio/git/idecomp/.github/workflows/release.yml`.
- `main.yml` workflow `name:` is `tests` — badge URLs reference this filename. Do not rename.
- `publish.yml` was renamed to `release.yml`. Any reference to `publish.yml` must be updated everywhere.

## Pre-commit Hook Conventions

- mypy hook uses `stages: [manual]` to prevent cfinterface import errors from blocking commits. Run with `pre-commit run --hook-stage manual --all-files`. File: `/home/rogerio/git/idecomp/.pre-commit-config.yaml`.
- ruff hook uses `args: [--fix]` for auto-correction; without it, ruff only reports and requires manual re-run.
- `pip install pre-commit && pre-commit install` uses bare `pip`, not `uv run pre-commit` — pre-commit is a system-level git hook installer.

## mypy Configuration

- `strict = true` replaces all explicit strict flags — do not repeat individual flags alongside it.
- `warn_return_any = false` must appear in `[tool.mypy]` to override what `strict = true` enables. File: `/home/rogerio/git/idecomp/pyproject.toml`.

## Sphinx / Furo Theme Conventions

- `html_theme = "furo"` is the only required theme setting; Furo must NOT appear in `extensions`. File: `/home/rogerio/git/idecomp/docs/source/conf.py`.
- Dual pygments settings required: `pygments_style = "friendly"` (light) and `pygments_dark_style = "monokai"` (dark).
- Brand colors: `#2962ff` (light) / `#5c8aff` (dark), matching inewave sibling project.
- `sphinx.ext.githubpages` must remain in `extensions` — creates `.nojekyll` for GitHub Pages.
- `pio.renderers.default = "sphinx_gallery"` at the top of `conf.py` is required for plotly charts.
- Local build: `uv sync --extra docs && uv run sphinx-build -M html docs/source docs/build`.

## RST Documentation Conventions

- Use explicit `.. code-block:: python` or `.. code-block:: bash` in all RST pages — Furo monokai dark style only applies to syntax-highlighted blocks, not anonymous `::` blocks.
- RST heading hierarchy: `=` underline for page title, `-` for sections, `^` for subsections. Reference: `/home/rogerio/git/idecomp/docs/source/geral/tutorial.rst`.
- All prose is in Brazilian Portuguese (pt_BR). Markdown headings omit diacritics (convention from pre-existing files); RST body prose retains full accented Portuguese.
- Do NOT add new guide pages (`guias/`) to `index.rst` in the same ticket that creates them — toctree updates are always a separate dependent ticket.
- Pages not linked from any toctree should use `:orphan:` on line 1. Pages properly linked via a toctree must NOT have `:orphan:`.

## Autosummary Conventions

- Use `.. autosummary:: :nosignatures:` (no `:toctree:` option) — individual class pages already exist; `:toctree:` generates duplicate stubs.
- Autosummary entries use fully qualified module paths (e.g., `idecomp.decomp.dadger.Dadger`), not re-exported paths from `__init__.py`.
- The autosummary block goes before the existing `.. toctree::` block in each reference index file. Files: `/home/rogerio/git/idecomp/docs/source/referencia/decomp/index.rst`, `/home/rogerio/git/idecomp/docs/source/referencia/libs/index.rst`.

## Sphinx Gallery Structure

- 4 example scripts in `/home/rogerio/git/idecomp/examples/`: `plot_dadger.py`, `plot_dec_oper_sist.py`, `plot_edit_dadger.py`, `plot_relato.py`.
- Mock data at `/home/rogerio/git/idecomp/examples/decomp/`. New examples must add mock data here.
- sphinx-gallery auto-generates `examples/index.rst` and `sg_execution_times.rst` — do NOT add these to a toctree manually.
- All examples use class-based API (`ClassName.read()`). No deprecated `le_arquivo`/`escreve_arquivo` patterns exist.

## API Reference Facts

- `idecomp` exports 41 DECOMP file classes via `idecomp.decomp` and 2 auxiliary classes via `idecomp.libs` (`Restricoes`, `UsinasHidreletricas`).
- Three base class types: `RegisterFile` (line-oriented), `BlockFile` (section-oriented), `ArquivoCSV` (CSV outputs, read-only).
- Properties returning tabular data return `pd.DataFrame`; scalar properties return typed values; missing data returns `None`.
- intersphinx for cfinterface: `conf.py` line 69: `"cfinterface": ("https://rjmalves.github.io/cfinterface/", None)`.

## Contributor Documentation Pattern

- CONTRIBUTING.md (root, markdown) handles environment setup, pre-commit hooks, quality tools, code conventions, PR workflow.
- `contribuicao.rst` (docs site) handles cfinterface architecture, class naming guidelines, DataFrame conventions.
- `contribuicao.rst` opens with `.. note::` admonition linking to CONTRIBUTING.md for environment setup.
- Files: `/home/rogerio/git/idecomp/CONTRIBUTING.md`, `/home/rogerio/git/idecomp/docs/source/geral/contribuicao.rst`.

## CHANGELOG Conventions

- Keep a Changelog format: `## [X.Y.Z] - YYYY-MM-DD` headings, `### Adicionado/Corrigido/Modificado/Depreciado` subheadings in Portuguese.
- `## [Nao Publicado]` section sits above the first versioned entry.
- GitHub compare links appear as reference-style links at the bottom of the file.
- Version anchor text uses no `v` prefix; URL uses `v` prefix: `[1.8.2]: .../compare/v1.8.1...v1.8.2`.
- File: `/home/rogerio/git/idecomp/CHANGELOG.md`.

## Plan-wide Quality Observations

- All 16 tickets scored 1.0 quality except ticket-006 (Furo theme migration, 0.85) where lint/type scoring was neutral due to conf.py-only changes.
- Mean quality score across all 16 tickets: ~0.99. No ticket fell below the 0.75 gate.
- Pure documentation and configuration tickets (markdown, RST, YAML, TOML) consistently score 1.0 because lint, type safety, and test delta dimensions default to 1.0 for non-code files.
- The `open-source-documentation-writer` agent handled all Epic 2-4 tickets; `python-task-automation-developer` handled Epic 1.
- Documentation-only tickets benefit from explicit pitfall lists in ticket specs — every case where an agent avoided a known error (e.g., not using `publish.yml`, not using `--all-extras`, not deleting cfinterface section from RST) traced back to a "Pitfalls to Avoid" entry in the ticket.
