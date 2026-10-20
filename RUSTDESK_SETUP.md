
# RustDesk Setup Guide

## 1. Install RustDesk

Download RustDesk from the official website:

https://rustdesk.com/

Install it on both the controlling computer and the computer you are authorized to access.

## 2. Prepare the remote computer

1. Open RustDesk.
2. Find the device ID displayed by the application.
3. Keep the computer powered on and connected to the internet.
4. Configure access using RustDesk's official security settings.
5. Require the remote user to approve the session unless you have explicitly configured an authorized unattended-access arrangement.

## 3. Connect

1. Open the Remote Desktop USB Toolkit.
2. Run connect_device.py on a computer with Python and RustDesk installed.
3. Enter the authorized computer's RustDesk ID.
4. Confirm that you have permission.
5. Complete any authentication or approval prompts in RustDesk.

## 4. Security

- Never share passwords or private keys in GitHub.
- A device ID is not a password or proof of authorization.
- Use encrypted connections and strong authentication.
- Only connect to computers you own or have permission to access.

## 5. Limitations

The toolkit currently launches the RustDesk client as a prototype.
Connection success, authentication, and cross-platform command behavior
must be tested on the actual computers.
