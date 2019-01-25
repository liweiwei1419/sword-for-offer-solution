# 40、最小的 K 个数（partition）
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
        l = 0
        r = size - 1
        while l <= r:
            p = self.__partition(input, l, r)
            if p == k - 1:
                return sorted(input[:p + 1])
            elif p > k - 1:
                # 此时  k-1  p
                r = p - 1
            else:
                # 此时 p k-1
                l = p + 1

    def __partition(self, input, left, right):
        # 只有一个数的时候，就没有必要 partition 了
        # 直接返回这个数的索引
        if left == right:
            return left
        pivot = input[left]
        l = left + 1
        r = right
        while True:
            while l <= right and input[l] <= pivot:
                l += 1
            while r > left and input[r] >= pivot:
                r -= 1
            if l > r:
                break
            input[l], input[r] = input[r], input[l]
            l += 1
            r -= 1
        input[left], input[r] = input[r], input[left]
        return r


if __name__ == '__main__':
    input = [9, 14, 1, 16, 19, 13, 12]
    k = 4
    solution = Solution()
    result = solution.getLeastNumbers_Solution(input, k)
    print(result)
