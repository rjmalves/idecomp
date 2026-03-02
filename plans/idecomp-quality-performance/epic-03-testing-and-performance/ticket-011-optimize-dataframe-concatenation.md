# ticket-011 Optimize DataFrame concatenation in BlockFile handlers

## Context

### Background

Three handler files in idecomp use an O(n^2) `pd.concat([df, df_estagio])` pattern inside `__concatena_blocos` loops. Each iteration creates a new DataFrame by concatenating the accumulator with the next block's data, which copies the entire accumulator on every iteration. The standard optimization is to collect all DataFrames into a list and call `pd.concat` once at the end (O(n) total copies). Additionally, `idecomp/decomp/modelos/mapcut.py` has three separate `pd.concat` in-loop occurrences in its property methods (`dados_tempo_viagem`, `dados_gnl`, `dados_custos`) that follow the same anti-pattern.

### Relation to Epic

This ticket addresses the "Optimize DataFrame creation in \_\_concatena_blocos pattern" goal of epic-03. It is a prerequisite for meaningful benchmark results in ticket-013, since the benchmark suite should measure performance after optimizations are applied.

### Current State

The O(n^2) `pd.concat` in-loop pattern exists in exactly 6 locations across 4 files:

1. `/home/rogerio/git/idecomp/idecomp/decomp/relato.py` line 90: `df = pd.concat([df, df_estagio], ignore_index=True)` inside `__concatena_blocos`
2. `/home/rogerio/git/idecomp/idecomp/decomp/custos.py` line 49: `df = pd.concat([df, df_estagio], ignore_index=True)` inside `__concatena_blocos`
3. `/home/rogerio/git/idecomp/idecomp/decomp/relgnl.py` line 56: `df = pd.concat([df, df_estagio], ignore_index=True)` inside `__concatena_blocos`
4. `/home/rogerio/git/idecomp/idecomp/decomp/modelos/mapcut.py` line 389-391: `df_tempo_viagem = pd.concat([df_tempo_viagem, ...])` in `dados_tempo_viagem`
5. `/home/rogerio/git/idecomp/idecomp/decomp/modelos/mapcut.py` line 438: `df_dados_gnl = pd.concat([df_dados_gnl, ...])` in `dados_gnl`
6. `/home/rogerio/git/idecomp/idecomp/decomp/modelos/mapcut.py` line 467: `df_custos = pd.concat([df_custos, ...])` in `dados_custos`

Note: `/home/rogerio/git/idecomp/idecomp/decomp/modelos/cortdeco.py` line 195 also has `pd.concat` in a loop, but that is in `SecaoDadosCortdeco.__le_arquivo` which constructs a DataFrame from binary file reading with complex index management. That case is structurally different (concatenating variable-sized chunks during binary file parsing) and should not be changed in this ticket.

## Specification

### Requirements

1. Rewrite `Relato.__concatena_blocos` to collect DataFrames into a list, then call `pd.concat(dfs, ignore_index=True)` once.
2. Rewrite `Custos.__concatena_blocos` to use the same collect-then-concat pattern.
3. Rewrite `Relgnl.__concatena_blocos` to use the same collect-then-concat pattern, preserving the `Estagio` column injection logic.
4. Rewrite `SecaoDadosMapcut.dados_tempo_viagem`, `dados_gnl`, and `dados_custos` properties to collect DataFrames into a list, then call `pd.concat` once.

### Inputs/Props

No interface changes. The methods receive the same inputs and return the same `Optional[pd.DataFrame]` types.

### Outputs/Behavior

All properties that call `__concatena_blocos` or the mapcut property methods must return DataFrames identical to the current implementation. The optimization is purely internal -- no change in API or output.

### Error Handling

Preserve existing `None` return behavior when no blocks are found. The edge case where `blocos` is empty must still return `None`.

### Out of Scope

- Changing `cortdeco.py` line 195 -- that is a binary file parsing loop, not a simple aggregation.
- Changing the `pd.concat([df_int, df_float], axis=1)` at `cortdeco.py` line 142 -- that is a column-wise join, not a row-wise accumulation.
- Deduplicating `__concatena_blocos` across files into a shared helper -- the three implementations have different signatures and slightly different logic (Relgnl adds an `Estagio` column, Custos filters with `isinstance(b, Block)`, Relato accepts `Union[T, List[T]]` with `indice_data`).

## Acceptance Criteria

- [ ] Given `idecomp/decomp/relato.py`, when `grep -n 'pd.concat\[' idecomp/decomp/relato.py` is run, then no match contains a loop accumulator pattern (i.e., no `df = pd.concat([df,` inside a `for` body).
- [ ] Given `idecomp/decomp/custos.py`, when `grep -n 'pd.concat\[' idecomp/decomp/custos.py` is run, then no match contains a loop accumulator pattern.
- [ ] Given `idecomp/decomp/relgnl.py`, when `grep -n 'pd.concat\[' idecomp/decomp/relgnl.py` is run, then no match contains a loop accumulator pattern.
- [ ] Given `idecomp/decomp/modelos/mapcut.py`, when the three properties `dados_tempo_viagem`, `dados_gnl`, `dados_custos` are inspected, then each collects DataFrames into a list and calls `pd.concat` exactly once outside the loop.
- [ ] Given the full test suite, when `pytest -x -q` is run, then all 310+ tests pass with no regressions.

## Implementation Guide

### Suggested Approach

For each `__concatena_blocos` method, apply this transformation:

**Before (relato.py pattern):**

```python
def __concatena_blocos(self, blocos, indice_data=None):
    df = None
    if not isinstance(blocos, list):
        blocos = [blocos]
    for b in blocos:
        df_estagio = b.data if indice_data is None else b.data[indice_data]
        if df is None:
            df = df_estagio
        else:
            df = pd.concat([df, df_estagio], ignore_index=True)
    if df is not None:
        return df
    return None
```

**After:**

```python
def __concatena_blocos(self, blocos, indice_data=None):
    if not isinstance(blocos, list):
        blocos = [blocos]
    dfs = [
        b.data if indice_data is None else b.data[indice_data]
        for b in blocos
    ]
    dfs = [df for df in dfs if df is not None]
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    return None
```

For `relgnl.py`, the `Estagio` column logic must be preserved. Collect `(i, df)` tuples, then assemble:

```python
def __concatena_blocos(self, bloco):
    dfs = []
    for i, b in enumerate(self.data.of_type(bloco)):
        if not isinstance(b, Block):
            continue
        df_estagio = b.data.copy()
        df_estagio["Estagio"] = i + 1
        dfs.append(df_estagio)
    if dfs:
        df = pd.concat(dfs, ignore_index=True)
        cols = [c for c in df.columns if c != "Estagio"]
        return df[["Estagio"] + cols]
    return None
```

For `mapcut.py` properties, replace `df_X = pd.DataFrame()` + `df_X = pd.concat([df_X, ...])` with a `dfs: list[pd.DataFrame] = []` + `dfs.append(pd.DataFrame(...))` + `pd.concat(dfs).reset_index(drop=True)` at the end.

### Key Files to Modify

- `idecomp/decomp/relato.py` -- rewrite `__concatena_blocos` (line 79-93)
- `idecomp/decomp/custos.py` -- rewrite `__concatena_blocos` (line 30-52)
- `idecomp/decomp/relgnl.py` -- rewrite `__concatena_blocos` (line 35-61)
- `idecomp/decomp/modelos/mapcut.py` -- rewrite `dados_tempo_viagem` (line 340-392), `dados_gnl` (line 406-440), `dados_custos` (line 443-468)

### Patterns to Follow

- Use list comprehension to collect DataFrames where possible (relato, custos).
- Use explicit `for` loop with `.append()` when additional per-iteration logic is needed (relgnl, mapcut).
- Preserve the `ignore_index=True` argument on `pd.concat` for relato/custos/relgnl.
- Preserve `reset_index(drop=True)` for mapcut properties.
- Maintain all existing type annotations (`IO[Any]`, `Optional[pd.DataFrame]`, etc.).

### Pitfalls to Avoid

- The `relgnl.py` implementation adds a column `col_estagio` separately and reorders columns at the end. The refactored version must produce the same column order (`["Estagio"] + original_cols`).
- The `custos.py` implementation filters blocks with `isinstance(b, Block)` -- this filter must be preserved in the list comprehension.
- Do NOT change the return type or the `None` return behavior when no blocks are found.
- Do NOT modify `cortdeco.py` -- its concat pattern is structurally different.

## Testing Requirements

### Unit Tests

No new tests needed. The existing test suite covers all properties that call `__concatena_blocos` (e.g., `test_relato.py`, `test_custos.py`, `test_relgnl.py`, `test_mapcut.py`). Passing the full suite is the verification.

### Integration Tests

Not applicable.

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-006-enable-mypy-strict-decomp.md (type annotations must be in place -- already completed)
- **Blocks**: ticket-013-create-benchmark-suite.md

## Effort Estimate

**Points**: 2
**Confidence**: High
