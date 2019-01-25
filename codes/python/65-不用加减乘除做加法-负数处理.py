# 65、不用加减乘除做加法

class Solution(object):
    def add(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF
        return num1 if num1 >> 31 == 0 else num1 - (1 << 32)


if __name__ == '__main__':
    num1 = 5
    num2 = -6
    solution = Solution()
    result = solution.add(num1, num2)
    print(result)

