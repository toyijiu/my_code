#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (47.46%)
# Total Accepted:    89.7K
# Total Submissions: 188.9K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_map = {}
        for index in range(len(s)):
            if s[index] in char_map.keys():
                char_map[s[index]] += 1
            else:
                char_map[s[index]] = 1
        
        single_flag = 0
        count = 0
        for key in char_map.keys():
            if char_map[key] %2 == 1:
                count += char_map[key]-1
                single_flag = 1
            if char_map[key] %2 == 0:
                count += char_map[key]

        return count + single_flag
