class Solution(object):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        marked = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if self.__has_path(matrix, string, 0, i, j, marked, rows, cols):
                    return True
        return False

    def __has_path(self, matrix, word, index, start_x, start_y, marked, m, n):
        # 注意：首先判断极端情况
        if index == len(word) - 1:
            return matrix[start_x][start_y] == word[-1]
        if matrix[start_x][start_y] == word[index]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y]:
                    if self.__has_path(matrix, word, index + 1, new_x, new_y, marked, m, n):
                        return True
            marked[start_x][start_y] = False
        return False


if __name__ == '__main__':
    matrix = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]
    ]

    str = "ABCEFSADEESE"

    solution = Solution()
    result = solution.hasPath(matrix, str)
    print(result)
