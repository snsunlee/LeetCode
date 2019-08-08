#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        currentStack=[root]
        res=[]
        while currentStack:
            nextStack=[]
            item=[]
            for i in currentStack:
                if i.left:nextStack.append(i.left)
                if i.right:nextStack.append(i.right)
                item.append(i.val)
            res.append(item)
            currentStack=nextStack
        return res[::-1]

