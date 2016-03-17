#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def proctExpectSelf(self, num):
        a = [1] * len(num)
        m = 1
        for i in range(len(num) - 1):
            m *= num[i]
            a[i + 1] *= m
        b = [1] * len(num)
        n = 1
        for j in range(len(num) - 1, 0, -1):
            n *= num[j]
            b[j - 1] *= n
        c = []
        for x in range(len(num)):
            l = a[x] * b[x]
            c.append(l)
        return c
