# Epic 2: Sphinx Modernization

## Goal

Replace the sphinx-rtd-theme with Furo for a modern documentation appearance with dark mode support, and ensure all sphinx-gallery examples build correctly with the new theme.

## Scope

- Migrate Sphinx theme from sphinx-rtd-theme to Furo
- Configure dark mode with monokai pygments style
- Update conf.py extensions and theme options
- Review and fix sphinx-gallery example scripts for compatibility

## Tickets

| Order | Ticket     | Title                                                 | Points |
| ----- | ---------- | ----------------------------------------------------- | ------ |
| 1     | ticket-006 | Migrate Sphinx Theme to Furo                          | 3      |
| 2     | ticket-007 | Update Sphinx-Gallery Examples for Furo Compatibility | 2      |

## Dependencies

- ticket-006 depends on ticket-001 (needs docs dependency group with furo instead of sphinx-rtd-theme)
- ticket-007 depends on ticket-006 (needs Furo theme configured)

## Completion Criteria

- `uv run sphinx-build -M html docs/source docs/build` succeeds with Furo theme
- Documentation site renders with dark mode toggle
- All 4 example scripts in `/examples/` build successfully in the gallery
- No sphinx-rtd-theme references remain in the codebase
