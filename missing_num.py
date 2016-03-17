#!/usr/bin/env python
# coding=utf-8
import time
class Solution(object):
    def missingNumber(self,nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return i + 1

start = time.time()
m = Solution()
num = [1,0,3]
print m.missingNumber(num)
end = time.time()
print end - start
