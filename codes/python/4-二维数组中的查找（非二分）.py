# 4、二维数组中的查找

class Solution(object):

    def searchArray(self, array, target):
        rows = len(array)
        if rows == 0:
            return False

        cols = len(array[0])
        if rows > 0 and cols > 0:
            row = 0
            col = cols - 1
            while row < rows and col >= 0:
                if target == array[row][col]:
                    return True
                elif target < array[row][col]:
                    col -= 1
                else:
                    row += 1
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
