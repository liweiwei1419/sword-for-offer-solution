# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归写法：得引入辅助函数

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 先写递归终止条件
        if root is None:
            return True
        return self.__helper(root.left, root.right)

    def __helper(self, p1, p2):
        if p1 is None and p2 is None:
            return True
        if p1 is None or p2 is None:
            return False
        return p1.val == p2.val and self.__helper(p1.left, p2.right) and self.__helper(p1.right, p2.left)
