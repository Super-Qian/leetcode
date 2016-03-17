#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def removeDuplicates(self,nums):
        size = 0
        length = len(nums)
        for i in range(length):
            if i == 0 or nums[i] != nums[i-1]:
                nums[size] = nums[i]
                size += 1
        return nums

m = Solution()
nums = [1,1,2,3,4,4]
print m.removeDuplicates(nums)
