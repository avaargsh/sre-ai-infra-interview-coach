# Release procedure

## Before a release

1. Update CHANGELOG.md.
2. Run `python tests/validate_skill.py`.
3. Run `python tests/check_references.py`.
4. Run `python -m unittest discover -s tests -p 'test_*.py' -v`.
5. Run `python scripts/package_skill.py` and inspect the ZIP manifest.
6. Test the Skill in at least one target host.
7. Run a conversational smoke test: the first prompt gives no answer; evaluation covers all five scoring dimensions; the next question uses a different mechanism; progress can be copied and resumed.

## Publish via GitHub Actions

Recommended release path:

1. Ensure `main` is green and CHANGELOG.md includes the target version.
2. Open **Actions → Build Skill Release → Run workflow**.
3. Select the `main` branch and enter a semantic version tag such as `v0.1.0`.
4. The workflow validates the source, builds the deterministic ZIP, creates the tag at the selected main commit, and publishes a GitHub Release with the ZIP attached.
5. Verify the Release page, notes, asset download, and asset contents.

The workflow also supports an existing version tag pushed to GitHub. It rejects an invalid version string and refuses to overwrite an existing Release. Do not run a manual release from a non-main branch.

## Rollback

Do not force-push published history. If a release is defective, publish a corrected patch version and mark the previous release as superseded. Record any security-driven asset removal or release replacement in the release notes.
