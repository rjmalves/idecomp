# ticket-004 Create Tag-Triggered Release Workflow

## Context

### Background

The current `publish.yml` triggers on GitHub release creation events. The inewave overhaul moved to a tag-triggered workflow that validates the tag version against `__version__`, creates a GitHub release automatically, and publishes to PyPI. idecomp should adopt the same pattern.

### Relation to Epic

Fourth ticket in Epic 1. Depends on ticket-001 for dependency groups (the release workflow installs `--extra test` and `--extra lint` for validation steps).

### Current State

File: `/home/rogerio/git/idecomp/.github/workflows/publish.yml`

- Name: `deploy`
- Trigger: `release: types: [created]`
- Single job `build-and-publish`: checkout, install uv, install python 3.11, `uv sync --all-extras --dev`, pytest, mypy, ruff check, uv build, pypa/gh-action-pypi-publish
- Uses trusted publishing (`id-token: write`)
- Environment: `pypi` with URL `https://pypi.org/p/idecomp`

## Specification

### Requirements

1. Rename the file from `publish.yml` to `release.yml`
2. Rename the workflow from `deploy` to `release`
3. Change trigger from `release: types: [created]` to `push: tags: ["v*"]`
4. Add a version validation step that:
   - Extracts version from `idecomp/__init__.py` using `grep` + regex (NOT `exec()` or `python -c "import idecomp"`)
   - Extracts tag version from `GITHUB_REF` (strips `refs/tags/v` prefix)
   - Compares them and fails if they do not match
5. Keep the test, mypy, and ruff validation steps but use `--extra test` and `--extra lint` instead of `--all-extras`
6. After successful build and publish, create a GitHub release using `gh release create $TAG --generate-notes`
7. Keep the trusted publishing setup (id-token: write, pypi environment)
8. Update Python version to 3.12

### Inputs/Props

- Current file: `/home/rogerio/git/idecomp/.github/workflows/publish.yml` (41 lines)
- Version source: `/home/rogerio/git/idecomp/idecomp/__init__.py` line `__version__ = "1.8.2"`

### Outputs/Behavior

- Pushing a tag `v1.8.3` triggers the workflow
- Version validation fails if tag `v1.8.3` does not match `__version__ = "1.8.3"` in `__init__.py`
- On success: tests pass, package is built, published to PyPI, and a GitHub release is created

### Error Handling

- Version mismatch between tag and `__init__.py` fails the workflow early (before build/publish)
- Test/lint failures prevent package publication

## Acceptance Criteria

- [ ] Given the repository, when listing files in `.github/workflows/`, then `release.yml` exists and `publish.yml` does not exist
- [ ] Given the `release.yml`, when inspecting the `on` trigger, then it is `push: tags: ["v*"]` and no `release` trigger exists
- [ ] Given the version validation step, when inspecting the shell commands, then it uses `grep -oP '__version__\s*=\s*"\K[^"]+'` (or equivalent regex) on `idecomp/__init__.py` and does NOT use `exec()`, `eval()`, or `python -c "import idecomp"`
- [ ] Given the `release.yml`, when inspecting install steps, then it uses `uv sync --extra test --extra lint` (not `--all-extras --dev`)
- [ ] Given the workflow, when inspecting the final steps, then after `pypa/gh-action-pypi-publish`, there is a step running `gh release create` with the tag and `--generate-notes`

## Implementation Guide

### Suggested Approach

1. Rename `/home/rogerio/git/idecomp/.github/workflows/publish.yml` to `release.yml` (use `git mv`)
2. Update the workflow `name` to `release`
3. Replace the `on` trigger:
   ```yaml
   on:
     push:
       tags:
         - "v*"
   ```
4. Add a version validation step early in the job:
   ```yaml
   - name: Validate version
     run: |
       PKG_VERSION=$(grep -oP '__version__\s*=\s*"\K[^"]+' idecomp/__init__.py)
       TAG_VERSION=${GITHUB_REF#refs/tags/v}
       if [ "$PKG_VERSION" != "$TAG_VERSION" ]; then
         echo "Version mismatch: __init__.py=$PKG_VERSION tag=$TAG_VERSION"
         exit 1
       fi
   ```
5. Change install step to `uv sync --extra test --extra lint`
6. Update Python to 3.12: `uv python install 3.12`
7. Add GitHub release creation step after PyPI publish:
   ```yaml
   - name: Create GitHub Release
     env:
       GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
     run: |
       gh release create ${{ github.ref_name }} --generate-notes
   ```
8. Add `contents: write` to permissions (needed for `gh release create`)

### Key Files to Modify

- `/home/rogerio/git/idecomp/.github/workflows/publish.yml` (rename to `release.yml` and rewrite)

### Patterns to Follow

- Match the inewave `release.yml` structure
- Use grep + regex for version extraction (never exec/eval)
- Trusted publishing with `pypa/gh-action-pypi-publish@release/v1`

### Pitfalls to Avoid

- Do NOT use `exec(open('__init__.py').read())` -- it fails because `__init__.py` has `from . import decomp` (relative import)
- Do NOT use `python -c "from idecomp import __version__"` -- it requires the package to be importable with all deps
- Do NOT forget `contents: write` permission for `gh release create`
- The `startsWith(github.ref, 'refs/tags')` guards on build/publish steps can be removed since the trigger already ensures this

## Testing Requirements

### Unit Tests

- Not applicable (YAML configuration)

### Integration Tests

- Validate YAML syntax
- Verify the grep regex correctly extracts version from `idecomp/__init__.py`

### E2E Tests

- Create a test tag on a branch to verify the workflow triggers (can be deleted after)

## Dependencies

- **Blocked By**: ticket-001-modernize-pyproject-toml.md
- **Blocks**: None

## Effort Estimate

**Points**: 3
**Confidence**: High
