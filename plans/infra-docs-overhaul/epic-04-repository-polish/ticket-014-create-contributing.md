# ticket-014 Create CONTRIBUTING.md

## Context

### Background

The repository currently has no `CONTRIBUTING.md` file. Contributor guidance exists only in `docs/source/geral/contribuicao.rst`, which is outdated: it references `pylama` (replaced by `ruff`), `black` (replaced by `ruff format`), `pip install -r dev-requirements.txt` (replaced by `uv sync --extra dev`), and `pip install git+...` for development installation. A modern `CONTRIBUTING.md` at the repository root is the standard location for contributor onboarding on GitHub.

### Relation to Epic

This is the second ticket in Epic 4 (Repository Polish). It creates the contributor workflow document that the README (ticket-013) will link to. It depends on the pre-commit configuration (ticket-005) and pyproject.toml extras (ticket-001), both already completed.

### Current State

- `/home/rogerio/git/idecomp/CONTRIBUTING.md` does not exist
- `/home/rogerio/git/idecomp/docs/source/geral/contribuicao.rst` (118 lines) contains:
  - cfinterface framework explanation (BlockFile, SectionFile, RegisterFile)
  - Outdated dev setup: `pip install -r dev-requirements.txt`
  - Code conventions: PEP8, static typing, DataFrame patterns
  - Testing: references `pylama` and `black` (deprecated tools)
- Pre-commit config at `/home/rogerio/git/idecomp/.pre-commit-config.yaml` uses `ruff` + `ruff-format` + `mypy` (manual stage)
- `pyproject.toml` defines 4 extras: `test`, `lint`, `docs`, `dev`

## Specification

### Requirements

1. Create `/home/rogerio/git/idecomp/CONTRIBUTING.md` with the following sections (all in pt_BR):
   - **Configuracao do Ambiente**: Clone, `uv sync --extra dev`, verify with `uv run pytest ./tests`
   - **Hooks de Pre-commit**: `pip install pre-commit && pre-commit install`, explain `stages: [manual]` for mypy, document `pre-commit run --hook-stage manual --all-files` for full mypy check
   - **Ferramentas de Qualidade**: ruff (linting + formatting), mypy (tipagem estatica), pytest (testes)
   - **Convencoes de Codigo**: PEP8 via ruff, tipagem estatica obrigatoria, propriedades retornam `pd.DataFrame` para dados tabulares, nomenclatura em `snake_case`
   - **Executando Testes**: `uv run pytest ./tests`, `uv run pytest --cov=idecomp ./tests` for coverage
   - **Construindo a Documentacao**: `uv sync --extra docs`, `uv run sphinx-build -M html docs/source docs/build`
   - **Fluxo de Pull Requests**: fork, branch, commit, push, open PR; CI runs lint/typecheck/test/docs automatically
2. Update `/home/rogerio/git/idecomp/docs/source/geral/contribuicao.rst` to:
   - Keep the cfinterface framework explanation (lines 1-37 of current file) intact — this is docs-appropriate architectural content
   - Keep the "Diretrizes de modelagem" section (lines 53-81) intact — class naming and DataFrame conventions are reference material
   - Replace the outdated "Convencoes de codigo" section (lines 83-101) with updated tool references: replace `black` with `ruff format`, remove `pylama` reference
   - Replace the outdated "Procedimentos de teste" section (lines 104-118) with: `uv run pytest ./tests`, `uv run mypy ./idecomp`, `uv run ruff check ./idecomp`
   - Add a note at the top of the file referencing `CONTRIBUTING.md` for environment setup instructions

### Inputs/Props

- All commands use `uv run <tool>` prefix (CI convention from learnings)
- Pre-commit hook configuration from `/home/rogerio/git/idecomp/.pre-commit-config.yaml`
- Dependency extras from `/home/rogerio/git/idecomp/pyproject.toml` lines 32-43

### Outputs/Behavior

- A new `CONTRIBUTING.md` file at the repository root (~80-120 lines)
- An updated `contribuicao.rst` with correct tool references and a pointer to `CONTRIBUTING.md`

### Error Handling

Not applicable (static documentation files).

## Acceptance Criteria

- [ ] Given the file `/home/rogerio/git/idecomp/CONTRIBUTING.md`, when inspected, then it exists and contains at least 6 markdown `##` section headings
- [ ] Given the CONTRIBUTING.md "Configuracao do Ambiente" section, when the setup commands are checked, then it shows `uv sync --extra dev` (not `pip install -r dev-requirements.txt`)
- [ ] Given the CONTRIBUTING.md "Hooks de Pre-commit" section, when inspected, then it documents `pre-commit run --hook-stage manual --all-files` for mypy and explains the `stages: [manual]` rationale (cfinterface import errors)
- [ ] Given the CONTRIBUTING.md "Ferramentas de Qualidade" section, when tool names are checked, then it references `ruff` for linting and formatting (not `pylama` or `black`)
- [ ] Given the file `/home/rogerio/git/idecomp/docs/source/geral/contribuicao.rst`, when the "Procedimentos de teste" section is checked, then it shows `uv run pytest`, `uv run mypy`, and `uv run ruff check` commands (not bare `pytest`, `mypy`, or `pylama`)

## Implementation Guide

### Suggested Approach

1. Create `/home/rogerio/git/idecomp/CONTRIBUTING.md` with the section structure from the Requirements
2. For the "Configuracao do Ambiente" section, show the complete flow: `git clone`, `cd idecomp`, `uv sync --extra dev`, `uv run pytest ./tests`
3. For the "Hooks de Pre-commit" section, explain: ruff and ruff-format run automatically on every commit; mypy uses `stages: [manual]` because cfinterface type stubs are incomplete and would block every commit; to run mypy manually use `pre-commit run --hook-stage manual --all-files` or directly `uv run mypy ./idecomp`
4. For "Ferramentas de Qualidade", list each tool with its command:
   - `uv run ruff check ./idecomp` (linting)
   - `uv run ruff format --check ./idecomp` (format check)
   - `uv run mypy ./idecomp` (type check)
   - `uv run pytest ./tests` (tests)
5. For "Construindo a Documentacao", show: `uv sync --extra docs` then `uv run sphinx-build -M html docs/source docs/build`
6. Open `/home/rogerio/git/idecomp/docs/source/geral/contribuicao.rst` and:
   - Add a `.. note::` admonition after the title directing readers to `CONTRIBUTING.md` for environment setup
   - Replace `black` references with `ruff format`
   - Replace `pylama ./idecomp --ignore E203` with `uv run ruff check ./idecomp`
   - Replace `pytest ./tests` with `uv run pytest ./tests`
   - Replace `mypy ./idecomp` with `uv run mypy ./idecomp`

### Key Files to Modify

- `/home/rogerio/git/idecomp/CONTRIBUTING.md` (new file)
- `/home/rogerio/git/idecomp/docs/source/geral/contribuicao.rst` (update outdated sections)

### Patterns to Follow

- All tool invocations use `uv run <tool>` prefix (established CI convention)
- Section headings in Portuguese without accents in markdown headings
- Use `.. code-block:: bash` in RST files (not anonymous `::` blocks) — consistent with the guide page convention from Epic 3

### Pitfalls to Avoid

- Do NOT reference `dev-requirements.txt` — it no longer exists; use `uv sync --extra dev`
- Do NOT reference `pylama` or `black` — replaced by `ruff`
- Do NOT reference `publish.yml` — renamed to `release.yml`
- Do NOT delete the cfinterface framework explanation from `contribuicao.rst` — it is valuable architectural reference content that belongs in the docs site
- Do NOT use `--all-extras` in any command — CI convention is `--extra <specific>`

## Testing Requirements

### Unit Tests

Not applicable (static documentation files).

### Integration Tests

Not applicable.

### E2E Tests

Verify `contribuicao.rst` builds without Sphinx warnings by running `uv run sphinx-build -M html docs/source docs/build` and checking for no warnings related to `contribuicao.rst`.

## Dependencies

- **Blocked By**: ticket-001-modernize-pyproject-toml.md, ticket-005-add-pre-commit-hooks.md (both completed)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: High
