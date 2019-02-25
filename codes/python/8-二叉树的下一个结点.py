# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.father = None


class Solution(object):
    def inorderSuccessor(self, q):
        """
        :type q: TreeNode
        :rtype: TreeNode
        """

        if q is None:
            return None

        # 分类讨论1：如果这个结点有右子树，返回这个右子树的最小者
        if q.right:
            node = q.right
            while node.left:
                node = node.left
            return node
        # 分类讨论2：如果这个结点没有右子树，向上追溯，追到父亲结点的左结点是自己
        while q.father:
            if q.father.left == q:
                return q.father
            q = q.father
        return None
