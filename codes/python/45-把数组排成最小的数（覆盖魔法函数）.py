# 45、把数组排成最小的数
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
# 例如输入数组[3, 32, 321]，则打印出这3个数字能排成的最小数字321323。


class NumCompare(str):
    def __lt__(self, other):
        return int(self + other) - int(other + self)


class Solution(object):
    def printMinNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        if len(nums) == 0:
            return ''
        # 自定义排序规则
        result = sorted(map(str, nums), key=NumCompare)
        return ''.join(result)


if __name__ == '__main__':
    nums = [3, 32, 321]
    solution = Solution()
    result = solution.printMinNumber(nums)
    print(result)
