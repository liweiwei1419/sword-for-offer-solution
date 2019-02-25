class Solution(object):
    def Power(self, base, exponent):
        """
        :type base: float
        :type exponent: int
        :rtype: float
        """

        if exponent == 0:
            return 1

        if exponent < 0:
            return 1 / self.Power(base, -exponent)

        # 如果是奇数
        if exponent & 1:
            return base * self.Power(base, exponent - 1)
        return self.Power(base * base, exponent >> 1)