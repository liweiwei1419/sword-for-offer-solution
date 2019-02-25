# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留。

class Solution(object):
    def deleteDuplication(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        # 一下子要看两个，所以是
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                # 删除的起点至少是 cur.next.next
                del_node = cur.next.next

                while del_node.next and del_node.val == del_node.next.val:
                    del_node = del_node.next
                # 来到了一个新的结点，值不同

                cur.next = del_node.next
                del_node.next = None
            else:
                cur = cur.next

        return dummy.next
