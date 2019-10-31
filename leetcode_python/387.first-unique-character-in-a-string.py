#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (49.22%)
# Total Accepted:    233.6K
# Total Submissions: 474.4K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_list = [0]*26
        #保证都是小写字母
        for index in range(len(s)):
            char_list[ord(s[index])-ord('a')] += 1
        
        for index in range(len(s)):
            if char_list[ord(s[index])-ord('a')] == 1:
                return index
        
        return -1

