import importlib.util
import platform
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("launcher", ROOT / "launcher.py")
launcher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(launcher)

class LauncherTests(unittest.TestCase):
    def test_project_readme_exists(self):
        self.assertTrue((ROOT / "README.md").is_file())

    def test_platform_check_scripts_exist(self):
        self.assertTrue((ROOT / "scripts" / "Check-Requirements.ps1").is_file())
        self.assertTrue((ROOT / "linux" / "check-system.sh").is_file())
        self.assertTrue((ROOT / "macos" / "check-system.sh").is_file())

    def test_detected_platform_is_a_string(self):
        self.assertIsInstance(platform.system(), str)

    def test_rustdesk_download_url_is_official(self):
        self.assertEqual(launcher.RUSTDESK_DOWNLOADS, "https://rustdesk.com/download/")

    def test_rustdesk_detection_is_read_only_result(self):
        result = launcher.find_rustdesk()
        self.assertTrue(result is None or isinstance(result, str))

    def test_rustdesk_integration_document_exists(self):
        self.assertTrue((ROOT / "docs" / "RUSTDESK_INTEGRATION.md").is_file())

if __name__ == "__main__":
    unittest.main()
