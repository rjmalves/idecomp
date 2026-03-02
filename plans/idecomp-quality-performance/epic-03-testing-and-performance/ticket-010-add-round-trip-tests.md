# ticket-010 Add round-trip tests for decomp handlers

> **[OUTLINE]** This ticket requires refinement before execution.
> It will be refined with learnings from earlier epics.

## Objective

Add round-trip tests (read -> write -> read, verify data equality) for all decomp handlers that have working write() methods. From inewave learnings, write() must be audited BEFORE planning which handlers get round-trip tests -- many Block.write() methods raise NotImplementedError. The handlers known to support write are: Hidr, Postos, Vazoes, Dadger, Dadgnl. However, this must be verified by grepping for NotImplementedError in block write methods.

## Anticipated Scope

- **Files likely to be modified**: `tests/decomp/test_hidr.py`, `tests/decomp/test_postos.py`, `tests/decomp/test_vazoes.py`, `tests/decomp/test_dadger.py`, `tests/decomp/test_dadgnl.py`, possibly new test files
- **Key decisions needed**: Which handlers actually support write() at the block/section level (not just the handler level)? Should binary files use tempfile pattern or mock_open?
- **Open questions**:
  - Does `Cortdeco.write()` work end-to-end or does `SecaoDadosCortdeco.write()` raise NotImplementedError?
  - Does `Hidr.write()` produce byte-identical output? Or just semantically equivalent?
  - Should round-trip tests for binary files (vazoes, cortdeco, mapcut, postos, hidr) use `tempfile.NamedTemporaryFile` pattern from inewave?

## Dependencies

- **Blocked By**: ticket-003-fix-identity-test-verify-suite.md (need all tests passing first)
- **Blocks**: None

## Effort Estimate

**Points**: 3
**Confidence**: Low (will be re-estimated during refinement)
