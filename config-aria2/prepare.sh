#!/bin/sh
set -e

UID=`id -u`
GID=`id -g`

echo
echo "UID: $UID"
echo "GID: $GID"
echo

echo "Setting conf"

touch /aria2/config/aria2.session

if [[ ! -e /aria2/config/aria2.conf ]]
then
    mkdir -p /aria2/config
    cp /etc/aria2.conf.default /aria2/config/aria2.conf
fi

echo "[DONE]"

echo "Setting owner and permissions"

chown -R $UID:$GID /aria2/config
chmod 755 /aria2/config
chmod 755 /aria2/downloads

echo "[DONE]"

echo "Starting aria2c"

exec aria2c \
    --conf-path=/aria2/config/aria2.conf \
  > /dev/stdout \
  2 > /dev/stderr

echo 'Exiting aria2'
