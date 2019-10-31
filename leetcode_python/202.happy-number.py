#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (44.23%)
# Total Accepted:    214.1K
# Total Submissions: 483.4K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 
#
class Solution:
    def get_digit_sum(self,n:int)->int:
        digit_sum = 0
        while n:
            digit_sum += pow(n%10,2)
            n //= 10
        return digit_sum
    def isHappy(self, n: int) -> bool:
        slow = self.get_digit_sum(n)
        fast = self.get_digit_sum(n)
        fast = self.get_digit_sum(fast)
        while slow != fast:
            slow = self.get_digit_sum(slow)
            fast = self.get_digit_sum(fast)
            fast = self.get_digit_sum(fast)

        return slow == 1
        
            

