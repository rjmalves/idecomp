# ticket-014 Create CONTRIBUTING.md

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Create a standalone CONTRIBUTING.md file at the repository root documenting the full contributor workflow: environment setup with uv, dependency installation by group, pre-commit hook usage, testing with pytest, type checking with mypy, code formatting with ruff, code conventions (PEP8, static typing, DataFrame patterns), and PR workflow. Content extracted and updated from the existing `docs/source/geral/contribuicao.rst` which currently references deprecated tools (pylama, black, pip/requirements.txt).

## Anticipated Scope

- **Files likely to be modified**:
  - `/home/rogerio/git/idecomp/CONTRIBUTING.md` (new file)
  - `/home/rogerio/git/idecomp/docs/source/geral/contribuicao.rst` (update to reference CONTRIBUTING.md or keep both in sync)
- **Key decisions needed**:
  - Whether to keep `contribuicao.rst` as a full page or convert it to a redirect/summary pointing to CONTRIBUTING.md
  - Which content from `contribuicao.rst` stays in docs vs. moves to CONTRIBUTING.md (cfinterface framework description is docs-appropriate; dev setup is CONTRIBUTING-appropriate)
  - Whether to include the cfinterface framework explanation or keep it in the architecture page (ticket-008)
- **Open questions**:
  - Should CONTRIBUTING.md reference pre-commit hook stages (normal vs. manual for mypy)?
  - Should it include a section on running sphinx-build locally?
  - Should the PR workflow section describe branch naming conventions?

## Dependencies

- **Blocked By**: ticket-001-modernize-pyproject-toml.md, ticket-005-add-pre-commit-hooks.md
- **Blocks**: None

## Effort Estimate

**Points**: 3
**Confidence**: Low (will be re-estimated during refinement)
