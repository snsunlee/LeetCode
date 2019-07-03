#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        pHead=head
        list_stack=[]
        while pHead:
            list_stack.append(pHead.val)
            pHead=pHead.next
        list_stack.sort()
        p1=head
        i=0
        while p1:
            p1.val=list_stack[i]
            i+=1
            p1=p1.next
        return head
