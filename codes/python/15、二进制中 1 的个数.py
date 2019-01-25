class Solution(object):
    def NumberOf1(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            if n & 1:
                ans += 1
            n = n >> 1

        return ans
