class Solution(object):
    def numberOfDice(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0 for _ in range(6 * n + 1)]

        # 动归数组初始值，表示 1 个骰子扔出 1-6 的可能数都为 1
        for i in range(1, 7):
            dp[i] = 1
        # 表示仍第 2 个骰子到第 n 个骰子
        for i in range(2, n + 1):
            # 从后向前写
            for j in range(6 * i, -1, -1):
                dp[j] = 0
                # 最后一个骰子可以扔 1 - 6 点
                for k in range(6, 0, -1):
                    if j - k < 0:
                        continue
                    dp[j] += dp[j - k]
        # 扔 n 个骰子的和为 [n, 6 * n]
        return dp[n:]


if __name__ == '__main__':
    solution = Solution()
    n = 2
    result = solution.numberOfDice(n)
    print(result)
