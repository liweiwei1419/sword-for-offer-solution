class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        # 将队列中前面已经逆序的元素放在 x 元素后面，使得整体逆序
        for _ in range(len(self.queue) - 1):
            ele = self.queue.pop(0)
            self.queue.append(ele)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queue:
            return self.queue.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.queue:
            return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
