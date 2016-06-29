#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def max_subarray(self, nums):
        x = y = 0
        sum = n = nums[0]
        for i in range(len(nums)):
            if n > 0:
                n += nums[i]
                y = i
            else:
                n = nums[i]
                x = i
            if n > sum:
                sum = n
        return sum, x, y

nums = [-2, 3, 1, -9, 4, 8, 3]
m = Solution()
sum, x, y =  m.max_subarray(nums)
print "Max sum is {}, from index {} to {}".format(sum, x, y)
