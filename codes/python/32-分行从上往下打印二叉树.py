# 44. 分行从上往下打印二叉树
# 从上到下按层打印二叉树，同一层的结点按从左到右的顺序打印，每一层打印到一行。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            cur_list = []
            for _ in range(size):
                top = queue.pop(0)
                cur_list.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.append(cur_list)
        return res
