#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (52.77%)
# Total Accepted:    518.6K
# Total Submissions: 982.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #遍历修改指针
        if head == None or head.next == None:
            return head
        #从前往后修改指针方向
        first_node = head
        second_node = head.next
        #注意头指针的next要修改为None
        head.next = None
        while second_node:
            next_node = second_node.next
            second_node.next = first_node
            first_node = second_node
            second_node = next_node
        return first_node
        

