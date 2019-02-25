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
        res = []
        self.helper(res, head)
        return res

    def helper(self, res, listnode):
        if listnode is None:
            return

        if listnode.next is None:
            res.append(listnode.val)
        self.helper(res, listnode.next)
