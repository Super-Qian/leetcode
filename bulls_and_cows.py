#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def get_hint(self, secret, guess):
        dics = {}
        dicg = {}
        a = 0
        for i in secret:
            dics[i] = dics.get(i, 0) + 1
        for i in guess:
            dicg[i] = dicg.get(i, 0) + 1
        for k in dics:
            if k in dicg:
                a += min(dics[k], dicg[k])
        b = a
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b -= 1
        a -= b
        return '%sA%sB' % (a, b)

m = Solution()
secret = '1994'
guess = '1004'
print m.get_hint(secret, guess)
