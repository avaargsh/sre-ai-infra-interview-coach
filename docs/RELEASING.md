# Release procedure

## Before a release

1. Update CHANGELOG.md.
2. Run python tests/validate_skill.py.
3. Run python tests/check_references.py.
4. Run python scripts/package_skill.py and inspect the ZIP file list.
5. Test the Skill in at least one target host.
6. Run a conversational smoke test: initial prompt gives no answer; evaluation covers all scoring dimensions; the next question uses a different mechanism; progress can be copied and resumed.

## Publish

1. Merge reviewed changes to main.
2. Create and push an annotated version tag, for example v0.1.0.
3. The release workflow validates and packages the Skill, then creates a GitHub Release with the ZIP attached.
4. Verify that the Release asset downloads and contains one top-level Skill directory with SKILL.md, agents/openai.yaml, references/, and LICENSE.

## Rollback

Do not force-push published history. If a release is defective, publish a corrected patch version and mark the previous release as superseded. Record any security-driven asset removal or release replacement in the release notes.
