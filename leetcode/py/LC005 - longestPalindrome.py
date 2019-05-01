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
                if judge == judge[::-1]:
                    return judge

            mx -= 1

        return s[0]

    def longestPalindrome2(self, s: str) -> str:
        if not s or set(s) == {s[0]}:
            return s

        mx = sl = len(s)

        while mx > 1:
            for offset in range(sl - mx + 1):
                judge = s[offset:mx + offset]
                if judge == judge[::-1]:
                    return judge
                hf = mx // 2
                if judge[:hf] == judge[-1 * hf:][::-1]:
                    return judge

            mx -= 1
            print("-" * 3)

        return s[0]

    def longestPalindrome3(self, s: str) -> str:
        """ 思路：
            s长度，则从每个元素开始，
                判断，
                    元素与相邻是否存在相同
                    若是：
                        位移
                    若否：
                        下一个元素
        """
        if not s or set(s) == {s[0]}:
            return s

        sl, mid, dist, fL, fR = len(s), 0, 1, 0, 0

        for k, v in enumerate(s):
            _right = k + 1
            _left = 2 * k - _right
            while -1 < _left and _right < sl:
                if s[_left] == s[_right]:
                    _dist = _right - _left
                    if _dist > dist:
                        fL, fR = _left, _right
                        dist = _dist

                    _right += 1
                    _left = 2 * k - _right

                else:
                    break

                _right = k
                _left = k - 1
                while -1 < _left and 0 < _right < sl:
                    if s[_left] == s[_right]:
                        _dist = _right - _left
                        if _dist >= dist:
                            fL, fR = _left, _right
                            dist = _dist

                        _right += 1
                        _left -= 1

                    else:
                        break

        return s[fL: fR + 1] or s[0]


if __name__ == '__main__':
    o = Solution().longestPalindrome3("aacaaaacf")
    print("result: %s" % o)
