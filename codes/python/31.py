# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV is None or popV is None:
            return False
        stack = []
        index = 0
        for num in pushV:
            stack.append(num)
            while stack and stack[-1] == popV[index]:
                stack.pop()
                index += 1
        return len(stack) == 0
