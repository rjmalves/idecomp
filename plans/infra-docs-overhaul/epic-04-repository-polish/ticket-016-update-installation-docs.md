# ticket-016 Update Installation Documentation

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Update the installation documentation page (`docs/source/geral/instalacao.rst`) to reflect the current Python >= 3.10 requirement (currently says >= 3.8), add uv as a secondary installation method alongside pip, and modernize the commands to use current best practices. All content in Brazilian Portuguese.

## Anticipated Scope

- **Files likely to be modified**:
  - `/home/rogerio/git/idecomp/docs/source/geral/instalacao.rst` (update content)
- **Key decisions needed**:
  - Whether to present pip as primary and uv as secondary, or give them equal weight
  - Whether to add a section about installing from source with uv (development setup)
  - Whether to remove the `pip install --upgrade pip` preamble (modernize to just `pip install idecomp`)
- **Open questions**:
  - Should the page mention conda/mamba as installation alternatives?
  - Should it include a section on verifying the installation (`python -c "import idecomp; print(idecomp.__version__)"`)
  - Should the development installation section reference `uv sync --extra dev` instead of `pip install git+...`?

## Dependencies

- **Blocked By**: None (independent)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
