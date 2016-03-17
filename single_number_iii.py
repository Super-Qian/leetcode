#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def singleNumber(self,nums):
        dict = {}
        num = []
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for j in dict:
            if dict[j] == 1:
                num.append(j)
        return num

m = Solution()
nums = [1,2,1,3,2,5]
print m.singleNumber(nums)
