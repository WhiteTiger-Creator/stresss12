#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cp "${SCRIPT_DIR}/access_audit.py" /app/access_audit.py
python3 /app/access_audit.py repair --output-dir /app/output
