# 50、字符串中第一个只出现一次的字符
# 在字符串中找出第一个只出现一次的字符。
#
# 如输入"abaccdeff"，则输出b。
#
# 如果字符串中不存在只出现一次的字符，返回#字符。
#
# 样例：
# 输入："abaccdeff"
#
# 输出：'b'

class Solution:
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return '#'

        counter = [0 for _ in range(256)]
        for alpha in s:
            counter[ord(alpha)] += 1
        for alpha in s:
            if counter[ord(alpha)] == 1:
                return alpha
        # 要注意：如果是 "aabbcc" 这种所有的字符都出现不止 1 次，
        # 就按照题意，返回 '#'
        return '#'


if __name__ == '__main__':
    s = "abaccdeff"
    solution = Solution()
    result = solution.firstNotRepeatingChar(s)
    print(result)
