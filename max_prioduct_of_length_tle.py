#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def max_product(self, worlds):
        result = 0
        length = len(worlds)
        for i in range(length):
            for j in range(length)[::-1]:
                judge = True
                if i == j:
                    continue
                for k in worlds[i]:
                    if k in worlds[j]:
                        judge = False
                if judge:
                    result = max(result, len(worlds[i]) * len(worlds[j]))
        return result

m = Solution()
worlds = ['a', 'ab', 'abc']
print m.max_product(worlds)
