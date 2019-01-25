# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 非递归写法：借助双端队列辅助判断

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 先写递归终止条件
        if root is None:
            return True

        # 其实应该用 from collections import deque
        deque = []

        deque.insert(0, root.left)
        deque.append(root.right)

        while deque:
            l_node = deque.pop(0)
            r_node = deque.pop()

            if l_node is None and r_node is None:
                continue
            if l_node is None or r_node is None:
                return False
            # 代码走到这里一定有 l_node 和 r_node 非空
            # 因此可以取出 val 进行判断了
            if l_node.val != r_node.val:
                return False
            deque.insert(0, l_node.right)
            deque.insert(0, l_node.left)
            deque.append(r_node.left)
            deque.append(r_node.right)
        return True
