#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (59.10%)
# Total Accepted:    453.8K
# Total Submissions: 767.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        #开始的想法是在TreeNode加一个depth字段来标识当前节点深度，再轮询遍历求最大值，
        #也可以用递归，当前树的最大深度为子树最大深度+1，退出条件是None节点的深度为1
        #递归还是要小心stack溢出的问题，尽量少用不用局部变量之类的
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

