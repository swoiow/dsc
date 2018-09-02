#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import re


def pf():
    v = platform.platform()
    v = v.lower()
    if re.search(re.compile("(debian|ubuntu)+"), v):
        return "debian"
    elif re.search(re.compile("(centos|fedora)+"), v):
        return "redhat"
