# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthNode(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: TreeNode
        """

        if root is None:
            return None

        # 1 表示递归处理，0 表示当前我就要处理这个结点
        stack = [(1, root)]

        while stack:
            type, node = stack.pop()
            if type == 0:
                k -= 1
                if k == 0:
                    return node
            else:
                if node.right:
                    stack.append((1, node.right))
                stack.append((0, node))
                if node.left:
                    stack.append((1, node.left))
