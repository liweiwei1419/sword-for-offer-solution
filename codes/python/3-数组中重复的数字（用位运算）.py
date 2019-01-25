# 3、数组中重复的数字
# 给定一个长度为 n 的整数数组 nums，数组中所有的数字都在 0∼n−1 的范围内。


class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """

        l = len(nums)
        if l == 0:
            return -1

        if l <= 99:
            state = 0
            for i in range(l):
                if nums[i] < 0 or nums[i] >= l:
                    return -1
                if ((state >> nums[i]) & 1) == 1:
                    # 重复了
                    return nums[i]
                # 没有重复，把那一位占1
                state ^= (1 << nums[i])

            return -1
        else:
            # counter = [0 for _ in range(l)]
            #
            # print(counter)
            # for i in range(l):
            #     if nums[i] < 0 or nums[i] > l - 1:
            #         return -1
            #     if counter[i] == 1:
            #         return nums[i]
            #     counter[i] += 1
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


if __name__ == '__main__':
    nums = [52, 35, 51, 77, 19, 10, 27, 37, 54, 26, 75, 9, 71, 81, 76, 75, 21, 100, 54, 50, 87, 40, 21, 87, 18, 23, 58, 12, 17, 84, 11, 6, 91, 73, 57, 19, 85, 65, 36, 44, 40, 77, 33, 56, 27, 48, 77, 59, 8, 65, 77, 13, 9, 52, 53, 9, 77, 73, 85, 33, 31, 10, 84, 94, 4, 13, 82, 12, 91, 89, 93, 40, 42, -100, 85, 36, 20, 33, 13, 48, 38, 93, 30, 87, 47, 44, 29, 47, 33, 52, 36, 55, 20, 29, 68, 58, 64, 5, 15, 26]

    print(len(nums))
    solution = Solution()
    result = solution.duplicateInArray(nums)
    print(result)
