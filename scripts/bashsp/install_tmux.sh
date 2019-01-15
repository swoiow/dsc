#!/usr/bin/env bash

set -ex

yum install -y libevent libevent-devel

file=~/.tmux.conf
if [ ! -f "$file" ]; then
    curl -sL -o "$file" https://github.com/swoiow/dsc/raw/master/config-tmux/.tmux.conf
fi

cd /usr/src
git clone https://github.com/tmux/tmux.git --depth 1
cd tmux
sh autogen.sh
./configure && make
make install
