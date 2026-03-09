# ticket-009 Create FAQ Documentation Page

## Context

### Background

The idecomp documentation has no FAQ page. Users encountering common issues with DECOMP file handling -- installation problems, read/write patterns, DataFrame manipulation, error messages, and version compatibility -- must search through scattered tutorial content or open GitHub issues. A dedicated FAQ page in Brazilian Portuguese consolidates answers to the most common questions in one discoverable location.

### Relation to Epic

This is the second of three guide pages in Epic 3. It is independent of ticket-008 (architecture) and ticket-010 (performance) and can be implemented in parallel. Ticket-012 will add this page to the index.rst toctree.

### Current State

- `docs/source/guias/` directory may or may not exist yet (ticket-008 creates it; this ticket must also create it if not present).
- The tutorial page (`docs/source/geral/tutorial.rst`) demonstrates the `ClassName.read()` / `.write()` pattern and DataFrame property access, serving as a style reference.
- `idecomp/decomp/__init__.py` exports 41 file classes. The most commonly used are: `Dadger`, `Relato`, `DecOperSist`, `Vazoes`, `Hidr`, `Caso`.
- File classes use `ClassName.read(path)` for reading and `instance.write(path)` for writing (input files only; output files have no `write` method).
- Some files support versioning via cfinterface's `VERSIONS` dict (e.g., `DecOperSist` has versions `"31.0.2"` and `"31.1.2"`).
- Mock data for examples lives at `examples/decomp/` (dadger.rv0, dec_oper_sist.csv, relato.rv0).

## Specification

### Requirements

1. Create directory `docs/source/guias/` if it does not exist.
2. Create file `docs/source/guias/faq.rst` containing:
   - A title "Perguntas Frequentes (FAQ)"
   - Organized into 5 thematic sections using RST section headers:
     1. **Instalacao** (3 questions): pip install issues, version conflicts, cfinterface dependency.
     2. **Leitura de Arquivos** (4 questions): how to read a file, supported file formats, handling missing files, file encoding.
     3. **Escrita de Arquivos** (3 questions): how to write modified input files, why output files cannot be written, how to handle write errors.
     4. **DataFrames e Dados** (3 questions): how to access data as DataFrames, how to filter/modify DataFrames, how properties map to DECOMP blocks/registers.
     5. **Erros Comuns** (3 questions): common error messages and their solutions (e.g., cfinterface parse errors, version mismatch, missing registers).
   - Minimum 16 Q&A entries total across all sections.
   - Each question uses a bold RST inline markup or a subsection header.
   - Each answer includes at least one `.. code-block:: python` example where applicable (minimum 8 code examples across all answers).
3. All prose must be in Brazilian Portuguese (pt_BR).
4. Use `.. code-block:: python` for all code examples (not anonymous `::` blocks).
5. Code examples must use the current class-based API (`ClassName.read()`), never deprecated patterns.

### Inputs/Props

- No runtime inputs. Static RST documentation file.

### Outputs/Behavior

- A new RST file at `docs/source/guias/faq.rst` that renders correctly with `uv run sphinx-build -M html docs/source docs/build`.

### Error Handling

- Not applicable (static documentation content).

## Acceptance Criteria

- [ ] Given the ticket is implemented, when checking the filesystem, then the file `docs/source/guias/faq.rst` exists.
- [ ] Given `docs/source/guias/faq.rst` exists, when running `uv run sphinx-build -M html docs/source docs/build`, then the build exits with code 0 and `docs/build/html/guias/faq.html` is produced.
- [ ] Given the file `docs/source/guias/faq.rst` is opened, when counting RST section headers at the second level (underlined with `-`), then there are exactly 5 thematic sections.
- [ ] Given the file `docs/source/guias/faq.rst` is opened, when counting question entries (bold text lines or third-level headers), then there are at least 16 entries.
- [ ] Given the file `docs/source/guias/faq.rst` is opened, when counting occurrences of `.. code-block:: python`, then there are at least 8 occurrences.

## Implementation Guide

### Suggested Approach

1. Create `docs/source/guias/` directory if it does not exist.
2. Write `faq.rst` with the 5-section structure. Use the following question structure for consistency:

   ```rst
   Como ler um arquivo do DECOMP?
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Para ler qualquer arquivo do DECOMP, utilize o metodo ``read`` da classe correspondente:

   .. code-block:: python

       from idecomp.decomp import Dadger
       arq = Dadger.read("./dadger.rv0")
   ```

3. For the "Instalacao" section, cover: `pip install idecomp`, cfinterface version pin (`<=1.8.3`), and Python version compatibility.
4. For "Leitura de Arquivos", cover: basic read pattern, listing all 41 supported classes, handling `FileNotFoundError`, and file encoding (UTF-8 vs Latin-1 in older DECOMP files).
5. For "Escrita de Arquivos", cover: the `write()` method on input files, explain that output files (Relato, DecOperSist, etc.) are read-only, and handling write permissions.
6. For "DataFrames e Dados", cover: how properties like `arq.convergencia` return `pd.DataFrame`, how to filter DataFrames, and how properties map to internal Register/Block models.
7. For "Erros Comuns", cover: cfinterface parse errors (malformed DECOMP files), version detection with `VERSIONS` dict, and missing register/block handling.
8. Verify locally: `uv run sphinx-build -M html docs/source docs/build`.

### Key Files to Modify

- `docs/source/guias/faq.rst` (new file, ~150-200 lines)

### Patterns to Follow

- Use `^` underline for third-level subsection headers (questions) within `-`-underlined sections, matching RST conventions from `docs/source/geral/tutorial.rst`.
- Brazilian Portuguese prose style from existing docs.
- `.. code-block:: python` for all code (Furo dark-mode convention).

### Pitfalls to Avoid

- Do NOT add the page to `index.rst` toctree -- that is ticket-012's scope.
- Do NOT use deprecated API patterns (`le_arquivo`, `escreve_arquivo`) -- all examples must use `ClassName.read()` / `.write()`.
- Do NOT reference `tests/mocks/` directory in examples -- use generic file paths that users would have in their own environments.
- Do NOT use anonymous `::` code blocks.

## Testing Requirements

### Unit Tests

- Not applicable (documentation content).

### Integration Tests

- Run `uv run sphinx-build -M html docs/source docs/build` and verify exit code 0.
- Verify `docs/build/html/guias/faq.html` exists.

### E2E Tests

- Not applicable.

## Dependencies

- **Blocked By**: ticket-006-migrate-sphinx-theme-to-furo.md (completed)
- **Blocks**: ticket-012-update-index-toctree.md

## Effort Estimate

**Points**: 2
**Confidence**: High
