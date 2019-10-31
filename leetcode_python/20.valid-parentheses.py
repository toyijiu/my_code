#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.21%)
# Total Accepted:    44.2K
# Total Submissions: 122K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack(object):
    def __init__(self, top = None):
        self.top = top

    def push(self,data):
        #创建新的节点放到栈顶
        self.top = Node(data, self.top)

    def pop(self):
        #拿出栈顶元素，原来的栈发生改变
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        #查看栈顶元素，原来的栈不变
        return self.top.data if self.top is not None else None

    def isEmpty(self):
        return self.peek() is None

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s):
            return True
        
        #构造一个stack，有入栈，出栈等操作，左括号入栈，右括号出栈，看是否匹配或者最后stack是否为空
        bracket_stack = Stack()
        for char_index in range(len(s)):
            if ((s[char_index] == ']' and bracket_stack.peek() == '[')
            or (s[char_index] == '}' and bracket_stack.peek() == '{') 
            or (s[char_index] == ')' and bracket_stack.peek() == '(')):
                bracket_stack.pop()
            elif s[char_index] == '[' or s[char_index] == '{' or s[char_index] == '(':
                bracket_stack.push(s[char_index])
            else:
                return False
        
        
        if bracket_stack.isEmpty():
            return True
        else:
            return False
                


        
