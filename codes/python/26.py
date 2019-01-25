# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # pRoot1 是大树
        # pRoot2 是小树
        result = False
        if pRoot1 and pRoot2:
            # 第 1 步：在树 A 中查找与根结点的值一样的结点
            # 这里排除了 pRoot2 是空树的情况
            if pRoot1.val == pRoot2.val:
                # 判断树 1 是不是包含树 2
                result = self.__doesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                # 如果树 1 不包含树 2
                return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(
                    pRoot1.right, pRoot2)
        return result

    def __doesTree1HaveTree2(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        # 走到这里说明 assert pRoot1.val == pRoot2.val 为 True
        return self.__doesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.__doesTree1HaveTree2(pRoot1.right,
                                                                                                 pRoot2.right)
