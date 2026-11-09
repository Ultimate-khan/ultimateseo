# Develop UltimateSEO

The repository includes the native engine, source catalog, portable skill and local fixtures. Keep client reports, captured website content, credentials and run outputs outside the source tree.

## Prepare the environment

```sh
python3 scripts/setup.py --dev
```

Activate `.venv` with `source .venv/bin/activate` on macOS/Linux, or `.venv\Scripts\Activate.ps1` in Windows PowerShell. Windows users can replace `python3` with `py -3` for setup.

Install optional local hosting fixtures when working on SFTP/FTPS behavior:

```sh
python -m pip install -e '.[hosting-test]'
```

## Check a change

```sh
ruff check .
ruff format --check .
python scripts/check_docs.py
python -m unittest discover -s tests -v
ultimateseo doctor
```

The suite includes deterministic fixtures for discovery fallbacks, empty/parser failures, permission categories, provenance, business-profile/competitor gates, incomplete evidence and browser setup. It also uses local fixtures for HTTP/browser crawling, extraction, robots and sitemap behavior, reputation calculations, catalog import and selection, planning, installation and file changes. Optional hosting fixtures require their corresponding dependencies. A fixture verifies defined behavior; it does not establish another website's availability or a client's search performance.

Development setup includes ReportLab and the test-only `pypdf` reader for report integration checks. They verify preserved evidence, escaped content, pagination, navigation, the exact logo, partial-output handling and font limitations. Client PDFs and visual QA renders stay outside the repository.

The [repository workflow](https://github.com/Ultimate-khan/ultimateseo/actions/workflows/tests.yml) runs across Linux, Windows and macOS with Python 3.10 and 3.12. Keep regressions reproducible and independent of external websites remaining unchanged.

## Update the posting library

Use [the posting guide](backlink-posting-guide.md) for the optional PDF importer and catalog structure. Preserve original source rows, unverified metric labels and dated primary-source guidance. Review exact posting routes, eligibility and content rules before qualifying an entry. Keep account-specific or client-specific observations outside the shared catalog.

## Build a skill upload asset

From reviewed source, run:

```sh
python3 scripts/validate_skill.py
python3 scripts/build_skill.py --out ../release-assets/ultimateseo-3.0.0-skill.zip
python3 scripts/build_skill.py --out ../release-assets/ultimateseo-skill.zip
```

Attach both archives and their checksums to every release. The stable `ultimateseo-skill.zip` name supports `/releases/latest/download/ultimateseo-skill.zip` only after a public latest release contains that exact asset.

The builder keeps the complete runtime and resources under one `ultimateseo/` folder and emits a SHA-256 sidecar. Developer tests and local environments stay outside the bundle. Existing output archives are preserved. Check that the archive, tag and version fields describe the same source before attaching the ZIP and checksum to a release. Runtime tests, a format check and a host's installation decision establish different things; report their results separately.

## Publish UltimateSEO to GitHub

The intended repository address is `https://github.com/Ultimate-khan/ultimateseo`; do not describe it as live until the repository has actually been created and inspected.

### 1. Run release preflight

Review the source for credentials, `.env` files, private Google exports, client reports, crawl databases and run folders. Keep those artifacts outside the repository. Then run:

```sh
python3 scripts/validate_skill.py
python3 scripts/check_docs.py
python3 scripts/run.py --version
python3 -m unittest discover -s tests
```

Use `py -3` on Windows when appropriate. Record actual results, including skipped or environment-dependent checks. Never convert an unrun check into a release claim.

### 2. Create an empty remote repository

In GitHub's web interface, create `ultimateseo` under the intended owner. Choose public or private visibility deliberately. For a new remote, do not initialize it with another README, license or `.gitignore`, because reviewed copies already exist locally.

If the actual owner differs from `Ultimate-khan`, update repository links in `README.md`, `pyproject.toml`, `CITATION.cff`, documentation and issue templates before committing.

### 3. Push the reviewed source

After creating the empty remote and reviewing the local Git state:

```sh
git init
git add .
git commit -m "Release UltimateSEO 3.0.0"
git branch -M main
git remote add origin https://github.com/Ultimate-khan/ultimateseo.git
git push -u origin main
```

If the folder is already a repository or has a remote, inspect its state instead of reinitializing or replacing configuration blindly. After pushing, inspect GitHub for the required files, working brand assets and absence of private material.

### 4. Create the release

Create tag `v3.0.0` targeting the reviewed `main` commit. Use **UltimateSEO 3.0.0** as the title and the approved [3.0.0 release notes](../CHANGELOG.md#300--ultimateseo-professionally-rebuilt) as the description. Attach `ultimateseo-skill.zip`, its SHA-256 sidecar, and the versioned archive/checksum when provided. A `.skill` package may also be attached when it contains the exact verified ZIP payload and has its own checksum.

### 5. Verify what users will download

Download the assets from the published release, compare their SHA-256 values with the sidecars, and install one into a disposable host/profile. Confirm the loaded name is `ultimateseo`, then run:

```sh
python3 scripts/run.py doctor
python3 scripts/run.py present --input examples/report-content.json --out ../verification-report
```

Inspect the HTML and PDF output. Repository creation, release availability, host registration, runtime readiness and live website access are separate outcomes; verify and report each independently.

See [Contributing](../CONTRIBUTING.md) for change descriptions and [Security](../SECURITY.md) for reporting vulnerabilities.
