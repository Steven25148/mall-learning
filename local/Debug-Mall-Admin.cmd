@echo off
title Mall Admin Debug Launcher
echo Starting MySQL, Redis, mall-admin and the admin web UI...
echo The backend will be rebuilt and remote debugging will listen on port 5005.
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Start-Mall.ps1" -Mode Admin -Build -DebugAdmin
if errorlevel 1 (
  echo.
  echo Startup failed. Check the messages above and D:\project\local\mall-admin.log.
  pause
  exit /b 1
)
echo.
echo Startup completed. Keep this window for the printed URLs and WSL IP.
pause
