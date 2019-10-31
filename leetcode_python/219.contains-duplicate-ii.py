 #
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (34.70%)
# Total Accepted:    184K
# Total Submissions: 530.3K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
# 
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #遍历，第一次遇到就存入map，第二次遇到就判断是否满足条件，不满足就更新map值
        index_map = {}
        for i in range(len(nums)):
            if nums[i] in index_map.keys():
                if i - index_map[nums[i]] <= k:
                    return True
                else:
                    #距离不满足就更新当前数字的index为当前最大值
                    index_map[nums[i]] = i
            else:
                #当前map没有该数字的存储情况，保存
                index_map[nums[i]] = i

        return False

