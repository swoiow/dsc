#!/usr/bin/env bash

set -ex

if [ `id -u` -eq 0 ];then
    curl -fsSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    python3 get-pip.py
else
    sudo curl -fsSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python get-pip.py
    sudo python3 get-pip.py
fi
