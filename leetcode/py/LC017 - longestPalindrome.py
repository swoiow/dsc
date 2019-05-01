#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s or set(s) == {s[0]}:
            return s

        mx = sl = len(s)

        while mx > 1:
            for offset in range(sl - mx + 1):
                judge = s[offset:mx + offset]
                hf = mx // 2
                if judge[:hf] == judge[-1 * hf:][::-1]:
                    return judge

            mx -= 1

        return s[0]


if __name__ == '__main__':
    o = Solution().longestPalindrome("babad")
    print(o)
