# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.__helper(root) != -1

    def __helper(self, node):
        """
        返回以 root 为根的二叉树的高度，如果左右子树其中之一不是 AVL ，则返回 -1
        :param node:
        :return:
        """
        if node is None:
            return 0
        left = self.__helper(node.left)
        right = self.__helper(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
