#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return None
        root = TreeNode(postorder[-1])
        loc = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[ : loc], postorder[ :loc])
        root.right = self.buildTree(inorder[loc+1:], postorder[loc:-1])
        return root  

