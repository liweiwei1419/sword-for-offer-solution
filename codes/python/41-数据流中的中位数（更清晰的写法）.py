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
        # 当前是奇数的时候，直接"最小堆" -> "最大堆"，就可以了
        # 此时"最小堆" 与 "最大堆" 的元素数组是相等的

        # 当前是偶数的时候，"最小堆" -> "最大堆"以后，最终我们要让"最小堆"多一个元素
        # 所以应该让 "最大堆" 拿出一个元素给 "最小堆"

        heapq.heappush(self.min_heap, num)
        temp = heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap, -temp)
        if self.count & 1 == 0:
            temp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, temp)
        self.count += 1
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
