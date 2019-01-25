# 65、不用加减乘除做加法

class Solution(object):
    def add(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # 特判
        if num1 == 0 or num2 == 0:
            return max(num1, num2)

        res = 0
        # 进位
        carry = 0
        for i in range(32):
            a = num1 & (1 << i)
            b = num2 & (1 << i)
            # 不进位的和
            s_ = (a ^ b) ^ carry
            # 下面计算进位，三者之中，任意两者同为 1 的时候，就可以进位
            carry = (a & b) | (a & carry) | (b & carry)
            carry <<= 1
            res += s_
        if res >> 31 == 0:
            return res
        return res - (1 << 32)


if __name__ == '__main__':
    num1 = -3
    num2 = -2

    solution = Solution()
    result = solution.add(num1, num2)
    print(result)

    # print(bin(-1 & 0b1111111111111111))
    # print(-1 & 0xffffffff)
