#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:

    def findLongestWord(self, s: str, d: list) -> str:
        d_ix = {k: v for v, k in enumerate("abcdefghijklmnopqrstuvwxyz", start=1)}
        stat = lambda w: [(c, w.count(c)) for c in "abcdefghijklmnopqrstuvwxyz" if c in w]
        intChar = lambda c: "%02d" * len(c) % tuple(d_ix[x] for x in c)

        bk = stat(s)
        key_bk = tuple(_[0] for _ in bk)
        d2 = sorted(d, key=lambda x: len(x), reverse=True)

        Crv, CrvO, CrvL = "", -1, 0  # Crv 最终结果，CrvO 当前的顺序，CrvL 当前的长度。
        for i in d2:
            si, _CrvL = stat(i), len(i)
            if all([c in key_bk for c, *_ in si]):
                rv = [dict(bk)[_c] >= _s for _c, _s in si]
                if all(rv):
                    if not Crv:
                        Crv, CrvO, CrvL = i, int(intChar(i)), _CrvL
                    else:
                        _CrvO = int(intChar(i))
                        if _CrvO < CrvO and _CrvL >= CrvL:
                            Crv, CrvO, CrvL = i, _CrvO, _CrvL

            if Crv and _CrvL < CrvL:
                return Crv

        return Crv
