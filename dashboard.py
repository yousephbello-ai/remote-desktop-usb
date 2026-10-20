
"""Remote Desktop USB Toolkit dashboard."""

import platform
import tkinter as tk
import webbrowser
from tkinter import messagebox


RUSTDESK_DOWNLOAD = "https://rustdesk.com/"
RUSTDESK_GUIDE = "https://rustdesk.com/docs/en/"


def open_download():
    webbrowser.open(RUSTDESK_DOWNLOAD)


def open_guide():
    webbrowser.open(RUSTDESK_GUIDE)


def show_status():
    messagebox.showinfo(
        "Connection status",
        "The dashboard is running.\n\n"
        "Remote connection integration is not configured yet."
    )


root = tk.Tk()
root.title("Remote Desktop USB Toolkit")
root.geometry("440x360")
root.minsize(360, 320)

tk.Label(
    root,
    text="Remote Desktop USB Toolkit",
    font=("Arial", 16, "bold")
).pack(pady=(24, 8))

tk.Label(
    root,
    text=f"Operating system: {platform.system()}"
).pack(pady=4)

tk.Label(
    root,
    text="Authorized device management",
    font=("Arial", 11)
).pack(pady=8)

tk.Button(
    root,
    text="Check Dashboard Status",
    command=show_status,
    width=28
).pack(pady=6)

tk.Button(
    root,
    text="Get Remote Desktop Client",
    command=open_download,
    width=28
).pack(pady=6)

tk.Button(
    root,
    text="Read Connection Guide",
    command=open_guide,
    width=28
).pack(pady=6)

tk.Label(
    root,
    text="Remote connections are not yet configured.",
    wraplength=350
).pack(pady=18)

root.mainloop()
