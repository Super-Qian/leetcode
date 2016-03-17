#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def productExpectSelf(self, nums):
        size = len(nums)
        output = [1] * size
        left = 1
        for i in range(size - 1):
            left *= nums[i]
            output[i + 1] *= left
        right = 1
        for j in range(size - 1, 0, -1):
            right *= nums[j]
            output[j - 1] *= right
        return output

m = Solution()
nums = [1, 2, 3, 4]
print m.productExpectSelf(nums)
