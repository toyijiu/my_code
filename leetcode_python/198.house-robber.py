#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (40.76%)
# Total Accepted:    291K
# Total Submissions: 713.6K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#
class Solution:
    def get_rob(self,nums:List[int],length:int):
        #设置递归的退出条件
        if not length:
            return 0
        #对于第i个房子，两种选择，偷或者不偷
        #递归的公式 mem_list[i] = max(nums[i]+mem_list[i-2],mem_list[i-1])
        #0个房子的结果
        second_last_sum = 0
        #1个房子的结果
        pre_sum = nums[0]

        for i in range(2,length+1):
            current_sum = max(nums[i-1] + second_last_sum,pre_sum)
            second_last_sum = pre_sum
            pre_sum = current_sum

        return pre_sum

    def rob(self, nums: List[int]) -> int:
        return self.get_rob(nums,len(nums))

