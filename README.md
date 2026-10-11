# Private resume source

Cloud source and compiled PDF for the scheduled refresh in `apoorvdarshan/apoorvdarshan/.github/workflows/refresh-profile.yml`, using scripts from `apoorvdarshan/profile`. This repository must remain private. The public PDF is published at https://apoorvdarshan.com/resume.

The workflow updates contributions and stars, compiles the source, validates the PDF, and records their SHA-256 hashes in `build.json`. Both files are mirrored to `~/rekisei` and `~/Documents` by the local resume sync, with dated backups and protection for local edits. Manual source changes must be committed here so later cloud runs preserve them.

The Documents resume files link directly to this checkout; preserve those symlinks. Editing them makes this checkout dirty and pauses automatic pulls until the edits are committed or reconciled. The background job writes backups under `~/.local/share/profile-automation/resume-backups`, linked from Documents, without requiring access to the protected Documents folder.
