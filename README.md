# Private resume source

Cloud source and compiled PDF for the scheduled refresh in `apoorvdarshan/apoorvdarshan/.github/workflows/refresh-profile.yml`, using scripts from `apoorvdarshan/profile`. This repository must remain private. The public PDF is published at https://apoorvdarshan.com/resume.

The workflow updates contributions and stars, compiles the source, validates the PDF, and records their SHA-256 hashes in `build.json`. Both files are mirrored to `~/rekisei` and `~/Documents` by the local resume sync, with dated backups and protection for local edits. Manual source changes must be committed here so later cloud runs preserve them.

The Documents resume files link directly to this checkout; preserve those symlinks. Editing them makes this checkout dirty and pauses automatic pulls until the edits are committed or reconciled. The background job writes backups under `~/.local/share/profile-automation/resume-backups`, linked from Documents, without requiring access to the protected Documents folder.

`android-downloads.json` stores the account-wide private Google Play report snapshot, daily history coverage and object provenance. Only explicitly validated production-app mappings contribute to public profile/resume badges; newly discovered or testing apps remain private. The dedicated reporting identity uses short-lived GitHub OIDC credentials, with no JSON key in this repository.

## Repository maintenance

[Build and interfaces](BUILD.md) · [Contributing](CONTRIBUTING.md) · [Security policy](SECURITY.md) · [Changes](CHANGELOG.md)

Private Scorecard results are available as private Actions artifacts. The scan
excludes Branch-Protection because the repository's `GITHUB_TOKEN` cannot read
classic protection rules. Protection was separately verified via the maintainer
API: linear history, no force pushes/deletion, resolved conversations and zero
required reviewers. No public Passing badge applies to this private repository.
