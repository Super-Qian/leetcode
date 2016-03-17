#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def containDuplicate(self,nums,k):
        dict = {}
        s = []
        n = None
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for k,v in dict.items():
            if v >= 2:
                n = k
        if n == None:
            return False
        for j in range(len(nums)):
            if n == nums[j]:
                s.append(j)
        for x in range(len(s)-1):
            if s[x+1] - s[x] <= k:
                return True
        return False

m = Solution()
nums = [1,1,2]
k =1 
print m.containDuplicate(nums,k)
