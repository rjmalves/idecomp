# Code Reviewer Memory — idecomp project

## Project Conventions

- Stack: Python, pandas, numpy, cfinterface framework
- Lint: ruff (default config, F401 not enabled by default)
- Type check: mypy strict on idecomp.decomp._ and idecomp.libs._
- Test framework: pytest + mock_open patterns for round-trip tests
- Python >= 3.10 (lowercase generics like `list[str]` are fine)
- No `from __future__ import annotations` — not used anywhere in codebase

## Confirmed Patterns

### Round-trip test mock_open extraction

cfinterface TextualRepository calls `open(path, "w", encoding=...)` then `.close()` directly
(no context manager overhead in mock_calls). So mock_calls structure is:

- [0] call(path, mode, encoding=...) <- open
- [1..n-2] call().write(...) <- writes
- [n-1] call().close()

`range(1, len(chamadas) - 1)` correctly extracts just the write calls for SectionFile/BlockFile.
`range(2, len(chamadas) - 1)` is used for RegisterFile (dadger, dadgnl) — likely a header/encoding
write at index 1 that should be skipped.

### pd.concat empty-list guard pattern

The safe pattern (used in relato.py, custos.py, relgnl.py):

```python
dfs = [...]
if dfs:
    return pd.concat(dfs, ignore_index=True)
return None
```

The UNSAFE pattern (found in mapcut modelos after refactor):

```python
dfs = [...]
return pd.concat(dfs).reset_index(drop=True)  # raises ValueError when dfs is []
```

pd.concat([]) raises `ValueError: No objects to concatenate` in pandas >= 2.x.

### PEP 562 lazy imports (decomp/**init**.py)

`globals()[name] = value` caching in `__getattr__` is the standard PEP 562 idiom.
`__dir__` returning `__all__` is minimal but documented and acceptable.

## Common False Positives to Avoid

- `type: ignore[override]` on cfinterface Block/Section read/write methods: intentional,
  cfinterface base signature returns bool but subclasses return None.
- `type: ignore[assignment]` in dadger.py: attribute types from cfinterface registers
  are not known to mypy; suppressing is correct.
- Redundant mypy overrides (e.g., `idecomp.decomp.modelos.blocos.*` after `idecomp.decomp.modelos.*`):
  harmless, not a bug.
