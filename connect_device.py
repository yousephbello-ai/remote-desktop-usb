
"""Launch RustDesk for an authorized device."""

import re
import shutil
import subprocess
import sys


def main():
    if len(sys.argv) > 2:
        print("Usage: python connect_device.py [DEVICE_ID]")
        return 2

    device_id = sys.argv[1] if len(sys.argv) == 2 else input(
        "Enter the RustDesk ID of your authorized device: "
    ).strip()

    if not re.fullmatch(r"[A-Za-z0-9-]{6,32}", device_id):
        print("Invalid device ID format.")
        return 2

    client = shutil.which("rustdesk")
    if not client:
        print("RustDesk was not found on this computer.")
        print("Install it from https://rustdesk.com/")
        return 1

    print("Device ID:", device_id)
    answer = input(
        "Continue only if you have permission to access this device. "
        "Open RustDesk? Type YES to continue: "
    ).strip()

    if answer != "YES":
        print("Cancelled.")
        return 0

    try:
        # Open the client; do not assume this argument starts a session
        # on every RustDesk version or operating system.
        subprocess.Popen([client, device_id])
        print("RustDesk was launched. Complete connection approval in the app.")
        return 0
    except OSError as exc:
        print("Could not launch RustDesk:", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
