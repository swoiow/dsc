#!/bin/sh
set -eu

: "${PUID:=65534}"
: "${PGID:=65534}"
: "${TZ:=Asia/Shanghai}"

# 可选：运行时覆盖时区
if [ -f "/usr/share/zoneinfo/$TZ" ]; then
  cp "/usr/share/zoneinfo/$TZ" /etc/localtime 2>/dev/null || true
  echo "$TZ" > /etc/timezone 2>/dev/null || true
fi

mkdir -p /app/configs/ /aria2/downloads
touch /app/configs/aria2.session

# 首次启动：把默认配置落到挂载目录
if [ ! -f /app/configs/aria2.conf ]; then
  cp /etc/aria2.conf /app/configs/aria2.conf
fi

# 如果容器以 root 运行：先修权限，再降权跑 aria2
if [ "$(id -u)" = "0" ]; then
  chown -R "$PUID:$PGID" /app/configs/ /aria2/downloads || true
  exec su-exec "$PUID:$PGID" aria2c --conf-path=/app/configs/aria2.conf
fi

# 非 root：直接跑（要求宿主机卷权限已正确）
exec aria2c --conf-path=/app/configs/aria2.conf
