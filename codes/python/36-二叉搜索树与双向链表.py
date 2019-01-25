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

    def __init__(self):
        self.linked_list_tail = None
        self.res = None

    def convert(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.__dfs(root)
        return self.res

    # 中序遍历
    def __dfs(self, root):
        if root is None:
            return
        self.__dfs(root.left)

        if self.linked_list_tail is None:
            self.linked_list_tail = root
            self.res = root
        else:
            self.linked_list_tail.right = root
            root.left = self.linked_list_tail
            self.linked_list_tail = root
        self.__dfs(root.right)
