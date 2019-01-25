# 83、股票的最大利润
#
#
# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股票可能获得的利润是多少？
#
# 例如一只股票在某些时间节点的价格为[9, 11, 8, 5, 7, 12, 16, 14]。
#
# 如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。
#
# 样例
# 输入：[9, 11, 8, 5, 7, 12, 16, 14]
#
# 输出：11

# 不能使用贪心算法，区别于 122. 买卖股票的最佳时机 II

class Solution(object):
    def maxDiff(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        max_profit = 0
        for i in range(1, l):
            if nums[i] - nums[i - 1] > 0:
                max_profit += (nums[i] - nums[i - 1])
        return max_profit


if __name__ == '__main__':
    nums = [9, 11, 8, 5, 7, 12, 16, 14]
    solution = Solution()
    result = solution.maxDiff(nums)
    print(result)
