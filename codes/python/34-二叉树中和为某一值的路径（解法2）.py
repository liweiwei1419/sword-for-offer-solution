# 47. 二叉树中和为某一值的路径
#
# 输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
#
# 从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
#
# 样例
# 给出二叉树如下所示，并给出num=22。
#       5
#      / \
#     4   6
#    /   / \
#   12  13  6
#  /  \    / \
# 9    1  5   1
#
# 输出：[[5,4,12,1],[5,6,6,5]]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findPath(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        self.__dfs(root, sum, [], res)
        return res

    def __dfs(self, node, residue, path, res):
        if node is None:
            return
        path.append(node.val)
        residue -= node.val

        if node.left is None and node.right is None and residue == 0:
            # 才用结算
            res.append(path[:])
            path.pop()
            return

        if node.left:
            self.__dfs(node.left, residue, path, res)

        if node.right:
            self.__dfs(node.right, residue, path, res)
        path.pop()