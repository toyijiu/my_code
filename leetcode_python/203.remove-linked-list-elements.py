#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (35.20%)
# Total Accepted:    207.3K
# Total Submissions: 587.7K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None

        second_last_node = None
        last_node = head
        while last_node:
            if last_node.val == val:
                #如果删除的是头结点
                if not second_last_node:
                    head = head.next
                    last_node = head
                else:
                    #要删除的是中间结点
                    second_last_node.next = last_node.next
                    last_node = last_node.next
            else:
                #不删除当前节点，往后走一步
                second_last_node = last_node
                last_node = last_node.next

        return head
                


