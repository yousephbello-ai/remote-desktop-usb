#!/usr/bin/env bash

echo "======================================"
echo "     Remote Desktop USB Toolkit"
echo "======================================"
echo

cd "$(dirname "$0")" || exit 1

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 was not found."
    echo "Install Python 3 using your Linux package manager."
    exit 1
fi

python3 main.py

echo
read -r -p "Press Enter to exit..."
