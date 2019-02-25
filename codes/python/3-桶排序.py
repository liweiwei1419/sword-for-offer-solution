class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """

        size = len(nums)
        if size < 2:
            return -1

        for i in range(size):
            if nums[i] < 0 or nums[i] > size - 1:
                return -1

        for i in range(size):

            # nums[i] 应该在 i 的位置上

            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                self.__swap(nums, i, nums[i])
        return -1

    def __swap(self, nums, index1, index2):
        if index1 == index2:
            return
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp
