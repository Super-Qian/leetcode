#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def max_production(self, nums):
        maxa = [0]*len(nums)
        mina = [0]*len(nums)
        max_product = maxa[0] = mina[0] = nums[0]
        for i in range(1, len(nums)):
            maxa[i] = max(maxa[i-1]*nums[i], mina[i-1]*nums[i], nums[i])
            mina[i] = min(maxa[i-1]*nums[i], mina[i-1]*nums[i], nums[i])
            if max_product < maxa[i]:
                max_product = maxa[i]
        return max_product

nums = [2, 0, 3, 4, 0, 5]
m = Solution()
print m.max_production(nums)
