@echo off
title Mall Full Project Launcher
echo Starting the complete local mall environment...
echo This includes infrastructure, all three backends and the admin web UI.
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Start-Mall.ps1" -Mode All
if errorlevel 1 (
  echo.
  echo Startup failed. Check the messages above and D:\project\local\*.log.
  pause
  exit /b 1
)
echo.
echo Startup completed. Keep this window for the printed URLs.
pause
