#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list_=[]
        phead=head
        while phead:
            list_.append(phead.val)
            phead=phead.next
        return list_==list_[::-1]
