# 46、把数字翻译成字符串

# 给定一个数字，我们按照如下规则把它翻译为字符串：
#
# 0翻译成”a”，1翻译成”b”，……，11翻译成”l”，……，25翻译成”z”。
#
# 一个数字可能有多个翻译。例如12258有5种不同的翻译，它们分别是”bccfi”、”bwfi”、”bczi”、”mcfi”和”mzi”。
#
# 请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。
#
# 样例


class Solution:
    def getTranslationCount(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = str(s)
        l = len(s)
        if l == 0:
            return 0
        dp = [None for _ in range(l)]

        # dp[i] 表示 s[0,i] ，包括 i ，一共有多少种翻译的方法

        dp[0] = 1
        for i in range(1, l):
            # 当前值至少是 dp[i-1]，因为 s[i] 可以单独翻译
            cur = dp[i - 1]

            # 看一看 s[i-1,i] 是不是可以翻译
            if 9 < int(s[i - 1:i + 1]) < 26:
                if i - 2 < 0:
                    # 12
                    cur += 1
                else:
                    # 要考虑到数组下标越界问题
                    cur += dp[i - 2]
            dp[i] = cur
        return dp[l - 1]


if __name__ == '__main__':
    s = 12258
    solution = Solution()
    result = solution.getTranslationCount(s)
    print(result)
