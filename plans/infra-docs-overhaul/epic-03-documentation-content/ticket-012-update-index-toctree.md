# ticket-012 Update index.rst Toctree with Guias Section

## Context

### Background

Tickets 008, 009, and 010 create three new guide pages (`arquitetura.rst`, `faq.rst`, `desempenho.rst`) in `docs/source/guias/`. These pages are not yet linked from the main `index.rst` toctree, so they are undiscoverable in the documentation sidebar. This ticket adds a new "Guias" toctree section to `index.rst` to make them visible and navigable.

### Relation to Epic

This is the final ticket in Epic 3. It depends on tickets 008, 009, and 010 being complete (the referenced `.rst` files must exist for the toctree to resolve without warnings).

### Current State

The file `docs/source/index.rst` has 3 toctree sections in this order:

1. **Apresentacao** (maxdepth 3): `apresentacao/apresentacao.rst`
2. **Geral** (maxdepth 3): `geral/instalacao`, `geral/tutorial`, `examples/index.rst`, `geral/contribuicao`
3. **Referencia** (maxdepth 2): `referencia/decomp/index.rst`, `referencia/libs/index.rst`

After the toctrees, there is a `:ref:\`genindex\`` link.

## Specification

### Requirements

1. Add a new `.. toctree::` section to `docs/source/index.rst` between the "Geral" and "Referencia" sections.
2. The new section must use:
   - `:caption: Guias`
   - `:maxdepth: 2`
3. The toctree entries must be, in this order:
   - `guias/arquitetura`
   - `guias/desempenho`
   - `guias/faq`
4. Do NOT modify the existing "Apresentacao", "Geral", or "Referencia" toctree sections.
5. Do NOT move `geral/contribuicao` to the Guias section -- it stays in "Geral".

### Inputs/Props

- No runtime inputs. Modification to an existing RST file.

### Outputs/Behavior

- The Furo sidebar renders a "Guias" section between "Geral" and "Referencia", containing three linked pages: Arquitetura, Desempenho, FAQ.

### Error Handling

- Not applicable (static documentation content).

## Acceptance Criteria

- [ ] Given the file `docs/source/index.rst` is opened, when inspecting toctree sections, then there are exactly 4 toctree blocks with captions in this order: "Apresentacao", "Geral", "Guias", "Referencia".
- [ ] Given the "Guias" toctree is present, when inspecting its entries, then it contains exactly 3 entries: `guias/arquitetura`, `guias/desempenho`, `guias/faq`.
- [ ] Given all guide pages exist (from tickets 008-010), when running `uv run sphinx-build -M html docs/source docs/build`, then the build exits with code 0 with no warnings about missing toctree references.
- [ ] Given the build succeeds, when opening `docs/build/html/index.html`, then the sidebar shows a "Guias" section with 3 page links.

## Implementation Guide

### Suggested Approach

1. Open `docs/source/index.rst`.
2. After the "Geral" toctree block (which ends with `geral/contribuicao`) and before the "Referencia" toctree block, insert:

   ```rst
   .. toctree::
      :caption: Guias
      :maxdepth: 2

      guias/arquitetura
      guias/desempenho
      guias/faq
   ```

3. Ensure there is a blank line before and after the new toctree block.
4. Verify locally: `uv run sphinx-build -M html docs/source docs/build`.

### Key Files to Modify

- `docs/source/index.rst` (add ~7 lines for the new toctree section)

### Patterns to Follow

- Match the existing toctree format: `:caption:` on its own line, `:maxdepth:` on the next, blank line, then entries with 3-space indent.
- Use relative paths without `.rst` extension, matching the convention used in the "Geral" section (e.g., `geral/instalacao` not `geral/instalacao.rst`).

### Pitfalls to Avoid

- Do NOT use `.rst` extension in toctree entries for the guias pages -- the existing "Geral" entries omit extensions (`geral/instalacao`, `geral/tutorial`, `geral/contribuicao`), so follow that convention. Note that `apresentacao/apresentacao.rst` and `referencia/*/index.rst` do include extensions -- both styles work, but within the same file, consistency with "Geral" is preferred for new entries.
- Do NOT modify any existing toctree sections.
- Do NOT reorder the 3 existing toctree sections.

## Testing Requirements

### Unit Tests

- Not applicable (documentation content).

### Integration Tests

- Run `uv run sphinx-build -M html docs/source docs/build` and verify exit code 0.
- Verify the built `docs/build/html/index.html` contains the text "Guias" as a sidebar caption.

### E2E Tests

- Not applicable.

## Dependencies

- **Blocked By**: ticket-008-create-architecture-page.md, ticket-009-create-faq-page.md, ticket-010-create-performance-guide.md
- **Blocks**: None

## Effort Estimate

**Points**: 1
**Confidence**: High
