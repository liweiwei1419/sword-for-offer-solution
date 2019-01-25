# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findKthToTail(self, pListHead, k):
        """
        :type pListHead: ListNode
        :type k: int
        :rtype: ListNode
        """
        if pListHead is None:
            return None
        counter = 0
        p = pListHead
        while p:
            counter += 1
            p = p.next
        if k > counter:
            return None
        p = pListHead
        for _ in range(counter - k):
            p = p.next
        return p
