#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def numRow(self, n):
        a = [[1], [1, 1]]
        if n == 1:
            return [[1]]
        if n == 2:
            return a
        for i in range(2, n):
            a.append([1])
            for j in range(1, i + 1):
                if i == j:
                    m = 1
                else:
                    m = a[i - 1][j - 1] + a[i - 1][j]
                a[i].append(m)
        return a
m = Solution()
print m.numRow(7)
