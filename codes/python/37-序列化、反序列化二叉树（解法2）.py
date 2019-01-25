# 37、序列化、反序列化二叉树


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 前序遍历
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        res = []
        if root is None:
            return '!'

        stack = [root]
        while stack:
            top = stack.pop()
            if top is None:
                res.append('!')
            else:
                stack.append(top.right)
                stack.append(top.left)
                res.append(str(top.val))
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = data.split(' ')
        return self.__build_tree(queue)

    def __build_tree(self, queue):
        if queue:
            top = queue.pop(0)
            if top != '!':
                root = TreeNode(int(top))
                root.left = self.__build_tree(queue)
                root.right = self.__build_tree(queue)
                return root
            else:
                return None
        # 如果 queue 为空，就什么都不做


if __name__ == '__main__':
    solution = Solution()

    n8 = TreeNode(8)
    n12 = TreeNode(12)
    n2 = TreeNode(2)
    n6 = TreeNode(6)
    n4 = TreeNode(4)

    n8.left = n12
    n8.right = n2
    n2.left = n6
    n2.right = n4

    result = solution.serialize(n8)
    print(result)

    result1 = solution.deserialize(result)
    print(result1.val)
