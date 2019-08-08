#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue=[root]
        while queue:
            left_node=None
            for _ in range(len(queue)):
                node=queue.pop(0)
                if left_node:left_node.next=node
                left_node=node
                if node.left :queue.append(node.left)
                if node.right:queue.append(node.right)
        return root
