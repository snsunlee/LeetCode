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
        phead=ListNode(-1)
        phead.next=head #head node
        cur=phead
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        while phead.next:
            print(phead.next.val)
            phead=phead.next
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)        
Solution().removeElements(head,4)