#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (40.64%)
# Total Accepted:    351.8K
# Total Submissions: 865.7K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 

# 
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #非负数，考虑进位
        if len(digits) == 0:
            return 0
        carry_bit = 0
        digits[-1] += 1
        for index in range(len(digits)-1,-1,-1):
            sum_bit = digits[index] + carry_bit
            carry_bit = sum_bit//10
            digits[index] = sum_bit % 10
        
        #如果最高位有进位
        if carry_bit:
            digits.insert(0,1)
        
        return digits
        

