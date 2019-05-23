#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        h = head
        while h:
            if h and h.next:
                tmp = h.next
                p.next = tmp
                # 交换 位置
                h.next = h.next.next
                tmp.next = h
                h = h.next
                p = p.next.next
            else:
                p.next = h
                h = h.next
        return dummy.next

