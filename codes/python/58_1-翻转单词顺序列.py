class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        size = len(s)
        arr = list(s)

        self.__reverse(arr, 0, size - 1)

        begin = 0
        index = 0
        while index < size:
            if arr[index] == ' ':
                self.__reverse(arr, begin, index - 1)
                begin = index + 1
            index += 1
        # 最后还要反转一下
        self.__reverse(arr, begin, size - 1)
        return ''.join(arr)

    def __reverse(self, arr, left, right):
        if left >= right:
            return
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = "I am a student."
    solution = Solution()
    result = solution.reverseWords(s)
    print(result)
