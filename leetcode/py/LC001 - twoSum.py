#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:

    def twoSum(self, nums: list, target: int) -> (list, tuple):
        hs = [(nums[0], 0)]

        for ix, x1 in enumerate(nums[1:], start=1):
            x2 = target - x1
            if x2 in [i[0] for i in hs]:
                return dict(hs)[x2], ix

            if x1 not in hs:
                hs.append((x1, ix))


if __name__ == '__main__':
    rest = Solution().twoSum()

    print(rest)
