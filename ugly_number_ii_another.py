#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def nthUglyNumber(self,n):
        a = [1]
        a2=a3=a5=0
        i = 1
        if n == 1:
            return 1
        while i != n:
            l2,l3,l5 = a[a2]*2,a[a3]*3,a[a5]*5
            m = min(l2,l3,l5)
            if m == l2:a2+=1
            if m == l3:a3+=1
            if m == l5:a5+=1
            i += 1
            a.append(m)
        return m

m = Solution()
print m.nthUglyNumber(6)
