#!/usr/bin/env bash
set -eu
echo "Remote Desktop USB Toolkit — macOS check"
echo "Computer: $(scutil --get ComputerName 2>/dev/null || hostname)"
echo "macOS: $(sw_vers -productVersion)"
echo "Architecture: $(uname -m)"
command -v tailscale >/dev/null 2>&1 && echo "Tailscale CLI detected" || echo "Tailscale CLI not detected (app may still be installed)"
echo "Read-only check: no settings changed."
