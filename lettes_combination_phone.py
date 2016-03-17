#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def letterCombination(self,digits):
        if digits == '':
            return []
        ss = []
        dict = {'0':' ','1':None,'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        a = dict[digits[0]]
        for i in range(1,len(digits)):
            b = dict[digits[i]]
            for n in range(len(a)):
                for j in range(len(b)):
                    s = a[n] + b[j]
                    ss.append(s)
            a = ss
            ss = []
        return a
m = Solution()
digits = '23'
print m.letterCombination(digits)
