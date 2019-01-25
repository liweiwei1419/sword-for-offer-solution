# 39、数组中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
# 假设数组非空，并且一定存在满足条件的数字。
#
# 思考题：
#
# 假设要求只能使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢？
# 样例
# 输入：[1,2,1,1,3]
#
# 输出：1
class Solution(object):
    def moreThanHalfNum_Solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        if l == 1:
            return nums[0]

        num = nums[0]
        times = 1
        for i in range(1, l):
            # 注意分类讨论的顺序，先看次数是不是 0
            # 以下的 3 种情况是互斥的
            if times == 0:
                num = nums[i]
                times += 1
            elif num == nums[i]:
                times += 1
            else:
                times -= 1
        return num
