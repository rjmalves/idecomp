# Accumulated Learnings: epic-01 + epic-02

**Plan**: idecomp-quality-performance
**Updated**: 2026-03-02
**Covers epics**: epic-01-foundation-and-storagetype-migration, epic-02-quality-and-type-safety

---

## Architecture and Configuration

- mypy strict is applied per-module via `[[tool.mypy.overrides]]` blocks in `/home/rogerio/git/idecomp/pyproject.toml` -- never set `strict = true` globally (breaks third-party import checking)
- `warn_return_any = false` must appear in both the global `[tool.mypy]` section AND every override block -- cfinterface `Block.data`, `Section.data`, `Register.data` all return `Any`
- 7 override blocks cover all production namespaces: `idecomp.decomp.*`, `idecomp.decomp.modelos.*`, `idecomp.decomp.modelos.blocos.*`, `idecomp.decomp.modelos.arquivoscsv.*`, `idecomp.libs.*`, `idecomp.libs.modelos.*`, `idecomp.config`
- Test files are explicitly excluded from mypy strict -- annotating pytest fixtures and mocks adds churn without safety benefit

## cfinterface Annotation Patterns (stable, applies to all subclasses)

- `IO[Any]` on every `read()` / `write()` override -- not `IO[str]`, which causes type errors at `Line.write()` returning `Union[str, bytes]`
- `# type: ignore[override]` with inline explanation on all `read()` / `write()` overrides
- `Optional[Any] = None` for `previous`, `next`, `data` parameters in `__init__` overrides
- `ClassVar[List[Type[T]]]` on BLOCKS, SECTIONS, REGISTERS, COLUMN_NAMES class attributes
- `-> None` on all property setters
- `cast("ClassName", super().read(...))` for narrowing return type in SectionFile subclasses (reference: `/home/rogerio/git/idecomp/idecomp/decomp/cortdeco.py`)
- Reference model for the full applied pattern: `/home/rogerio/git/idecomp/idecomp/decomp/modelos/dadger.py`

## Import Architecture

- PEP 562 lazy import pattern (`_LAZY_IMPORTS` dict + `__getattr__` + `__dir__`) is implemented in `/home/rogerio/git/idecomp/idecomp/decomp/__init__.py` for all 41 handler classes
- Three required elements: `_LAZY_IMPORTS: dict[str, str]`, `__getattr__` with `globals()[name] = value` cache, `__dir__` returning `sorted(_LAZY_IMPORTS.keys())`
- Without `__dir__`, `dir(idecomp.decomp)` only shows already-cached names -- always include it
- Threshold for conversion: 10+ eagerly imported symbols; `libs/__init__.py` (1 symbol) was not converted
- `StorageType` enum was introduced in epic-01 to replace bare string literals `"TEXT"` / `"BINARY"` -- all handler files now use `StorageType.TEXT` / `StorageType.BINARY` (reference: `/home/rogerio/git/idecomp/idecomp/decomp/arquivos.py`)

## Ticket Design Lessons

- Cleanup-only tickets that verify work done by preceding tickets tend to be no-ops -- ticket-008 (replace bare type-ignores) found 0 remaining ignores after tickets 006/007 applied the policy inline; merge verification into the annotation ticket's acceptance criteria instead
- File counts in ticket specs must be verified with `ls` before writing -- the "43 handler imports" spec had the actual count as 41 (`ls idecomp/decomp/*.py | grep -v __init__ | wc -l`)
- Large mechanical annotation batches (40+ files, 5-6 repetitive fix patterns) are well-suited to a single specialist dispatch rather than iterative per-file instructions

## Agent Routing

- `python-task-automation-developer` is effective for repetitive annotation work across 40+ files with predictable fix patterns (tickets 006, 007)
- Orchestrator handles configuration changes and single-file fixes (tickets 004, 005, 008, 009)

## Quality Scores (epic-02)

- ticket-007 (libs strict): quality 0.90 -- test delta 0.0 (no new tests, type-annotation only)
- ticket-008 (bare ignores): quality 1.0 -- no-op ticket, all criteria pre-satisfied
- ticket-009 (lazy imports): quality 0.90 -- test delta 0.0 (existing tests served as regression)
- Mean epic-02 quality: ~0.93 (tickets with scores); type-annotation-only tickets systematically score 0.0 on test delta dimension -- this is expected and not a defect
