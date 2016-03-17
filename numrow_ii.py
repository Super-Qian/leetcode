#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def numRow(self, n):
        a = [[1], [1, 1]]
        for i in range(2, n+1):
            a.append([1])
            for j in range(1, i + 1):
                if i == j:
                    m = 1
                else:
                    m = a[i - 1][j - 1] + a[i - 1][j]
                a[i].append(m)
        return a[n]
m = Solution()
print m.numRow(0)
