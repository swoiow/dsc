#!/usr/bin/env python
# -*- coding: utf-8 -*

from __init__ import pf
from fabric.api import settings, sudo


def depend_redhat():
    """
    sudo yum install -y gcc-c++ make
    """
    for line in depend_redhat.__doc__.split("\n"):
        sudo(line)


def depend_debian():
    """
    sudo apt-get install -y build-essential
    """
    for line in depend_debian.__doc__.split("\n"):
        sudo(line)


def install_node_v8():
    c = None
    system_platform = pf()

    if system_platform == "debian":
        depend_debian()
        c = """
        curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
        apt-get install -y nodejs
        """

    elif system_platform == "redhat":
        depend_redhat()
        c = """
        curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
        yum install -y nodejs
        """

    if c:
        with settings(warn_only=True):
            for line in c.split("\n"):
                sudo(line)


def install_node_v10():
    c = None
    system_platform = pf()
    if system_platform == "debian":
        depend_debian()
        c = """
        curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
        apt-get install -y nodejs
        """

    elif system_platform == "redhat":
        depend_redhat()
        c = """
        curl --silent --location https://rpm.nodesource.com/setup_10.x | sudo bash -
        yum install -y nodejs
        """

    with settings(warn_only=True):
        for line in c.split("\n"):
            sudo(line)
