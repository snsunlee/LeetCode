#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        phead=ListNode(-1)
        phead.next=head #head node
        cur=phead
        while cur.next:
            if cur.next.next and cur.next.val==cur.next.next.val:
                dupNum=cur.next.val
                node=cur
                while node.next and node.next.val==dupNum:
                    node=node.next
                cur.next=node.next
            else:
                cur=cur.next
        return phead.next

