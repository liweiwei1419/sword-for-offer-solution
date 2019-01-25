# 33. 二叉搜索树的后序遍历序列

#
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
#
# 如果是则返回true，否则返回false。
#
# 假设输入的数组的任意两个数字都互不相同。
#
# 样例
# 输入：[4, 8, 6, 12, 16, 14, 10]
#
# 输出：true


class Solution:
    def verifySquenceOfBST(self, sequence):
        """
        :type sequence: List[int]
        :rtype: bool
        """
        # 先写特殊情况
        l = len(sequence)
        if l == 0:
            return False
        if l == 1:
            return True

        return self.__helper(sequence, 0, l - 1)

    def __helper(self, sequence, left, right):
        # 先写递归终止条件
        if left >= right:
            return True
        # 此时区间最右边的数作为标定元素
        pivot = sequence[right]
        # 设置一个遍历指针，把 [left, right -1] 这个区间里的元素全部看一遍

        # 正确的情况是：最右边的元素把前面的数组分成两部分：
        # 第 1 部分的元素全部严格小于最右边的元素
        # 第 2 部分的元素全部严格大于最右边的元素
        point = left
        while sequence[point] < pivot:
            point += 1
        # 此时 [left, point - 1] 中的元素都严格比最右边的元素小
        # 下面就依次验证后面的元素是不是都严格比最右边的元素大就好了
        mid = point - 1
        # 此后，所有的数都应该比 pivot 大
        while point < right:
            if sequence[point] > pivot:
                point += 1
            else:
                return False
        return self.__helper(sequence, left, mid) and self.__helper(
            sequence, mid + 1, right - 1)


if __name__ == '__main__':
    # sequence = [4, 8, 6, 12, 16, 14, 10]
    sequence = [2, 1, 3]
    solution = Solution()
    result = solution.verifySquenceOfBST(sequence)
    print(result)
