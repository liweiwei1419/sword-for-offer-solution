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
        queue = [root]
        while queue:
            top = queue.pop(0)
            top.left, top.right = top.right, top.left
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        return root
