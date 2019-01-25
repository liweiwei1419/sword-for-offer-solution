# 48. 复杂链表的复刻
#
#
# 请实现一个函数可以复制一个复杂链表。
#
# 在复杂链表中，每个结点除了有一个指针指向下一个结点外，还有一个额外的指针指向链表中的任意结点或者null。

# Definition for singly-linked list with a random pointer.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        # 第 1 步：根据 next 指针复制出一个新旧合一的链表
        cur_node = head
        while cur_node:
            # 先暂存 cur_node 的 next_node 下一次遍历要用
            next_node = cur_node.next
            new_node = ListNode(cur_node.val)

            cur_node.next = new_node
            new_node.next = next_node
            # 指针遍历到下一个结点
            cur_node = next_node
        # 第 2 步：根据旧结点 random 指针，给新结点的 random 指针做出正确的指向
        cur_node = head
        while cur_node:
            new_node = cur_node.next
            # 同样要先暂存 cur_node.next_node
            next_node = new_node.next
            # 要记得做非空判断，因为题目中说了 random 有可能为空
            new_node.random = cur_node.random.next if cur_node.random else None
            cur_node = next_node

        # 第 3 步：旧结点和新结点分离（拆分链表）
        cur_node = head
        res = cur_node.next
        while cur_node:
            new_node = cur_node.next
            next_node = new_node.next
            # 恢复原始结点
            cur_node.next = new_node.next
            # 恢复拷贝结点
            # 这里也要同样注意空指针的问题，克隆结点的最后一个结点的下一个结点是 null
            new_node.next = next_node.next if next_node else None
            cur_node = next_node
        return res
