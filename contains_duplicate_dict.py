#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def cotainDuplicate(self,nums):
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                return True
        return False
m = Solution()
nums = [1,5,-2,-4,0]
print m.cotainDuplicate(nums)
