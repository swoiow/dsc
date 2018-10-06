#!/usr/bin/env bash

docker stop pyserver
docker rm pyserver

if [ ! -f ./certs/ssl.key ] || [ ! -f ./certs/ssl.crt ] ; then
    docker run -it --rm -v $PWD/certs:/work frapsoft/openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout /work/ssl.key -out /work/ssl.crt -subj "/C=CN/ST=GD/L=GZ/O=Global Security/OU=Docker Dev/CN=pyserver.me/"
    cat $PWD/certs/ssl.crt $PWD/certs/ssl.key > $PWD/certs/ssl.pem
    curl -SL -o $PWD/certs/server.py https://github.com/swoiow/dsc/raw/master/tools/unix/picker.py
fi

docker run -itd \
  --rm \
  -p 0.0.0.0:8000:8000 \
  --name pyserver \
  -w="/tmp" \
  -v /tmp/www/downloads:/tmp \
  -v /tmp/www/certs:/certs \
  python:3.7.0-alpine3.7 python /certs/server.py -c /certs/ssl.pem
