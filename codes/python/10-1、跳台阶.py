# 10-2、变态跳台阶

# 使用滚动变量


class Solution(object):
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1

        while n:
            c = a + b
            a = b
            b = c
            n -= 1
        return a
