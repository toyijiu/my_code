#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.40%)
# Total Accepted:    100.9K
# Total Submissions: 256.1K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #二分法找一个数，其平方是目标数
        low_num = 0
        high_num = num
        while low_num <= high_num:
            middle_num = low_num + (high_num-low_num)//2
            pow_num = middle_num*middle_num
            if pow_num == num:
                return True
            elif pow_num > num:
                high_num = middle_num-1
            else:
                low_num = middle_num+1
        
        return False

