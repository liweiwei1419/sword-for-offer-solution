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

    def __get_list_node_size(self, root):
        node = root
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    def findFirstCommonNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        s1 = self.__get_list_node_size(headA)
        s2 = self.__get_list_node_size(headB)

        # 我们默认 l1 >= l2
        h1 = headA
        h2 = headB

        if s2 > s1:
            # 如果 B 长度更长，把二者交换
            h1 = headB
            h2 = headA
        # 现在 h1 上走 (s1 - s2) 这么多长度
        for _ in range(abs(s1 - s2)):
            h1 = h1.next
        # 然后齐头并进
        while h1 and h2 and h1.val != h2.val:
            h1 = h1.next
            h2 = h2.next

        # 走到这里，如果是因为 h1 和 h2 都空了，返回 Node
        if h1 is None and h2 is None:
            return None
        else:
            return h1
