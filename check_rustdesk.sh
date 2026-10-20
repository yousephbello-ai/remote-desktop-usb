
#!/usr/bin/env bash

echo "Remote Desktop USB Toolkit"
echo "=========================="

if command -v python3 >/dev/null 2>&1; then
    echo "Python is installed:"
    python3 --version
else
    echo "Python 3 was not found."
fi

if command -v rustdesk >/dev/null 2>&1; then
    echo "RustDesk command was found:"
    command -v rustdesk
else
    echo "RustDesk was not found on PATH."
    echo "It may still be installed elsewhere."
    echo "Download: https://rustdesk.com/"
fi

echo
echo "Check complete. No connection was started."
