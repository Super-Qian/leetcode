#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def sushu(self, num):
        i = 2
        if num <= 1:
            return False
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    def nsushu(self):
        for i in range(100):
            if self.sushu(i):
                print i

m = Solution()
m.nsushu()
