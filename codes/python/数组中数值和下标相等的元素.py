class Solution(object):
    def getNumberSameAsIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 使用二分法
        size = len(nums)
        l = 0
        r = size - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < mid:
                l = mid + 1
            else:
                assert nums[mid] >= mid
                r = mid
        return l if nums[l] == l else -1


if __name__ == '__main__':
    solution = Solution()
    nums = [-3, -1, 1, 3, 5]
    result = solution.getNumberSameAsIndex(nums)
    print(result)
