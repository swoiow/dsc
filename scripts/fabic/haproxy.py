#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import cd, settings, sudo


def download():
    """
    curl -o haproxy.tar.gz https://www.haproxy.org/download/1.8/src/haproxy-1.8.8.tar.gz
    tar xzf haproxy.tar.gz
    """

    with cd("/usr/src"), settings(warn_only=True):
        for line in download.__doc__.split("\n"):
            sudo(line)


def install():
    """
    make TARGET=linux2628 USE_PCRE=1 USE_STATIC_PCRE=1 USE_OPENSSL=1 USE_ZLIB=1
    make install
    """

    download()

    with cd("/usr/src/haproxy-1.8.8"), settings(warn_only=True):
        for line in install.__doc__.split("\n"):
            sudo(line)
