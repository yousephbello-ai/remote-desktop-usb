LINUX SUPPORT
Run: chmod +x check-system.sh && ./check-system.sh
For internet access, install Tailscale using its official instructions and authenticate the device to your own private network.
For incoming desktop access, a server such as xrdp may be appropriate depending on distribution and desktop environment.
Do not expose RDP or VNC ports directly to the public internet. Keep the OS updated and use strong account credentials.
The included check script is read-only; it does not install software or change firewall settings.
