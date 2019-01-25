# 42. 栈的压入、弹出序列
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
#
# 假设压入栈的所有数字均不相等。
#
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
#
# 注意：若两个序列为空或长度不等则视为并不是一个栈的压入、弹出序列。


class Solution(object):
    def isPopOrder(self, pushV, popV):
        """
        :type pushV: list[int]
        :type popV: list[int]
        :rtype: bool
        """
        if len(pushV) == 0 and len(popV) == 0:
            return False
        if pushV is None or popV is None or len(pushV) != len(popV):
            return False
        stack = []
        index = 0
        for ele in pushV:
            stack.append(ele)
            while stack and stack[-1] == popV[index]:
                stack.pop()
                index += 1
        return len(stack) == 0


if __name__ == '__main__':
    pushV = []
    popV = []
    solution = Solution()
    result = solution.isPopOrder(pushV, popV)
    print(result)
