# ticket-016 Update Installation Documentation

## Context

### Background

The Sphinx documentation page `docs/source/geral/instalacao.rst` contains outdated information: it states Python >= 3.8 (actual requirement is >= 3.10), recommends `python -m pip install --upgrade pip` as a preamble step, uses anonymous `::` code blocks instead of `.. code-block:: bash`, and does not mention `uv` as an installation alternative. The page needs to be modernized to match the current project configuration.

### Relation to Epic

This is the fourth and final ticket in Epic 4 (Repository Polish). It is independent of all other tickets. It updates the Sphinx documentation installation page to be consistent with the modernized `pyproject.toml` (ticket-001, completed) and the README installation section (ticket-013).

### Current State

The file `/home/rogerio/git/idecomp/docs/source/geral/instalacao.rst` contains 43 lines with:

- Title "Instalacao" with `=` underline (correct RST heading hierarchy)
- Python >= 3.8 compatibility statement (incorrect)
- A paragraph about virtual environments with a link to the `venv` docs
- A `pip install --upgrade pip` preamble section
- "Instalando a versao distribuida oficialmente" section: `pip install idecomp`, `pip install --upgrade idecomp`, `pip install --upgrade idecomp==x.y.z`
- "Instalando a versao de desenvolvimento" section: `pip uninstall idecomp` then `pip install git+...`
- All code blocks use anonymous `::` syntax (not `.. code-block:: bash`)

## Specification

### Requirements

1. Update Python version requirement from `>= 3.8` to `>= 3.10`
2. Remove the `pip install --upgrade pip` preamble — it is unnecessary for modern Python
3. Keep the virtual environment recommendation paragraph (it is still valid)
4. Modernize "Instalando a versao distribuida oficialmente" section:
   - Primary: `pip install idecomp`
   - Show upgrade: `pip install --upgrade idecomp`
   - Show version pin: `pip install idecomp==x.y.z`
   - Secondary alternative: `uv add idecomp` (in a separate subsection or note)
5. Modernize "Instalando a versao de desenvolvimento" section:
   - Primary: `git clone` + `cd idecomp` + `uv sync --extra dev`
   - Alternative: `pip install git+https://github.com/rjmalves/idecomp`
   - Remove the `pip uninstall idecomp` preamble step (unnecessary)
6. Add a "Verificando a instalacao" subsection: `python -c "import idecomp; print(idecomp.__version__)"`
7. Replace all anonymous `::` code blocks with explicit `.. code-block:: bash` directives (Furo theme convention from Epic 3 learnings)
8. All prose in Brazilian Portuguese (pt_BR)

### Inputs/Props

- Actual Python requirement: `requires-python = ">= 3.10"` from `/home/rogerio/git/idecomp/pyproject.toml` line 13
- Development extras: `uv sync --extra dev` installs test + lint + docs (from pyproject.toml lines 32-43)
- RST heading hierarchy: `=` for page title, `-` for sections, `^` for subsections (from Epic 3 conventions)

### Outputs/Behavior

An updated `instalacao.rst` of approximately 55-70 lines that renders correctly in the Sphinx/Furo documentation site with syntax-highlighted bash code blocks.

### Error Handling

Not applicable (static RST documentation file).

## Acceptance Criteria

- [ ] Given the file `/home/rogerio/git/idecomp/docs/source/geral/instalacao.rst`, when the Python version text is checked, then it states `Python >= 3.10` (not `>= 3.8`)
- [ ] Given the file, when searched for `pip install --upgrade pip` or `pip install ---upgrade pip`, then no such preamble line exists
- [ ] Given the file, when code blocks are checked, then every code block uses `.. code-block:: bash` directive (no anonymous `::` blocks)
- [ ] Given the file, when the `uv` tool is searched, then at least one section mentions `uv add idecomp` or `uv sync --extra dev` as an alternative installation method
- [ ] Given the file, when a "Verificando a instalacao" subsection is searched, then it contains `python -c "import idecomp; print(idecomp.__version__)"` in a code block

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/docs/source/geral/instalacao.rst`
2. Update line 4: change `Python >= 3.8` to `Python >= 3.10`
3. Keep the virtual environment paragraph (lines 6-7) but simplify slightly
4. Remove the `pip install --upgrade pip` block entirely (lines 9-11)
5. Rewrite "Instalando a versao distribuida oficialmente" section:
   - Use `.. code-block:: bash` for all code blocks
   - Show `pip install idecomp`, upgrade, and version pin commands
   - Add a `.. tip::` admonition for the `uv` alternative: `uv add idecomp`
6. Rewrite "Instalando a versao de desenvolvimento" section:
   - Primary flow: `git clone`, `cd idecomp`, `uv sync --extra dev`
   - Alternative: `pip install git+https://github.com/rjmalves/idecomp`
   - Remove the `pip uninstall` preamble
7. Add "Verificando a instalacao" subsection with `-` underline:

   ```rst
   Verificando a instalacao
   ------------------------

   Apos a instalacao, verifique se o pacote esta disponivel:

   .. code-block:: bash

       python -c "import idecomp; print(idecomp.__version__)"
   ```

8. Verify RST heading hierarchy: `=` for title, `-` for sections, `^` for subsections (if any)

### Key Files to Modify

- `/home/rogerio/git/idecomp/docs/source/geral/instalacao.rst` (update)

### Patterns to Follow

- Use `.. code-block:: bash` for all shell commands (Furo monokai dark style only applies to syntax-highlighted blocks, per Epic 3 learnings)
- RST heading hierarchy: `=` for page title, `-` for sections (matching `/home/rogerio/git/idecomp/docs/source/geral/tutorial.rst` convention)
- Use `.. tip::` admonition for the uv alternative (non-intrusive, visually distinct)

### Pitfalls to Avoid

- Do NOT use anonymous `::` code blocks — Furo dark mode does not highlight them properly
- Do NOT remove the virtual environment recommendation paragraph — it is still valid guidance
- Do NOT use `--all-extras` in any uv command — use `--extra dev` specifically
- Do NOT add conda/mamba instructions — out of scope for this ticket
- Do NOT change the filename or its position in the toctree — `geral/instalacao` is already linked from `index.rst`

## Testing Requirements

### Unit Tests

Not applicable (static RST documentation file).

### Integration Tests

Not applicable.

### E2E Tests

Verify the page builds without Sphinx warnings by running `uv run sphinx-build -M html docs/source docs/build` and checking for no warnings related to `instalacao.rst`.

## Dependencies

- **Blocked By**: None (independent)
- **Blocks**: None

## Effort Estimate

**Points**: 1
**Confidence**: High
