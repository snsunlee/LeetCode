#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(root,path,res):
            if root.left is None and root.right is None:
                res.append(path+str(root.val))
                return 
            if root.left:
                helper(root.left, path + str(root.val)+'->', res)
            if root.right:
                helper(root.right, path + str(root.val)+'->', res)

        if root is None:
            return []
        res = []
        helper(root, '', res)
        return res

