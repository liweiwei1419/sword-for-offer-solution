# -*- coding:utf-8 -*-
class Solution:
    def lastRemaining(self, n, m):
        if n == 0 and m == 0:
            return -1

        l = list(range(n))
        bt = 0
        while len(l) > 1:
            bt = (bt + m - 1) % len(l)
            l.pop(bt)

        return l[0]


if __name__ == '__main__':
    n = 1
    m = 1
    solution = Solution()
    result = solution.lastRemaining(n, m)
    print(result)
