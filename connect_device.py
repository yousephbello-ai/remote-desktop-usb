
"""Launcher for authorized RustDesk sessions."""

import re
import shutil
import subprocess
import sys


def main():
    print("Remote Desktop USB Toolkit")
    print("Use only computers you are authorized to access.\n")

    device_id = input("Enter the authorized RustDesk device ID: ").strip()

    if not re.fullmatch(r"[A-Za-z0-9-]{6,32}", device_id):
        print("Invalid ID format.")
        return

    client = shutil.which("rustdesk")

    if not client:
        print("RustDesk was not found on this computer.")
        print("Install the official client from https://rustdesk.com/")
        return

    print("Opening RustDesk for the selected device...")
    try:
        subprocess.Popen([client, "--connect", device_id])
    except OSError as exc:
        print(f"Could not launch RustDesk: {exc}")


if __name__ == "__main__":
    main()
