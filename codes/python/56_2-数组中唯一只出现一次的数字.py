class Solution(object):
    def findNumberAppearingOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0

        for i in range(32):
            count = 0
            for num in nums:
                # 不要忘记 & 1
                if (num >> i) & 1:
                    count += 1
            if count % 3:
                res += 1 << i
        return res


if __name__ == '__main__':
    nums = [1, 0, 0, 0, 2, 1, 1]
    solution = Solution()
    result = solution.findNumberAppearingOnce(nums)
    print(result)
