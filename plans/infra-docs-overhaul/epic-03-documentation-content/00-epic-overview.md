# Epic 3: Documentation Content Expansion

## Goal

Expand the idecomp documentation with three new guide pages (architecture, FAQ, performance), improve the API reference with autosummary blocks, and update the index.rst toctree. All content in Brazilian Portuguese.

## Scope

- Create `arquitetura.rst` page describing idecomp's package structure, cfinterface framework, and data flow
- Create `faq.rst` page with 15+ frequently asked questions about DECOMP file handling
- Create `desempenho.rst` page with performance tips, import times, batch optimization
- Add autosummary blocks to module index RSTs for decomp/ and libs/
- Update `index.rst` toctree with new "Guias" section

## Tickets

| Order | Ticket     | Title                                         | Points |
| ----- | ---------- | --------------------------------------------- | ------ |
| 1     | ticket-008 | Create Architecture Documentation Page        | 3      |
| 2     | ticket-009 | Create FAQ Documentation Page                 | 3      |
| 3     | ticket-010 | Create Performance Guide Page                 | 3      |
| 4     | ticket-011 | Improve API Reference with Autosummary Blocks | 2      |
| 5     | ticket-012 | Update index.rst Toctree with Guias Section   | 1      |

## Dependencies

- ticket-008 through ticket-011 are independent of each other
- ticket-012 depends on ticket-008, ticket-009, ticket-010 (needs the new pages to exist)
- All tickets depend on Epic 2 completion (Furo theme must be in place)

## Completion Criteria

- Three new .rst files exist in `docs/source/guias/`
- Sphinx build succeeds with no warnings for the new pages
- API reference pages show autosummary tables with class/method listings
- index.rst toctree includes the "Guias" section
