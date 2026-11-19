#!/usr/bin/env python3
"""Zip each skill in .claude/skills/ into dist/skills/<name>.zip for upload to
Claude.ai (Settings > Capabilities > Skills) or the Claude API Skills endpoint."""
import pathlib, zipfile
root = pathlib.Path(__file__).resolve().parent.parent
out = root / "dist" / "skills"
out.mkdir(parents=True, exist_ok=True)
for skill in sorted((root / ".claude" / "skills").iterdir()):
    if not (skill / "SKILL.md").exists():
        continue
    z = out / f"{skill.name}.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in skill.rglob("*"):
            if f.is_file():
                zf.write(f, pathlib.Path(skill.name) / f.relative_to(skill))
    print("packaged", z.relative_to(root))
