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
        self.__dfs(nums, 0, [], marked, res)
        return res

    def __dfs(self, nums, start, path, marked, res):
        if start == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not marked[i]:
                if i > 0 and nums[i] == nums[i - 1] and not marked[i - 1]:
                    continue
                marked[i] = True
                path.append(nums[i])
                self.__dfs(nums, start + 1, path, marked, res)
                path.pop()
                marked[i] = False


if __name__ == '__main__':
    nums = [1, 1, 2]
    solution = Solution()
    result = solution.permutation(nums)
    print(result)
