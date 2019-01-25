# 64、求 1 + 2 + 3 + ... + n

class Solution(object):
    def getSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        return (n ** 2 + n) >> 1


if __name__ == '__main__':
    n = 1000
    solution = Solution()
    result = solution.getSum(n)
    print(result)
