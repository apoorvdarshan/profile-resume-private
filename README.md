# Private resume source

Cloud source and compiled PDF for the scheduled refresh in `apoorvdarshan/apoorvdarshan/.github/workflows/refresh-profile.yml`, using scripts from `apoorvdarshan/profile`. This repository must remain private. The public PDF is published at https://apoorvdarshan.com/resume.

The workflow updates contributions and stars, compiles the source, validates the PDF, and records their SHA-256 hashes in `build.json`. Both files are mirrored to `~/rekisei` and `~/Documents` by the local resume sync, with dated backups and protection for local edits. Manual source changes must be committed here so later cloud runs preserve them.
