#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (30.62%)
# Total Accepted:    328.9K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution:
    def mySqrt(self, x: int) -> int:
        #二分查找确定上下界
        low_border = 0
        high_border = x
        middle_num = low_border + (high_border-low_border)//2
        while low_border <= middle_num and middle_num <= high_border:
            compare_square = middle_num*middle_num
            if compare_square > x:
                high_border = middle_num-1
                middle_num = low_border + (high_border-low_border)//2
            elif compare_square < x:
                low_border = middle_num+1
                middle_num = low_border + (high_border-low_border)//2
            else:
                return middle_num
        
        #此时的middle要么是结果的上界，要么是下界
        if middle_num*middle_num < x:
            return middle_num
        else:
            #最小值不能小于0
            return max(0,middle_num-1)
