#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (53.53%)
# Total Accepted:    228K
# Total Submissions: 425.9K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
class Solution:
    def get_all_digits(self,num):
        sum = 0
        while num > 0:
            sum += num%10
            num //= 10
        return sum
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.get_all_digits(num)
        return num

