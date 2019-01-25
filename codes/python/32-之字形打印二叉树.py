# 45. 之字形打印二叉树
# 请实现一个函数按照之字形顺序从上向下打印二叉树。
#
# 即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
# 样例
# 输入如下图所示二叉树[8, 12, 2, null, null, 6, 4, null, null, null, null]
#     8
#    / \
#   12  2
#      / \
#     6   4
# 输出：[[8], [2, 12], [6, 4]]

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
        turn_left = True
        while queue:
            cur_list = []
            size = len(queue)
            for _ in range(size):
                top = queue.pop(0)
                if turn_left:
                    cur_list.append(top.val)
                else:
                    cur_list.insert(0, top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.append(cur_list)
            turn_left = not turn_left
        return res


if __name__ == '__main__':
    res = []
    res.insert(0, 1)
    res.insert(0, 2)
    res.insert(0, 3)
    print(res)

    a = True
    for _ in range(10):
        a = not a
    print(a)
