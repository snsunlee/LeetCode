#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:return 
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        while n:
            fast = fast.next
            n -= 1
        slow = dummy
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

