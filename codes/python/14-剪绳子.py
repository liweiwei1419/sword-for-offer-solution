class Solution(object):
    def maxProductAfterCutting(self, length):
        """
        :type length: int
        :rtype: int
        """

        assert length > 1

        dp = [0 for _ in range(length + 1)]

        dp[1] = 1

        for i in range(2, length + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[length]


if __name__ == '__main__':
    length = 8

    solution = Solution()
    result = solution.maxProductAfterCutting(length)
    print(result)
