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
        map = dict()
        dummy_node = ListNode(-1)
        # p 指针用于新链表的 next 指针赋值
        p = dummy_node

        # 遍历一次链表，做两件事
        # 1、复制结点
        # 2、只管 next 指针
        cur_node = head
        while cur_node:
            new_node = ListNode(cur_node.val)
            # 把新旧结点的对应关系放在一个 map 里
            map[cur_node] = new_node
            cur_node = cur_node.next

            p.next = new_node
            p = new_node

        # 接下来做随机指针的复制
        for old_node, new_node in map.items():
            # 要记得判断是否为空，否则 None 不能作为 map  key
            if old_node.random:
                new_node.random = map[old_node.random]
        return dummy_node.next
