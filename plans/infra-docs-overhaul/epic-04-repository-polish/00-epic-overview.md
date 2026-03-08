# Epic 4: Repository Polish

## Goal

Polish the repository's public-facing files: expand the README with badges and sections, create a CONTRIBUTING.md, reformat the CHANGELOG to Keep a Changelog standard, and update installation documentation.

## Scope

- Expand README.md with badges (CI, codecov, PyPI, license, docs), structured sections in Portuguese
- Create CONTRIBUTING.md with environment setup, quality tools, testing, code conventions, PR workflow
- Reformat CHANGELOG.md to Keep a Changelog format with Portuguese categories
- Update installation documentation for Python >= 3.10, pip primary + uv secondary

## Tickets

| Order | Ticket     | Title                                           | Points |
| ----- | ---------- | ----------------------------------------------- | ------ |
| 1     | ticket-013 | Expand README with Badges and Sections          | 2      |
| 2     | ticket-014 | Create CONTRIBUTING.md                          | 3      |
| 3     | ticket-015 | Reformat CHANGELOG to Keep a Changelog Standard | 2      |
| 4     | ticket-016 | Update Installation Documentation               | 2      |

## Dependencies

- ticket-013 depends on ticket-002 (needs final CI workflow name for badge URL)
- ticket-014 depends on ticket-001 and ticket-005 (references dep groups and pre-commit)
- ticket-015 is independent
- ticket-016 is independent

## Completion Criteria

- README.md displays CI, codecov, PyPI version, license, and docs badges
- CONTRIBUTING.md covers full contributor workflow with uv-based setup
- CHANGELOG.md follows Keep a Changelog format with Portuguese categories
- Installation docs reference Python >= 3.10 and show both pip and uv commands
