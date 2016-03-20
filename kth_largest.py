#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def findkthLargest(self, nums, k):
        new_nums = sorted(nums, reverse=True)
        return new_nums[k - 1]

nums = [3, 2, 1, 5, 6, 4]
k = 2
m = Solution()
print m.findkthLargest(nums, k)
