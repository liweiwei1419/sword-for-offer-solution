# # 56、数字在排序数组中出现的次数
# 统计一个数字在排序数组中出现的次数。
#
# 例如输入排序数组[1, 2, 3, 3, 3, 3, 4, 5]和数字3，由于3在这个数组中出现了4次，因此输出4。


class Solution(object):

    def getNumberOfK(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0

        # 设置辅助函数，给一个 nums，一个 k，返回大于等于 k 的第一个数的索引
        return self.__helper(nums, k + 1) - self.__helper(nums, k)

    def __helper(self, nums, k):
        """
        返回大于等于 k 的第一个数的索引
        :param nums:
        :param k:
        :return:
        """
        size = len(nums)
        if size == 0:
            return 0

        l = 0
        # 注意：这里一定要写 size
        r = size
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= k:
                r = mid
            else:
                assert nums[mid] < k
                # [1,2,3,4,5]
                l = mid + 1
        return l


if __name__ == '__main__':
    nums = [2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10]
    k = 5
    solution = Solution()
    # result = solution.get_left(nums, 5, )
    # print(result)

    result = solution.getNumberOfK(nums, k)
    print(result)
