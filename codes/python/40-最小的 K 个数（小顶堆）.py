# 40、最小的 K 个数（小顶堆）
# 输入n个整数，找出其中最小的k个数。
#
# 注意：
#
# 数据保证k一定小于等于输入数组的长度;
# 输出数组内元素请按从小到大顺序排序;
# 样例
# 输入：[1,2,3,4,5,6,7,8] , k=4
#
# 输出：[1,2,3,4]


class Solution(object):

    def getLeastNumbers_Solution(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        size = len(input)
        if size == 0:
            return []
        if k == size:
            return sorted(input)
        import heapq

        l = []
        for num in input[:k]:
            heapq.heappush(l, -num)
        for num in input[k:]:
            top = l[0]
            if top < -num:
                heapq.heappushpop(l, -num)
        return sorted([-num for num in l])

    def getLeastNumbers_Solution1(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        size = len(input)
        if size == 0:
            return []
        if k == size:
            return sorted(input)
        import heapq
        heapq.heapify(input)
        return sorted(heapq.nsmallest(k, input))


if __name__ == '__main__':
    input = [9, 14, 1, 16, 19, 13, 12]
    k = 4
    solution = Solution()
    result = solution.getLeastNumbers_Solution(input, k)
    print(result)
