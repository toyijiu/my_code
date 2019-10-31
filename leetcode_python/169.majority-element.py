#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (51.42%)
# Total Accepted:    349.4K
# Total Submissions: 678.4K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        majority_num = nums[0]
        majority_size = 1
        for i in range(1,len(nums)):
            if nums[i] == majority_num:
                majority_size += 1
            elif majority_size == 0:
                majority_num = nums[i]
                majority_size = 1
            else:
                majority_size -= 1
        
        return majority_num

