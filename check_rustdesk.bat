
@echo off
setlocal

echo Remote Desktop USB Toolkit
echo ==========================

where python >nul 2>&1
if errorlevel 1 (
    echo Python was not found.
    echo Install Python from https://www.python.org/
) else (
    echo Python is installed.
    python --version
)

where rustdesk >nul 2>&1
if errorlevel 1 (
    echo RustDesk was not found on PATH.
    echo It may still be installed elsewhere.
    echo Download: https://rustdesk.com/
) else (
    echo RustDesk command was found.
)

echo.
echo Check complete. No connection was started.
pause
