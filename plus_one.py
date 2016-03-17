#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def plusOne(self,digits):
        m = 0
        for i in digits:
            m = m*10+i
        m += 1
        num = []
        while m>=10:
            n = m%10
            num.append(n)
            m /= 10
        num.append(m)
        num.reverse()
        return num

solve = Solution()
num = [0]
print solve.plusOne(num)
