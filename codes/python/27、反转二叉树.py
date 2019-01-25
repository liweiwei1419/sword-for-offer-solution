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

        # 按照前序遍历的方式
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
