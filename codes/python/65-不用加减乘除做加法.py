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

        while True:
            # 先做不进位加法
            s = num1 ^ num2
            # 再计算进位
            carry = num1 & num2
            if carry == 0:
                return s
            num1 = s
            num2 = carry << 1


if __name__ == '__main__':
    num1 = 100
    num2 = 200
    solution = Solution()
    result = solution.add(num1, num2)
    print(result)
