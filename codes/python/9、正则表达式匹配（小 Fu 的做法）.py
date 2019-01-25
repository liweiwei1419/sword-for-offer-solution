# 9、正则表达式匹配
class Solution(object):

    # 状态：dp[i][j] 表示 s 中前 i 个字符与 p 的前 j 个字符组成的表示式是否匹配
    # i 和 j 表示个数
    # 代码中出现 i 均表示 s 中的索引或者个数
    # 代码中出现 j 均表示 p 中的索引或者个数
    # 出现 -1 都表示当前考虑的
    # 出现 -2 都表示当前再前一个

    # 参考资料：http://www.voidcn.com/article/p-zioiffqq-mm.html

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)

        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        # 当 s 和 p 的长度都为 0 的时候，定义成匹配
        dp[0][0] = True

        # 特判
        for j in range(2, m + 1):
            if p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True

        # 下面分别对字符串 s 和模式串 p 进行匹配
        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # 这是最麻烦的情况

                    if p[j - 2] != s[i - 1] and p[j - 2] != '.':
                        # 例子：s a
                        #        j-1
                        #      p b    *
                        #        j-2  j-1
                        # 此时只能把 * 当成 0 次，即 * 和它之前的字母不出现，所以一下子要减去 2
                        # p[j - 2] != '.' 这一点别忘了
                        # 不能匹配
                        dp[i][j] = dp[i][j - 2]
                    else:
                        # 接下来是可以匹配
                        # 例子：s a
                        #        j-1
                        #      p .    *
                        #        j-2  j-1
                        # 此时把 * 当成 0 次，
                        # 此时把 * 当成 1 次，
                        # 此时把 * 当成 多 次，直接把 i - 1 ，这是最难的地方
                        dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]
        return dp[n][m]


if __name__ == '__main__':
    solution = Solution()
    s = 'aaa'
    p = 'ab*ac*a'
    result = solution.isMatch(s, p)
    print(result)
