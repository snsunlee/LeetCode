#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res,stack=[],[root]
        if not root:
            return []
        while stack:
            root=stack.pop()
            res.append(root.val)
            if root.left:stack.append(root.left)
            if root.right:stack.append(root.right)
        return res[::-1]

