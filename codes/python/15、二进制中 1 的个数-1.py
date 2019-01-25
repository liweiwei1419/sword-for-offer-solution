class Solution(object):
    def NumberOf1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print((-1 & (2**31-1)) >> 1)
        # print((-3) >> 1)
        n = n & (2 ** 32 - 1)
        # print(n)
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
            # print(n)
        return count
