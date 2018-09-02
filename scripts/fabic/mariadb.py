#!/usr/bin/env python
# -*- coding: utf-8 -*

from fabric.api import sudo, settings


def install():
    """
    curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
    yum install -y MariaDB-server
    """
    with settings(warn_only=True):
        for line in install.__doc__.split("\n"):
            sudo(line)


def setup():
    """
    """
