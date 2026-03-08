# ticket-007 Update Sphinx-Gallery Examples for Furo Compatibility

## Context

### Background

idecomp has 4 example scripts in `/examples/` that are rendered by sphinx-gallery into the documentation. After migrating to the Furo theme (ticket-006), these examples must be verified to build correctly. The inewave overhaul revealed that sphinx-gallery can fail due to cfinterface import errors during example execution, and example scripts may use deprecated API patterns.

### Relation to Epic

Second and final ticket of Epic 2. Depends on ticket-006 (Furo must be configured before verifying gallery builds).

### Current State

Directory: `/home/rogerio/git/idecomp/examples/`

- `plot_dadger.py` - Example reading/plotting dadger data
- `plot_dec_oper_sist.py` - Example reading/plotting dec_oper_sist data
- `plot_edit_dadger.py` - Example editing dadger data
- `plot_relato.py` - Example reading/plotting relato data
- `README.rst` - Gallery index page
- `decomp/` - Subdirectory (likely contains mock data for examples)

Sphinx-gallery config in `conf.py`:

```python
sphinx_gallery_conf = {
    "examples_dirs": "../../examples",
    "gallery_dirs": "examples",
    "backreferences_dir": "gen_modules/generated",
}
```

## Specification

### Requirements

1. Review each of the 4 example scripts for:
   - Deprecated API patterns (e.g., `le_arquivo`/`escreve_arquivo` which were deprecated in v1.0.0)
   - Import errors that would cause sphinx-gallery to fail during build
   - Plotly renderer compatibility with sphinx-gallery (the `pio.renderers.default = "sphinx_gallery"` is already set in conf.py)
2. Run `uv run sphinx-build -M html docs/source docs/build` and verify the gallery builds without errors
3. If any example script fails:
   - Fix import paths or API usage
   - If cfinterface import errors prevent execution, add `sphinx_gallery_conf["abort_on_example_error"] = False` to `conf.py` as a fallback
4. Verify the gallery renders correctly with Furo theme (thumbnail grid, example pages)
5. Update `README.rst` in the examples directory if its content references sphinx-rtd-theme or outdated information

### Inputs/Props

- Example scripts: `/home/rogerio/git/idecomp/examples/plot_dadger.py`, `plot_dec_oper_sist.py`, `plot_edit_dadger.py`, `plot_relato.py`
- Gallery config: `/home/rogerio/git/idecomp/docs/source/conf.py` (sphinx_gallery_conf section)
- Example data: `/home/rogerio/git/idecomp/examples/decomp/`

### Outputs/Behavior

- All 4 example scripts execute during sphinx-build without errors (or gracefully handle import failures)
- The gallery page at `examples/index.html` shows thumbnails for all examples
- Individual example pages render correctly with Furo theme

### Error Handling

- If cfinterface import errors prevent example execution, set `abort_on_example_error = False` to allow partial gallery builds
- If plotly rendering fails in sphinx-gallery, add `plot_gallery = False` for affected examples or switch to matplotlib-only plots

## Acceptance Criteria

- [ ] Given the example scripts in `/home/rogerio/git/idecomp/examples/`, when inspecting each script, then no deprecated API patterns (`le_arquivo`, `escreve_arquivo`) are used
- [ ] Given a virtual environment with docs extras, when running `uv run sphinx-build -M html docs/source docs/build`, then the sphinx-gallery extension produces output in `docs/build/html/examples/` without errors (exit code 0)
- [ ] Given the built documentation, when inspecting `docs/build/html/examples/index.html`, then it contains thumbnail entries for all 4 example scripts
- [ ] Given the `examples/README.rst`, when inspecting its content, then it does not reference `sphinx-rtd-theme` or any removed/outdated concepts

## Implementation Guide

### Suggested Approach

1. Read each example script in `/home/rogerio/git/idecomp/examples/`:
   - `plot_dadger.py`
   - `plot_dec_oper_sist.py`
   - `plot_edit_dadger.py`
   - `plot_relato.py`
2. Check for deprecated API usage (`le_arquivo`, `escreve_arquivo`) and fix if found
3. Check that imports resolve correctly (the examples likely import from `idecomp.decomp`)
4. Run the full sphinx-build: `uv run sphinx-build -M html docs/source docs/build`
5. If gallery errors occur:
   - Check error messages for cfinterface import issues
   - If needed, add `"abort_on_example_error": False` to `sphinx_gallery_conf` in `conf.py`
6. Inspect the generated gallery HTML to verify thumbnails and example pages render
7. Review and update `examples/README.rst` if needed

### Key Files to Modify

- `/home/rogerio/git/idecomp/examples/plot_dadger.py` (if deprecated APIs found)
- `/home/rogerio/git/idecomp/examples/plot_dec_oper_sist.py` (if deprecated APIs found)
- `/home/rogerio/git/idecomp/examples/plot_edit_dadger.py` (if deprecated APIs found)
- `/home/rogerio/git/idecomp/examples/plot_relato.py` (if deprecated APIs found)
- `/home/rogerio/git/idecomp/docs/source/conf.py` (only if `abort_on_example_error` needed)

### Patterns to Follow

- Preserve existing example functionality; only fix deprecated patterns
- Use the current idecomp API (class-based file reading, not deprecated `le_arquivo`/`escreve_arquivo`)
- Follow the plotly sphinx-gallery renderer pattern already configured in `conf.py`

### Pitfalls to Avoid

- Do NOT rewrite examples entirely; make minimal changes to fix compatibility
- Do NOT remove the `pio.renderers.default = "sphinx_gallery"` line from `conf.py`; it is required for plotly charts in gallery
- Do NOT change `sphinx_gallery_conf["examples_dirs"]` or `"gallery_dirs"` paths
- cfinterface import errors at example execution time are a known issue; use `abort_on_example_error = False` rather than trying to fix cfinterface

## Testing Requirements

### Unit Tests

- Not applicable

### Integration Tests

- Run `uv run sphinx-build -M html docs/source docs/build` and verify exit code 0
- Verify `docs/build/html/examples/index.html` exists and is non-empty

### E2E Tests

- Open the built gallery page in a browser and verify thumbnails and example pages render

## Dependencies

- **Blocked By**: ticket-006-migrate-sphinx-theme-to-furo.md
- **Blocks**: None (Epic 3 depends on Epic 2 being complete, but not specifically on this ticket)

## Effort Estimate

**Points**: 2
**Confidence**: Medium (cfinterface import issues may require investigation)
