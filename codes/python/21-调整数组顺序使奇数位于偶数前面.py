# import heapq
#
# l = [-62, -41, -30, -28, -16, -22, -13, -19, -15, -17]
# heapq.heapify(l)
# print(l)


class Solution(object):
    def reOrderArray(self, array):
        """
        :type array: List[int]
        :rtype: void
        """
        # 特判
        size = len(array)
        if size < 2:
            return

        l = 0
        r = size - 1

        while True:
            while l <= r and array[l] & 1 == 1:
                l += 1
            while r >= l and array[r] & 1 == 0:
                r -= 1
            if l > r:
                break

            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
        return array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    solution = Solution()
    result = solution.reOrderArray(array)
    print(result)
