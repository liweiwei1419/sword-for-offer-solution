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
        for _ in range(k - 1):
            # 注意：先移动，再判断是否为空
            fast = fast.next
            if fast is None:
                return None

        slow = pListHead
        # 注意：下一个结点不为空的时候，才往下走
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow
