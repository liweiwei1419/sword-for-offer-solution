# -*- coding:utf-8 -*-
class Solution:
    def lastRemaining(self, n, m):
        # 特判
        if n == 0 and m == 0:
            return -1

        l = [i for i in range(n)]
        bt = 0
        while len(l) > 1:

            # 在这一行模拟约瑟夫环操作
            # 1、m - 1 ：因为当前数字算 1 个，走 m - 1 步
            # 2、len(l)：每次删去一个数，所以得动态取
            bt = (bt + m - 1) % len(l)

            l.pop(bt)
        return l[0]


if __name__ == '__main__':
    n = 5
    m = 3
    solution = Solution()
    result = solution.lastRemaining(n, m)
    print(result)
