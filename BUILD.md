# Private validation

Run `python3 scripts/validate-private.py` to check the source/PDF build manifest,
JSON snapshots and absence of committed credentials. CI prints only success/failure,
never resume text or private report records. The existing external profile
workflow compiles the PDF and validates page bounds before publication.

Inputs: private source, PDF, build.json and store snapshots. Outputs: validation
exit code, and private Scorecard artifact. This is a private data repository, not
FLOSS software eligible for a public OpenSSF Passing badge. Scorecard does not
publish its private results or obtain a public badge.
