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
        # 应该先判断下一个结点是否为空，如果不为空，则递归调用，在回溯的时候，才添加到结果中
        if listnode.next:
            self.helper(res, listnode.next)
        # 回溯时添加
        res.append(listnode.val)
