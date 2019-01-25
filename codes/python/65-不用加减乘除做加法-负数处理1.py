# 65、不用加减乘除做加法


# 因为 Python

class Solution(object):
    def add(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        while True:
            # 不进位加法
            s = num1 ^ num2
            # 计算进位
            carry = num1 & num2

            # 手动把高于 32 位的部分变成 0
            num1 = s & 0xFFFFFFFF
            num2 = carry << 1

            if carry == 0:
                break
        # 如果是正数和 0 ，就直接返回这个正数好了
        if num1 >> 31 == 0:
            return num1
        # 如果是负数
        return num1 - (1 << 32)


if __name__ == '__main__':
    num1 = 5
    num2 = -6
    solution = Solution()
    result = solution.add(num1, num2)
    print(result)

    print(0x7fffffff)
