
"""Basic tests for the local device registry."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import device_manager


class DeviceManagerTests(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.registry = Path(self.temp_dir.name) / "device_registry.json"
        self.patch_registry = patch.object(
            device_manager, "REGISTRY", self.registry
        )
        self.patch_registry.start()

    def tearDown(self):
        self.patch_registry.stop()
        self.temp_dir.cleanup()

    def test_add_and_list_device(self):
        device_manager.add_device("My Test PC", "123456789")
        devices = device_manager.list_devices()

        self.assertEqual(len(devices), 1)
        self.assertEqual(devices[0]["name"], "My Test PC")
        self.assertEqual(devices[0]["rustdesk_id"], "123456789")

    def test_duplicate_name_is_rejected(self):
        device_manager.add_device("My PC")
        with self.assertRaises(ValueError):
            device_manager.add_device("my pc")

    def test_invalid_id_is_rejected(self):
        with self.assertRaises(ValueError):
            device_manager.add_device("My PC", "bad id!")

    def test_remove_device(self):
        device_manager.add_device("My PC")
        self.assertTrue(device_manager.remove_device("My PC"))
        self.assertEqual(device_manager.list_devices(), [])

    def test_registry_is_valid_json(self):
        device_manager.add_device("My PC")
        data = json.loads(self.registry.read_text(encoding="utf-8"))
        self.assertIn("devices", data)


if __name__ == "__main__":
    unittest.main()
