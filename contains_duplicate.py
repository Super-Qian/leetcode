#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def containsDuplicate(self,nums):
        nums.sort()
        num = list(set(nums))
        num.sort()
        if num == nums:
            return False
        return True

m = Solution()
nums = [1,5,-2,-4,0]
print m.containsDuplicate(nums)
