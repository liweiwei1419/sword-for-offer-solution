# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    flag = 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True
        self.__dfs(root)
        return self.flag

    def __dfs(self, node):
        """
        返回以 root 为根的二叉树的高度，如果左右子树其中之一不是 AVL ，则返回 -1
        :param node:
        :return:
        """
        if node is None:
            return 0
        left = self.__dfs(node.left)
        right = self.__dfs(node.right)

        if abs(left - right) > 1:
            self.flag = 0
            # 这里不能写 return
        return max(left, right) + 1
