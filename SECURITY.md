
# Security Policy

## Purpose
This project is intended for remote desktop access to computers owned by the operator or managed with explicit permission.

## Required protections
- Require authentication before allowing a connection.
- Require the remote user to approve access.
- Encrypt connections in transit.
- Use unique credentials for each authorized device.
- Provide a clear way to end a remote session.
- Keep an audit log of connection attempts and sessions.
- Never expose remote desktop ports directly to the public internet without appropriate protection.
- Never store passwords, private keys, or access tokens in GitHub.

## Network design
Prefer a trusted VPN or an established secure remote-access solution rather than building a custom internet-facing remote-control protocol.

## Supported platforms
Windows and Linux are initial targets. macOS support requires separate testing and appropriate operating-system permissions.

## Reporting security issues
Do not publish private credentials, access tokens, or sensitive device information in issue reports.
