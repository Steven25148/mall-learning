#!/usr/bin/env bash
set -euo pipefail
base=/mnt/d/project/local
mode=${1:-admin}
debug_mode=${2:-normal}
restart_mode=${3:-keep}

case "$mode" in
  admin) modules=(mall-admin) ;;
  all) modules=(mall-admin mall-portal mall-search) ;;
  *) echo "Unsupported mode: $mode" >&2; exit 2 ;;
esac

if [ "$mode" = all ]; then
  if ! pgrep -f '^/mnt/d/project/local/runtime/mongodb.*bin/mongod' >/dev/null; then
    "$base/runtime/mongodb-linux-x86_64-ubuntu2404-8.0.4/bin/mongod" --dbpath "$base/data/mongo" --bind_ip 127.0.0.1 --fork --logpath "$base/mongo.log"
  fi
  bash "$base/start-elasticsearch.sh"
fi

for module in "${modules[@]}"; do
  if [ "$restart_mode" = restart ] && pgrep -f "^java .*${module}/target/${module}-1.0-SNAPSHOT.jar" >/dev/null; then
    pkill -f "^java .*${module}/target/${module}-1.0-SNAPSHOT.jar"
    for attempt in $(seq 1 20); do
      if ! pgrep -f "^java .*${module}/target/${module}-1.0-SNAPSHOT.jar" >/dev/null; then break; fi
      sleep 1
    done
  fi
  if ! pgrep -f "^java .*${module}/target/${module}-1.0-SNAPSHOT.jar" >/dev/null; then
    module_debug=normal
    if [ "$module" = mall-admin ] && [ "$debug_mode" = debug ]; then module_debug=debug; fi
    nohup bash "$base/run-backend.sh" "$module" "$module_debug" > "$base/${module}.log" 2>&1 < /dev/null &
  elif [ "$module" = mall-admin ] && [ "$debug_mode" = debug ] && ! ss -ltn | grep -q ':5005 '; then
    echo 'mall-admin is already running without remote debug. Stop it before using -DebugAdmin.' >&2
    exit 1
  fi
done

for module in "${modules[@]}"; do
  case "$module" in
    mall-admin) port=8080 ;;
    mall-portal) port=8085 ;;
    mall-search) port=8081 ;;
  esac
  ready=false
  for attempt in $(seq 1 90); do
    if curl -fsS "http://127.0.0.1:${port}/actuator/health" >/dev/null; then ready=true; break; fi
    sleep 1
  done
  if [ "$ready" != true ]; then
    echo "$module did not become ready. See $base/${module}.log" >&2
    exit 1
  fi
done
