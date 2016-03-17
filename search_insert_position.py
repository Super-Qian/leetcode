#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def searchInsert(self,nums,target):
        for i in range(len(nums)):
            if nums[i] > target:
                return 0
            elif nums[i] == target:
                return i
            elif i == len(nums)-1 or nums[i] < target and nums[i+1] > target:
                return i+1


m = Solution()
nums = [1,3,5,6]
print m.searchInsert(nums,0)
