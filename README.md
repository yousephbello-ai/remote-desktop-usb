# Remote Desktop USB Toolkit

A cross-platform starter toolkit for computers you own or are explicitly authorized to administer.

## Supported platforms
- **Windows:** PowerShell checks and opt-in RDP configuration. Microsoft's built-in RDP host is not available on Windows Home.
- **Linux:** read-only system check and guidance for distribution-specific remote desktop servers such as xrdp.
- **macOS:** read-only system check and guidance for Screen Sharing or Remote Management.

## Secure internet connectivity
Use a private, authenticated VPN such as Tailscale between devices. Do **not** forward RDP (TCP 3389) or VNC ports directly to the public internet. Authenticate each device and restrict access to trusted users.

## Repository layout
- `scripts/`: Windows PowerShell checks, enable and disable scripts.
- `config/`: optional Windows registry settings and non-secret example JSON.
- `linux/`: Linux check script and setup guidance.
- `macos/`: macOS check script and setup guidance.
- `portable/`: instructions for a normal USB toolkit.
- `bootable/`: Rufus and boot-media guidance.

## Getting started
1. Review scripts before running them.
2. On Windows, run `scripts/Check-Requirements.ps1`. If the edition supports RDP and you choose to enable it, run `scripts/Enable-RDP.ps1` in an elevated PowerShell session and confirm the prompt.
3. On Linux, run `chmod +x linux/check-system.sh && ./linux/check-system.sh`.
4. On macOS, run `chmod +x macos/check-system.sh && ./macos/check-system.sh`.
5. Install and authenticate your private VPN on both endpoints, then enable the relevant remote access service using that OS's supported settings.
6. Connect using an authorized account and the target device's private VPN address or private DNS name.

## USB options
A normal USB drive can carry this toolkit and its scripts. It does not bypass authentication or automatically configure a computer.

The bootable folder contains instructions only, not an ISO. Rufus writes a genuine OS image to USB and may erase it. Obtain images from their official publishers and verify them. A live OS does not automatically configure the installed OS for remote access. Mac boot media has model-specific requirements; Rufus is not a universal Mac boot-media solution.

## Security rules
- Never store passwords, VPN authentication keys, recovery codes, or private keys in Git or on an unencrypted USB drive.
- Do not expose RDP/VNC directly to the public internet.
- Do not use this toolkit to bypass logins, consent, or access controls.
- Keep operating systems and remote-access clients updated.

## Status
This is an initial starter toolkit, not yet a one-click installer or finished bootable image. Linux/macOS scripts currently perform read-only checks; their host configuration remains OS- and environment-specific.
