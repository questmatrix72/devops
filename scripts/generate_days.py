#!/usr/bin/env python3

from pathlib import Path

root = Path(__file__).resolve().parents[1]
base = root / "tasks"
base.mkdir(parents=True, exist_ok=True)

total_days = 90

#generate folder and ensure README.md exists without overwriting.
for i in range(total_days):
    day_num = i+1
    day_dir = base / f"day-{day_num:02d}"
    day_dir.mkdir(parents=True, exist_ok=True)
    readme  = day_dir / "README.md"
    if not readme.exists():
        readme.write_text("")