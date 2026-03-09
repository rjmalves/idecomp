# ticket-013 Expand README with Badges and Sections

## Context

### Background

The current `README.md` is a minimal 37-line file with only two badges (CI and codecov), a brief description paragraph, a short installation section referencing the outdated Python >= 3.8 requirement, and a documentation link. As the primary landing page for the GitHub repository, it needs to be expanded with a complete set of badges, structured sections in Brazilian Portuguese, a code example, and links to the newly created documentation site.

### Relation to Epic

This is the first ticket in Epic 4 (Repository Polish). It modernizes the repository's most visible public-facing file. The badge URLs depend on CI workflow names established in ticket-002 (already completed). The documentation links reference the Sphinx site built and deployed in Epics 2-3.

### Current State

The file `/home/rogerio/git/idecomp/README.md` contains:

- Two badges: `tests` (from `main.yml`) and `codecov`
- A description paragraph in Portuguese
- A 3-item feature bullet list
- An installation section with `Python >= 3.8` (incorrect, should be `>= 3.10`)
- A `pip install` and `pip install git+...` command pair
- A documentation link to `https://rjmalves.github.io/idecomp`

## Specification

### Requirements

1. Add badges in a single row at the top: CI (already present), codecov (already present), PyPI version (shields.io), Python version (shields.io), License (shields.io), Docs (shields.io linking to GitHub Pages)
2. Keep the existing description paragraph; expand the feature bullet list to 5-6 items covering: file read/write, DataFrame output, class-per-file mapping, cfinterface foundation, type safety
3. Add a "Exemplo Rapido" section with a code block showing `Dadger.read()` and accessing a property
4. Modernize the "Instalacao" section: Python >= 3.10, `pip install idecomp` as primary, `uv add idecomp` as secondary alternative
5. Add a "Projetos Relacionados" section linking to `inewave` and `cfinterface` GitHub repos
6. Add a "Contribuindo" section with a one-liner pointing to `CONTRIBUTING.md`
7. Add a "Licenca" section referencing MIT and the `LICENSE.md` file
8. All prose in Brazilian Portuguese (pt_BR)

### Inputs/Props

- Badge URLs use `https://img.shields.io/` for PyPI, Python, license, and docs badges
- CI badge URL: `https://github.com/rjmalves/idecomp/actions/workflows/main.yml/badge.svg` (already correct in file)
- Codecov badge URL: already correct in file
- PyPI badge: `https://img.shields.io/pypi/v/idecomp`
- Python badge: `https://img.shields.io/pypi/pyversions/idecomp`
- License badge: `https://img.shields.io/pypi/l/idecomp`
- Docs badge: `https://img.shields.io/badge/docs-online-blue` linking to `https://rjmalves.github.io/idecomp/`

### Outputs/Behavior

A complete README.md file of approximately 80-120 lines with all sections described above, rendering correctly on GitHub with all badges displayed inline.

### Error Handling

Not applicable (static markdown file).

## Acceptance Criteria

- [ ] Given the file `/home/rogerio/git/idecomp/README.md`, when inspected, then it contains exactly 6 badge image links in the first content block: tests (main.yml), codecov, PyPI version, Python versions, license, and docs
- [ ] Given the README badge block, when the CI badge URL is checked, then it references `actions/workflows/main.yml/badge.svg` (not `tests.yml` or any other filename)
- [ ] Given the README "Instalacao" section, when the Python version text is checked, then it states `Python >= 3.10` (not `>= 3.8`)
- [ ] Given the README "Instalacao" section, when the installation commands are checked, then it shows `pip install idecomp` as primary and `uv add idecomp` as a secondary alternative
- [ ] Given the README "Exemplo Rapido" section, when inspected, then it contains a fenced Python code block using `Dadger` class with the class-based `read()` API pattern

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/README.md`
2. Replace the badge block at the top with all 6 badges, each as `[![name](image-url)](link-url)` on a single line separated by spaces
3. Keep the existing description paragraph (lines 6-7 of current file) unchanged
4. Expand the feature bullet list (currently 3 items) to include: leitura e escrita de arquivos, dados tabulares com pandas DataFrame, mapeamento classe-por-arquivo, base no framework cfinterface, tipagem estatica
5. Add the "Exemplo Rapido" section with a `python` fenced code block showing:
   ```python
   from idecomp.decomp.dadger import Dadger
   dadger = Dadger.read("dadger.rv0")
   ```
6. Rewrite the "Instalacao" section with the correct Python version and both pip/uv commands
7. Add sections: "Documentacao" (link to site), "Projetos Relacionados" (inewave, cfinterface), "Contribuindo" (link to CONTRIBUTING.md), "Licenca" (MIT)
8. All section headings use `##` markdown format (already the convention in the current file)

### Key Files to Modify

- `/home/rogerio/git/idecomp/README.md` (rewrite)

### Patterns to Follow

- Badge formatting: `[![alt](img-url)](link-url)` with two trailing spaces for line break between badge line and next content
- Section headings in Portuguese without accents in markdown (matching current file's `## Instalacao` pattern — note: the current README uses `## Instalacao` without cedilla, but proper Portuguese uses accents; follow the existing convention for heading text)
- Code blocks use triple-backtick fences with `python` language specifier (markdown convention, not RST)

### Pitfalls to Avoid

- Do NOT use `actions/workflows/tests.yml` for the CI badge — the workflow file is `main.yml` even though its display name is `tests`
- Do NOT reference `publish.yml` anywhere — it was renamed to `release.yml`
- Do NOT state Python >= 3.8 — the actual requirement in `pyproject.toml` is `>= 3.10`
- Do NOT add a `dev-requirements.txt` reference — the project uses `pyproject.toml` extras
- Do NOT use the deprecated `le_arquivo`/`escreve_arquivo` API in the code example — use the class-based `ClassName.read()` pattern

## Testing Requirements

### Unit Tests

Not applicable (static markdown file).

### Integration Tests

Not applicable.

### E2E Tests

Verify the README renders correctly by visually inspecting `https://github.com/rjmalves/idecomp` after pushing, or by running a local markdown preview tool.

## Dependencies

- **Blocked By**: ticket-002-restructure-ci-workflow.md (needs final workflow name for badge URL; already completed)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: High
