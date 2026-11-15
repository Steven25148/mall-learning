#!/usr/bin/env bash
set -euo pipefail
cd /mnt/d/project/mall
module=${1:-mall-admin}
debug_mode=${2:-normal}
jar_path="$module/target/$module-1.0-SNAPSHOT.jar"
if [ ! -f "$jar_path" ]; then
  echo "Missing $jar_path. Run Start-Mall.ps1 with -Build first." >&2
  exit 1
fi
java_options=(-Xms128m -Xmx512m)
if [ "$module" = mall-admin ] && [ "$debug_mode" = debug ]; then
  java_options+=('-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005')
fi
exec java "${java_options[@]}" -jar "$jar_path" --spring.datasource.username=mall --spring.datasource.password=CHANGE_ME_LOCAL_PASSWORD '--spring.datasource.url=jdbc:mysql://localhost:3306/mall?useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/Shanghai&useSSL=false&allowPublicKeyRetrieval=true' --server.address=0.0.0.0
