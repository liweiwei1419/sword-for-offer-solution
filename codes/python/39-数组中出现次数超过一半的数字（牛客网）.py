# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        res = numbers[0]
        times = 1
        for num in numbers[1:]:
            if times == 0:
                res = num
                times = 1
            elif res == num:
                times += 1
            else:
                times -= 1
        # 验证 res 是不是超过一半
        times = 0
        for num in numbers:
            if num == res:
                times += 1
        return res if times > len(numbers) // 2 else 0
