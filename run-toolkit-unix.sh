#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
if command -v python3 >/dev/null 2>&1; then
  exec python3 launcher.py
fi
echo "Python 3 is required. Install it from your operating system's trusted package source."
exit 1
