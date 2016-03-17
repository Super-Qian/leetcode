#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def happyNumber(self, n):
        a = []
        b = [n]
        while True:
            while n >= 10:
                m = n % 10
                a.append(m)
                n /= 10
            a.append(n)
            n = 0
            for i in a:
                n += i * i
            if n == 1:
                return True
            elif n in b:
                return False
            else:
                b.append(n)
            a = []
            print b


m = Solution()
print m.happyNumber(7)
