class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)

        # 1、去掉多余的空格
        i = 0
        while i < size and s[i] == ' ':
            i += 1

        j = size - 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        if i > j:
            return False

        s = s[i:j - i + 1]
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if len(s) == 0:
            return False
        if len(s) == 1 and s[0] == '.':
            return False
        # 点的个数
        dot_cnt = 0
        # e 的个数
        e_cnt = 0

        size = len(s)
        i = -1
        while i < size - 1:
            i += 1
            if '0' <= s[i] <= '9':
                continue
            elif s[i] == '.':
                dot_cnt += 1
                # 如果没有 e，并且点的数量大于 1
                if e_cnt or dot_cnt > 1:
                    return False
            elif s[i] == 'e' or s[i] == 'E':
                e_cnt += 1
                if i == 0 or i == size - 1 or e_cnt > 1:
                    return False
                # '.' 后面不能加上
                if i == 1 and s[0] == '.':
                    return False
                if s[i + 1] == '+' or s[i + 1] == '-':
                    if i + 2 == size:
                        return False
                    i += 1
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = '123.45e+6'
    result = solution.isNumber(s)
    print(result)
