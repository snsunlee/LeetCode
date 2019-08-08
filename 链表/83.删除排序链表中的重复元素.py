#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        self.hash={}
        preHead=None
        phead=head
        pphead=head
        while phead:
            if phead.val not in self.hash:
                self.hash[phead.val]=1
                preHead=phead
                phead=phead.next
            else:
                preHead.next=phead.next
                phead=phead.next
        return pphead

