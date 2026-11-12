# Enables Windows RDP only after explicit confirmation. Run as Administrator.
$ErrorActionPreference = 'Stop'
$p = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $p.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
  throw "Open PowerShell as Administrator."
}
$edition = (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion').EditionID
if ($edition -match '^(Core|CoreSingleLanguage|CoreCountrySpecific)$') {
  Write-Warning "Windows Home cannot host Microsoft's built-in RDP. No changes made."
  exit 2
}
Write-Warning "Use a private authenticated VPN for internet access. Never expose TCP 3389 directly to the internet."
$answer = Read-Host "Type ENABLE to enable RDP and require Network Level Authentication"
if ($answer -cne 'ENABLE') { Write-Host "Cancelled."; exit 0 }
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections -Value 0
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication -Value 1
Write-Host "RDP enabled with NLA. No users, router rules, firewall rules, or credentials were changed."
