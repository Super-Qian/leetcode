#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def bulbSwitch(self,n):
        import math
        if n == 0:
            return 0
        m = math.sqrt(n)
        print int(m)

m = Solution()
m.bulbSwitch(8)
