#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        self.min_depth=float('inf')
        def findPathMain(root,path_stock,current_depth):
            current_depth+=1
            path_stock.append(root)
            isLeaf=root.left==None and root.right==None
            if isLeaf:
                if self.min_depth>current_depth:
                    self.min_depth=current_depth
            else:
                if root.left:findPathMain(root.left,path_stock,current_depth)
                if root.right:findPathMain(root.right,path_stock,current_depth)
            path_stock.pop(0)
        findPathMain(root,[],0)
        return self.min_depth



