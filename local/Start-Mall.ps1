param(
  [ValidateSet('Infra', 'Admin', 'All')]
  [string]$Mode = 'Admin',
  [switch]$Build,
  [switch]$DebugAdmin,
  [switch]$SkipFrontend
)

$ErrorActionPreference = 'Stop'
$base = $PSScriptRoot
$distro = 'Ubuntu-24.04'

if ($Mode -eq 'All') {
  $systemServices = @('mysql', 'redis-server', 'rabbitmq-server')
} else {
  $systemServices = @('mysql', 'redis-server')
}

Write-Host "Starting WSL infrastructure for mode: $Mode"
wsl -d $distro -u root -- systemctl start @systemServices
if ($LASTEXITCODE -ne 0) { throw 'Unable to start WSL infrastructure services.' }

if ($Build) {
  if ($Mode -eq 'Infra') { throw '-Build requires -Mode Admin or -Mode All.' }
  $buildCommand = if ($Mode -eq 'All') {
    'cd /mnt/d/project/mall && mvn package -DskipTests -Ddocker.skip=true'
  } else {
    'cd /mnt/d/project/mall && mvn -pl mall-admin -am package -DskipTests -Ddocker.skip=true'
  }
  Write-Host 'Building backend JAR files...'
  wsl -d $distro -- bash -lc $buildCommand
  if ($LASTEXITCODE -ne 0) { throw 'Backend build failed.' }
}

if ($Mode -ne 'Infra') {
  $debugFlag = if ($DebugAdmin) { 'debug' } else { 'normal' }
  $restartFlag = if ($Build) { 'restart' } else { 'keep' }
  wsl -d $distro -- bash /mnt/d/project/local/start-backends.sh ($Mode.ToLowerInvariant()) $debugFlag $restartFlag
  if ($LASTEXITCODE -ne 0) { throw 'Unable to start backend services. Check D:\project\local\mall-*.log.' }
}

$guestIp = ((wsl -d $distro -- hostname -I).Trim() -split '\s+')[0]
if (!$guestIp) { throw 'Unable to determine the Ubuntu WSL IP address.' }

if ($Mode -ne 'Infra' -and !$SkipFrontend) {
  $frontend = Join-Path $base '..\mall-admin-web'
  Set-Content (Join-Path $frontend '.env.development.local') "VITE_BASE_SERVER_URL=http://${guestIp}:8080"
  $nodeCommand = Get-Command node -ErrorAction SilentlyContinue
  $nodePath = if ($nodeCommand) { $nodeCommand.Source } else { "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe" }
  if (!(Test-Path $nodePath)) { throw "Node.js was not found: $nodePath" }
  try {
    $null = Invoke-WebRequest http://127.0.0.1:5173 -TimeoutSec 2
  } catch {
    Start-Process -FilePath $nodePath -ArgumentList 'node_modules/vite/bin/vite.js --host 127.0.0.1 --port 5173 --strictPort' -WorkingDirectory $frontend -WindowStyle Hidden -RedirectStandardOutput (Join-Path $base 'web.log') -RedirectStandardError (Join-Path $base 'web-error.log')
  }
}

Write-Host ''
Write-Host "WSL IP: $guestIp"
if ($Mode -eq 'Infra') {
  Write-Host 'MySQL and Redis are ready. Start MallAdminApplication in IDEA with Debug.'
} else {
  if (!$SkipFrontend) { Write-Host 'Admin UI: http://127.0.0.1:5173' }
  Write-Host "Admin Swagger: http://${guestIp}:8080/swagger-ui.html"
  if ($Mode -eq 'All') {
    Write-Host "Portal Swagger: http://${guestIp}:8085/swagger-ui.html"
    Write-Host "Search Swagger: http://${guestIp}:8081/swagger-ui.html"
  }
  if ($DebugAdmin) { Write-Host "Remote debug: attach IDEA to ${guestIp}:5005 before sending the request." }
  Write-Host 'Local demo login: admin / macro123'
}
