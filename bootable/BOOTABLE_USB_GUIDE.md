# Create a bootable USB safely

## Important
- This repository does **not** provide an operating-system ISO or a custom bootable image.
- Writing an ISO to a USB drive usually erases the USB drive. Back up its contents first.
- Use a computer and USB drive you own or are authorized to manage.
- Booting a live operating system does not automatically configure remote access on the installed operating system.
- Never use boot media to bypass another person's login, encryption, or access controls.

## 1. Get an ISO from its official publisher
Choose the operating system you actually intend to boot and download its ISO only from the publisher:
- Ubuntu: https://ubuntu.com/download
- Fedora: https://fedoraproject.org/workstation/download
- Debian: https://www.debian.org/distrib/

Follow that publisher's instructions to find the checksum for the exact ISO release you downloaded. Do not copy a checksum from an unrelated mirror, forum, or different release.

## 2. Verify the ISO on Windows
1. Copy `bootable/VERIFY-ISO.ps1` to the Windows computer.
2. Open PowerShell.
3. Run `powershell -ExecutionPolicy Bypass -File .\VERIFY-ISO.ps1` from the folder containing the script, or use its full path.
4. Enter the ISO's full file path.
5. Paste the 64-character SHA-256 checksum published by the operating-system publisher.
6. Continue only if the script reports **MATCH**. A mismatch means you should not use that file.

The verifier only reads the ISO and calculates its SHA-256 hash. It does not download, mount, or flash anything.

## 3. Write the USB with Rufus on Windows
1. Download Rufus from its official website: https://rufus.ie/
2. Insert the intended USB drive and confirm its contents are backed up.
3. Open Rufus and carefully confirm the selected device is the correct USB drive.
4. Select the verified ISO and use the settings recommended by that operating-system publisher.
5. Start the write operation only after confirming the target drive. Rufus will erase the selected USB drive.
6. Safely eject the USB when Rufus finishes.

Rufus is a Windows utility; it is not a universal way to create boot media for every Mac model. For macOS installation media, follow Apple's instructions for the exact Mac model and macOS version: https://support.apple.com/en-us/101578

## 4. Boot and test
Use the computer manufacturer's documented one-time boot menu. Test the live environment without installing or changing disks first. If you do not recognize the device, stop and ask its owner or administrator.

## 5. Return to the remote-desktop project
Once the machine is running its normal installed OS, use the relevant platform check and the attended RustDesk connection guide in this repository. Bootable media is separate from remote-desktop setup and does not create a remote connection by itself.
