#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import settings, sudo


def backup():
    """
    mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
    mv /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.backup
    mv /etc/yum.repos.d/epel-testing.repo /etc/yum.repos.d/epel-testing.repo.backup
    """
    with settings(warn_only=True):
        for line in backup.__doc__.split("\n"):
            sudo(line)


def aliyun():
    """
    curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
    curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
    yum makecache
    """

    backup()

    with settings(warn_only=True):
        for line in aliyun.__doc__.split("\n"):
            sudo(line)


def tuna():
    """
    curl -sL -o /etc/yum.repos.d/CentOS-Base.repo https://github.com/swoiow/dsc/raw/master/scripts/fabic/rpm/tuna_base_7.repo
    curl -sL -o /etc/yum.repos.d/epel.repo https://github.com/swoiow/dsc/raw/master/scripts/fabic/rpm/tuna_epel_7.repo
    yum makecache
    """

    backup()

    with settings(warn_only=True):
        for line in tuna.__doc__.split("\n"):
            sudo(line)
