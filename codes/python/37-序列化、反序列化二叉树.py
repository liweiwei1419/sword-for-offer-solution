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

        res = ''
        if root is None:
            # 后面这个空格不能丢
            return '! '
        res += str(root.val)
        res += ' '
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(' ')
        return self.__helper(arr)

    def __helper(self, arr):
        if arr:
            top = arr.pop(0)
            if top != '!':
                root = TreeNode(int(top))
                root.left = self.__helper(arr)
                root.right = self.__helper(arr)
                return root
            else:
                return None


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
