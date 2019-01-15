#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import re


def pf(v=None):
    if not v:
        from fabric.api import run

        v = run("python -c 'import platform; print(platform.platform())'")

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


def lines(fc, split_flag="\n"):
    if hasattr(fc, "__doc__"):
        command = fc.__doc__
    elif isinstance(fc, (tuple, list)):
        command = fc
    else:
        command = None

    if command:
        command = (c.strip() for c in command.split(split_flag) if c.strip())
        for line in command:
            yield line
