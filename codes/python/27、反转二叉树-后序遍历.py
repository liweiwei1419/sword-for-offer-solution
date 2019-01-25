# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def mirror(self, root):
        """
        :type root: TreeNode
        :rtype: void
        """
        # 先写递归终止条件
        if root is None:
            return root

        # 按照后序遍历的方式
        self.mirror(root.left)
        self.mirror(root.right)
        root.left, root.right = root.right, root.left
