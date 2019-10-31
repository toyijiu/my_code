#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.25%)
# Total Accepted:    147.4K
# Total Submissions: 395.6K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        #计算数后面0的个数，就是计算[1,n]间的min(2_num,5_num)的值,由于公约数有2的个数肯定大于5，其实就是计算5为公约数的个数
        '''
        #这个遍历的方法还是太慢了，大数据的时候超时
        five_nums = 0
        for i in range(5,n+1,5):
            test_num = i
            while test_num >= 5 and test_num %5 == 0:
                five_nums += 1
                test_num /= 5
        
        return five_nums
        '''
        #其实可以直接把n来整除，结果就是当前可以得到的5的公约数的个数，结果如果>=5则循环
        five_nums = 0
        while n >=5 :
            five_nums += n//5
            n = n//5
        return five_nums
        

