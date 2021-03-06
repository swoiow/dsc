#!/usr/bin/env bash

if [ `id -u` -eq 0 ];then
    curl -fsSL get.docker.com | bash
    rm -f /usr/local/bin/docker-compose
    curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
else
    sudo curl -fsSL get.docker.com | bash
    sudo rm -f /usr/local/bin/docker-compose
    sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

curl -sL -o /etc/docker/daemon.json https://github.com/swoiow/dsc/raw/master/config-docker/daemon.json
systemctl enable docker
service docker restart
