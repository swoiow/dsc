#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import cd, settings, sudo


def download():
    """
    curl -o screen.tar.gz http://ftp.gnu.org/gnu/screen/screen-4.6.0.tar.gz
    tar xzf screen.tar.gz
    """

    with cd("/usr/src"), settings(warn_only=True):
        for line in download.__doc__.split("\n"):
            sudo(line)


def install():
    """
    ./configure
    make
    """

    with cd("/usr/src/screen-4.6.0"), settings(warn_only=True):
        for line in install.__doc__.split("\n"):
            sudo(line)
