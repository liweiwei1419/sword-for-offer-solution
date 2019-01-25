# 36. 二叉搜索树与双向链表
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def convert(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        head, _ = self.__dfs(root)

        return head

    def __dfs(self, root):
        # 如果这个结点是叶子结点
        if root.left is None and root.right is None:
            return (root, root)

        # 如果有左孩子，还有右边孩子
        if root.left and root.right:
            ll, lr = self.__dfs(root.left)
            rl, rr = self.__dfs(root.right)
            # 下面穿针引线
            lr.right = root
            root.left = lr
            root.right = rl
            rl.left = root
            return (ll, rr)
        # 走到这里，就是二者之一为空
        if root.left:
            ll, lr = self.__dfs(root.left)
            lr.right = root
            root.left = lr
            return (ll, root)

        if root.right:
            rl, rr = self.__dfs(root.right)
            root.right = rl
            rl.left = root
            return (root, rr)
