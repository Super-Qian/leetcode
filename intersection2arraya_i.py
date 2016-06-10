#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def inter(self, nums1, nums2):
        a = []
        for i in nums1:
            if i in nums2 and i not in a:
                a.append(i)
        return a

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
m = Solution()
print m.inter(nums1, nums2)
