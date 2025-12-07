<!-- copilot-instructions for chrissabato.com Pelican site -->
# Project-specific instructions for AI coding agents

This repo is a Pelican static site using a custom theme at `themes/sabato` and a
folder-per-post content layout under `content/` (each post lives in a directory
with an `index.md`, e.g. `content/20250522/index.md`). Use these notes to be
productive immediately when making changes.

- **Build / Dev workflows**
  - Primary make targets are in `Makefile`:
    - `make html` — generate site to `output/` (uses `pelican -s pelicanconf.py`).
    - `make devserver [PORT=8000]` or `make serve` — serve built files locally.
    - Use flags: `DEBUG=1` for Pelican debug, `RELATIVE=1` for relative URLs.
  - Alternative (richer) tasks are in `tasks.py` (requires `invoke`):
    - `inv build`, `inv rebuild`, `inv regenerate`, `inv serve`, `inv livereload`.
    - `inv livereload` watches theme templates and `content/` for changes.
  - Direct Pelican run (equivalent):
    - `pelican content -o output -s pelicanconf.py`

- **Production / Publishing**
  - Production settings live in `publishconf.py` (sets `SITEURL`, feeds, and
    deployment variables). `Makefile` has a `publish` target that runs Pelican
    with `publishconf.py`.
  - There are two deployment approaches in this repo:
    - `publishconf.py` defines `PUBLISH_COMMAND` (scp/rsync style) — inspect and
      update `SSH_USER`, `SSH_HOST`, `SSH_PORT`, `SSH_TARGET_PATH` there.
    - `tasks.py:publish` uses an `rsync` command that expects `CONFIG` keys
      named like `ssh_user`, `ssh_host`, `ssh_port`, `ssh_path`. Verify the
      mapping between `publishconf.py` variables and what the `publish` task
      expects before running `inv publish`.

- **Content conventions**
  - Posts are stored as `content/<slug-or-date>/index.md`. `pelicanconf.py`
    uses `PATH_METADATA = '(?P<slug>.*)\\..*'` so filenames and folders map to
    slugs differently than a simple flat `content/` layout — preserve the
    folder-per-post structure when creating new posts.
  - Static assets inside a post folder are copied because `STATIC_PATHS = ['.']`.
  - `IGNORE_FILES` prevents editor temp files from being processed (see
    `pelicanconf.py`).

- **Theme & templates**
  - Theme lives at `themes/sabato`.
  - Edit page structure in `themes/sabato/templates/*.html` (examples:
    `article.html`, `index.html`, `base.html`).
  - Static CSS/JS is under `themes/sabato/static/` (example CSS files:
    `static/css/custom.css`, `static/css/style.css`). When editing CSS/JS,
    prefer `inv livereload` or `make devserver` to see changes quickly.

- **Code and testing patterns**
  - There are no automated unit tests in this repo. For runtime checks:
    - Rebuild locally (`make html` / `inv build`) then run the dev server
      (`make serve` / `inv serve`) and inspect `output/`.

- **Common pitfalls for automation**
  - Deployment variable mismatch: `publishconf.py` and `tasks.py` use different
    variable names for SSH/rsync. Confirm values are present in the runtime
    config before running `inv publish`.
  - Windows considerations: some deployment commands use `rsync` and `scp` — on
    Windows, ensure an SSH/rsync toolchain (WSL, Git for Windows with scp, or
    PuTTY tools) is available, or run deployment from a Unix environment.

If any of these areas look incomplete or you'd like me to add examples (for
editing templates, adding a new post, or wiring CI), tell me which part to
expand and I'll update this file.
