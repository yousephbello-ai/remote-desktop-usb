# RustDesk Integration Plan

## Why RustDesk

The toolkit will use the official RustDesk client as its remote-desktop engine rather than implementing a new screen-capture, input-control, or network protocol.

Official documentation:
- Client installation and configuration: https://rustdesk.com/docs/en/client/
- Self-hosted server overview: https://rustdesk.com/docs/en/self-host/
- Server OSS installation: https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/install/
- Client configuration: https://rustdesk.com/docs/en/self-host/client-configuration/

RustDesk documents support for Windows, macOS, multiple Linux distributions, Android, iOS (not remotely controllable), and web.

## Planned connection modes

### Mode A — public RustDesk infrastructure
Use the official RustDesk client with its default public infrastructure for initial testing. This is the simplest way to validate that two authorized devices can connect. Review the service's current privacy and operational terms before using it for sensitive work.

### Mode B — self-hosted RustDesk Server OSS
For more control, deploy the open-source RustDesk server on a dedicated, maintained Linux host or VPS. The server uses:
- `hbbs`: ID/rendezvous and signaling service.
- `hbbr`: relay service when a direct peer-to-peer connection cannot be established.

The server's public key is used by clients to verify encrypted connections. Keep the server private key on the server only; distribute only the public key to clients.

Do not deploy a public server until its host, firewall, DNS, updates, backups, and monitoring are deliberately configured. Follow the official installation guide and expose only the ports required by the chosen deployment. If WebSocket support is not needed, leave its ports closed.

## Toolkit integration rules

1. The toolkit may detect whether RustDesk is installed and open its official download/documentation page.
2. The toolkit must not silently install software, enable unattended access, create permanent passwords, or change firewall/router settings.
3. Any unattended-access setup must be an explicit local action by the device owner or authorized administrator.
4. Never place RustDesk IDs, passwords, private keys, recovery codes, or server private keys in this Git repository or on an unencrypted USB drive.
5. Use a strong unique authentication method, restrict who can connect, keep clients updated, and review session permissions.
6. Use a private VPN as an optional additional network boundary where appropriate; do not expose Windows RDP or VNC directly to the public internet.
7. A USB copy is a launcher and documentation carrier. It does not bypass login, consent, OS permissions, or endpoint security.

## Implementation stages

- [x] Select an established cross-platform remote desktop engine.
- [ ] Add read-only RustDesk installation detection to the launcher.
- [ ] Add a menu action that opens official installation and setup guidance.
- [ ] Add platform-specific, owner-confirmed setup checklists.
- [ ] Build and test portable launcher packages on Windows, Linux, and macOS.
- [ ] Validate connection between two devices owned by or explicitly authorized for the operator.
- [ ] Consider self-hosted server deployment only after the operator has a suitable server and domain/network plan.

## Current limitation

This document does not install or configure RustDesk. The toolkit remains a starter project until the later implementation and cross-platform tests are completed.
