# ticket-008 Create Architecture Documentation Page

## Context

### Background

The idecomp documentation currently has an "Apresentacao" (overview) section and a "Geral" section with installation, tutorial, and contribution pages, but lacks a dedicated architecture page explaining the package's internal structure. New users and contributors have no guide to understand how idecomp maps DECOMP binary/text files to Python objects via the cfinterface framework. This ticket creates an `arquitetura.rst` page in a new `docs/source/guias/` directory to fill that gap. All content is written in Brazilian Portuguese.

### Relation to Epic

This is the first of three guide pages (architecture, FAQ, performance) that comprise Epic 3's content expansion. The architecture page provides foundational understanding that the FAQ and performance pages build upon. Ticket-012 will add this page to the index.rst toctree.

### Current State

- `docs/source/guias/` directory does not exist yet; it must be created.
- The Furo theme is active (`html_theme = "furo"` in `docs/source/conf.py`), with `language = "pt_BR"`.
- `idecomp/__init__.py` eagerly imports the `decomp` subpackage (`from . import decomp`).
- `idecomp/decomp/__init__.py` eagerly imports all 41 file classes (Dadger, Relato, DecOperSist, etc.).
- File classes in `idecomp/decomp/` inherit from cfinterface base classes: `RegisterFile` (for register-based files like dadger) and `BlockFile` (for block-based files like relato). CSV-based outputs use `ArquivoCSV`.
- Register/Block models live in `idecomp/decomp/modelos/` (45 files) and `idecomp/decomp/modelos/blocos/`.
- `idecomp/libs/` contains 2 modules: `restricoes.py` and `usinas_hidreletricas.py` with a `modelos/` subdirectory.
- intersphinx is configured for cfinterface at `https://rjmalves.github.io/cfinterface/`.

## Specification

### Requirements

1. Create directory `docs/source/guias/` if it does not exist.
2. Create file `docs/source/guias/arquitetura.rst` containing:
   - A title "Arquitetura do idecomp"
   - A section "Visao Geral" (2-3 paragraphs) explaining that idecomp provides a Python interface to DECOMP files, built on the cfinterface framework.
   - A section "Estrutura de Pacotes" describing the top-level layout: `idecomp/decomp/` (41 file classes for DECOMP files), `idecomp/libs/` (2 classes for auxiliary LIBS files), `idecomp/decomp/modelos/` (register/block models), `idecomp/decomp/modelos/blocos/` (block definitions), `idecomp/decomp/modelos/arquivoscsv/` (CSV-based output adapter).
   - A section "Framework cfinterface" explaining the three file base classes: `RegisterFile` (e.g., Dadger), `BlockFile` (e.g., Relato), and `ArquivoCSV` (e.g., DecOperSist), with intersphinx cross-references to cfinterface documentation.
   - A section "Fluxo de Dados" describing the data flow: raw DECOMP file on disk -> `ClassName.read(path)` -> parsed Python object -> `.property` accessors return `pd.DataFrame` or typed values -> optional `.write(path)` for input files.
   - A section "Modelos e Registros" explaining how each file class delegates parsing to model classes in `modelos/` (Register subclasses for line-oriented formats, Block subclasses for section-oriented formats).
3. All prose must be in Brazilian Portuguese (pt_BR).
4. Use `.. code-block:: python` for all code examples (not anonymous `::` blocks) per Furo dark-mode convention from learnings.
5. Include at least one code example showing the read/write flow (e.g., `Dadger.read()` and property access).
6. Cross-reference cfinterface classes using intersphinx (e.g., `:class:`cfinterface.files.registerfile.RegisterFile``).

### Inputs/Props

- No runtime inputs. This is a static RST documentation file.

### Outputs/Behavior

- A new RST file at `docs/source/guias/arquitetura.rst` that renders correctly with `uv run sphinx-build -M html docs/source docs/build`.
- The page appears under the Furo sidebar when added to the toctree (done in ticket-012).

### Error Handling

- Not applicable (static documentation content).

## Acceptance Criteria

- [ ] Given the directory `docs/source/guias/` does not exist, when the ticket is implemented, then the directory `docs/source/guias/` exists and contains the file `arquitetura.rst`.
- [ ] Given the file `docs/source/guias/arquitetura.rst` exists, when running `uv run sphinx-build -M html docs/source docs/build 2>&1 | grep -c "arquitetura"`, then the output count is >= 1 (file is processed) and the build exits with code 0.
- [ ] Given the file `docs/source/guias/arquitetura.rst` is opened, when inspecting its content, then it contains exactly 5 sections: "Visao Geral", "Estrutura de Pacotes", "Framework cfinterface", "Fluxo de Dados", and "Modelos e Registros".
- [ ] Given the file `docs/source/guias/arquitetura.rst` is opened, when searching for `.. code-block:: python`, then at least 1 match is found (code example present with explicit directive).

## Implementation Guide

### Suggested Approach

1. Create the `docs/source/guias/` directory.
2. Write `arquitetura.rst` with the RST structure. Use the existing `docs/source/geral/tutorial.rst` as a style reference for Brazilian Portuguese prose and `.. code-block:: python` usage.
3. For the package structure section, reference the actual module layout: `idecomp/decomp/__init__.py` imports 41 classes; `idecomp/libs/__init__.py` imports `UsinasHidreletricas`; `idecomp/decomp/modelos/` contains 45+ model files.
4. For the cfinterface section, use intersphinx cross-references. The mapping is already configured in `conf.py` line 69: `"cfinterface": ("https://rjmalves.github.io/cfinterface/", None)`.
5. For the data flow section, use a simple code example like:
   ```python
   from idecomp.decomp import Dadger
   arq = Dadger.read("./dadger.rv0")
   titulo = arq.te  # acessa o registro TE
   ```
6. Verify the build locally: `uv run sphinx-build -M html docs/source docs/build`.

### Key Files to Modify

- `docs/source/guias/arquitetura.rst` (new file, ~80-120 lines)

### Patterns to Follow

- Follow the RST heading style used in `docs/source/geral/tutorial.rst`: `=` underline for title, `-` underline for sections.
- Follow the Brazilian Portuguese prose style from `tutorial.rst` and `apresentacao.rst`.
- Use `.. code-block:: python` (never anonymous `::` blocks) per Furo convention from learnings.

### Pitfalls to Avoid

- Do NOT add the page to `index.rst` toctree -- that is ticket-012's scope.
- Do NOT add Furo to the `extensions` list in `conf.py` -- it is a theme, not an extension (learnings).
- Do NOT use anonymous `::` code blocks -- Furo's monokai dark style only applies to `.. code-block::` directives.
- Do NOT deeply document cfinterface internals -- link to cfinterface docs via intersphinx instead.

## Testing Requirements

### Unit Tests

- Not applicable (documentation content).

### Integration Tests

- Run `uv run sphinx-build -M html docs/source docs/build` and verify exit code 0.
- Verify the built HTML file exists at `docs/build/html/guias/arquitetura.html`.

### E2E Tests

- Not applicable.

## Dependencies

- **Blocked By**: ticket-006-migrate-sphinx-theme-to-furo.md (completed -- Furo theme is active)
- **Blocks**: ticket-012-update-index-toctree.md

## Effort Estimate

**Points**: 2
**Confidence**: High
