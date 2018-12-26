#!/usr/bin/env bash

set -ex

yum install autoconf automake

cd /usr/src
curl -sL https://github.com/hishamhm/htop/archive/2.2.0.tar.gz | tar -xz

cd htop-2.2.0
./autogen.sh && ./configure && make
make install
