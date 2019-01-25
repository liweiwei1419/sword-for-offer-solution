# 66、构建乘积数组

class Solution(object):
    def multiply(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        l = len(A)
        if l == 0:
            return []
        b = [None for _ in range(l)]

        b[0] = 1
        # 计算下三角连乘的结果
        for i in range(1, l):
            b[i] = b[i - 1] * A[i - 1]

        temp = 1
        for i in range(l - 2, -1, -1):
            temp *= A[i + 1]
            b[i] *= temp
        return b
