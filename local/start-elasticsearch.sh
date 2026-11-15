#!/usr/bin/env bash
set -euo pipefail
base=/mnt/d/project/local
if curl --noproxy '*' -fsS --max-time 3 http://127.0.0.1:9200 >/dev/null 2>&1; then
  echo 'Elasticsearch is already running.'
  exit 0
fi
if ! pgrep -f '^/mnt/d/project/local/runtime/elasticsearch-8.18.0/jdk/bin/java.*org.elasticsearch.bootstrap.Elasticsearch' >/dev/null; then
  ES_JAVA_OPTS='-Xms512m -Xmx512m -Djava.net.preferIPv4Stack=true' nohup "$base/runtime/elasticsearch-8.18.0/bin/elasticsearch" >> "$base/elasticsearch.log" 2>&1 < /dev/null &
fi
for attempt in $(seq 1 90); do
  if curl --noproxy '*' -fsS --max-time 2 http://127.0.0.1:9200 2>/dev/null; then
    exit 0
  fi
  sleep 1
done
echo "Startup failed or timed out. See $base/elasticsearch.log" >&2
exit 1
