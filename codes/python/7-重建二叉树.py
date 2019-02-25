# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        返回构造的 TreeNode 根结点
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 在编码过程中，一定要保证 len(pre) == len(tin)，否则逻辑一定不正确
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            # 这里要返回结点，而不是返回具体的数
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        # 直接得到在中序遍历中的位置，下面算好偏移量就好了，如果容易算错，记得拿具体例子
        pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
        return root
