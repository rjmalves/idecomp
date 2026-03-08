# ticket-006 Migrate Sphinx Theme to Furo

## Context

### Background

idecomp's documentation uses `sphinx-rtd-theme`, which lacks dark mode and has a dated appearance. The inewave overhaul migrated to Furo, a modern Sphinx theme with built-in dark/light mode toggle and clean typography. idecomp should adopt the same theme for consistency across sibling projects.

### Relation to Epic

First ticket of Epic 2. Depends on ticket-001 which replaces `sphinx-rtd-theme` with `furo` in the docs dependency group. Blocks ticket-007 (gallery examples must be verified after theme change).

### Current State

File: `/home/rogerio/git/idecomp/docs/source/conf.py` (129 lines)

- `html_theme = "sphinx_rtd_theme"`
- `extensions` list includes `"sphinx_rtd_theme"`
- `html_theme_options` configured for RTD: `logo_only`, `collapse_navigation`, `sticky_navigation`, `navigation_depth`, `includehidden`, `titles_only`
- `pygments_style = "sphinx"`
- `html_logo = "_static/logo_idecomp_svg.svg"`
- Existing extensions: autosummary, autodoc, intersphinx, mathjax, viewcode, githubpages, sphinx_gallery, numpydoc

## Specification

### Requirements

1. Replace `html_theme = "sphinx_rtd_theme"` with `html_theme = "furo"`
2. Remove `"sphinx_rtd_theme"` from the `extensions` list (Furo is not loaded as an extension)
3. Replace `html_theme_options` with Furo-specific options:
   ```python
   html_theme_options = {
       "light_css_variables": {
           "color-brand-primary": "#2962ff",
           "color-brand-content": "#2962ff",
       },
       "dark_css_variables": {
           "color-brand-primary": "#5c8aff",
           "color-brand-content": "#5c8aff",
       },
       "sidebar_hide_name": True,
   }
   ```
4. Change `pygments_style` to `"friendly"` and add `pygments_dark_style = "monokai"` for dark mode code blocks
5. Keep `html_logo` pointing to the existing SVG logo
6. Keep all other extensions unchanged (autosummary, autodoc, intersphinx, mathjax, viewcode, githubpages, sphinx_gallery, numpydoc)
7. Remove the `from typing import List` import if no longer needed (check if `exclude_patterns: List[str]` can use `list[str]` since Python >= 3.10)

### Inputs/Props

- File: `/home/rogerio/git/idecomp/docs/source/conf.py`

### Outputs/Behavior

- `uv run sphinx-build -M html docs/source docs/build` produces documentation with Furo theme
- The site has a dark/light mode toggle button in the header
- Code blocks use friendly pygments in light mode and monokai in dark mode
- The idecomp SVG logo appears in the sidebar

### Error Handling

- If Furo is not installed, sphinx-build fails with a clear error about missing theme
- If the logo path is wrong, Furo shows a warning but builds successfully

## Acceptance Criteria

- [ ] Given the updated `conf.py`, when searching for `sphinx_rtd_theme`, then the string does not appear anywhere in the file (not in `extensions`, not in `html_theme`, not in imports)
- [ ] Given the updated `conf.py`, when inspecting `html_theme`, then it equals `"furo"`
- [ ] Given the updated `conf.py`, when inspecting `pygments_style` and `pygments_dark_style`, then they equal `"friendly"` and `"monokai"` respectively
- [ ] Given the updated `conf.py`, when inspecting `html_theme_options`, then it contains `"dark_css_variables"` and `"sidebar_hide_name"` keys (Furo-specific options, not RTD options)
- [ ] Given a virtual environment with the docs extras installed, when running `uv run sphinx-build -M html docs/source docs/build`, then the build completes without errors and `docs/build/html/index.html` contains `furo` in its HTML source

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/docs/source/conf.py`
2. Remove `"sphinx_rtd_theme"` from the `extensions` list (line 49)
3. Change `html_theme = "sphinx_rtd_theme"` to `html_theme = "furo"` (line 89)
4. Replace the entire `html_theme_options` dict with Furo options
5. Change `pygments_style = "sphinx"` to `pygments_style = "friendly"` (line 81)
6. Add `pygments_dark_style = "monokai"` after the pygments_style line
7. Optionally update `exclude_patterns: List[str] = []` to `exclude_patterns: list[str] = []` and remove the `from typing import List` import
8. Run `uv run sphinx-build -M html docs/source docs/build` to verify

### Key Files to Modify

- `/home/rogerio/git/idecomp/docs/source/conf.py`

### Patterns to Follow

- Match the inewave Furo configuration for consistency
- Keep all existing extensions except `sphinx_rtd_theme`
- Furo does not need to be listed in extensions; it is configured purely via `html_theme`

### Pitfalls to Avoid

- Do NOT remove `sphinx.ext.githubpages` from extensions (it creates the `.nojekyll` file needed for GitHub Pages)
- Do NOT remove `html_logo` -- Furo supports logos via the same `html_logo` config
- Do NOT add Furo to extensions -- it is a theme, not an extension; adding it causes a warning
- The `html_theme_options` keys are completely different between RTD and Furo; do not try to adapt the old keys

## Testing Requirements

### Unit Tests

- Not applicable (configuration file)

### Integration Tests

- Run `uv run sphinx-build -M html docs/source docs/build` and verify it exits with code 0
- Verify `docs/build/html/index.html` exists and references Furo CSS

### E2E Tests

- Open the built docs locally and verify the dark mode toggle works

## Dependencies

- **Blocked By**: ticket-001-modernize-pyproject-toml.md (furo must be in the docs dependency group)
- **Blocks**: ticket-007-update-sphinx-gallery-examples.md

## Effort Estimate

**Points**: 3
**Confidence**: High
