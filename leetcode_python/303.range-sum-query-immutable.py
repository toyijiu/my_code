#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (36.72%)
# Total Accepted:    128.1K
# Total Submissions: 348.9K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# 
#
class NumArray:

    def __init__(self, nums: List[int]): 
        self.sum_list = []
        #testcase不保证nums一定非空，所以一定要加判断，之前没加一直失败
        if len(nums) == 0:
            return
        self.sum_list.append(nums[0])
        for index in range(1,len(nums)):
            self.sum_list.append(nums[index]+self.sum_list[-1])


    def sumRange(self, i: int, j: int) -> int:
        #init()计算0-下标的和，再做个减法
        if i == 0:
            return self.sum_list[j]
        else:
            return self.sum_list[j] - self.sum_list[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

