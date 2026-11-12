# Read-only Windows capability check
$ErrorActionPreference = 'Continue'
$os = Get-CimInstance Win32_OperatingSystem
$edition = (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion').EditionID
Write-Host "Windows: $($os.Caption)"
Write-Host "Version: $($os.Version)"
Write-Host "Edition: $edition"
if ($edition -match '^(Core|CoreSingleLanguage|CoreCountrySpecific)$') {
  Write-Warning "Windows Home cannot host Microsoft's built-in Remote Desktop."
}
$rdp = Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server'
Write-Host "RDP disabled flag: $($rdp.fDenyTSConnections) (0=enabled, 1=disabled)"
Write-Host "No settings were changed."
