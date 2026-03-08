# Epic 02 Learnings: Sphinx Modernization

**Epic**: epic-02-sphinx-modernization
**Date**: 2026-03-08
**Tickets**: ticket-006, ticket-007
**Files changed**: `docs/source/conf.py` only (ticket-006); no files changed (ticket-007)

---

## Patterns Established

- **Furo theme is configured exclusively via `html_theme`, not `extensions`**: Unlike `sphinx-rtd-theme`, Furo must NOT appear in the `extensions` list. Adding it there causes a warning. The only required change is `html_theme = "furo"` plus the `html_theme_options` dict. See `/home/rogerio/git/idecomp/docs/source/conf.py` lines 43-54.

- **Dual pygments style pattern for dark/light mode**: Furo requires two separate pygments settings: `pygments_style = "friendly"` for light mode and `pygments_dark_style = "monokai"` for dark mode. A single `pygments_style` setting (as with RTD) leaves dark mode code blocks unstyled. See `/home/rogerio/git/idecomp/docs/source/conf.py` lines 39-40.

- **`sidebar_hide_name` with SVG logo**: When an `html_logo` is set, `"sidebar_hide_name": True` in `html_theme_options` prevents the project name from appearing redundantly next to the logo in the sidebar. Without it, both the logo and the text name display together. See `/home/rogerio/git/idecomp/docs/source/conf.py` lines 53.

- **Brand color split into `light_css_variables` and `dark_css_variables`**: Furo uses CSS variable overrides to apply brand colors per mode. The pattern uses `"color-brand-primary"` and `"color-brand-content"` keys — primary for interactive elements, content for text/links. The light and dark values use different blue shades (`#2962ff` vs `#5c8aff`) to maintain contrast ratios in each mode. See `/home/rogerio/git/idecomp/docs/source/conf.py` lines 44-53.

- **`from typing import List` replaced by built-in `list[str]`**: The original `conf.py` used `from typing import List` for the `exclude_patterns` type annotation. Since idecomp targets Python >= 3.10, this was updated to the built-in `list[str]` syntax and the import removed. See `/home/rogerio/git/idecomp/docs/source/conf.py` line 36.

- **Example scripts use current class-based API (`ClassName.read()`) with no deprecated patterns**: All 4 example scripts in `/home/rogerio/git/idecomp/examples/` (`plot_dadger.py`, `plot_dec_oper_sist.py`, `plot_edit_dadger.py`, `plot_relato.py`) already use the modern API. No `le_arquivo` or `escreve_arquivo` calls were found. The gallery was already clean before ticket-007 ran.

- **`pio.renderers.default = "sphinx_gallery"` is pre-existing and theme-agnostic**: The plotly renderer configuration at the top of `conf.py` (lines 4-6) predates the Furo migration and requires no changes when switching themes. It is a sphinx-gallery-specific setting, not an RTD-specific one.

---

## Architectural Decisions

- **conf.py is the single point of control for theme, pygments, and gallery**: The entire epic's scope was one file. No other files (pyproject.toml, CI workflows, example scripts) required modification. This confirms the epic-01 assessment that `furo` was already in the `docs` dependency group, and the theme switch is purely a `conf.py` concern.

- **`abort_on_example_error = False` was NOT needed**: The ticket spec anticipated potential cfinterface import errors during gallery execution and listed this as a fallback. In practice, all 4 examples executed without error — the examples use idecomp's own API (not cfinterface directly), and the mock data files in `/home/rogerio/git/idecomp/examples/decomp/` are sufficient for clean execution. The fallback option was researched but not applied.

- **RTD `html_theme_options` keys are wholly incompatible with Furo**: The original conf.py had RTD-specific keys (`logo_only`, `collapse_navigation`, `sticky_navigation`, `navigation_depth`, `includehidden`, `titles_only`). These were completely replaced, not adapted. The two themes have no overlapping option keys. Any future theme migration must treat `html_theme_options` as a clean replacement, not a patch.

- **`sphinx.ext.githubpages` retained**: This extension creates the `.nojekyll` file required for GitHub Pages to serve the docs correctly. It is not RTD-specific. Removing it when switching themes would silently break the Pages deployment. It stays in `extensions` regardless of theme.

---

## Files & Structures Created

- `/home/rogerio/git/idecomp/docs/source/conf.py` — Updated in place: Furo theme, dual pygments styles, Furo `html_theme_options`, `sphinx_rtd_theme` removed from extensions, `from typing import List` replaced with built-in `list[str]`. No other files were modified in this epic.

---

## Conventions Adopted

- **Theme options must be a full replacement, never a patch**: When switching Sphinx themes, the `html_theme_options` dict must be completely rewritten for the new theme. Keeping any keys from the previous theme's dict causes Sphinx to emit warnings about unknown options (RTD keys are silently ignored by Furo, but this creates noise in build logs).

- **Example mock data lives in `examples/decomp/`**: The 3 mock data files (`dadger.rv0`, `dec_oper_sist.csv`, `relato.rv0`) live at `/home/rogerio/git/idecomp/examples/decomp/`. Example scripts reference them via relative path `"./decomp/<filename>"`. This directory must be preserved and the files kept in sync with the format expected by the examples. Any new example script must place its mock data here.

- **sphinx-gallery conf keys are stable and must not be changed**: The `sphinx_gallery_conf` dict at `/home/rogerio/git/idecomp/docs/source/conf.py` lines 72-76 uses `examples_dirs`, `gallery_dirs`, and `backreferences_dir` paths that are consistent with the project's directory layout. These paths must not be altered in future tickets — the gallery output goes to `docs/build/html/examples/` and `docs/source/gen_modules/generated/`.

- **Brand colors from inewave sibling project are used verbatim**: The Furo CSS variable values (`#2962ff` / `#5c8aff`) match the inewave project's Furo configuration. This is an explicit cross-project consistency choice. Future theming work should consult the inewave conf.py before introducing any color changes.

---

## Surprises & Deviations

- **ticket-007 required zero code changes**: The ticket was allocated 2 points with medium confidence, anticipating potential API deprecation fixes or cfinterface fallback configuration. In practice, all 4 example scripts were already using the current API, the mock data was complete, and the gallery built cleanly without `abort_on_example_error`. The verification step was still valuable — it confirmed the gallery is healthy — but the ticket was a pure audit, not an implementation.

- **conf.py was already partially modernized before the plan**: The original `conf.py` (as of commit `f84091f`) had the full scaffold: autosummary, intersphinx, sphinx-gallery, numpydoc, plotly renderer, SVG logo. The only gaps were the RTD theme, `sphinx_rtd_theme` in extensions, the legacy `pygments_style = "sphinx"`, no dark pygments style, and `from typing import List`. Epic 2 was a targeted diff, not a rewrite.

- **Git history shows conf.py was not changed in the epic-01 commit**: The epic-01 completion commit (`e20d968`) included `pyproject.toml` and CI workflow changes but did not touch `conf.py`. The furo dependency was added to `pyproject.toml` in that commit, but the theme activation in `conf.py` was deferred to epic-02 as designed. This confirms the correct sequencing.

- **No `html_logo` change needed**: The ticket spec noted the logo path must be preserved. The original `html_logo = "_static/logo_idecomp_svg.svg"` was already set before this epic and Furo supports the same `html_logo` config key as RTD. No path changes were needed.

---

## Recommendations for Future Epics

- **Epic 3 (Documentation Content)**: New RST pages added to `docs/source/` will render with the Furo theme. Use `.. code-block:: python` with explicit language hints — Furo's monokai dark style is optimized for syntax-highlighted blocks. Avoid using `::` (anonymous code blocks) since pygments will not apply syntax coloring. Build locally with `uv sync --extra docs && uv run sphinx-build -M html docs/source docs/build` before finalizing any RST content.

- **Epic 3 (autosummary)**: The `autosummary_generate = True` setting at `/home/rogerio/git/idecomp/docs/source/conf.py` line 30 auto-generates stub pages from `.. autosummary::` directives. When ticket-011 improves the API reference, ensure that `_templates/autosummary/` contains the correct templates. The `numpydoc_show_class_members = False` setting (line 61) suppresses member tables in class pages — adjust this if the improved autosummary should show members inline.

- **Epic 3 (intersphinx)**: The intersphinx mapping at `/home/rogerio/git/idecomp/docs/source/conf.py` lines 62-70 includes `cfinterface` pointing to `https://rjmalves.github.io/cfinterface/`. Any new documentation page that cross-references cfinterface types can use `:class:`cfinterface.SomeClass`` and it will resolve. Do not add cfinterface types to the API reference directly.

- **Epic 4 (CONTRIBUTING.md)**: When documenting the local docs build process, the command is `uv sync --extra docs && uv run sphinx-build -M html docs/source docs/build`. The built output at `docs/build/html/index.html` can be opened directly. The gallery examples take significant time to execute on first build but are cached in `docs/source/examples/` on subsequent runs.

- **No future sphinx-rtd-theme work needed**: The string `sphinx_rtd_theme` no longer appears anywhere in `docs/source/conf.py`. Any future search for this string returning results would indicate a regression. The pyproject.toml `docs` extra group (added in epic-01) lists `furo` as the theme package — do not re-add `sphinx-rtd-theme`.
