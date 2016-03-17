#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def moveZeroes(self,nums):
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                nums[x],nums[y] = nums[y],nums[x]
                y += 1
        return nums

solute = Solution()
num = [9,10,0,30,0]
print solute.moveZeroes(num)
