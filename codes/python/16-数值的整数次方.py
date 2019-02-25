class Solution(object):
    def Power(self, base, exponent):
        """
        :type base: float
        :type exponent: int
        :rtype: float
        """

        if exponent < 0:
            base = 1 / base
            # 负数变成正数
            exponent = -exponent

        res = 1
        while exponent:
            if exponent & 1:
                res *= base
            base *= base
            exponent >>= 1
        return res
