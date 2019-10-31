#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (50.95%)
# Total Accepted:    304.2K
# Total Submissions: 596.6K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #每个字符映射一个素数，判断两者的乘积是否一样就行
        #或者存一个list保存各个字符的个数
        if len(s) == len(t) and len(s) == 0:
            return True
        if len(s) != len(t):
            return False
        char_list = [0]*26
        for index in range(len(s)):
            char_list[ord(s[index])-ord('a')] += 1
            char_list[ord(t[index])-ord('a')] -= 1
            
        for index in range(len(char_list)):
            if char_list[index] != 0:
                return False
        return True

