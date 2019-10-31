#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.65%)
# Total Accepted:    492.3K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    #计算以index的字符为中心点的最长回文
    def get_max_palindromic(self,test_str,index):
        odd_length = 1
        even_length = 0
        #计算偶数长度的，以当前的index为前面的字符
        if index < len(test_str)-1 and test_str[index] == test_str[index+1]:
            even_pre_index = index
            even_latter_index = index+1
            even_length = 2
            while even_pre_index > 0 and even_latter_index < len(test_str)-1 and test_str[even_pre_index-1] == test_str[even_latter_index+1]:
                even_pre_index -= 1
                even_latter_index += 1
                even_length += 2
        
        #计算奇数长度的
        odd_pre_index = odd_latter_index = index
        while odd_pre_index > 0 and odd_latter_index < len(test_str)-1 and test_str[odd_pre_index-1] == test_str[odd_latter_index+1]:
            odd_pre_index -= 1
            odd_latter_index += 1
            odd_length += 2
        
        if even_length >= odd_length:
            return even_pre_index,even_latter_index
        else:
            return odd_pre_index,odd_latter_index

    def longestPalindrome(self, s: str) -> str:
        #遍历每个字符，以每个字符为中心向两边扩展计算当前的最大回文，最后求出最大的
        if len(s) == 0:
            return ""
        
        pre_index = 0
        latter_index = 0
        for index in range(len(s)):
            temp_pre,temp_latter = self.get_max_palindromic(s,index)
            if temp_latter - temp_pre > latter_index - pre_index:
                latter_index = temp_latter
                pre_index = temp_pre
        
        return s[pre_index:latter_index+1]

