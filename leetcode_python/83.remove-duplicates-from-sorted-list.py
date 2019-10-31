#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (41.85%)
# Total Accepted:    300.9K
# Total Submissions: 718.9K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #链表长度为0或者1
        if head == None or head.next == None:
            return head

        cur_node = head.next
        pre_node = head
        compare_num = head.val

        while cur_node != None:
            #数字重复，删除该节点,有GC不用考虑删除问题
            if cur_node.val == compare_num:
                pre_node.next = cur_node.next
                cur_node = cur_node.next
            else:
                compare_num = cur_node.val
                pre_node = pre_node.next
                cur_node = cur_node.next
        
        return head



