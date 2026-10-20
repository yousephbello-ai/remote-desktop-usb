
"""Remote Desktop USB Toolkit — Dashboard."""

import platform
import shutil
import subprocess
import tkinter as tk
import webbrowser

from tkinter import messagebox, simpledialog

from device_manager import add_device, remove_device, list_devices

RUSTDESK_URL = "https://rustdesk.com/"
RUSTDESK_GUIDE = "https://rustdesk.com/docs/en/"


def refresh_devices():
    device_list.delete(0, tk.END)

    for device in list_devices():
        label = device["name"]
        device_id = device.get("rustdesk_id", "")
        if device_id:
            label += f" — {device_id}"
        device_list.insert(tk.END, label)


def add_device_dialog():
    name = simpledialog.askstring(
        "Register device",
        "Enter a name for your authorized computer:",
        parent=root
    )
    if not name:
        return

    device_id = simpledialog.askstring(
        "Device ID",
        "Enter its RustDesk ID (optional):",
        parent=root
    )
    if device_id is None:
        return

    try:
        add_device(name, device_id)
        refresh_devices()
        messagebox.showinfo(
            "Saved",
            "Device record saved locally. This does not authorize access."
        )
    except (ValueError, OSError) as exc:
        messagebox.showerror("Could not add device", str(exc))


def remove_selected():
    selection = device_list.curselection()
    if not selection:
        messagebox.showinfo("Select device", "Choose a device first.")
        return

    records = list_devices()
    index = selection[0]

    if index >= len(records):
        refresh_devices()
        return

    name = records[index]["name"]

    if messagebox.askyesno(
        "Remove device",
        f"Remove '{name}' from this local registry?"
    ):
        try:
            remove_device(name)
            refresh_devices()
        except OSError as exc:
            messagebox.showerror("Could not remove device", str(exc))


def connect_selected():
    selection = device_list.curselection()
    if not selection:
        messagebox.showinfo("Select device", "Choose a device first.")
        return

    records = list_devices()
    index = selection[0]
    if index >= len(records):
        refresh_devices()
        return

    device_id = records[index].get("rustdesk_id", "")
    if not device_id:
        messagebox.showinfo(
            "Missing ID",
            "Edit this device record to add its RustDesk ID."
        )
        return

    client = shutil.which("rustdesk")
    if not client:
        messagebox.showinfo(
            "RustDesk not found",
            "Install the official client from " + RUSTDESK_URL
        )
        webbrowser.open(RUSTDESK_URL)
        return

    if not messagebox.askyesno(
        "Confirm connection",
        "Only continue if you are authorized to access this device.\n\n"
        "Open RustDesk for " + records[index]["name"] + "?"
    ):
        return

    try:
        subprocess.Popen([client, "--connect", device_id])
    except OSError as exc:
        messagebox.showerror("Launch failed", str(exc))


def show_status():
    messagebox.showinfo(
        "Toolkit status",
        f"Platform: {platform.system()}\n"
        f"Registered local records: {len(list_devices())}\n\n"
        "The dashboard does not verify remote session status."
    )


root = tk.Tk()
root.title("Remote Desktop USB Toolkit")
root.geometry("500x560")
root.minsize(360, 450)

tk.Label(
    root,
    text="Remote Desktop USB Toolkit",
    font=("Arial", 16, "bold")
).pack(pady=(16, 6))

tk.Label(
    root,
    text=f"Operating system: {platform.system()}"
).pack()

device_list = tk.Listbox(root, height=12, width=48)
device_list.pack(fill="both", expand=True, padx=16, pady=12)

buttons = [
    ("Add Authorized Device Record", add_device_dialog),
    ("Remove Selected Device", remove_selected),
    ("Refresh Device List", refresh_devices),
    ("Connect Selected with RustDesk", connect_selected),
    ("Open RustDesk Website", lambda: webbrowser.open(RUSTDESK_URL)),
    ("Read Connection Guide", lambda: webbrowser.open(RUSTDESK_GUIDE)),
    ("Check Dashboard Status", show_status),
]

for label, action in buttons:
    tk.Button(root, text=label, command=action).pack(pady=3)

tk.Label(
    root,
    text="Local records are not proof of authorization.",
    wraplength=420
).pack(pady=(8, 12))

refresh_devices()
root.mainloop()
