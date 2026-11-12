@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 launcher.py
  goto :eof
)
where python >nul 2>nul
if %errorlevel%==0 (
  python launcher.py
  goto :eof
)
echo Python 3 is required. Install it from https://www.python.org/downloads/
pause
