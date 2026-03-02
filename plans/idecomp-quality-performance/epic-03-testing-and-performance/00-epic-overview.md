# Epic 03: Testing and Performance

## Goals

1. Add round-trip tests for handlers that support write() (hidr, postos, vazoes, dadger, dadgnl)
2. Optimize DataFrame creation in Relato's `__concatena_blocos` pattern (O(n^2) concat)
3. Add pytest-xdist for parallel test execution
4. Create a benchmark baseline for read performance

## Scope

- **In scope**: Round-trip tests, concatenation optimization, parallel testing, benchmark baseline
- **Out of scope**: New handler implementations, API changes, documentation

## Tickets

| Ticket     | Title                                                  | Points |
| ---------- | ------------------------------------------------------ | ------ |
| ticket-010 | Add round-trip tests for decomp handlers               | 3      |
| ticket-011 | Optimize DataFrame concatenation in BlockFile handlers | 2      |
| ticket-012 | Add pytest-xdist and optimize test execution           | 2      |
| ticket-013 | Create benchmark suite for read performance            | 2      |

## Success Criteria

- Round-trip tests exist for all handlers with working write() methods
- `__concatena_blocos` uses collect-then-concat pattern (no O(n^2) loop)
- `pytest -n auto` runs successfully
- Benchmark baseline documented in `benchmarks/`
