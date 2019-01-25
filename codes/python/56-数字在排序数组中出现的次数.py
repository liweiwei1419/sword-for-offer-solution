# # 56、数字在排序数组中出现的次数
# 统计一个数字在排序数组中出现的次数。
#
# 例如输入排序数组[1, 2, 3, 3, 3, 3, 4, 5]和数字3，由于3在这个数组中出现了4次，因此输出4。


class Solution(object):

    # 返回大于等于 target 的第 1 个数
    def get_left(self, nums, target):
        # [2,3,4,5,5,5,5,5,5,5]
        # [1,1,1,1,1,1,1,1,1,2,3,4,5,5,5,5,5,5,5]
        if nums[0] == target:
            return 0
        l = 1
        r = len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                assert nums[mid] >= target
                # 不能排除 mid
                r = mid
        return l

    def getNumberOfK(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        return self.get_left(nums, k + 1) - self.get_left(nums, k)


if __name__ == '__main__':
    nums = [2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10]
    k = 5
    solution = Solution()
    # result = solution.get_left(nums, 5, )
    # print(result)

    result = solution.getNumberOfK(nums, k)
    print(result)
