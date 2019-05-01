#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:

    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        mix_l = sorted(nums1 + nums2)
        sl = len(mix_l)
        m, p = sl % 2 == 0 and (sl / 2, -1) or (sl // 2, 0)

        return mix_l[m] / 1.0 \
            if p == 0 \
            else sum(mix_l[int(m + p):int(m + 1)]) * 1.0 / 2

    def findMedianSortedArrays2(self, nums1, nums2) -> float:
        # TODO: 正确的做法是缩小列表的长度
        pass


if __name__ == '__main__':
    o = Solution().findMedianSortedArrays([1, 2, 3], [3, 4])
    print(o)
