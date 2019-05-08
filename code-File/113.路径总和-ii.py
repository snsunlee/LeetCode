#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:return[]
        res=[]
        self.dfs(root,sum,res,[root.val])
        return res
    def dfs(self,root,target,res,path):
        if not root:return 
        if sum(path)==target and not root.left and not root.right:###找到一个
            res.append(path)
            return
        if root.left:self.dfs(root.left,target,res,path+[root.left.val])
        if root.right:self.dfs(root.right,target,res,path+[root.right.val])
