#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def reverse_velwel(self, s):
        a = ['a', 'i', 'e', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        b = []
        news = ""
        for i in s:
            if i in a:
                b.append(i)
        b = b[::-1]
        n = 0
        for l in s:
            if l in a:
                news += b[n]
                n += 1
            else:
                news += l
        return news

s = 'leetcode'
m = Solution()
print m.reverse_velwel(s)
