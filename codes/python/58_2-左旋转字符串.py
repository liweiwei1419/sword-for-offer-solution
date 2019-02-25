class Solution(object):
    def leftRotateString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """

        size = len(s)
        # 特判
        if size == 0 or n % size == 0:
            return s
        n = n % size
        arr = list(s)
        self.__reverse(arr, 0, size - 1)

        self.__reverse(arr, 0, size - 1 - n)
        self.__reverse(arr, size - n, size - 1)

        return ''.join(arr)

    def __reverse(self, arr, left, right):
        if left >= right:
            return
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = "abcdefg"
    n = 2
    solution = Solution()
    result = solution.leftRotateString(s, n)
    print(result)
