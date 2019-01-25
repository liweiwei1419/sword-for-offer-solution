# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 穿针引线的写法，一定要画图才能写出来
# 比较麻烦，还是递归处理简单

class Solution(object):
    def merge(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 引入头结点可以简化对问题的讨论
        dummy_node = ListNode(-1)
        cur_node = dummy_node
        p1 = l1
        p2 = l2

        while p1 and p2:
            # 两者都不为空，才须要比较
            # 其中有一个为空的时候，把其中一个接到另一个尾巴就好了
            if p1.val < p2.val:
                # next 指针修改
                cur_node.next = p1
                # p1 后移
                p1 = p1.next
            else:
                cur_node.next = p2
                p2 = p2.next
            cur_node = cur_node.next
        # 跳出循环的时候，一定有：p1 为空或者 p2 为空
        # 其中有一个为空的时候，把其中一个接到另一个尾巴就好了
        if p1 is None:  # 这一句写成 if not p1 也是可以的，不过不好理解
            cur_node.next = p2
        if not p2:
            cur_node.next = p1
        return dummy_node.next
