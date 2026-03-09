# ticket-015 Reformat CHANGELOG to Keep a Changelog Standard

## Context

### Background

The current `CHANGELOG.md` uses an ad-hoc format: each version is a top-level `# vX.Y.Z` heading followed by an unstructured bullet list. Entries mix different types of changes (new features, bug fixes, dependency updates) without categorization. The file has no dates, no `[Unreleased]` section, and no inter-version comparison links. Reformatting to the Keep a Changelog standard improves readability and enables automated tooling.

### Relation to Epic

This is the third ticket in Epic 4 (Repository Polish). It is independent of all other tickets — no blocking dependencies.

### Current State

The file `/home/rogerio/git/idecomp/CHANGELOG.md` contains 89 lines covering 15 versions from v1.0.0 to v1.8.2. Each version uses a `# vX.Y.Z` heading with bullet points below. No dates, no categories, no `[Unreleased]` section.

Git tag dates are available for all versions:

- v1.8.2: no tag yet (unreleased on current branch)
- v1.8.1: 2026-02-04
- v1.8.0: 2026-02-02
- v1.7.3: 2025-12-29
- v1.7.2: 2025-12-29
- v1.7.1: 2025-01-22
- v1.7.0: 2025-01-10
- v1.6.0: 2024-10-04
- v1.5.0: 2024-08-16
- v1.4.0: 2024-04-22
- v1.3.0: 2024-02-23
- v1.2.0: 2024-02-05
- v1.1.1: 2024-01-04
- v1.1.0: 2023-12-29
- v1.0.1: 2023-12-21
- v1.0.0: 2023-12-21

## Specification

### Requirements

1. Reformat `/home/rogerio/git/idecomp/CHANGELOG.md` to follow the [Keep a Changelog](https://keepachangelog.com/) standard
2. Use Portuguese category names as `###` subheadings under each version:
   - **Adicionado** — new features and file support
   - **Corrigido** — bug fixes
   - **Modificado** — changes to existing functionality, dependency updates, refactors
   - **Removido** — removed features or deprecated items
   - **Depreciado** — newly deprecated features (if any)
3. Add a `## [Nao Publicado]` section at the top for unreleased changes (currently empty)
4. Version headings format: `## [X.Y.Z] - YYYY-MM-DD` using dates from git tags listed above
5. For v1.8.2, use `2026-02-04` as date (same as v1.8.1 release, since it was a hotfix with no separate tag yet)
6. Add GitHub compare links at the bottom of the file for each version pair
7. Preserve ALL existing content — only restructure, do not delete or rephrase entries
8. Add a file header with the project name and a reference to the Keep a Changelog standard

### Inputs/Props

- Current file: `/home/rogerio/git/idecomp/CHANGELOG.md` (89 lines)
- Git tag dates listed in Context section above
- GitHub repo URL: `https://github.com/rjmalves/idecomp`

### Outputs/Behavior

A reformatted CHANGELOG.md of approximately 140-180 lines with:

- Header block explaining the format
- `[Nao Publicado]` section
- Each version with date and categorized entries
- Compare links at the bottom

### Error Handling

Not applicable (static markdown file).

## Acceptance Criteria

- [ ] Given the file `/home/rogerio/git/idecomp/CHANGELOG.md`, when version headings are checked, then every version from v1.0.0 to v1.8.2 uses the format `## [X.Y.Z] - YYYY-MM-DD`
- [ ] Given the CHANGELOG version v1.7.0, when its entries are checked, then entries are categorized under `### Adicionado`, `### Corrigido`, and `### Modificado` subheadings (v1.7.0 has all three types)
- [ ] Given the CHANGELOG, when the top of the file is checked, then it contains a `## [Nao Publicado]` section before the first versioned section
- [ ] Given the bottom of the CHANGELOG, when compare links are checked, then there is a link `[X.Y.Z]: https://github.com/rjmalves/idecomp/compare/vPREV...vX.Y.Z` for each version pair
- [ ] Given the CHANGELOG entry count, when original entries are compared to reformatted entries, then no content has been deleted — all original bullet points are present (possibly reclassified under category headings)

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/CHANGELOG.md`
2. Add a header:

   ```markdown
   # Changelog

   Todas as mudancas relevantes deste projeto serao documentadas neste arquivo.

   O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

   ## [Nao Publicado]
   ```

3. For each existing version entry, classify every bullet point:
   - Entries starting with "Suporte a leitura/escrita", "Adicionado", "Novos dados" -> **Adicionado**
   - Entries starting with "Fix", "Correcao" -> **Corrigido**
   - Entries starting with "Atualiza", "Gestao do projeto", "Dependencia", "Uso de slots", "Padronizacao", "Simplifica", "Descontinuado" -> **Modificado**
   - Entries about deprecation ("Metodos le_arquivo e escreve_arquivo deprecados") -> **Depreciado**
4. Rewrite each version heading from `# vX.Y.Z` to `## [X.Y.Z] - YYYY-MM-DD` using the dates from git tags
5. Under each version heading, group entries by category with `###` subheadings
6. At the bottom, add compare links:
   ```markdown
   [Nao Publicado]: https://github.com/rjmalves/idecomp/compare/v1.8.2...HEAD
   [1.8.2]: https://github.com/rjmalves/idecomp/compare/v1.8.1...v1.8.2
   [1.8.1]: https://github.com/rjmalves/idecomp/compare/v1.8.0...v1.8.1

   ...
   [1.0.0]: https://github.com/rjmalves/idecomp/releases/tag/v1.0.0
   ```

### Key Files to Modify

- `/home/rogerio/git/idecomp/CHANGELOG.md` (reformat in place)

### Patterns to Follow

- Keep a Changelog standard: `## [version] - date` with `### Category` subheadings
- Portuguese category names: Adicionado, Corrigido, Modificado, Removido, Depreciado
- Compare links use GitHub `compare/vOLD...vNEW` URL format

### Pitfalls to Avoid

- Do NOT delete or rephrase any existing entry text — only move entries under category headings
- Do NOT add entries for pre-1.0 versions (they are not in the current CHANGELOG and adding them is out of scope)
- Do NOT use accented characters in section headings (e.g., use "Nao Publicado" not "Nao Publicado" — matching the project's heading convention of omitting accents)
- Do NOT invent dates — use only the git tag dates listed in the Context section

## Testing Requirements

### Unit Tests

Not applicable (static markdown file).

### Integration Tests

Not applicable.

### E2E Tests

Verify the CHANGELOG renders correctly on GitHub by visual inspection or local markdown preview.

## Dependencies

- **Blocked By**: None (independent)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: High
