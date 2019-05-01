#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        bucket = []
        ctx = 0

        while (l1 or l2 or ctx):
            s = (l1 and l1.val or 0) + (l2 and l2.val or 0) + ctx
            bucket.append(s % 10)
            ctx = s >= 10 and 1 or 0

            l1, l2 = l1 and l1.next or 0, l2 and l2.next or 0
        return bucket


if __name__ == '__main__':
    o = Solution().addTwoNumbers([5], [5])

    print(o)
