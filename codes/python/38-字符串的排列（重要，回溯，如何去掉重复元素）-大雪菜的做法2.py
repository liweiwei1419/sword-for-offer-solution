# 38、数字排列
# 输入一组数字（可能包含重复数字），输出其所有的排列方式。
#
# 样例
# 输入：[1,2,3]
#
# 输出：
#       [
#         [1,2,3],
#         [1,3,2],
#         [2,1,3],
#         [2,3,1],
#         [3,1,2],
#         [3,2,1]
#       ]

# 参考资料：https://www.acwing.com/solution/AcWing/content/776/

class Solution:
    def permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        l = len(nums)
        res = []
        if l == 0:
            return res
        # 因为含有重复数组，所以先排序
        nums.sort()
        path = [0 for _ in range(l)]
        self.__dfs(nums, 0, 0, path, 0, res)

        return res

    def __dfs(self, nums, index, start, path, state, res):
        if index == len(nums):
            res.append(path[:])
            return

        if index == 0 or nums[index] != nums[index - 1]:
            start = 0

        for i in range(start, len(nums)):
            if (state >> i & 1) == 0:
                # 如果当前的数没有使用过
                path[i] = nums[index]
                self.__dfs(nums, index + 1, i + 1, path, state + (1 << i), res)


if __name__ == '__main__':
    nums = [1, 1, 2]
    solution = Solution()
    result = solution.permutation(nums)
    print(result)
