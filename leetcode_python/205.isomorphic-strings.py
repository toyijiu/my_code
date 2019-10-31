#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (36.66%)
# Total Accepted:    187.9K
# Total Submissions: 511.6K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution:
    def to_int(self,s:str)->int:
        #弄一个map来排序，字符串转化成数字比较是否相同
        count_num = 1;
        char_flag = {}
        result_num = 0
        for i in range(len(s)):
            #index = ord(s[i]) - ord('a')
            if s[i] in char_flag.keys():
                result_num = result_num*10 + char_flag[s[i]]
            else:
                char_flag[s[i]] = count_num
                count_num += 1
        return result_num

    def isIsomorphic(self, s: str, t: str) -> bool:
        int_s = self.to_int(s)
        int_t = self.to_int(t)
        return int_s == int_t


