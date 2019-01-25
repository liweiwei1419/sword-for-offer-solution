# 10-2、变态跳台阶

#


class Solution:
    def jumpFloorII(self, number):
        if number == 0:
            return 1
        if number == 1:
            return 1
        dp = [1 for _ in range(number + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, number + 1):
            for j in range(1, i):
                dp[i] += dp[j]
        return dp[number]
