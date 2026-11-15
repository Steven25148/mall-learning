#!/usr/bin/env bash
set -euo pipefail
systemctl start mysql redis-server rabbitmq-server
mysql < /mnt/d/project/local/init-user.sql
count=$(mysql -N -e "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='mall'")
if [ "$count" = 0 ]; then mysql mall < /mnt/d/project/mall/document/sql/mall.sql; fi
rabbitmqctl add_vhost /mall || true
rabbitmqctl add_user mall mall || true
rabbitmqctl set_permissions -p /mall mall '.*' '.*' '.*'
