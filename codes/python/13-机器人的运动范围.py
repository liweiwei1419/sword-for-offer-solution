class Solution(object):

    def __count_bit_sum(self, num):
        res = 0
        while num:
            res += num % 10
            num //= 10
        return res

    def __in_area(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols

    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if threshold < 0 or rows == 0 or cols == 0:
            return 0

        if threshold == 0:
            return 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        marked = [[False for _ in range(cols)] for _ in range(rows)]

        queue = [(0, 0)]
        res = 0

        while queue:
            top_x, top_y = queue.pop(0)

            for direction in directions:
                new_x = top_x + direction[0]
                new_y = top_y + direction[1]

                if self.__in_area(new_x, new_y, rows, cols) \
                        and not marked[new_x][new_y] \
                        and self.__count_bit_sum(new_x) + self.__count_bit_sum(new_y) <= threshold:
                    queue.append((new_x, new_y))
                    # 注意：应该写在这里，而不是 pop 出队列的时候
                    marked[new_x][new_y] = True
                    res += 1
        return res


if __name__ == '__main__':
    k = 18
    m = 40
    n = 40
    solution = Solution()
    result = solution.movingCount(k, m, n)
    print(result)
