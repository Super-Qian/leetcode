#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def majority_elements(slef, nums):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for j in dic:
            if dic[j] > len(nums) / 2:
                return j

m = Solution()
nums = [3, 3, 4]
print m.majority_elements(nums)
