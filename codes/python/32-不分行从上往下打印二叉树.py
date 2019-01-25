# 43. 不分行从上往下打印二叉树
# 从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。
#

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            # 弹出队首元素，索引编号 0 不要忘记写了
            top = queue.pop(0)
            res.append(top.val)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        return res
