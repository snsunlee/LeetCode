# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre_head=None
        cur_head=pHead
        while cur_head:
            next_head=cur_head.next
            cur_head.next=pre_head
            pre_head=cur_head
            cur_head=next_head
        return pre_head
        ##test case
        # while pre_head:
        #     print(pre_head.val)
        #     pre_head=pre_head.next

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
a.next=b
b.next=c
c.next=d
head=a
Solution().ReverseList(head)