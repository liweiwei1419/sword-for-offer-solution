# 34. 链表中环的入口结点
# 给定一个链表，若其中包含环，则输出环的入口节点。
#
# 若其中不包含环，则输出null。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def entryNodeOfLoop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先考虑边界情况
        if head is None or head.next is None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            # 慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # 说明链表中不存在环
                break

        if fast is None or fast.next is None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        # 走到这里，说明 slow == fast
        return slow


if __name__ == '__main__':
    # [1, 2, 3, 7, 4, 5, 6]
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l7 = ListNode(7)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l3.next = l7
    l7.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l2
    solution = Solution()
    result = solution.entryNodeOfLoop(l1)
    print(result)
