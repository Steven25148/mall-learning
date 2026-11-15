$ErrorActionPreference = 'Stop'
$base = Join-Path $PSScriptRoot 'runtime/mysql-8.4.13-winx64'
$data = Join-Path $PSScriptRoot 'mysql-data'
$existing = Get-Process mysqld -ErrorAction SilentlyContinue
if ($existing) { Write-Host 'MySQL is already running.'; exit }
Start-Process -FilePath "$base/bin/mysqld.exe" -ArgumentList '--no-defaults',"--basedir=$base","--datadir=$data",'--bind-address=127.0.0.1','--port=3306' -WindowStyle Hidden -RedirectStandardOutput "$PSScriptRoot/mysql-out.log" -RedirectStandardError "$PSScriptRoot/mysql-error.log"
