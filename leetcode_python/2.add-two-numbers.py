#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.62%)
# Total Accepted:    785.8K
# Total Submissions: 2.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #剩余的list和进位之间的加法
    def add_carrybit(self,cur_node,carry_bit):
        pre_node = cur_node
        while carry_bit and cur_node:
            temp_val = cur_node.val + carry_bit
            cur_node.val = temp_val % 10
            carry_bit = temp_val // 10
            pre_node = cur_node
            cur_node = cur_node.next
        #最后还有进位
        if carry_bit:
            pre_node.next = ListNode(1)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_bit = 0
        
        pre_node1 = temp_node1 = l1
        temp_node2 = l2
        temp_val = 0
        while temp_node1 and temp_node2:
            temp_val = temp_node1.val + temp_node2.val + carry_bit
            temp_node1.val = temp_val % 10
            carry_bit = temp_val // 10
            pre_node1 = temp_node1
            temp_node1 = temp_node1.next
            temp_node2 = temp_node2.next
        #l1的长度更长
        if temp_node1:
            self.add_carrybit(temp_node1,carry_bit)
        #l2的长度更长
        elif temp_node2:
            pre_node1.next = temp_node2
            self.add_carrybit(temp_node2,carry_bit)
        #l1和l2一样长但是最后的进位为1
        elif carry_bit:
            pre_node1.next = ListNode(1)


        return l1

