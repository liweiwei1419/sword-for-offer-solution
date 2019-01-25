# 66. 两个链表的第一个公共结点
# 输入两个链表，找出它们的第一个公共结点。
#
# 样例
# 给出两个链表如下所示：
# A：        a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
#
# 输出第一个公共节点c1

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def findFirstCommonNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        p1 = headA
        p2 = headB

        while p1 != p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next

        return p1
