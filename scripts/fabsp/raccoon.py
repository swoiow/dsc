#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
debug: racoon -d -F -v -f /etc/racoon/racoon.conf
"""

from fabric.api import sudo


def install():
    """
    yum install y https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/i/ipsec-tools-0.8.2-5.el7.x86_64.rpm
    """
    for line in setup.__doc__.split("\n"):
        sudo(line)


def setup():
    """
    groupadd vpn
    useradd -M -N -s /sbin/nologin mobile
    usermod -aG vpn mobile

    firewall-cmd --add-masquerade --permanent
    firewall-cmd --zone=public --add-port=500/udp --permanent
    firewall-cmd --zone=public --add-port=4500/udp --permanent

    iptables -t nat -A POSTROUTING -s 192.168.30.100/28 -o eth0 -j MASQUERADE
    iptables -A FORWARD -s 192.168.30.100/28 -j ACCEPT
    """

    for line in setup.__doc__.split("\n"):
        sudo(line)
