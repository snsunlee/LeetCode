#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        current_stack=[root]
        res=[]
        while current_stack:
            next_stack=[]
            item=[]
            for i in current_stack:
                if i.left:next_stack.append(i.left)
                if i.right:next_stack.append(i.right)
                item.append(i.val)
            res.append(item)
            current_stack=next_stack
        return res
