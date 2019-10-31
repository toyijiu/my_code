#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.09%)
# Total Accepted:    44.7K
# Total Submissions: 148.6K
# Testcase Example:  '3'
#
# Find the n^th digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 2^31).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution:
    def findNthDigit(self, n: int) -> int:
        #一位数9个，二位数90个，3位数900个,4位数9000个
        #先计算整个数列的最后一个数是几位数
        count_num = 0
        digit_num = 1

        pre_n = n
        n -= (9*pow(10,digit_num-1)*digit_num)
        while n>0:
            digit_num += 1
            pre_n = n
            n -= (9*pow(10,digit_num-1)*digit_num)
        
        #pre_n表示digit_num位数的数字个数和
        #取的最后一个数字的第几位，0表示取的上一个数字的最后一位
        tail_num = pre_n % digit_num
        num_value = pow(10,digit_num-1)+(pre_n//digit_num)
        #如果tai_num是0表示是取上一个数的最后一位
        if tail_num == 0:
            return (num_value-1)%10
        else:
            #否则取当前数从高位数的第tail_num位
            for i in range(digit_num-tail_num):
                num_value //= 10
            return num_value%10
        



