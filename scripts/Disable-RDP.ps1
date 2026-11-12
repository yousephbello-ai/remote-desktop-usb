# Disables Microsoft's built-in RDP host. Run as Administrator.
$ErrorActionPreference = 'Stop'
$p = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $p.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) { throw "Run as Administrator." }
$answer = Read-Host "Type DISABLE to turn off RDP"
if ($answer -cne 'DISABLE') { Write-Host "Cancelled."; exit 0 }
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections -Value 1
Write-Host "RDP disabled. Review any custom firewall rules separately."
