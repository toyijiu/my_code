#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.43%)
# Total Accepted:    360.3K
# Total Submissions: 891.3K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #二分查找
        low_index = 0
        high_index = len(nums) - 1
        middle_index = low_index + (high_index - low_index)//2
        while middle_index >= low_index and middle_index <= high_index:
            #找到了
            if nums[middle_index] == target:
                 return middle_index
            #目标数比中间数大
            elif nums[middle_index] < target: 
                low_index = middle_index + 1
            else:
                high_index = middle_index - 1
            middle_index = low_index + (high_index - low_index)//2
        
        #还没找到，此时和middle_index当前数比较
        if nums[middle_index] > target:
            #在左侧插入时注意最小的插入位置为0
            return max(middle_index-1,0)
        else:
            return middle_index + 1
        

