# Epic 01 Learnings: Packaging & CI Modernization

**Epic**: epic-01-packaging-ci-modernization
**Date**: 2026-03-08
**Tickets**: ticket-001 through ticket-005
**Files changed**: `pyproject.toml`, `.github/workflows/main.yml`, `.github/workflows/docs.yml`, `.github/workflows/release.yml` (renamed from `publish.yml`), `.pre-commit-config.yaml` (new)

---

## Patterns Established

- **Dependency group split (4 extras)**: `pyproject.toml` uses `test = [pytest, pytest-cov]`, `lint = [ruff, mypy]`, `docs = [sphinx, furo, ...]`, `dev = ["idecomp[test,lint,docs]"]` as a self-referencing alias. Each CI job installs only its required extra via `uv sync --extra <group>`. See `/home/rogerio/git/idecomp/pyproject.toml` lines 32-43.

- **4-parallel-job CI pattern**: `main.yml` runs `lint`, `typecheck`, `test`, `docs` as fully independent jobs. `lint` and `typecheck` both install `--extra lint`. `test` matrix covers Python 3.10/3.11/3.12 with codecov upload. `docs` installs `--extra docs` and runs sphinx-build. No `needs:` dependencies between any of the 4 jobs. See `/home/rogerio/git/idecomp/.github/workflows/main.yml`.

- **Official GitHub Pages 2-job deploy pattern**: `docs.yml` uses a `build` job (sphinx-build + `actions/upload-pages-artifact@v3`) followed by a `deploy` job (`needs: build`, `actions/deploy-pages@v4`, `environment: github-pages`). Top-level `permissions: pages: write, id-token: write` and `concurrency: group: "pages", cancel-in-progress: false` are mandatory for this pattern. See `/home/rogerio/git/idecomp/.github/workflows/docs.yml`.

- **Tag-triggered release with regex version validation**: `release.yml` triggers on `push: tags: ["v*"]`. Version is extracted with `grep -oP '__version__\s*=\s*"\K[^"]+'` on `idecomp/__init__.py`, not via `exec()` or Python import. GitHub release is created after PyPI publish via `gh release create ${{ github.ref_name }} --generate-notes`. See `/home/rogerio/git/idecomp/.github/workflows/release.yml`.

- **mypy pre-commit hook at `stages: [manual]`**: The `.pre-commit-config.yaml` registers mypy as `language: system`, `entry: uv run mypy ./idecomp`, `pass_filenames: false`, `stages: [manual]`. This prevents cfinterface import errors from blocking every commit while keeping mypy available for deliberate invocation via `pre-commit run --hook-stage manual --all-files`. See `/home/rogerio/git/idecomp/.pre-commit-config.yaml`.

- **ruff hook with `args: [--fix]`**: The ruff pre-commit hook includes `args: [--fix]` so it auto-corrects fixable issues rather than just reporting them. Without this flag, the hook only reports and the commit still requires manual re-run. See `/home/rogerio/git/idecomp/.pre-commit-config.yaml`.

---

## Architectural Decisions

- **`strict = true` replaces explicit mypy flags**: The ticket specified many redundant mypy flags (`disallow_untyped_defs`, `no_implicit_optional`, etc.) explicitly alongside `strict = true`. The implementation correctly omits the redundant flags because `strict = true` already enables all of them. Only the overrides that conflict with strict mode (`warn_return_any = false`) were made explicit. **Rejected alternative**: listing all flags verbosely for documentation purposes (rejected because `strict = true` is self-documenting and the redundancy creates maintenance risk).

- **`uv python install` without version in docs.yml**: The `build` job in `docs.yml` uses `uv python install` with no explicit version, relying on uv to select from `.python-version` or `pyproject.toml`'s `requires-python`. This differs from `main.yml` which explicitly pins `3.12`. **Accepted because**: docs builds are not version-sensitive; using the project default is appropriate and avoids a hard pin that diverges from the matrix.

- **`publish.yml` renamed to `release.yml` via git mv**: The file rename was done preserving git history through `git mv`, not a delete-and-create. This preserves the audit trail for the old trigger model. Future maintainers should verify `release.yml` exists and `publish.yml` does not before adding any references.

- **Workflow name kept as `tests`**: `main.yml` retains `name: tests` even though it now runs lint, typecheck, test, and docs. This was a deliberate constraint: the README badge URL references `actions/workflows/main.yml/badge.svg` and renaming the workflow would visually change the badge label but not break it. Badge references must be audited in ticket-013 before changing.

---

## Files & Structures Created

- `/home/rogerio/git/idecomp/pyproject.toml` — Modernized with split dependency groups, full classifiers, `[tool.mypy]` with strict settings and cfinterface override, `[tool.ruff.lint]` with E/F/I/UP rule sets.
- `/home/rogerio/git/idecomp/.github/workflows/main.yml` — 4-parallel-job workflow replacing the former single sequential job.
- `/home/rogerio/git/idecomp/.github/workflows/docs.yml` — 2-job official Pages deployment replacing `peaceiris/actions-gh-pages@v3`.
- `/home/rogerio/git/idecomp/.github/workflows/release.yml` — Tag-triggered release workflow (renamed from `publish.yml`).
- `/home/rogerio/git/idecomp/.pre-commit-config.yaml` — New file with ruff (auto-fix) and mypy (manual stage) hooks.

---

## Conventions Adopted

- **All tool invocations in CI use `uv run <tool>`**: Never call `python -m pytest` or bare `ruff` in workflow steps; always prefix with `uv run`. This ensures the project's virtual environment is active and the correct tool version is used.

- **CI installs only the minimal required extras per job**: `lint` job uses `--extra lint`, `test` job uses `--extra test`, `docs` job uses `--extra docs`. Never use `--all-extras` or `--dev` in CI — this would increase install time and mask missing dependency declarations.

- **`cfinterface` pin `>=1.8,<=1.8.3` is immutable**: This constraint must not be removed or widened in any future ticket. It is at `/home/rogerio/git/idecomp/pyproject.toml` line 9 and exists because newer versions of cfinterface introduced breaking changes.

- **`warn_return_any = false` must appear in both `[tool.mypy]` and `[[tool.mypy.overrides]]` for cfinterface**: `strict = true` re-enables `warn_return_any`. The top-level override relaxes it for all code; the per-module override is belt-and-suspenders for cfinterface specifically.

- **Concurrency group `"pages"` with `cancel-in-progress: false`**: When migrating any future docs deployment workflow, always preserve this exact concurrency configuration. `cancel-in-progress: true` would abort a running deployment mid-way and leave Pages in an inconsistent state.

- **Version extraction in release workflows uses grep regex, never exec/import**: `grep -oP '__version__\s*=\s*"\K[^"]+'` is the correct pattern. Python import (`from idecomp import __version__`) fails in fresh CI environments because relative imports in `__init__.py` require the package to be properly installed. `exec(open('__init__.py').read())` fails for the same reason.

---

## Surprises & Deviations

- **mypy strict flag verbosity**: Tickets specified all individual strict flags explicitly in the spec section for documentation clarity, but the final `pyproject.toml` correctly omits them as redundant under `strict = true`. This was the right call. Future ticket authors should note that specifying redundant flags in a spec is an anti-pattern — the spec should match what should be written, not serve as documentation for what `strict` implies.

- **`docs.yml` Python version unspecified**: The ticket did not specify which Python version the docs `build` job should use (unlike `main.yml` which explicitly pins 3.12 for non-matrix jobs). The implementation used `uv python install` without a version, which is valid. Future tickets touching `docs.yml` should note this difference from `main.yml` and decide whether to align them.

- **`release.yml` does not run `ruff format --check`**: The validation steps in `release.yml` include `ruff check` but not `ruff format --check`. This is consistent with the ticket spec (which only listed `ruff check` in the validation steps), but differs from `main.yml`'s `lint` job which checks both. This is an intentional asymmetry: format violations are caught in normal CI before a release is tagged.

- **`publish.yml` deleted**: The git status shows the file was renamed (`RM .github/workflows/publish.yml -> .github/workflows/release.yml`). Any documentation in epics 3 or 4 that references `publish.yml` must be updated to `release.yml`.

---

## Recommendations for Future Epics

- **Epic 2 (Sphinx Modernization)**: The `docs` extra in `pyproject.toml` already includes `furo` (replacing `sphinx-rtd-theme`). The `docs.yml` workflow already builds with `--extra docs`. Epic 2 only needs to change `docs/source/conf.py` — no workflow or dependency changes required. Verify `furo` is resolvable before starting ticket-006.

- **Epic 3 (Documentation Content)**: All new Sphinx pages must build successfully under the `docs` job in `main.yml` and the `build` job in `docs.yml`. Test sphinx-build locally with `uv sync --extra docs && uv run sphinx-build -M html docs/source docs/build` before writing tickets. If cfinterface causes sphinx-gallery import errors, the mitigation pattern from inewave (skipping problematic examples) should be documented in the ticket.

- **Epic 4 (Repository Polish)**: CONTRIBUTING.md should document the pre-commit hook setup: `pip install pre-commit && pre-commit install` for regular hooks, and `pre-commit run --hook-stage manual --all-files` for mypy. The `stages: [manual]` design decision should be explained. Reference `/home/rogerio/git/idecomp/.pre-commit-config.yaml` directly in the contributing guide.

- **Badge URL stability**: `main.yml` workflow name is `tests`. If ticket-013 updates the README, it should reference `[![Tests](https://github.com/rjmalves/idecomp/actions/workflows/main.yml/badge.svg)](...)`. Do not assume the workflow display name will match — it is `tests`, not `CI` or `main`.

- **Release workflow trigger**: Any ticket that involves bumping `__version__` in `idecomp/__init__.py` must also consider that pushing a `v*` tag will trigger `release.yml` and attempt PyPI publication. Coordinate version bumps and tag pushes explicitly. The version validation step in `release.yml` will catch mismatches but the workflow will still be triggered.
