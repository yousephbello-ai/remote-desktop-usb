
"""Local device registry for Remote Desktop USB Toolkit."""

import json
import re
from pathlib import Path

REGISTRY = Path(__file__).resolve().parent / "device_registry.json"


def load_registry():
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return {"devices": []}

        devices = data.get("devices", [])
        if not isinstance(devices, list):
            devices = []

        return {"devices": [
            d for d in devices
            if isinstance(d, dict)
            and isinstance(d.get("name"), str)
        ]}
    except (OSError, json.JSONDecodeError):
        return {"devices": []}


def save_registry(data):
    REGISTRY.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )


def add_device(name, rustdesk_id=""):
    name = name.strip()
    rustdesk_id = rustdesk_id.strip()

    if not name or len(name) > 80:
        raise ValueError("Enter a name between 1 and 80 characters.")

    if rustdesk_id and not re.fullmatch(
        r"[A-Za-z0-9-]{6,32}", rustdesk_id
    ):
        raise ValueError("The device ID format is invalid.")

    data = load_registry()

    if any(
        d["name"].casefold() == name.casefold()
        for d in data["devices"]
    ):
        raise ValueError("That device name already exists.")

    record = {"name": name}
    if rustdesk_id:
        record["rustdesk_id"] = rustdesk_id

    data["devices"].append(record)
    save_registry(data)
    return record


def remove_device(name):
    data = load_registry()
    original_count = len(data["devices"])

    data["devices"] = [
        d for d in data["devices"]
        if d["name"] != name
    ]

    save_registry(data)
    return len(data["devices"]) < original_count


def list_devices():
    return load_registry()["devices"]


if __name__ == "__main__":
    print("Remote Desktop USB — Local Device Registry")
    for device in list_devices():
        print("-", device["name"])
  
