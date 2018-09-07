#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import platform
import re


def pf():
    v = platform.platform()
    v = v.lower()
    if re.search(re.compile("(debian|ubuntu)+"), v):
        return "debian"
    elif re.search(re.compile("(centos|fedora)+"), v):
        return "redhat"


def exec_bash(func):
    from fabric.api import sudo

    @functools.wraps(func)
    def swap(*args, **kwargs):
        command = func.__doc__
        if command:
            command = (c.strip() for c in command.split("\n") if c.strip())
            for line in command:
                sudo(line)

        func(*args, **kwargs)

    return swap
