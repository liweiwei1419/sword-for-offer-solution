# 28. 在O(1)时间删除链表结点
# 给定单向链表的一个节点指针，定义一个函数在O(1)时间删除该结点。
#
# 假设链表一定存在，并且该节点一定不是尾节点。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void
        """
        next = node.next
        node.val = next.val
        node.next = next.next
        next.next = None
