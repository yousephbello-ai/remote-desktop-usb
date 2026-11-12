# Connect Two Authorized Devices

This guide uses the official RustDesk client. The first milestone is an attended session: a person at the remote computer can see and approve the connection.

Official client guide: https://rustdesk.com/docs/en/client/

## 1. Prepare the Windows computer you want to access

1. Sign in to Windows using an account authorized to administer that computer.
2. Download RustDesk only from https://rustdesk.com/download/ or the official RustDesk GitHub releases linked from its website.
3. Install and open RustDesk.
4. Follow RustDesk's on-screen permission prompts. Do not dismiss security warnings.
5. Keep the RustDesk window visible. Note the device ID shown by RustDesk.
6. For the first test, use the displayed one-time password and keep a person present at the Windows computer to approve the incoming session.

## 2. Prepare the controlling device

Install the official RustDesk client on the device you will use to connect. RustDesk publishes clients for Windows, macOS, Linux and Android. iOS can initiate some workflows but cannot be controlled remotely according to the current client documentation.

## 3. Start an attended connection

1. On the controlling device, open RustDesk.
2. Enter the Windows computer's RustDesk ID in the connection field.
3. Select Connect.
4. Enter the current one-time password supplied by the person at the Windows computer, if requested.
5. The person at the Windows computer should review the request and approve it only if they recognize the operator.
6. Confirm that keyboard, mouse, screen and clipboard permissions are appropriate for the task.
7. End the session when finished.

Never post a device ID together with a password in a public issue, chat, screenshot, or repository. Do not share the one-time password with anyone you do not trust.

## 4. Security settings

- Keep attended approval enabled for the initial setup.
- Use a strong unique password if you later choose to enable unattended access; store it in a reputable password manager, never in this repository or on an unencrypted USB drive.
- Restrict incoming access using RustDesk's security settings and approved device/user controls where available. An ID allowlist is an extra filter, not a substitute for authentication.
- Keep RustDesk and the operating system updated.
- Do not expose RDP or VNC ports directly to the public internet.
- Do not enable unattended access on a computer unless its owner or authorized administrator explicitly approves it and understands the risk.

## 5. Troubleshooting

- If the device ID is not visible, confirm RustDesk is running and shows a ready/online status.
- If macOS is the controlled device, grant only the required Screen Recording and Accessibility permissions through macOS privacy settings.
- On Linux, desktop environment, display server and session type can affect remote-control permissions.
- If a connection fails, check that both devices have internet access and that security software is not blocking the official client. Do not disable the firewall wholesale.

## Scope of this milestone

This guide does not automate installation, password setup, service installation, firewall changes, or unattended access. Those steps remain explicit actions in the official client UI.
