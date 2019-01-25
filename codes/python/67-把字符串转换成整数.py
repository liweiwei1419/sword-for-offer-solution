# 67、把字符串转换成整数


class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """

        # 去掉左右空格
        s = str.strip()

        l = len(s)
        if l == 0:
            return 0

        # 遍历指针
        index = 0
        # 符号
        sign = 1
        # 第 1 位符号位
        s_sign = s[0]

        # 最终结果
        res = 0

        INT_MIN = -1 << 31
        INT_MAX = (1 << 31) - 1

        # 符号位是正或负号的时候 index 都加 1
        if s_sign == '+':
            index += 1
        elif s_sign == '-':
            index += 1
            sign = -1

        for i in range(index, l):
            c = s[i]
            if c.isdigit():
                cint = ord(c) - ord('0')
                res = res * 10 + cint
                if res * sign > INT_MAX:
                    break
            else:
                break

        res *= sign

        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        return res


if __name__ == '__main__':
    solution = Solution()
    str = '2147483647'
    result = solution.strToInt(str)
    print(result)
