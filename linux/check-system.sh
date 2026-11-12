#!/usr/bin/env bash
set -eu
echo "Remote Desktop USB Toolkit — Linux check"
echo "Host: $(hostname)"
if [ -r /etc/os-release ]; then . /etc/os-release; echo "Distribution: ${PRETTY_NAME:-unknown}"; fi
echo "Kernel: $(uname -sr)"
command -v tailscale >/dev/null 2>&1 && echo "Tailscale CLI detected" || echo "Tailscale CLI not detected"
echo "Read-only check: no settings changed."
