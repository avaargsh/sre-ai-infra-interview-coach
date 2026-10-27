#!/usr/bin/env python3
"""Build a deterministic ZIP with only files required by the installable Skill."""
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


def main() -> int:
    missing = [str(item) for item in FILES if not (ROOT / item).is_file()]
    if missing:
        print("Missing package files: " + ", ".join(missing), file=sys.stderr)
        return 1

    DIST.mkdir(exist_ok=True)
    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in sorted(FILES, key=lambda item: item.as_posix()):
            file_path = ROOT / relative
            info = ZipInfo((Path(ROOT.name) / relative).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, file_path.read_bytes())

    with ZipFile(ARCHIVE) as archive:
        names = archive.namelist()
        if not any(name.endswith("/SKILL.md") for name in names):
            print("Archive verification failed: SKILL.md missing", file=sys.stderr)
            return 1
        if any(name.startswith((".github/", "tests/", "scripts/")) for name in names):
            print("Archive verification failed: development files leaked into package", file=sys.stderr)
            return 1
    print(f"Created {ARCHIVE.relative_to(ROOT)} ({ARCHIVE.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
