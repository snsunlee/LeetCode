class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_A=self.len_ListNode(headA)
        len_B=self.len_ListNode(headB)
        ###如果长度相同 一起前进 直到相交
        if len_A==len_B:
            while headA!=headB:
                headA=headA.next
                headB=headB.next
            return headA
        else:
            for i in range(abs(len_A-len_B)):
                if len_B>len_A:
                    headB=headB.next
                if len_A>len_B:
                    headA=headA.next
            while headA!=headB:
                headA=headA.next
                headB=headB.next
            return headA
    def len_ListNode(self,head):
        if not head:
            return 0
        len_=0
        while head:
            len_+=1
            head=head.next
        return len_