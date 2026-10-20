
"""Remote Desktop USB Toolkit — device dashboard."""

import json
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, simpledialog

REGISTRY = Path(__file__).parent / "device_registry.json"


def load_devices():
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        return data.get("devices", [])
    except (OSError, json.JSONDecodeError):
        return []


def refresh_devices():
    device_list.delete(0, tk.END)
    for device in load_devices():
        device_list.insert(tk.END, device["name"])


def add_device():
    name = simpledialog.askstring(
        "Register device",
        "Enter a name for your authorized computer:"
    )
    if not name or not name.strip():
        return

    devices = load_devices()
    devices.append({"name": name.strip()})

    REGISTRY.write_text(
        json.dumps(
            {
                "devices": devices,
                "security": {
                    "require_authentication": True,
                    "require_user_approval": True,
                    "encrypted_connections_only": True
                }
            },
            indent=2
        ),
        encoding="utf-8"
    )

    refresh_devices()
    messagebox.showinfo(
        "Device added",
        "The device name was saved locally."
    )


root = tk.Tk()
root.title("Remote Desktop USB Toolkit")
root.geometry("440x420")

tk.Label(
    root,
    text="Authorized Device Manager",
    font=("Arial", 16, "bold")
).pack(pady=16)

device_list = tk.Listbox(root, height=12, width=42)
device_list.pack(padx=16, pady=8)

tk.Button(
    root,
    text="Add Device Name",
    command=add_device
).pack(pady=6)

tk.Button(
    root,
    text="Refresh List",
    command=refresh_devices
).pack(pady=6)

tk.Label(
    root,
    text="Names only — remote connections are not enabled.",
    wraplength=360
).pack(pady=12)

refresh_devices()
root.mainloop()
