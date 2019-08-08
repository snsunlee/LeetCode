#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findPath(self, root, sum):###查找包含 root 根节点的 路径之和 的数目
        result = 0
        if not root:
            return result

        if root.val == sum:
            result += 1

        result += self.findPath(root.left, sum - root.val)
        result += self.findPath(root.right, sum - root.val)
        return result
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        result = 0
        if not root:
            return result

        result += self.findPath(root, sum)
        result += self.pathSum(root.left, sum)
        result += self.pathSum(root.right, sum)

        return result

