#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (27.97%)
# Total Accepted:    829K
# Total Submissions: 3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #一个256长度的array存储该字符的上一次出现的index，一前一后两个指针指向subString的前后
        #遍历字符串，找到重复的char就就更新位置信息，并把前一个的指针指向之前位置的后一位
        if len(s) == 0:
            return 0
        char_index = [-1]*256
        pre_index = 0
        latter_index = 0
        max_length = 0

        for latter_index in range(len(s)):
            temp_index = char_index[ord(s[latter_index])]
            #之前已经有相同的字母在temp_index
            if temp_index != -1:
                pre_index = max(pre_index,temp_index+1)

            #更新当前的最大长度
            max_length = max(max_length,latter_index-pre_index+1)
            #更新该字符的最新位置
            char_index[ord(s[latter_index])] = latter_index
            

        return max_length
            

