class Solution(object):

    # 把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。
    # 例如 6、8 都是丑数，但 14 不是，因为它包含因子 7 。
    # 习惯上我们把 1 当做是第一个丑数。
    # 求按从小到大的顺序的第 N 个丑数。

    # 动态规划

    def getUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 0:
            return 0
        if n == 1:
            return 1

        dp = [None for _ in range(n)]
        # 根据题意：习惯上我们把 1 当做第一个丑数。
        dp[0] = 1
        m2 = 0
        m3 = 0
        m5 = 0
        for i in range(1, n):
            dp[i] = min(dp[m2] * 2, dp[m3] * 3, dp[m5] * 5)
            while dp[m2] * 2 <= dp[i]:
                m2 += 1
            while dp[m3] * 3 <= dp[i]:
                m3 += 1
            while dp[m5] * 5 <= dp[i]:
                m5 += 1
        return dp[n - 1]
