#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.16%)
# Total Accepted:    321.6K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        #只保留字符串中的英文和数字,\W表示匹配非字母字符就是除了[A-Za-z0-9_]之外的
        s = re.sub("[\W]+","",s).lower()
        pre_index = 0
        last_index = len(s)-pre_index-1
        while pre_index < last_index:
            if s[pre_index] != s[last_index]:
                return False
            
            pre_index += 1
            last_index -= 1
        
        return True

