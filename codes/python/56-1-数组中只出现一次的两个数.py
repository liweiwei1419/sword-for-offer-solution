# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
#
# 请写程序找出这两个只出现一次的数字。
#
# 你可以假设这两个数字一定存在。
#
# 样例
# 输入：[1,2,3,3,4,4]
#
# 输出：[1,2]

class Solution(object):
    def findNumsAppearOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        if l < 2:
            raise Exception('程序出错')
        if l == 2:
            return nums

        # 全部相与一遍
        xor = 0
        for num in nums:
            xor ^= num

        # 最末尾的 1 从右向左边数在第几位
        counter = 0
        while xor & 1 == 0:
            xor >>= 1
            counter += 1

        res = [0, 0]
        for num in nums:
            if (num >> counter) & 1 == 1:
                res[1] ^= num
            else:
                res[0] ^= num
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 4]
    solution = Solution()
    result = solution.findNumsAppearOnce(nums)
    print(result)
