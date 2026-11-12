#!/usr/bin/env python3
"""Cross-platform menu for the Remote Desktop USB Toolkit.

This launcher is intentionally non-privileged and does not enable remote access.
It detects the current OS, performs read-only checks, and opens official guidance.
"""
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import webbrowser

ROOT = Path(__file__).resolve().parent
RUSTDESK_DOWNLOADS = "https://rustdesk.com/download/"

def find_rustdesk():
    """Return a likely RustDesk executable/app path, or None; never runs it."""
    for executable in ("rustdesk", "rustdesk.exe"):
        found = shutil.which(executable)
        if found:
            return found

    system = platform.system()
    candidates = []
    if system == "Windows":
        for variable in ("ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA"):
            base = __import__("os").environ.get(variable)
            if base:
                candidates.append(Path(base) / "RustDesk" / "rustdesk.exe")
    elif system == "Darwin":
        candidates.append(Path("/Applications/RustDesk.app"))
    elif system == "Linux":
        candidates.extend((Path("/usr/bin/rustdesk"), Path("/usr/local/bin/rustdesk")))
    return next((str(path) for path in candidates if path.exists()), None)

def check_rustdesk():
    location = find_rustdesk()
    if location:
        print("RustDesk appears to be installed:", location)
        print("Open it yourself and verify the device identity and access permissions.")
    else:
        print("RustDesk was not found in common installation locations.")
        print("Use option 4 to open the official download page.")
    return location

def run_read_only_check():
    system = platform.system()
    if system == "Windows":
        script = ROOT / "scripts" / "Check-Requirements.ps1"
        command = ["powershell", "-NoProfile", "-ExecutionPolicy", "RemoteSigned", "-File", str(script)]
    elif system == "Linux":
        script = ROOT / "linux" / "check-system.sh"
        command = ["bash", str(script)]
    elif system == "Darwin":
        script = ROOT / "macos" / "check-system.sh"
        command = ["bash", str(script)]
    else:
        print(f"Unsupported operating system: {system}")
        return
    if not script.is_file():
        print(f"Check script not found: {script}")
        return
    subprocess.run(command, check=False)

def show_guidance():
    system = platform.system()
    print("\nDetected platform:", system)
    if system == "Windows":
        print("Review scripts/Enable-RDP.ps1. Run it manually as Administrator only if this PC supports RDP hosting.")
        print("Windows Home cannot host Microsoft's built-in RDP server.")
    elif system == "Linux":
        print("Read linux/README.txt. Incoming desktop setup depends on your distribution and desktop environment.")
    elif system == "Darwin":
        print("Read macos/README.txt. Enable Screen Sharing or Remote Management deliberately in System Settings.")
    else:
        print("See README.md for platform support.")
    print("\nRustDesk is the planned cross-platform remote desktop engine.")
    print("Read docs/RUSTDESK_INTEGRATION.md before configuring a connection.")
    print("Use an authenticated private VPN where appropriate.")
    print("Never expose RDP (TCP 3389) or VNC directly to the public internet.")
    print("This launcher does not store credentials or change system settings.")

def main():
    print("Remote Desktop USB Toolkit")
    print("==========================")
    print("Detected OS:", platform.system(), platform.release(), platform.machine())
    while True:
        print("\n1. Run read-only system check")
        print("2. Show setup guidance")
        print("3. Check whether RustDesk appears to be installed")
        print("4. Open the official RustDesk download page")
        print("5. Display project README")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            run_read_only_check()
        elif choice == "2":
            show_guidance()
        elif choice == "3":
            check_rustdesk()
        elif choice == "4":
            opened = webbrowser.open(RUSTDESK_DOWNLOADS)
            if not opened:
                print("Could not open a browser. Visit:", RUSTDESK_DOWNLOADS)
        elif choice == "5":
            readme = ROOT / "README.md"
            print(readme.read_text(encoding="utf-8") if readme.exists() else "README.md not found.")
        elif choice == "0":
            return
        else:
            print("Please choose 0, 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        sys.exit(0)
