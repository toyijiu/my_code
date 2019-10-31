#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (41.63%)
# Total Accepted:    213.5K
# Total Submissions: 512.8K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true 
# Explanation: 20 = 1
# 
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# Explanation: 24 = 16
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #通常的办法是递归判断是否能被整除2然后递归除以2
        #但其实这个 数的最高bit为1，后面的为0就行
        if n < 1:
            return False
        while n > 1:
            if n % 2:
                return False
            n /= 2

        return n == 1   

