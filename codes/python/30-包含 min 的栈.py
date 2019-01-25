# 定义两个栈，一个存放入的值，另一个存最小值，两个栈应该是同步 push 和 pop，否则还要分类讨论，代码编写容易出错。


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        if len(self.stack) == 0:
            self.helper.append(x)
            self.stack.append(x)
        else:
            # 如果将要 push 的元素比辅助栈的栈顶元素还大，不能放这个元素，
            # 此时应该把辅助栈的栈顶元素再复制一份
            peek = self.helper[-1]
            if x > peek:
                self.stack.append(x)
                self.helper.append(peek)
            else:
                self.stack.append(x)
                self.helper.append(x)

    def pop(self):
        """
        :rtype: void
        """

        if len(self.stack) == 0:
            return
        self.helper.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.helper[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
