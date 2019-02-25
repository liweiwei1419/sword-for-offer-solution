class Solution:

    def __init__(self):
        self.chars = [0 for _ in range(256)]
        self.strs = []

    def firstAppearingOnce(self):
        """
        :rtype: str
        """
        for char in self.strs:
            if self.chars[ord(char)] == 1:
                return char
        return '#'

    def insert(self, char):
        """
        :type char: str
        :rtype: void
        """
        self.chars[ord(char)] += 1
        self.strs.append(char)
