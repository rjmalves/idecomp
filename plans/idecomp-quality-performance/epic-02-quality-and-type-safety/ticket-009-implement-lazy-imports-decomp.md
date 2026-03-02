# ticket-009 Implement lazy imports for decomp module

## Context

### Background

`idecomp/decomp/__init__.py` eagerly imports all 43 handler classes at package load time. This means `import idecomp` triggers importing all handler files, their model files, and transitively cfinterface, pandas, and numpy. The PEP 562 lazy import pattern (`__getattr__` + `__dir__`) can defer these imports until the specific handler is first accessed, reducing import time for users who only need a subset of handlers.

### Relation to Epic

This is the final ticket in Epic 02. It improves runtime performance through lazy loading while maintaining full backward compatibility for `from idecomp.decomp import Dadger` style imports.

### Current State

- `idecomp/decomp/__init__.py` has 43 eager import statements (lines 3-43)
- `idecomp/__init__.py` has `from . import decomp` which triggers all 43 imports
- `idecomp/libs/__init__.py` has only 1 import (`UsinasHidreletricas`) -- not worth converting

## Specification

### Requirements

1. Replace the 43 eager imports in `idecomp/decomp/__init__.py` with PEP 562 lazy import pattern:
   - A `_LAZY_IMPORTS: dict[str, str]` dictionary mapping class names to module paths
   - A `__all__` list generated from `sorted(_LAZY_IMPORTS.keys())`
   - A `def __getattr__(name: str) -> Any:` function that imports on first access and caches via `globals()[name] = value`
   - A `def __dir__() -> list[str]: return __all__` function
2. All existing import patterns must continue to work:
   - `from idecomp.decomp import Dadger`
   - `import idecomp.decomp; idecomp.decomp.Dadger`
   - `from idecomp.decomp import *`
3. `idecomp/libs/__init__.py` is NOT converted (only 1 import, overhead negligible)
4. After conversion, all 310 tests must pass
5. The `__getattr__` function must have `-> Any` return annotation for mypy strict compatibility

### Inputs/Props

- File: `/home/rogerio/git/idecomp/idecomp/decomp/__init__.py`

### Outputs/Behavior

- `idecomp/decomp/__init__.py` uses PEP 562 lazy import pattern
- `dir(idecomp.decomp)` returns all 43 class names
- First access to any handler class triggers its import and caches it
- Subsequent accesses bypass `__getattr__` entirely

### Error Handling

- If a class name is not in `_LAZY_IMPORTS`, `__getattr__` raises `AttributeError(f"module 'idecomp.decomp' has no attribute '{name}'")`

## Acceptance Criteria

- [ ] Given `idecomp/decomp/__init__.py`, when opened, then it contains `_LAZY_IMPORTS` dict with 43 entries
- [ ] Given `idecomp/decomp/__init__.py`, when opened, then it contains `def __getattr__(name: str) -> Any:` and `def __dir__() -> list[str]:`
- [ ] Given the command `python -c "from idecomp.decomp import Dadger; print(type(Dadger))"`, when executed, then it prints `<class 'idecomp.decomp.dadger.Dadger'>`
- [ ] Given the command `python -c "import idecomp.decomp; print(len(dir(idecomp.decomp)))"`, when executed, then the output includes all 43 handler names
- [ ] Given the command `pytest -v`, when executed, then all 310 tests pass

## Implementation Guide

### Suggested Approach

Replace the contents of `idecomp/decomp/__init__.py` with:

```python
from typing import Any
import importlib

_LAZY_IMPORTS: dict[str, str] = {
    "Arquivos": ".arquivos",
    "AvlCortesFpha": ".avl_cortesfpha_dec",
    "AvlTurbMax": ".avl_turb_max",
    "Caso": ".caso",
    "Cortdeco": ".cortdeco",
    "Custos": ".custos",
    "Dadger": ".dadger",
    "Dadgnl": ".dadgnl",
    "DecAvlEvap": ".dec_avl_evap",
    "DecCortesEvap": ".dec_cortes_evap",
    "DecDesvFpha": ".dec_desvfpha",
    "DecEcoCotajus": ".dec_eco_cotajus",
    "DecEcoDiscr": ".dec_eco_discr",
    "DecEcoEvap": ".dec_eco_evap",
    "DecEcoQlat": ".dec_eco_qlat",
    "DecEstatEvap": ".dec_estatevap",
    "DecEstatFpha": ".dec_estatfpha",
    "DecFcfCortes": ".dec_fcf_cortes",
    "DecOperEvap": ".dec_oper_evap",
    "DecOperGnl": ".dec_oper_gnl",
    "DecOperInterc": ".dec_oper_interc",
    "DecOperRee": ".dec_oper_ree",
    "DecOperRheSoft": ".dec_oper_rhesoft",
    "DecOperSist": ".dec_oper_sist",
    "DecOperUsie": ".dec_oper_usie",
    "DecOperUsih": ".dec_oper_usih",
    "DecOperUsit": ".dec_oper_usit",
    "Decomptim": ".decomptim",
    "EcoFpha": ".eco_fpha",
    "Fcfnw": ".fcfnw",
    "Hidr": ".hidr",
    "InviabUnic": ".inviabunic",
    "Mapcut": ".mapcut",
    "OperDesvioFpha": ".oper_desvio_fpha",
    "OperDispUsihRee": ".oper_disp_usih_ree",
    "OperDispUsihSubm": ".oper_disp_usih_subm",
    "OperDispUsih": ".oper_disp_usih",
    "Postos": ".postos",
    "Relato": ".relato",
    "Relgnl": ".relgnl",
    "Vazoes": ".vazoes",
}

__all__ = sorted(_LAZY_IMPORTS.keys())


def __getattr__(name: str) -> Any:
    if name in _LAZY_IMPORTS:
        module = importlib.import_module(
            _LAZY_IMPORTS[name], __name__
        )
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(
        f"module {__name__!r} has no attribute {name!r}"
    )


def __dir__() -> list[str]:
    return __all__
```

### Key Files to Modify

- `/home/rogerio/git/idecomp/idecomp/decomp/__init__.py`

### Patterns to Follow

- Exact same pattern as inewave's `inewave/nwlistop/__init__.py` and `inewave/newave/__init__.py`. See `/home/rogerio/git/inewave/inewave/nwlistop/__init__.py` for reference.
- `__dir__` is required alongside `__getattr__` (inewave learning)
- `globals()[name] = value` caching eliminates repeat `__getattr__` calls (inewave learning)
- `-> Any` return annotation on `__getattr__` is required for mypy strict (inewave learning)

### Pitfalls to Avoid

- Do NOT forget `__dir__` -- without it, `dir(idecomp.decomp)` returns only already-cached names
- Do NOT forget `globals()[name] = value` caching -- without it, every access goes through `__getattr__`
- Module names must be extracted from the existing imports, not guessed -- verify each `_LAZY_IMPORTS` value matches the actual module filename
- Do NOT convert `idecomp/libs/__init__.py` -- it has only 1 import, overhead is negligible
- Do NOT change `idecomp/__init__.py` -- `from . import decomp` triggers the subpackage `__init__.py` but `__getattr__` handles deferred class loading

## Testing Requirements

### Unit Tests

No new tests. All 310 existing tests serve as regression tests for import compatibility.

### Integration Tests

- `python -c "from idecomp.decomp import Dadger; print(Dadger)"` -- works
- `python -c "from idecomp.decomp import *; print(Dadger)"` -- works
- `python -c "import idecomp.decomp; print(idecomp.decomp.Dadger)"` -- works

### E2E Tests

Not applicable.

## Dependencies

- **Blocked By**: ticket-008-replace-bare-type-ignores.md
- **Blocks**: None (last ticket in epic-02)

## Effort Estimate

**Points**: 2
**Confidence**: High (pattern is well-established from inewave)

## Out of Scope

- Converting `idecomp/libs/__init__.py` to lazy imports
- Benchmarking import time improvements (deferred to epic-03)
- Changing `idecomp/__init__.py`
