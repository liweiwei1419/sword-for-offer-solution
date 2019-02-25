# 9、正则表达式匹配
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        n = len(s)
        m = len(p)
        # 初始化成 -1 表示未计算过
        f = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        return self.dp(0, 0, s, p, f, n, m)

    def dp(self, x, y, s, p, f, n, m):

        if f[x][y] != -1:
            return f[x][y]
        if y == m:
            # 如果模式串用完了，看看字符串是不是也用完了
            f[x][y] = (x == n)
            return f[x][y]
        first_match = x < n and (s[x] == p[y] or p[y] == '.')

        if y + 1 < m and p[y + 1] == '*':
            res = self.dp(x, y + 2, s, p, f, n, m) or self.dp(x + 1, y, s, p, f, n, m)
        else:
            res = first_match and self.dp(x + 1, y + 1, s, p, f, n, m)

        f[x][y] = res
        return f[x][y]


if __name__ == '__main__':
    solution = Solution()
    s = 'aaa'
    p = 'ab*ac*a'
    result = solution.isMatch(s, p)
    print(result)
