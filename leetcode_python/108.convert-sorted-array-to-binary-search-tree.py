#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (49.17%)
# Total Accepted:    237.5K
# Total Submissions: 482.9K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def create_tree(self,nums,low_index,high_index):
        #退出条件,升序树注意high_index对应的是left，low_index对应的是right
        if low_index > high_index:
            #超出范围，None节点
            return None
        elif low_index == high_index:
            #叶子节点
            return TreeNode(nums[low_index])
        elif high_index - low_index == 1:
            #2个节点，大的为root，小的为左边叶子
            root = TreeNode(nums[high_index])
            root.left = TreeNode(nums[low_index])
            root.right = None
            return root
        elif high_index - low_index == 2:
            #3个节点，左边叶子最小，右边叶子最大
            root = TreeNode(nums[low_index+1])
            root.left = TreeNode(nums[low_index])
            root.right = TreeNode(nums[high_index])
            return root

        middle_index = low_index + (high_index - low_index)//2
        root = TreeNode(nums[middle_index])
        root.left = self.create_tree(nums,low_index,middle_index-1)
        root.right = self.create_tree(nums,middle_index+1,high_index)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #思路还是递归，有点像二分查找的思路，只不过middle_index做root节点，左边较小的数组做左子树，右边较大的数组做右子树
        #注意left是较小的，right是较大的，只有一个叶子时固定为左叶子
        if len(nums) == 0:
            return None
        return self.create_tree(nums,0,len(nums)-1)

