#!/usr/bin/env python3
"""Build and verify a deterministic ZIP containing only installable Skill files."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ARCHIVE = DIST / f"{ROOT.name}-skill.zip"
FILES = [
    Path("SKILL.md"),
    Path("LICENSE"),
    Path("agents/openai.yaml"),
    Path("references/answer-template.md"),
    Path("references/progress-template.md"),
    Path("references/scenario-design.md"),
    Path("references/scoring-rubric.md"),
]


def fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return 1


def main() -> int:
    missing = [str(item) for item in FILES if not (ROOT / item).is_file()]
    if missing:
        return fail("missing package files: " + ", ".join(missing))

    DIST.mkdir(exist_ok=True)
    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in sorted(FILES, key=lambda item: item.as_posix()):
            file_path = ROOT / relative
            info = ZipInfo((Path(ROOT.name) / relative).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, file_path.read_bytes())

    expected = {(Path(ROOT.name) / relative).as_posix() for relative in FILES}
    with ZipFile(ARCHIVE) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            return fail("archive contains duplicate paths")
        if set(names) != expected:
            missing_names = sorted(expected - set(names))
            unexpected_names = sorted(set(names) - expected)
            return fail(f"archive manifest mismatch; missing={missing_names}, unexpected={unexpected_names}")
        skill_files = [name for name in names if Path(name).name.lower() == "skill.md"]
        if skill_files != [f"{ROOT.name}/SKILL.md"]:
            return fail(f"expected exactly one Skill entry point, got: {skill_files}")
        if ARCHIVE.stat().st_size <= 0:
            return fail("archive is empty")

    print(f"PASS: packaged {len(expected)} allowlisted files into {ARCHIVE.relative_to(ROOT)} ({ARCHIVE.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
