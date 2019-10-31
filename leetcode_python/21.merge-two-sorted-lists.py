#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (52.15%)
# Total Accepted:    42.5K
# Total Submissions: 81.3K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        sorted_list = ListNode(0)
        list_index = sorted_list
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                list_index.next = ListNode(0)
                list_index = list_index.next
                list_index.val = l1.val
                l1 = l1.next
            else:
                list_index.next = ListNode(0)
                list_index = list_index.next
                list_index.val = l2.val
                l2 = l2.next

        if l1 != None:
            list_index.next = l1
        elif l2 != None:
            list_index.next = l2
        return sorted_list.next


        
