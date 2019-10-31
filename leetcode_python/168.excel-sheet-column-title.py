#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (28.49%)
# Total Accepted:    163.4K
# Total Submissions: 573.3K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        #10进制转26进制
        char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notation = len(char_list)
        result = ""
        while n > 0:
            result += char_list[(n-1)%notation]
            n = (n-1) //notation
        
        return result[::-1]

