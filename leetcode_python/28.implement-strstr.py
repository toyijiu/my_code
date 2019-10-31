#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (37.47%)
# Total Accepted:    35.8K
# Total Submissions: 95.2K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
#Sunday算法，。具体的算法可以百度
class Solution:
    def isIn(self,haystack,needle,index):
        offset = 0
        for temp_offset in range(len(needle)):
            #不匹配字符
            if haystack[temp_offset + index] != needle[temp_offset]:
                #当前已经到主字符串的末尾了
                if index + len(needle) >= len(haystack):
                    return False,len(needle)
                #如果needle中没有字符匹配到后一个字符
                else:
                    last_char = haystack[index+len(needle)]
                    #主串排序后的一个字符在needle中从右往左数的第一个index
                    last_char_index = needle[::-1].find(last_char)
                    if last_char_index == -1:
                        return False,len(needle)+1
                    else:
                        return False,last_char_index +1
        
        return True,0


    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        #长度不满足
        if len(haystack) < len(needle):
            return -1

        index = 0
        while index <  (len(haystack) - len(needle) + 1):  
            check_flag,offset = self.isIn(haystack,needle,index)
            if check_flag:
                return index
            else:
                #没找到，需要直接跳offset
                index += offset
        
        return -1



