#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (34.54%)
# Total Accepted:    131.2K
# Total Submissions: 379.9K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
#
class Solution:
    def get_key(self,dict,value):
        return [k for k,v in dict.items() if v == value]

    def to_int(self,str_list):
        int_list = []
        for index in range(len(str_list)):
            int_list.append(str_list.index(str_list[index]))

        print("int list:",int_list)
        return int_list
    def wordPattern(self, pattern: str, str: str) -> bool:
        #solution1
        '''
        #将pattern和str的各个word作为map的key和val来判断是否符合模式
        #注意有个限制，不同的key对应的val要不一样
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        pattern_map = {}
        for index in range(len(pattern)):
            #如果当前的val在map中已经有了，返回False
            if str_list[index] in pattern_map.values():
                #获取对应value的key list,如果当前的key不在map的key list，返回false
                if not (pattern[index] in self.get_key(pattern_map,str_list[index])):
                    return False
            if not pattern[index] in pattern_map.keys():
                pattern_map[pattern[index]] = str_list[index]
            elif pattern[index] in pattern_map.keys() and str_list[index] != pattern_map[pattern[index]]:
                return False
        
        return True
        '''
        #solution2
        '''
        #看了下其他人的答案，其实直接把每个字符出现的第一个index作为映射的值，pattern和str都转换成对应的int list
        #最后判断两个list是否相等就行了
        #但是这个的效率反而比上一个低了很多，可读性好了很多，时间只超过了15.32%,第一个是百分之60多
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        
        return self.to_int(pattern) == self.to_int(str_list)
        '''
        #solution3
        #再改一下，取消函数调用，直接用一个函数来计算两个list映射后的int list是否相同
        #这个时间复杂度上也只超过了20%，目前还是第一个solution时间效率上最高。。。
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        for index in range(len(pattern)):
            if pattern.index(pattern[index]) != str_list.index(str_list[index]):
                return False
        
        return True
            

