
"""Check the basic structure of Remote Desktop USB Toolkit."""

import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "README.md",
    "main.py",
    "config.json",
    "device_manager.py",
    "device_registry.json",
    "remote_access.json",
    "dashboard.py",
    "test_device_manager.py",
    "run_tests.sh",
    "SECURITY.md",
]

def main():
    print("Remote Desktop USB Toolkit — Project Check")
    print("Operating system:", platform.system())
    print("Python version:", sys.version.split()[0])
    print()

    missing = []

    for filename in REQUIRED_FILES:
        if (ROOT / filename).is_file():
            print("[OK]     ", filename)
        else:
            print("[MISSING]", filename)
            missing.append(filename)

    print()
    if missing:
        print("Check finished. Some files are missing.")
        return 1

    print("All required files are present.")
    print("This check does not test remote connections or security.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
