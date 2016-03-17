#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isPowerOfTwo(self,n):
        while n % 2 == 0:
            n /= 2
        return n == 1

m = Solution()
print m.isPowerOfTwo(8)
