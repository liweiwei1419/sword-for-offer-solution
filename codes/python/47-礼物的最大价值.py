# 47、礼物的最大价值

# 在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
#
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或者向下移动一格直到到达棋盘的右下角。
#
# 给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？


class Solution(object):
    def getMaxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        dp = [None for _ in range(n)]

        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][0]
                else:
                    dp[j] = grid[i][j] + max(dp[j - 1], dp[j])

        return dp[n - 1]


if __name__ == '__main__':
    grid = [
        [2, 3, 1],
        [1, 7, 1],
        [4, 6, 1]
    ]

    solution = Solution()
    result = solution.getMaxValue(grid)
    print(result)
