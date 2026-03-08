# ticket-011 Improve API Reference with Autosummary Blocks

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Enhance the API reference pages in `docs/source/referencia/decomp/index.rst` and `docs/source/referencia/libs/index.rst` with autosummary directive blocks that generate method/attribute tables for each documented class. Currently these pages are plain toctree listings; autosummary adds navigable tables showing the public interface at a glance.

## Anticipated Scope

- **Files likely to be modified**:
  - `docs/source/referencia/decomp/index.rst` (add autosummary blocks)
  - `docs/source/referencia/libs/index.rst` (add autosummary blocks)
  - Individual `.rst` files in `docs/source/referencia/decomp/arquivos/` (may need autosummary directives per class)
  - `docs/source/conf.py` (may need autosummary template customization)
- **Key decisions needed**:
  - Whether to use `.. autosummary::` at the module index level or at each individual class page
  - Whether to create custom autosummary templates in `_templates/`
  - The canonical public class list for decomp/ (the 34 classes in `idecomp/decomp/__init__.py`)
- **Open questions**:
  - Does the existing `autosummary_generate = True` in `conf.py` already generate stubs?
  - Should autosummary show methods and attributes, or just classes?
  - Are there autosummary templates from inewave that can be reused?

## Dependencies

- **Blocked By**: ticket-006-migrate-sphinx-theme-to-furo.md
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: Low (will be re-estimated during refinement)
