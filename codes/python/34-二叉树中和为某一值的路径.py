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
        # 递归，就应该先写递归终止条件
        if node is None:
            return
        # 走到这里 node 肯定非空，所以可以使用 left 和 right 成员变量
        # 走完以后，要记得回溯，状态要重置
        # 先把它加到路径中，在各种 if 都不成立的最后，要记得 pop 出去
        path.append(node.val)
        if node.left is None and node.right is None:
            # 如果是叶子结点，并且 residue 就等于当前结点的值
            if node.val == residue:
                res.append(path[:])
                # 注意：这里不要 return ，如果要 return，return 之前把 path 执行 pop 操作
        # 走到这里是非叶子结点，所以左边要走一走，右边也要走一走
        if node.left:
            self.__dfs(node.left, residue - node.val, path, res)
        if node.right:
            self.__dfs(node.right, residue - node.val, path, res)
        path.pop()