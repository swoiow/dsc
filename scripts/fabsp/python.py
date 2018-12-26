#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _internal_utils import exec_bash, pf
from fabric.api import cd, run, settings, sudo


@exec_bash
def depend_redhat():
    """
    yum install -y gcc make
    yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel gdbm-devel xz-devel libffi-devel
    """


@exec_bash
def depend_debian():
    """
    apt-get update
    apt-get install -y gcc make
    apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
    """


def download_py2():
    """
    curl -sL https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz | tar -xz
    """

    with cd("/usr/src"), settings(warn_only=True):
        for line in download_py2.__doc__.split("\n"):
            sudo(line)


def download_py3():
    """
    curl -sL https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz | tar -xz
    """

    with cd("/usr/src"), settings(warn_only=True):
        for line in download_py3.__doc__.split("\n"):
            sudo(line)


def depend():
    depend_map = [
        ("debian", depend_debian),
        ("redhat", depend_redhat),
    ]

    ret = run("python -c 'import platform;platform.platform()'")
    dict(depend_map)[pf(ret)]()


def setup_pip():
    """
    curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
    python get-pip.py
    """

    with cd("/usr/src"), settings(warn_only=True):
        for line in setup_pip.__doc__.split("\n"):
            sudo(line)


def install_py2():
    """
    ./configure --enable-optimizations --enable-shared
    make -s -j2
    make install
    ln -sf /usr/local/bin/python /usr/bin/python
    echo "/usr/local/lib/" > /etc/ld.so.conf.d/python3.conf
    ldconfig
    """

    depend()

    download_py2()

    with cd("/usr/src/Python-2.7.15"), settings(warn_only=True):
        for line in install_py2.__doc__.split("\n"):
            sudo(line)


def install_py3():
    """
    ./configure --enable-optimizations --enable-shared
    make -s -j2
    make install
    ln -sf /usr/local/bin/python3 /usr/bin/python3
    echo "/usr/local/lib/" > /etc/ld.so.conf.d/python3.conf
    ldconfig
    """

    depend()

    download_py3()

    with cd("/usr/src/Python-3.6.8"), settings(warn_only=True):
        for line in install_py3.__doc__.split("\n"):
            sudo(line)
