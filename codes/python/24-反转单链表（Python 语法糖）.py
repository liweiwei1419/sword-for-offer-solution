# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 穿针引线，可以看到 while 循环体部分的代码是首尾相连的，有些单链表的题目也有这种规律，感觉很神奇
# 在 Python 中，其实还有更简便的写法，就跟斐波拉契数列一样


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
