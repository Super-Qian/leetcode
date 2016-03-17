#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def nthuglyNUmber(self, n):
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q.append(m)
        return q[-1]

m = Solution()
print m.nthuglyNUmber(10)
