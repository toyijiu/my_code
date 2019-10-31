#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (53.02%)
# Total Accepted:    198.3K
# Total Submissions: 373.9K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# 
# 
# Note:
# 
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
# 
# 
#
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #通过map来存储是否有相同的数字
        num_map = {}
        for index in range(len(nums1)):
            if not nums1[index] in num_map.keys():
                num_map[nums1[index]] = 1
        
        same_list = []
        for index in range(len(nums2)):
            if nums2[index] in num_map.keys() and not nums2[index] in same_list:
                same_list.append(nums2[index])

        return same_list


