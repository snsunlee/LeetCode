#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.maxDepth(root.left)-self.maxDepth(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def maxDepth(self,root):
        if not root:return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
