#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                res.append(node.val)
                ###pop 结合stack的后进先出
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res

