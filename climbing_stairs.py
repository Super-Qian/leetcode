#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def climbStairs(self,n):
        if n <= 0:
            return 0
        s = [0,1]
        for i in range(n):
            s[0],s[1] = s[1],s[0] + s[1]
        return s[1]

n = 0
m = Solution()
print m.climbStairs(n)
