
# Remote Desktop USB Toolkit — Start Here

Welcome! This project is a prototype for organizing authorized
remote desktop connections using RustDesk.

## Before you start

- Use only computers you own or have permission to access.
- Install RustDesk on the controlling and remote computers.
- Keep authentication enabled.
- Require remote-user approval unless an authorized unattended-access
  arrangement has been explicitly configured.
- Never store passwords, private keys, or access tokens in this repository.

## Windows

1. Open the project folder.
2. Run `check_rustdesk.bat`.
3. Read `RUSTDESK_SETUP.md` before connecting.

## Linux

1. Open a terminal in the project folder.
2. Run `bash check_rustdesk.sh`.
3. Read `RUSTDESK_SETUP.md` before connecting.

## Python tests

Run:

`python -m unittest -v test_device_manager.py`

## Current limitations

- The dashboard and registry are prototypes.
- A saved device record does not prove authorization.
- The launcher has not been verified across all RustDesk versions.
- This project does not create a bootable operating system.
- Remote sessions, authentication, and security still require real-world testing.

## Official RustDesk resources

Website: https://rustdesk.com/

Documentation: https://rustdesk.com/docs/en/
