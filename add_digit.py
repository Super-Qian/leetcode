#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def addDigits(self,num):
        while True:
            m = num % 10
            num /= 10
            num += m
            if num < 10:
                return num

m = Solution()
num = 343
print m.addDigits(num)
