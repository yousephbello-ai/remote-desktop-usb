
# Remote Access Setup

## Provider
This project plans to integrate with RustDesk for remote desktop connectivity.

Official website: https://rustdesk.com/

Documentation: https://rustdesk.com/docs/en/

## Initial setup
1. Install the official RustDesk client on each authorized computer.
2. Configure and test the client locally before connecting over the internet.
3. Verify each computer's identity through a trusted channel.
4. Require authentication and obtain permission from the computer's owner.
5. Use encrypted connections and keep all clients updated.

## Custom dashboard integration
The current Python dashboard manages device names only.
It does not yet launch authenticated sessions or retrieve connection status.

A future integration must use documented provider capabilities and must not expose credentials in source code.

## Network options
Use the provider's supported infrastructure or a properly secured, self-hosted deployment. Review the provider's security and firewall documentation before changing network settings.

## USB limitations
The USB drive contains the toolkit, not a complete remote desktop operating system.
Remote access software may require installation, operating-system permissions, or additional configuration on each target computer.

## Safety
Only connect to computers you own or have explicit authorization to administer.
