#!/usr/bin/env python3

from pathlib import Path
import re

# Project root (one level above scripts/)
root = Path(__file__).resolve().parents[1]

# README file inside scripts/
scripts_dir = root / "scripts"
readme_file = scripts_dir / "README.md"

# Base directory for generated folders
base = root / "modules"
base.mkdir(parents=True, exist_ok=True)

if not readme_file.exists():
    print("README.md not found inside scripts folder.")
    exit(1)


def sanitize_name(name: str) -> str:
    """
    Convert:
    'Module 1: Onboarding and Welcome'
    into:
    'module-1-onboarding-and-welcome'
    """
    name = name.strip().lower()

    # Remove special characters except spaces and hyphen
    name = re.sub(r"[^a-z0-9\s-]", "", name)

    # Replace spaces with hyphens
    name = re.sub(r"\s+", "-", name)

    # Remove duplicate hyphens
    name = re.sub(r"-+", "-", name)

    return name.strip("-")


# Read README.md line by line
with readme_file.open("r") as f:
    for index, line in enumerate(f, start=1):
        folder_name = line.strip()

        if not folder_name:
            continue

        clean_name = sanitize_name(folder_name)

        # Prefix with 01-, 02-, etc.
        final_folder_name = f"{index:02d}-{clean_name}"

        module_dir = base / final_folder_name
        module_dir.mkdir(parents=True, exist_ok=True)

        # Ensure README.md exists inside each folder
        module_readme = module_dir / "README.md"
        if not module_readme.exists():
            module_readme.write_text("")

        print(f"Created: {final_folder_name}")