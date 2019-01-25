class Solution(object):
    def findContinuousSequence(self, sum):
        """
        :type sum: int
        :rtype: List[List[int]]
        """

        res = []

        left = 1
        right = 2

        half = sum // 2 + 1
        while left < right <= half:
            cur_sum = (left + right) * (right - left + 1) // 2
            if cur_sum == sum:
                res.append([i for i in range(left, right + 1)])
                right += 1
            elif cur_sum < sum:
                right += 1
            else:
                assert cur_sum > sum
                left += 1
        return res


if __name__ == '__main__':
    sum = 15
    solution = Solution()
    result = solution.findContinuousSequence(sum)
    print(result)
