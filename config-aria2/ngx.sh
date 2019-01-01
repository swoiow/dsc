#!/usr/bin/env bash

set -xe

apk add --no-cache openssl
rm -rf /var/cache/apk/*

OUT=`echo $PASSWORD | openssl passwd -apr1 -stdin`
PWD=$OUT

echo $USERNAME":"$PWD > /etc/nginx/pass_file

chmod 644 /etc/nginx/pass_file

exec nginx -g 'daemon off;'
