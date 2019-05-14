#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        phead = ListNode(-1) # head
        phead.next = head
        cur = phead
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return phead.next


