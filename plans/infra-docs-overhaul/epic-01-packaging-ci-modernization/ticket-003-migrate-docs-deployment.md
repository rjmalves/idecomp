# ticket-003 Migrate Docs Deployment to Official GitHub Pages Actions

## Context

### Background

The current `docs.yml` workflow uses `peaceiris/actions-gh-pages@v3`, which is deprecated and no longer maintained. GitHub now provides official actions for Pages deployment: `actions/upload-pages-artifact@v3` and `actions/deploy-pages@v4`. The inewave overhaul successfully migrated to these official actions.

### Relation to Epic

Independent ticket within Epic 1. Does not depend on the pyproject.toml changes (it only changes the deployment mechanism, not what gets installed).

### Current State

File: `/home/rogerio/git/idecomp/.github/workflows/docs.yml`

- Triggers: push to `main`, workflow_dispatch
- Single `docs` job: checkout, install uv, install python, `uv sync --all-extras --dev`, pytest, sphinx-build, deploy with `peaceiris/actions-gh-pages@v3`
- Deploys to `gh-pages` branch with `force_orphan: true`
- Uses `${{ secrets.GITHUB_TOKEN }}`

## Specification

### Requirements

1. Replace `peaceiris/actions-gh-pages@v3` deployment with official GitHub Pages actions
2. Add top-level `permissions` block: `pages: write`, `id-token: write`
3. Add `concurrency` group to prevent concurrent deployments: `group: "pages"`, `cancel-in-progress: false`
4. Split into 2 jobs:
   - **build**: checkout, install uv, install python, `uv sync --extra docs`, sphinx-build, `actions/upload-pages-artifact@v3` pointing to `docs/build/html`
   - **deploy**: depends on build, uses `actions/deploy-pages@v4`, environment `github-pages`
5. Remove the pytest step from the docs workflow (tests run in `main.yml`)
6. Remove the `--all-extras --dev` install; use `--extra docs` instead
7. Keep triggers: push to `main`, workflow_dispatch

### Inputs/Props

- Current file: `/home/rogerio/git/idecomp/.github/workflows/docs.yml` (33 lines)

### Outputs/Behavior

- Documentation deploys to GitHub Pages using the official deployment mechanism
- Deployment uses OIDC token (id-token: write) instead of GITHUB_TOKEN for Pages
- Concurrent pushes to main do not cause race conditions in deployment

### Error Handling

- If sphinx-build fails, the upload-pages-artifact step is skipped and deploy job is skipped
- The concurrency group ensures only one deployment runs at a time

## Acceptance Criteria

- [ ] Given the updated `docs.yml`, when parsing the YAML, then `peaceiris/actions-gh-pages` does not appear anywhere in the file
- [ ] Given the updated `docs.yml`, when inspecting the top-level keys, then `permissions` contains `pages: write` and `id-token: write`, and `concurrency` has `group: "pages"` with `cancel-in-progress: false`
- [ ] Given the `build` job, when inspecting its steps, then it runs `uv sync --extra docs` (not `--all-extras`) and uses `actions/upload-pages-artifact@v3` with `path: docs/build/html`
- [ ] Given the `deploy` job, when inspecting its configuration, then it has `needs: build`, uses `actions/deploy-pages@v4`, and sets `environment: name: github-pages`
- [ ] Given the updated `docs.yml`, when searching for `pytest`, then no pytest step exists in any job

## Implementation Guide

### Suggested Approach

1. Open `/home/rogerio/git/idecomp/.github/workflows/docs.yml`
2. Add top-level `permissions` and `concurrency` blocks after the `on` trigger
3. Rename the existing `docs` job to `build` and modify its steps:
   - Keep: checkout, install uv, install python
   - Change: `uv sync --all-extras --dev` to `uv sync --extra docs`
   - Remove: pytest step
   - Keep: sphinx-build step
   - Replace: peaceiris action with `actions/upload-pages-artifact@v3` with `path: docs/build/html`
4. Add a new `deploy` job:
   ```yaml
   deploy:
     needs: build
     runs-on: ubuntu-latest
     environment:
       name: github-pages
       url: ${{ steps.deployment.outputs.page_url }}
     steps:
       - name: Deploy to GitHub Pages
         id: deployment
         uses: actions/deploy-pages@v4
   ```

### Key Files to Modify

- `/home/rogerio/git/idecomp/.github/workflows/docs.yml`

### Patterns to Follow

- Match the inewave `docs.yml` structure with build + deploy jobs
- Use the official GitHub Pages actions pattern from GitHub's documentation

### Pitfalls to Avoid

- Do NOT keep the pytest step; tests belong in `main.yml` only
- Do NOT forget the `id-token: write` permission; it is required for the official Pages deployment
- Do NOT set `cancel-in-progress: true`; this could cancel an active deployment mid-way
- The `environment: name: github-pages` must match the GitHub Pages environment configured in the repo settings

## Testing Requirements

### Unit Tests

- Not applicable (YAML configuration)

### Integration Tests

- Validate YAML syntax
- Verify no references to `peaceiris` remain

### E2E Tests

- After merging to main, verify docs deploy successfully to the GitHub Pages URL

## Dependencies

- **Blocked By**: None (independent within Epic 1)
- **Blocks**: None

## Effort Estimate

**Points**: 2
**Confidence**: High
