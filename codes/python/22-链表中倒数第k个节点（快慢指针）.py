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
        fast = pListHead
        # 要注意的临界点1：
        for _ in range(k - 1):
            fast = fast.next
            if fast is None:
                return None
        slow = pListHead
        # 要注意的临界点2：
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow
