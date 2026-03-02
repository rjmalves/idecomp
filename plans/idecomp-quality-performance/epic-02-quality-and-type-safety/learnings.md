# Epic 02 Learnings: Quality and Type Safety

**Plan**: idecomp-quality-performance
**Epic**: epic-02-quality-and-type-safety
**Extracted**: 2026-03-02
**Git range**: cd5a85d..ff25afc (2 commits covering tickets 004-009)

---

## Patterns Established

- **`cast()` for SectionFile.read() return narrowing** -- When a cfinterface `SectionFile` subclass overrides `read()` and calls `super().read()`, wrap the result with `cast("ClassName", a)` from `typing`. This is the correct type-safe fix rather than `# type: ignore[return-value]` or a runtime `isinstance` assert. Established in `/home/rogerio/git/idecomp/idecomp/decomp/cortdeco.py` at the `read()` classmethod.

- **`IO[Any]` for all read/write overrides in cfinterface subclasses** -- Use `IO[Any]` (not `IO[str]`) for the file parameter on every `Block`, `Section`, and `Register` `read()` / `write()` override. `IO[str]` caused 193 errors in the inewave project because `Line.write()` returns `Union[str, bytes]`. Pattern applied uniformly across all 41 handler files and 42 model files under `/home/rogerio/git/idecomp/idecomp/decomp/`.

- **`warn_return_any = false` per override block in mypy config** -- Every `[[tool.mypy.overrides]]` block must repeat `warn_return_any = false`, not just the global `[tool.mypy]` section. cfinterface's `Block.data`, `Section.data`, and `Register.data` all return `Any`, so omitting this setting floods mypy output with hundreds of meaningless `[return-any]` errors. Config lives in `/home/rogerio/git/idecomp/pyproject.toml`.

- **Per-module strict overrides, never global strict** -- `strict = true` must appear only in `[[tool.mypy.overrides]]` blocks targeting `idecomp.*` modules. Setting `strict = true` globally breaks third-party imports. See `/home/rogerio/git/idecomp/pyproject.toml` for the 7-override pattern covering `idecomp.decomp.*`, `idecomp.decomp.modelos.*`, `idecomp.decomp.modelos.blocos.*`, `idecomp.decomp.modelos.arquivoscsv.*`, `idecomp.libs.*`, `idecomp.libs.modelos.*`, and `idecomp.config`.

- **PEP 562 lazy import pattern for large `__init__.py` files** -- Replace N eager import statements with a `_LAZY_IMPORTS: dict[str, str]` mapping class names to relative module paths, a `__getattr__` that imports and caches via `globals()[name] = value`, and a `__dir__` that returns `sorted(_LAZY_IMPORTS.keys())`. Both `__getattr__` and `__dir__` are required: without `__dir__`, `dir()` only returns already-cached names. The `globals()` cache prevents repeat calls through `__getattr__`. Return annotation `-> Any` on `__getattr__` is required for mypy strict compliance. Implemented in `/home/rogerio/git/idecomp/idecomp/decomp/__init__.py`.

---

## Architectural Decisions

- **Decision: `warn_return_any = false` globally, not silenced per-call-site** -- Alternative was to annotate every call to `Block.data` / `Section.data` / `Register.data` with `cast()` or `# type: ignore[return-any]`. Rejected because cfinterface's `Any`-typed data attributes are used at hundreds of call sites across 89 files. Setting the flag at the mypy config level silences all of them at zero code-change cost, while preserving the strictness of all other `return-any` checks.

- **Decision: Do not convert `idecomp/libs/__init__.py` to lazy imports** -- `libs/__init__.py` exports only 1 class (`UsinasHidreletricas`). The overhead of eager import for a single handler is negligible and the added indirection of PEP 562 is not justified. Threshold for conversion: 10+ eagerly imported symbols.

- **Decision: Do not annotate test files under mypy strict** -- Test files in `tests/` were explicitly excluded from all `[[tool.mypy.overrides]]` blocks. Adding strict annotations to test files would require annotating pytest fixtures, mock objects, and parametrize decorators, adding churn without safety benefit. This was a deliberate out-of-scope decision in the original ticket design.

---

## Files and Structures Created

- `/home/rogerio/git/idecomp/pyproject.toml` -- Added 38 lines of `[tool.mypy]` configuration: one global section with `warn_return_any = false`, plus 7 `[[tool.mypy.overrides]]` blocks (one per module namespace). This is the authoritative mypy strict configuration for the project.

- `/home/rogerio/git/idecomp/idecomp/decomp/__init__.py` -- Rewritten from 41 eager import lines to 61-line PEP 562 lazy module with `_LAZY_IMPORTS` dict (41 entries), `__all__`, `__getattr__`, and `__dir__`.

- `/home/rogerio/git/idecomp/idecomp/decomp/cortdeco.py` -- Added `cast` import and wrapped `super().read()` return with `cast("Cortdeco", a)` to resolve the sole baseline mypy error.

---

## Conventions Adopted

- **Every `# type: ignore` must include a specific error code AND an inline explanation** -- Format: `# type: ignore[error-code]  # reason in under 60 chars`. Example: `import pandas as pd  # type: ignore[import-untyped]  # no pandas-stubs package`. Bare `# type: ignore` (no code) is prohibited; the zero-bare-ignores policy is enforced by CI via `grep -r '# type: ignore$' idecomp/ --include="*.py"`.

- **`Optional[Any]` for cfinterface `__init__` parameters** -- When overriding `Block.__init__` or `Register.__init__`, annotate `previous`, `next`, and `data` as `Optional[Any] = None`. These come from cfinterface's dynamic construction machinery and their types are not inferrable from stubs.

- **`ClassVar[List[Type[T]]]` for BLOCKS, SECTIONS, REGISTERS class attributes** -- Class-level container attributes (e.g., `BLOCKS`, `SECTIONS`, `COLUMN_NAMES`) require explicit `ClassVar` annotation under mypy strict to avoid `[assignment]` errors. Pattern used across all model files.

- **`-> None` on all property setters** -- Under mypy strict, setters must declare explicit `-> None` return type. Applied uniformly to all property setters in decomp and libs modules.

---

## Surprises and Deviations

- **ticket-008 was a complete no-op** -- The ticket was designed as a cleanup pass after tickets 006 and 007 to replace any remaining bare `# type: ignore` comments. In practice, tickets 006 and 007 already replaced ALL bare ignores during the strict-mode annotation work. When ticket-008 ran, `grep -r '# type: ignore$' idecomp/` returned zero matches immediately. The ticket completed with no file changes. This means the 3-point cleanup ticket was unnecessary work in the plan -- future epics of this kind should merge the "cleanup" verification into the strict-mode enablement tickets as a final acceptance check, not a separate ticket.

- **Handler count was 41, not 43 as stated in ticket-006 and ticket-009** -- The ticket said "~43 handler files" and the `_LAZY_IMPORTS` dict was specified with 43 entries. The actual count of non-`__init__` `.py` files in `idecomp/decomp/` is 41, and the implemented `_LAZY_IMPORTS` dict has 41 entries. The discrepancy originated in the initial plan estimate. Actual file count should be verified with `ls idecomp/decomp/*.py | grep -v __init__ | wc -l` before writing ticket specs that reference this number.

- **Tickets 006 covered 63 files in a single specialist dispatch, not iterative batches** -- The ticket implementation guide suggested iterating module-by-module with intermediate `mypy` checks. The specialist agent (python-task-automation-developer) instead processed all 63 files in a single batch dispatch covering `idecomp/decomp/*.py` and `idecomp/decomp/modelos/*.py`. This worked because the annotation patterns are highly repetitive (same 5-6 fix types across all files) and the agent could apply them mechanically. Single-batch dispatch is appropriate when the fix set is predictable and pattern-driven. The commit for ticket-006 is at `b83332b`.

- **`modelos/dadger.py` was the largest single-file change** -- With 1025 line changes in `idecomp/decomp/modelos/dadger.py` (the largest model file in the project), this file dominated the ticket-006 diff. The high change count is explained by the large number of Block subclasses in dadger, each requiring `__init__`, `read`, `write`, and property annotations. Future tickets touching dadger should account for its size.

---

## Recommendations for Future Epics

- **Merge bare-ignore cleanup into the strict-mode ticket, not a separate ticket** -- ticket-008 existed as a 3-point standalone ticket but ended up doing nothing because tickets 006/007 enforced the policy inline. For epic-03 and beyond, include `grep -r '# type: ignore$' idecomp/ | wc -l == 0` as an acceptance criterion directly on any annotation ticket rather than creating a separate cleanup ticket.

- **Use `grep -c` to verify handler file counts before writing ticket specs** -- The 43-vs-41 discrepancy shows that estimates based on memory or prior-project counts can be wrong. Run `ls idecomp/decomp/*.py | grep -v __init__ | wc -l` before writing any ticket that references a specific file count in the decomp module.

- **The 5-pattern mypy annotation set is stable for all cfinterface subclasses** -- For any future module added to idecomp that extends cfinterface `Block`, `Section`, or `Register`, the full annotation pattern is: (1) `IO[Any]` on read/write, (2) `# type: ignore[override]` on read/write with explanation, (3) `Optional[Any]` on `__init__` params, (4) `ClassVar` on class attributes, (5) `-> None` on setters. Reference: `/home/rogerio/git/idecomp/idecomp/decomp/modelos/dadger.py` for the complete applied pattern.

- **PEP 562 lazy imports are viable for any `__init__.py` exporting 10+ symbols** -- The pattern in `/home/rogerio/git/idecomp/idecomp/decomp/__init__.py` can be copy-adapted to any package. The three required elements are `_LAZY_IMPORTS` dict, `__getattr__` with `globals()` cache, and `__dir__`. Do not omit `__dir__` -- this was a confirmed pitfall in inewave.

- **`python-task-automation-developer` is the right agent for large mechanical annotation batches** -- Tickets 006 and 007 were dispatched to `python-task-automation-developer`. For repetitive pattern application across 40+ files, this agent outperforms interactive iteration. Reserve `python-rest-api-service-developer` or `hpc-python-developer` for tickets with non-trivial logic changes.
