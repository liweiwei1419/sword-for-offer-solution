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
        stack1 = []
        stack2 = []
        node1 = headA
        while node1:
            stack1.append(node1)
            node1 = node1.next
        node2 = headB
        while node2:
            stack2.append(node2)
            node2 = node2.next
        # 注意：这里有陷阱，一定要先设置一个 result 结点
        # 如果两个链表没有公共元素，res 不会被赋值
        res = None
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val == node2.val:
                # 这里暂存一下，最后一个相等的结点才是我们求的
                res = node1
                continue
            if stack1 is None or stack2 is None:
                return None
        return res
