#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.62%)
# Total Accepted:    48.8K
# Total Submissions: 154.2K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #遍历找出最短的字符串和其长度，再遍历找到公共前缀的最末位index
        if not len(strs):
            return ""
        min_len = len(strs[0])
        min_str = strs[0]
        #求出最短字符串的长度
        for str_index in range(len(strs)):
            if min_len > len(strs[str_index]):
                min_len = len(strs[str_index])
                min_str = strs[str_index]
        
        for char_index in range(min_len):
            comp_char = strs[0][char_index]
            for str_index in range(len(strs)):
                if strs[str_index][char_index] != comp_char:
                    return min_str[0:char_index]
        
        
        #全部匹配最短的字符串
        return min_str


        
        
        
