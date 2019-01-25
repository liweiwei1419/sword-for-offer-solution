# 56. 从1到n整数中1出现的次数
#
# 输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。
#
# 例如输入12，从1到12这些整数中包含“1”的数字有1，10，11和12，其中“1”一共出现了5次。
#
# 样例
# 输入： 12
# 输出： 5
class Solution(object):
    def numberOf1Between1AndN_Solution(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        number = []
        while n:
            number.append(n % 10)
            n //= 10

        res = 0
        for i in range(len(number) - 1, -1, -1):
            left = 0
            right = 0
            # 想清楚这里 t 为什么从 1 开始
            t = 1
            for j in range(len(number) - 1, i, -1):
                left = left * 10 + number[j]

            for j in range(i - 1, -1, -1):
                right = right * 10 + number[j]
                t *= 10
            # print(left, right)
            # 至少有左边的数这么多
            res += left * t
            # print(number[i], left, right, t, left * t)
            if number[i] == 1:
                res += right + 1
            elif number[i] > 1:
                res += t
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 45032
    result = solution.numberOf1Between1AndN_Solution(n)
    print('result', result)
