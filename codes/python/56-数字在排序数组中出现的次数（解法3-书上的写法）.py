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

        k_right = self.__get_right_k(nums, k)
        k_left = self.__get_left_k(nums, k)

        if k_right == -1 or k_left == -1:
            return 0

        return k_right - k_left + 1

    def __get_right_k(self, nums, k):
        # 找到最右边的 index ，使得 nums[index] = k
        size = len(nums)
        if size == 0:
            return -1
        l = 0
        r = size - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] <= k:
                # [1,2,5,5,5,7]
                l = mid
            elif nums[mid] > k:
                r = mid - 1
        if nums[l] != k:
            return -1
        return l

    def __get_left_k(self, nums, k):
        # 找到最左边的 index ，使得 nums[index] = k
        size = len(nums)
        if size == 0:
            return -1
        l = 0
        r = size - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= k:
                r = mid
            else:
                assert nums[mid] < k
                l = mid + 1
        if nums[l] != k:
            return -1
        return l


if __name__ == '__main__':
    nums = [2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10]
    k = 5
    solution = Solution()
    # result = solution.get_left(nums, 5, )
    # print(result)

    result = solution.getNumberOfK(nums, k)
    print(result)
