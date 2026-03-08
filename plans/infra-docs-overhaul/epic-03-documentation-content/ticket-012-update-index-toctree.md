# ticket-012 Update index.rst Toctree with Guias Section

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Update `docs/source/index.rst` to add a new "Guias" toctree section between the "Geral" and "Referencia" sections, linking to the architecture (`arquitetura.rst`), performance (`desempenho.rst`), and FAQ (`faq.rst`) pages created in tickets 008-010. This makes the new guide pages discoverable in the documentation sidebar.

## Anticipated Scope

- **Files likely to be modified**:
  - `docs/source/index.rst` (add new toctree section)
  - `docs/source/guias/` directory may need to be created if not done by earlier tickets
- **Key decisions needed**:
  - The exact placement of the "Guias" section in index.rst (between Geral and Referencia)
  - The order of pages within the Guias section (architecture first, then performance, then FAQ)
  - Whether to set a different maxdepth for the Guias section
- **Open questions**:
  - Should the "Geral" section's contribuicao.rst link be moved to the Guias section, or kept in Geral?
  - Should the Guias section caption be "Guias" or "Guias e Tutoriais"?

## Dependencies

- **Blocked By**: ticket-008-create-architecture-page.md, ticket-009-create-faq-page.md, ticket-010-create-performance-guide.md
- **Blocks**: None

## Effort Estimate

**Points**: 1
**Confidence**: Low (will be re-estimated during refinement)
