Write-Host "Operating system: Windows"
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture
