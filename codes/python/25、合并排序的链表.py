# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def merge(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # 代码能走到这里说明 l1 和 l2 均非空
        # 比较那个小就行了
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        # 走到这里 l1.val >= l2.val
        l2.next = self.merge(l1, l2.next)
        return l2
