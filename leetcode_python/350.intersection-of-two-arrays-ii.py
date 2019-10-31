#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (46.79%)
# Total Accepted:    179.6K
# Total Submissions: 383.9K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# 
# 
# Note:
# 
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #通过map来存储是否有相同的数字
        #这个要考虑相同的个数
        num_map = {}
        for index in range(len(nums1)):
            if not nums1[index] in num_map.keys():
                num_map[nums1[index]] = 1
            else:
                num_map[nums1[index]] += 1
        
        same_list = []
        for index in range(len(nums2)):
            if nums2[index] in num_map.keys() and num_map[nums2[index]] > 0:
                same_list.append(nums2[index])
                num_map[nums2[index]] -= 1

        return same_list

