class Solution(object):
    def getMissingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        size = len(nums)
        l = 0
        r = size

        while l < r:

            mid = l + (r - l) // 2
            if nums[mid] > mid:
                # [0,1,2,3,4,6]
                # mid 有可能是要求的数
                r = mid
            else:
                assert nums[mid] <= mid
                l = mid + 1
        return l


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2, 4]
    result = solution.getMissingNumber(nums)
    print(result)
