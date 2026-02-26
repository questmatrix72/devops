#!/bin/bash
set -euo pipefail

# usage ./scripts/generate_modules.sh
# generate folders based on README.md file if needed 

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/generate_modules.py"