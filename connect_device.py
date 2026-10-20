
"""Open the official remote desktop client website."""

import webbrowser

RUSTDESK_URL = "https://rustdesk.com/"


def main():
    print("Remote Desktop USB Toolkit")
    print("Remote sessions are not configured by this script.")
    print("Opening the official RustDesk website...")

    webbrowser.open(RUSTDESK_URL)


if __name__ == "__main__":
    main()
