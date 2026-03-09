# ticket-010 Create Performance Guide Page

## Context

### Background

The idecomp documentation has no guidance on performance characteristics or optimization strategies. Users processing large DECOMP datasets or running batch operations have no reference for expected read/write times, memory considerations, or efficient patterns. This ticket creates a `desempenho.rst` page with practical performance guidance, written in Brazilian Portuguese.

### Relation to Epic

This is the third of three guide pages in Epic 3. It is independent of ticket-008 and ticket-009 and can be implemented in parallel. Ticket-012 will add this page to the index.rst toctree.

### Current State

- `docs/source/guias/` directory may or may not exist yet (created by ticket-008 or ticket-009).
- `idecomp/__init__.py` eagerly imports the `decomp` subpackage, which in turn eagerly imports all 41 file classes from `idecomp/decomp/__init__.py`. This means `import idecomp` triggers the import of all 41 class definitions.
- There is no `benchmarks/` directory in the repository.
- The codebase uses `pandas` DataFrames for all tabular data output. File classes like `DecOperSist` can produce large DataFrames with columns for estagio, cenario, patamar, etc.
- Some file classes support version detection via cfinterface's `VERSIONS` dict (e.g., `DecOperSist` checks versions `"31.0.2"` and `"31.1.2"`).
- Gallery examples in `examples/` demonstrate typical usage patterns with mock data.

## Specification

### Requirements

1. Create directory `docs/source/guias/` if it does not exist.
2. Create file `docs/source/guias/desempenho.rst` containing:
   - A title "Guia de Desempenho"
   - A section "Importacao" (2-3 paragraphs) documenting the eager import behavior: `import idecomp` loads all 41 class definitions. Recommend importing specific classes when startup time matters (`from idecomp.decomp.dadger import Dadger` instead of `from idecomp.decomp import Dadger`).
   - A section "Leitura e Escrita de Arquivos" describing typical I/O patterns: single-file read, batch processing of multiple files (e.g., reading all `dec_oper_sist.csv` files from multiple scenarios), and tips for efficient batch processing (reading files in a loop, collecting DataFrames, concatenating with `pd.concat`).
   - A section "Uso de Memoria" explaining that each read file holds its parsed data in memory; for large batch operations, recommend reading, extracting the needed DataFrame, and discarding the file object. Include a code example showing this pattern.
   - A section "Dicas de Otimizacao" with 3-5 practical tips: use specific imports, process files in batches with generators, filter DataFrames early, use `del` to free memory, and consider `gc.collect()` for very large batch operations.
3. All prose must be in Brazilian Portuguese (pt_BR).
4. Use `.. code-block:: python` for all code examples (not anonymous `::` blocks).
5. Include at least 3 code examples showing performance-relevant patterns.
6. Do NOT include actual benchmark numbers (the repository has no benchmarks directory). Instead, describe how users can profile their own workflows using Python's `time` module.

### Inputs/Props

- No runtime inputs. Static RST documentation file.

### Outputs/Behavior

- A new RST file at `docs/source/guias/desempenho.rst` that renders correctly with `uv run sphinx-build -M html docs/source docs/build`.

### Error Handling

- Not applicable (static documentation content).

## Acceptance Criteria

- [ ] Given the ticket is implemented, when checking the filesystem, then the file `docs/source/guias/desempenho.rst` exists.
- [ ] Given `docs/source/guias/desempenho.rst` exists, when running `uv run sphinx-build -M html docs/source docs/build`, then the build exits with code 0 and `docs/build/html/guias/desempenho.html` is produced.
- [ ] Given the file `docs/source/guias/desempenho.rst` is opened, when inspecting section headers, then it contains exactly 4 sections: "Importacao", "Leitura e Escrita de Arquivos", "Uso de Memoria", and "Dicas de Otimizacao".
- [ ] Given the file `docs/source/guias/desempenho.rst` is opened, when counting occurrences of `.. code-block:: python`, then there are at least 3 occurrences.

## Implementation Guide

### Suggested Approach

1. Create `docs/source/guias/` directory if it does not exist.
2. Write `desempenho.rst` following the 4-section structure.
3. For the "Importacao" section, demonstrate the two import styles:

   ```python
   # Importa todos os 41 modulos (mais lento)
   from idecomp.decomp import Dadger

   # Importa apenas o modulo necessario (mais rapido)
   from idecomp.decomp.dadger import Dadger
   ```

4. For the "Leitura e Escrita" section, show a batch processing pattern:

   ```python
   from pathlib import Path
   import pandas as pd
   from idecomp.decomp.dec_oper_sist import DecOperSist

   dfs = []
   for caminho in Path("./resultados").glob("*/dec_oper_sist.csv"):
       arq = DecOperSist.read(str(caminho))
       dfs.append(arq.tabela)
   df_total = pd.concat(dfs, ignore_index=True)
   ```

5. For "Uso de Memoria", show the read-extract-discard pattern:
   ```python
   arq = DecOperSist.read("./dec_oper_sist.csv")
   df = arq.tabela
   del arq  # libera o objeto do arquivo da memoria
   ```
6. Verify locally: `uv run sphinx-build -M html docs/source docs/build`.

### Key Files to Modify

- `docs/source/guias/desempenho.rst` (new file, ~80-120 lines)

### Patterns to Follow

- RST heading style from `docs/source/geral/tutorial.rst`: `=` for title, `-` for sections.
- Brazilian Portuguese prose style from existing docs.
- `.. code-block:: python` for all code examples.

### Pitfalls to Avoid

- Do NOT add the page to `index.rst` toctree -- that is ticket-012's scope.
- Do NOT include actual benchmark numbers -- the repo has no benchmarks infrastructure, and numbers would become stale.
- Do NOT recommend lazy import migration -- that is a code change outside the scope of documentation.
- Do NOT use anonymous `::` code blocks.

## Testing Requirements

### Unit Tests

- Not applicable (documentation content).

### Integration Tests

- Run `uv run sphinx-build -M html docs/source docs/build` and verify exit code 0.
- Verify `docs/build/html/guias/desempenho.html` exists.

### E2E Tests

- Not applicable.

## Dependencies

- **Blocked By**: ticket-006-migrate-sphinx-theme-to-furo.md (completed)
- **Blocks**: ticket-012-update-index-toctree.md

## Effort Estimate

**Points**: 2
**Confidence**: High
