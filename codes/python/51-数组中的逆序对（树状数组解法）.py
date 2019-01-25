# 51、数组中的逆序对（分治解法）
# 在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
#
# 输入一个数组，求出这个数组中的逆序对的总数。
#
# 样例
# 输入：[1,2,3,4,5,6,0]
#
# 输出：6


class Solution(object):
    def inversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        class FenwickTree:
            def __init__(self, n):
                self.size = n
                self.tree = [0 for _ in range(n + 1)]

            def __lowbit(self, index):
                return index & (-index)

            # 单点更新：从下到上，最多到 len，可以取等
            def update(self, index, delta):
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            # 区间查询：从上到下，最少到 1，可以取等
            def query(self, index):
                res = 0
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res

        # 特判
        l = len(nums)
        if l < 2:
            return 0

        # 原始数组去除重复以后从小到大排序
        s = list(set(nums))

        # 构建最小堆，因为从小到大一个一个拿出来，用堆比较合适
        import heapq
        heapq.heapify(s)

        # 由数字查排名
        rank_map = dict()
        index = 1
        # 不重复数字的个数
        size = len(s)
        for _ in range(size):
            num = heapq.heappop(s)
            rank_map[num] = index
            index += 1

        res = 0
        # 树状数组只要不重复数字个数这么多空间就够了
        ft = FenwickTree(size)
        # 从后向前看，拿出一个数字来，就更新一下，然后向前查询比它小的个数
        for i in range(l - 1, -1, -1):
            rank = rank_map[nums[i]]
            ft.update(rank, 1)
            res += ft.query(rank - 1)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 0]
    solution = Solution()
    result = solution.inversePairs(nums)
    print(result)
