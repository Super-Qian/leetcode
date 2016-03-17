#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def isAnagram(self, s, t):
        dict1 = {}
        for char in s:
            if char not in dict1:
                dict1[char] = 1
            else:
                dict1[char] += 1
        dict2 = {}
        for c in t:
            if c not in dict2:
                dict2[c] = 1
            else:
                dict2[c] += 1
        if not cmp(dict2, dict1):
            return True
        return False


m = Solution()
s = 'a'
t = 'a'
print m.isAnagram(s, t)
