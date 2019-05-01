#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:

    def reverse(self, x: int) -> int:
        y = int("".join(list(str(abs(x)))[::-1])) * (x >= 0 and 1 or -1)
        return y in range(-2147483648, 2147483647) and y or 0
