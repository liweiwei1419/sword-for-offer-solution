# 4、二维数组中的查找

class Solution(object):

    # 二分法查找规律
    # 1、从右到左，找第 1 个小于或者等于 target 的数
    # 2、从上到下，找第 1 个大于或者等于 target 的数

    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(array)
        if rows == 0:
            return False
        cols = len(array[0])

        col = cols - 1
        row = 0

        while row < rows and col >= 0:

            # print('row', row, 'col', col, array[row][0])
            # 1、从右到左，找第 1 个小于或者等于 target 的数
            if col == 0 and array[row][0] > target:
                return False
            l = 0
            r = col
            while l < r:
                mid = l + (r - l + 1) // 2
                if array[row][mid] <= target:
                    l = mid
                else:
                    assert array[row][mid] > target
                    r = mid - 1
            col = l

            # 2、从上到下，找第 1 个大于或者等于 target 的数
            if row == rows - 1 and array[rows - 1][col] < target:
                return False

            l = row
            r = rows - 1
            while l < r:
                mid = l + (r - l) // 2
                if array[mid][col] >= target:
                    r = mid
                else:
                    assert array[mid][col] < target
                    l = mid + 1
            row = l

            if array[row][col] == target:
                return True

        return False


if __name__ == '__main__':
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    target = 16
    solution = Solution()
    result = solution.searchArray(array, target)
    print(result)

