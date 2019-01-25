# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 递归写法：用递归就不用思考穿针引线这种事情了。


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归的终止条件一定要写对：考虑结点为空和但结点的情况
        if head is None or head.next is None:
            return head
        next = head.next
        new_head = self.reverseList(next)
        next.next = head
        head.next = None
        return new_head
