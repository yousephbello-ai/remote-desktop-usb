# Remote Desktop USB Toolkit

A cross-platform starter toolkit for computers you own or are explicitly authorized to administer.

## Supported platforms
- **Windows:** PowerShell checks and opt-in RDP configuration. Microsoft's built-in RDP host is not available on Windows Home.
- **Linux:** read-only system check and guidance for distribution-specific remote desktop servers such as xrdp.
- **macOS:** read-only system check and guidance for Screen Sharing or Remote Management.
- **RustDesk client:** official clients are available for Windows, macOS, Linux and Android. The toolkit can check common locations for an installed client and open the official download page.

## Launch the toolkit
For source-code use, Python 3 is required:
- Windows: double-click `Run-Toolkit-Windows.bat`.
- Linux/macOS: run `chmod +x run-toolkit-unix.sh && ./run-toolkit-unix.sh`.

Windows, Linux, and macOS portable packages are built by the **Build cross-platform portable packages** GitHub Actions workflow. Open the repository Actions tab, select the latest successful run, and download the artifact matching your operating system. Extract the ZIP to a USB drive. On Windows, double-click `Run-Toolkit.bat`; on Linux/macOS, run `./Run-Toolkit.sh`. The packaged launchers do not require Python; they still do not install RustDesk or change remote-access settings. Artifacts are temporary workflow downloads (30-day retention), not permanent releases.

The launcher detects the current OS, offers a read-only system check, checks common locations for RustDesk, opens the official download page, and displays setup guidance. It does not install RustDesk, enable remote access, collect credentials, or change system settings.

## Remote desktop engine
The selected remote desktop engine is **RustDesk**. See:
- [RustDesk integration plan](docs/RUSTDESK_INTEGRATION.md)
- [Connect two authorized devices](docs/CONNECT_TWO_DEVICES.md)
- [Official RustDesk client documentation](https://rustdesk.com/docs/en/client/)

The first connection milestone is an attended session using the one-time password and approval on the remote computer. Unattended access is not enabled by this toolkit.

## Secure internet connectivity
Use a private, authenticated VPN between devices where appropriate. Do **not** forward RDP (TCP 3389) or VNC ports directly to the public internet. Authenticate each device and restrict access to trusted users.

## Repository layout
- `launcher.py`: cross-platform menu launcher (Python 3).
- `Run-Toolkit-Windows.bat`, `run-toolkit-unix.sh`: launch helpers.
- `scripts/`: Windows PowerShell checks, enable and disable scripts.
- `config/`: optional Windows registry settings and non-secret example JSON.
- `linux/`: Linux check script and setup guidance.
- `macos/`: macOS check script and setup guidance.
- `portable/`: instructions for a normal USB toolkit.
- `bootable/`: boot-media guide and a read-only SHA-256 ISO verifier.
- `docs/`: architecture and connection guides.
- `tests/`: basic launcher tests.
- `.github/workflows/`: automated Python checks on pushes and pull requests.

## Getting started
1. Review scripts before running them.
2. On Windows, run `scripts/Check-Requirements.ps1`. If the edition supports RDP and you choose to enable it, run `scripts/Enable-RDP.ps1` in an elevated PowerShell session and confirm the prompt.
3. On Linux, run `chmod +x linux/check-system.sh && ./linux/check-system.sh`.
4. On macOS, run `chmod +x macos/check-system.sh && ./macos/check-system.sh`.
5. Install RustDesk on both devices from its official download page.
6. Follow [the attended connection walkthrough](docs/CONNECT_TWO_DEVICES.md). Keep someone present at the Windows computer for the first test and approve only recognized connection requests.

## USB options
A normal USB drive can carry this toolkit and its scripts. It does not bypass authentication or automatically configure a computer.

The bootable folder contains instructions and a read-only SHA-256 verifier, not an ISO. See [the bootable USB guide](bootable/BOOTABLE_USB_GUIDE.md). Rufus writes a genuine OS image to USB and may erase it. Obtain images from their official publishers and verify them. A live OS does not automatically configure the installed OS for remote access. Mac boot media has model-specific requirements; Rufus is not a universal Mac boot-media solution.

## Security rules
- Never store passwords, VPN authentication keys, recovery codes, or private keys in Git or on an unencrypted USB drive.
- Do not expose RDP/VNC directly to the public internet.
- Do not use this toolkit to bypass logins, consent, or access controls.
- Keep operating systems and remote-access clients updated.
- Prefer attended sessions and one-time passwords for initial testing. Enable unattended access only after explicit owner/admin approval and a separate security review.

## Current scope and limitations
This repository is a starter launcher and configuration toolkit, not a finished one-click remote desktop product. RustDesk detection checks common executable/application locations only; it does not prove the installed version is current or trusted. The toolkit does not install RustDesk or automate pairing. Linux/macOS scripts currently perform read-only checks; host configuration remains OS- and environment-specific. The bootable folder is documentation only; no bootable image is included. Windows RDP hosting requires a supported Windows edition. The GitHub Actions workflow runs Python launcher checks, not full operating-system integration tests.
