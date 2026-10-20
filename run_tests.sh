
#!/usr/bin/env bash
set -e

echo "Remote Desktop USB Toolkit"
echo "Running device manager tests..."

python3 -m unittest -v test_device_manager.py

echo
echo "Tests completed successfully."
