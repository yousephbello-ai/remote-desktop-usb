# Verify an operating-system ISO against a SHA-256 value from its official publisher.
# This script is read-only: it does not download, mount, or write images to USB media.

$ErrorActionPreference = "Stop"

Write-Host "ISO SHA-256 verifier" -ForegroundColor Cyan
Write-Host "This checks a local ISO only. It will not write to or format a USB drive."
$isoPath = Read-Host "Enter the full path to the ISO file"
if ([string]::IsNullOrWhiteSpace($isoPath) -or -not (Test-Path -LiteralPath $isoPath -PathType Leaf)) {
    Write-Error "The ISO file was not found. Check the path and try again."
    exit 1
}

$expected = (Read-Host "Paste the official SHA-256 checksum").Trim()
if ($expected -notmatch '^[A-Fa-f0-9]{64}$') {
    Write-Error "The checksum must contain exactly 64 hexadecimal characters."
    exit 1
}

$actual = (Get-FileHash -LiteralPath $isoPath -Algorithm SHA256).Hash
Write-Host ""
Write-Host "Calculated: $actual"
Write-Host "Expected:   $($expected.ToUpperInvariant())"

if ($actual -eq $expected.ToUpperInvariant()) {
    Write-Host "MATCH: the file matches the checksum you supplied." -ForegroundColor Green
    exit 0
}

Write-Host "MISMATCH: do not use this ISO. Re-download it from the official publisher and verify the published checksum." -ForegroundColor Red
exit 2
