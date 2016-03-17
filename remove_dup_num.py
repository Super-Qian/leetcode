#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def removeDuplicates(self,nums):
        for i in range(len(nums)-2):
            for j in range(i,len(nums)-2):
                if nums[j] >= nums[j+1]:
                    nums[j+1],nums[j+2] = nums[j+2],nums[j+1]
        for x in range(len(nums)-1):
            if nums[x] >= nums[x+1]:
                return nums[:x+1]

m = Solution()
num = [1,1]
print m.removeDuplicates(num)
