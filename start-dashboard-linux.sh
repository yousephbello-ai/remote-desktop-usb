
#!/usr/bin/env bash

cd "$(dirname "$0")" || exit 1

if ! command -v python3 >/dev/null 2>&1; then
    echo "Please install Python 3."
    exit 1
fi

python3 dashboard.py
