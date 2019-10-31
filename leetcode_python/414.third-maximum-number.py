#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (28.67%)
# Total Accepted:    85.4K
# Total Submissions: 297.4K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_list = [nums[0]]*3
        
        for index in range(1,len(nums)):
            if nums[index] > max_list[0]:
                max_list[2] = max_list[1]
                max_list[1] = max_list[0]
                max_list[0] = nums[index]
            elif nums[index] > max_list[1] and nums[index] < max_list[0]:
                max_list[2] = max_list[1]
                max_list[1] = nums[index]
            elif nums[index] > max_list[2] and nums[index] < max_list[1]:
                max_list[2] = nums[index]
        
        
        if max_list[0] > max_list[1] and max_list[1] > max_list[2]:
            return max_list[2]
        else:
            return max_list[0]
        


