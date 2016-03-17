#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def uglyNumber(self, num):
        if num <= 0:
            return False
        for i in [5, 3, 2]:
            while num % i == 0:
                num /= i
        return num == 1

m = Solution()
num = 90
print m.uglyNumber(num)
