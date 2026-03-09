# ticket-011 Improve API Reference with Autosummary Blocks

## Context

### Background

The API reference pages for `decomp/` and `libs/` currently use plain `.. toctree::` listings that link to individual class pages but provide no at-a-glance summary of what each class does. Sphinx's `.. autosummary::` directive can generate summary tables showing each class with its one-line docstring, making the API reference more navigable. The `autosummary_generate = True` setting is already enabled in `conf.py`, and the `sphinx.ext.autosummary` extension is already loaded.

### Relation to Epic

This ticket is independent of the three guide pages (tickets 008-010) and can be implemented in parallel. It improves the existing API reference section rather than creating new guide content.

### Current State

- `docs/source/referencia/decomp/index.rst` contains a `.. toctree::` with 41 entries pointing to individual class RST files in `arquivos/`.
- `docs/source/referencia/libs/index.rst` contains a `.. toctree::` with 2 entries (`restricoes`, `usinas_hidreletricas`).
- Individual class RST files (e.g., `docs/source/referencia/decomp/arquivos/dadger.rst`) use `.. autoclass::` with `:members:` to document each class and its register models.
- `conf.py` has `autosummary_generate = True` (line 30), `sphinx.ext.autosummary` in extensions (line 20), and `templates_path = ["_templates"]` (line 31).
- The `docs/source/_templates/autosummary/` directory does not exist yet.
- `numpydoc_show_class_members = False` (line 61) suppresses member tables on class pages; this ticket does NOT change that setting.

## Specification

### Requirements

1. Add an `.. autosummary::` block to `docs/source/referencia/decomp/index.rst` listing all 41 file classes from `idecomp.decomp`. The block must appear before the existing `.. toctree::` block and use the `:nosignatures:` option to keep the table clean.
2. Add an `.. autosummary::` block to `docs/source/referencia/libs/index.rst` listing the 2 classes from `idecomp.libs` (`Restricoes`, `UsinasHidreletricas`). Same placement and options.
3. Each autosummary entry uses the fully qualified module path (e.g., `idecomp.decomp.dadger.Dadger`) so that autosummary can resolve the class and extract its docstring.
4. Keep the existing `.. toctree::` blocks intact -- the autosummary table supplements them, it does not replace them.
5. Add a brief introductory paragraph in Brazilian Portuguese above each autosummary block explaining that the table below shows all available classes with descriptions.

### Inputs/Props

- No runtime inputs. Modifications to existing RST files.

### Outputs/Behavior

- The `decomp/index.rst` page renders an autosummary table with 41 rows (one per file class) showing class name and one-line docstring.
- The `libs/index.rst` page renders an autosummary table with 2 rows.
- The existing toctree navigation is preserved unchanged.

### Error Handling

- Not applicable (static documentation content).

## Acceptance Criteria

- [ ] Given the file `docs/source/referencia/decomp/index.rst` is opened, when searching for `.. autosummary::`, then exactly 1 autosummary block is found containing 41 class entries.
- [ ] Given the file `docs/source/referencia/libs/index.rst` is opened, when searching for `.. autosummary::`, then exactly 1 autosummary block is found containing 2 class entries.
- [ ] Given both index files are modified, when running `uv run sphinx-build -M html docs/source docs/build`, then the build exits with code 0.
- [ ] Given the build succeeds, when opening `docs/build/html/referencia/decomp/index.html` in a browser, then a summary table is visible listing class names with their docstring descriptions.

## Implementation Guide

### Suggested Approach

1. Edit `docs/source/referencia/decomp/index.rst`:
   - After the title and label, add a paragraph in Portuguese: "A tabela abaixo lista todas as classes disponiveis para manipulacao dos arquivos do DECOMP."
   - Add the autosummary block:

     ```rst
     .. autosummary::
        :nosignatures:

        idecomp.decomp.dadger.Dadger
        idecomp.decomp.relato.Relato
        idecomp.decomp.dec_oper_sist.DecOperSist
        ...
     ```

   - List all 41 classes using the fully qualified path from their source module (not from the `__init__.py` re-export), as autosummary needs the actual module path to resolve docstrings.
   - Keep the existing `.. toctree::` block below the autosummary block.

2. Edit `docs/source/referencia/libs/index.rst`:
   - Add a similar paragraph and autosummary block with:

     ```rst
     .. autosummary::
        :nosignatures:

        idecomp.libs.restricoes.Restricoes
        idecomp.libs.usinas_hidreletricas.UsinasHidreletricas
     ```

3. Build and verify: `uv run sphinx-build -M html docs/source docs/build`.

### Key Files to Modify

- `docs/source/referencia/decomp/index.rst` (add ~50 lines for autosummary block)
- `docs/source/referencia/libs/index.rst` (add ~10 lines for autosummary block)

### Patterns to Follow

- Use `:nosignatures:` option on autosummary to keep tables clean (class names only, no `__init__` signatures).
- Use fully qualified module paths for autosummary entries (e.g., `idecomp.decomp.dadger.Dadger`), not re-exported paths.

### Pitfalls to Avoid

- Do NOT remove or modify the existing `.. toctree::` blocks -- they control sidebar navigation.
- Do NOT change `numpydoc_show_class_members` in `conf.py` -- it is intentionally `False`.
- Do NOT create custom autosummary templates in `_templates/` -- the default templates are sufficient for class summary tables.
- Do NOT use `.. autosummary:: :toctree:` option -- the individual class pages already exist via the toctree; adding `:toctree:` to autosummary would generate duplicate stub pages.

## Testing Requirements

### Unit Tests

- Not applicable (documentation content).

### Integration Tests

- Run `uv run sphinx-build -M html docs/source docs/build` and verify exit code 0.
- Verify `docs/build/html/referencia/decomp/index.html` contains `<table` elements from autosummary rendering.

### E2E Tests

- Not applicable.

## Dependencies

- **Blocked By**: ticket-006-migrate-sphinx-theme-to-furo.md (completed)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: High
