#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (49.31%)
# Total Accepted:    104.4K
# Total Submissions: 211.5K
# Testcase Example:  '"a"\n"b"'
#
# 
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return
# false. 
# 
# 
# Each letter in the magazine string can only be used once in your ransom
# note.
# 
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# 
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #用一个list来统计magazine中各个字符的个数，在遍历判断ransomNote中是否有
        char_list = [0]*26
        for index in range(len(magazine)):
            char_index = ord(magazine[index]) - ord('a')
            char_list[char_index] += 1

        for index in range(len(ransomNote)):
            char_index = ord(ransomNote[index]) - ord('a')
            if char_list[char_index] <= 0:
                return False
            else:
                char_list[char_index] -= 1

        return True

