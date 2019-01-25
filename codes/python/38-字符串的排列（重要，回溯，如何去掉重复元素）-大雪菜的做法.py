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
        marked = [False for _ in range(l)]
        path = [0 for _ in range(l)]
        self.__dfs(nums, 0, 0, path, marked, res)
        return res

    def __dfs(self, nums, index, start, path, marked, res):
        if index == len(nums):
            res.append(path[:])
            return
        for i in range(start, len(nums)):
            if not marked[i]:
                marked[i] = True
                path[i] = nums[index]
                if index + 1 < len(nums) and nums[index] != nums[index + 1]:
                    self.__dfs(nums, index + 1, 0, path, marked, res)
                else:
                    self.__dfs(nums, index + 1, i + 1, path, marked, res)
                marked[i] = False


if __name__ == '__main__':
    nums = [1, 1, 2]
    solution = Solution()
    result = solution.permutation(nums)
    print(result)
