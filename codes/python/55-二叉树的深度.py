# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def treeDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        queue = [(1, root)]
        res = 0
        while queue:
            top = queue.pop(0)
            cur_depth, node = top[0], top[1]
            res = max(res, cur_depth)
            if node.left:
                queue.append((cur_depth + 1, node.left))
            if node.right:
                queue.append((cur_depth + 1, node.right))
        return res
