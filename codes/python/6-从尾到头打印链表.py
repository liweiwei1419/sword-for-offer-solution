# 17. 从尾到头打印链表
# 输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。
# 返回的结果用数组存储。


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):

    def printListReversingly(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        p = head
        stack = []
        while p:
            stack.insert(0, p.val)
            p = p.next
        return stack
