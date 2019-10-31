#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (42.66%)
# Total Accepted:    357.8K
# Total Submissions: 838.5K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirrorTree(self,left_tree,right_tree):
        if left_tree == None and right_tree == None:
            return True
        elif left_tree == None and right_tree != None:
            return False
        elif left_tree != None and right_tree == None:
            return False
        return left_tree.val == right_tree.val and self.isMirrorTree(left_tree.left,right_tree.right) and self.isMirrorTree(left_tree.right,right_tree.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        #和判断两个二叉树是否相同类似，只是这里left对应right，交换了一下,递归的思路
        if root == None:
            return True
        return self.isMirrorTree(root.left,root.right)

