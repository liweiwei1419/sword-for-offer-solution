# 54. 数据流中的中位数
#
#
# 如何得到一个数据流中的中位数？
#
# 如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
#
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
#
# 样例
# 输入：1, 2, 3, 4
#
# 输出：1,1.5,2,2.5
#
# 解释：每当数据流读入一个数据，就进行一次判断并输出当前的中位数。

import heapq


class Solution:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.count = 0

    def insert(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.count += 1
        if self.count & 1 == 1:
            heapq.heappush(self.max_heap, -num)
            temp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, temp)
        else:
            heapq.heappush(self.min_heap, num)
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -temp)

        # print(self.min_heap)
        # print(self.max_heap)

    def getMedian(self):
        """
        :rtype: float
        """
        if self.count & 1 == 1:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] + (-self.max_heap[0])) / 2


if __name__ == '__main__':
    solution = Solution()
    solution.insert(1)
    result = solution.getMedian()
    print(result)
    solution.insert(2)
    result = solution.getMedian()
    print(result)

    solution.insert(3)
    result = solution.getMedian()
    print(result)

    solution.insert(4)
    result = solution.getMedian()
    print(result)
