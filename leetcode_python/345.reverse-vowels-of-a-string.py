#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (40.88%)
# Total Accepted:    143.9K
# Total Submissions: 352.1K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_str = "aeiouAEIOU"
        #字符串为常量，不能修改，要先转换成list，最后返回时再转回来
        
        result = list(s)
        pre_index = 0
        last_index = len(result) - 1
        while last_index > pre_index:
            while pre_index < len(result) and not result[pre_index] in vowel_str:
                pre_index += 1
            while last_index >= 0 and not result[last_index] in vowel_str:
                last_index -= 1
            #判断是否相遇
            if pre_index < last_index:
                temp_char = result[pre_index]
                result[pre_index] = result[last_index]
                result[last_index] = temp_char
                pre_index += 1
                last_index -= 1
            else:
                break
        
        return ''.join(result)

