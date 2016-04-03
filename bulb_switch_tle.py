#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def bulb_switch(self, n):
        m = 0
        if n == 1:
            return 1
        for i in range(1, n + 1):
            if n % i == 0:
                m += 1
        if m % 2 == 0:
            return self.bulb_switch(n - 1)
        else:
            return self.bulb_switch(n - 1) + 1

m = Solution()
print m.bulb_switch(999)
