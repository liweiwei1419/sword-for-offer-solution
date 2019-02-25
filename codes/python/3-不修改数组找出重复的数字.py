class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """

        size = len(nums)
        assert size > 1

        l = 1
        r = size - 1

        while l < r:
            mid = l + (r - l + 1) // 2
            counter = 0
            for num in nums:
                if num < mid:
                    counter += 1
            if counter < mid:
                # 小于 4 的数最多只能是 3 个
                # 符合的话，重复的数一定在 [mid,right] 中
                l = mid
            else:
                assert counter >= mid

                r = mid - 1
        # 不要返回 nums[l] 了，l 和 r 不是索引
        return l
