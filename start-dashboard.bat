
@echo off
title Remote Desktop USB Toolkit

cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
    echo Python was not found.
    echo Install Python 3 from https://www.python.org/
    pause
    exit /b 1
)

python dashboard.py

if errorlevel 1 (
    echo.
    echo The dashboard encountered an error.
    echo Check that Python and Tkinter are installed.
    pause
)
