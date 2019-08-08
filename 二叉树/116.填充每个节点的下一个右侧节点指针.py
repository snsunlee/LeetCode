#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
# Definition for a Node.
# class Node:
#     def __init__(self, val, left, right, next):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue=[root]
        while queue:
            pre_node=None
            for _ in range(len(queue)):
                node=queue.pop(0)
                if pre_node:pre_node.next=node
                pre_node=node
                if pre_node.left or pre_node.right: 
                    queue.append(pre_node.left)
                    queue.append(pre_node.right)
        return root
