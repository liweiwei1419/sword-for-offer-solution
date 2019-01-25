# 3、数组中重复的数字

class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """

        l = len(nums)
        if l == 0:
            return -1

        for num in nums:
            if num < 0 or num >= l:
                return -1
        for i in range(l):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # 注意：千万不能这么写！！！ nums[i], nums[nums[i]] = nums[nums[i]], nums[i]

                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                # self.__swap(nums, i, nums[i])
        return -1

    def __swap(self, nums, index1, index2):
        if index1 == index2:
            return
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp


if __name__ == '__main__':
    nums = [2, 3, 5, 4, 3, 2, 6, 7]
    solution = Solution()
    result = solution.duplicateInArray(nums)
    print(result)
