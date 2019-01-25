# 42. 连续子数组的最大和


# 输入一个 非空 整型数组，数组里的数可能为正，也可能为负。
#
# 数组中一个或连续的多个整数组成一个子数组。
#
# 求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
# 样例
# 输入：[1, -2, 3, 10, -4, 7, 2, -5]
#
# 输出：18


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        dp = [0 for _ in range(l)]
        dp[0] = nums[0]

        for i in range(1, l):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        # 最后不要忘记拉通求一遍最大值，或者在上面遍历的时候，就保存最大值
        return max(dp)


if __name__ == '__main__':
    nums = [1, -2, 3, 10, -4, 7, 2, -5]

    solution = Solution()
    result = solution.maxSubArray(nums)
    print(result)
