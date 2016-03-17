#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def removeElement(self,nums,val):
        n = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i],nums[n] = nums[n],nums[i]
                n += 1
        for j in range(len(nums)):
            if nums[j] == val:
                return nums[:j]

m = Solution()
nums = [3,3,4]
val = 3
print m.removeElement(nums,val)
