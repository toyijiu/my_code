#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (43.36%)
# Total Accepted:    355K
# Total Submissions: 818.5K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#
class Solution:
    def climbStairs(self, n: int) -> int:
        #递归
        #本质上就是斐波那契数列
        count_ways = [0,1,2]
        if n < 3:
            return count_ways[n]
        for stair_num in range(3,n+1):
            count_ways.append(count_ways[stair_num-1]+count_ways[stair_num-2])
        return count_ways[-1]


