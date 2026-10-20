
"""Remote Desktop USB Toolkit.
Dashboard and authorized-device launcher.
"""

import json
import platform
import re
import shutil
import subprocess
import sys
import tkinter as tk
import webbrowser

from pathlib import Path
from tkinter import messagebox, simpledialog

BASE_DIR = Path(__file__).resolve().parent
REGISTRY = BASE_DIR / "device_registry.json"

RUSTDESK_URL = "https://rustdesk.com/"
RUSTDESK_GUIDE = "https://rustdesk.com/docs/en/"


def load_devices():
    """Load the locally stored device names."""
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        devices = data.get("devices", [])
        return [
            device for device in devices
            if isinstance(device, dict)
            and isinstance(device.get("name"), str)
        ]
    except (OSError, json.JSONDecodeError):
        return []


def save_devices(devices):
    """Save device names without storing credentials."""
    data = {
        "devices": devices,
        "security": {
            "require_authentication": True,
            "require_user_approval": True,
            "encrypted_connections_only": True
        }
    }

    REGISTRY.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )


def refresh_devices():
    device_list.delete(0, tk.END)

    for device in load_devices():
        device_list.insert(tk.END, device["name"])


def add_device():
    name = simpledialog.askstring(
        "Register device",
        "Enter a name for your authorized computer:",
        parent=root
    )

    if not name or not name.strip():
        return

    name = name.strip()
    devices = load_devices()

    if any(d["name"].casefold() == name.casefold()
           for d in devices):
        messagebox.showinfo(
            "Already registered",
            "That device name is already in the list."
        )
        return

    devices.append({"name": name})
    try:
        save_devices(devices)
        refresh_devices()
        messagebox.showinfo(
            "Device added",
            "Device name saved locally. This does not connect it."
        )
    except OSError as exc:
        messagebox.showerror(
            "Save failed",
            str(exc)
        )


def remove_device():
    selection = device_list.curselection()

    if not selection:
        messagebox.showinfo(
            "Select a device",
            "Choose a device name first."
        )
        return

    name = device_list.get(selection[0])

    if not messagebox.askyesno(
        "Remove device",
        f"Remove '{name}' from this local list?"
    ):
        return

    devices = [
        d for d in load_devices()
        if d["name"] != name
    ]

    try:
        save_devices(devices)
        refresh_devices()
    except OSError as exc:
        messagebox.showerror("Save failed", str(exc))


def connect_device():
    """Ask for a RustDesk ID and launch an installed client."""
    device_id = simpledialog.askstring(
        "Connect with RustDesk",
        "Enter the RustDesk ID of a computer you are authorized to access:",
        parent=root
    )

    if not device_id:
        return

    device_id = device_id.strip()

    if not re.fullmatch(r"[A-Za-z0-9-]{6,32}", device_id):
        messagebox.showerror(
            "Invalid ID",
            "Check the device ID and try again."
        )
        return

    client = shutil.which("rustdesk")

    if not client:
        messagebox.showinfo(
            "RustDesk not found",
            "Install the official RustDesk client on this computer:\n"
            + RUSTDESK_URL
        )
        webbrowser.open(RUSTDESK_URL)
        return

    try:
        # Client command-line behavior can vary by version.
        subprocess.Popen([client, "--connect", device_id])
        messagebox.showinfo(
            "Client launched",
            "RustDesk was asked to open. Complete its normal "
            "authentication and approval steps."
        )
    except OSError as exc:
        messagebox.showerror(
            "Launch failed",
            str(exc)
        )


def open_rustdesk():
    webbrowser.open(RUSTDESK_URL)


def open_guide():
    webbrowser.open(RUSTDESK_GUIDE)


def show_status():
    messagebox.showinfo(
        "Toolkit status",
        f"Dashboard platform: {platform.system()}\n\n"
        f"Registered local device names: {len(load_devices())}\n\n"
        "Remote sessions are not verified by this dashboard.\n"
        "RustDesk must be installed and configured separately."
    )


root = tk.Tk()
root.title("Remote Desktop USB Toolkit")
root.geometry("480x570")
root.minsize(360, 460)

tk.Label(
    root,
    text="Remote Desktop USB Toolkit",
    font=("Arial", 16, "bold")
).pack(pady=(18, 5))

tk.Label(
    root,
    text=f"Operating system: {platform.system()}"
).pack(pady=3)

tk.Label(
    root,
    text="Local device names",
    font=("Arial", 11, "bold")
).pack(pady=(12, 4))

device_list = tk.Listbox(root, height=9, width=42)
device_list.pack(fill="both", expand=True, padx=18, pady=6)

buttons = [
    ("Add Device Name", add_device),
    ("Remove Selected Name", remove_device),
    ("Refresh Device List", refresh_devices),
    ("Connect Using RustDesk", connect_device),
    ("Get RustDesk Client", open_rustdesk),
    ("Read Connection Guide", open_guide),
    ("Check Dashboard Status", show_status),
]

for label, action in buttons:
    tk.Button(
        root,
        text=label,
        command=action,
        width=30
    ).pack(pady=3)

tk.Label(
    root,
    text="Device names are local records, not proof of authorization.",
    wraplength=420
).pack(pady=(10, 14))

refresh_devices()
root.mainloop()
