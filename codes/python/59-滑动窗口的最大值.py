# 同 LeetCode 第 239 题，传送门：滑动窗口最大值。
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 关键：如果后进来一个数，前面的元素比它小
        # 那么前面的元素就永远不可能是"滑动窗口中的最大值"

        l = len(nums)
        if l == 0 or k <= 0:
            return []

        res = []
        window = []
        for i in range(l):

            # 考虑什么时候，要把最大移除
            # 左边界划出的时候，应该是 window.pop(0)
            # [0,1,2,3,4]
            #     [    i]
            # window[0] == i - k 这个条件特别容易忽略
            if i >= k and window[0] == i - k:
                window.pop(0)
            # 考虑把不可能是最大的元素全部 kill 掉
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)

            # 什么时候有滑动窗口呢？
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    solution = Solution()
    result = solution.maxSlidingWindow(nums, k)
    print(result)
