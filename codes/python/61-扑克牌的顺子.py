# 61 、扑克牌顺子


class Solution(object):
    def isContinuous(self, numbers):
        """
        :type numbers: List[int]
        :rtype: bool
        """
        size = len(numbers)
        if size != 5:
            return False
        # 最小值和最大值都设置成一个不可能取到的值
        min_val = 14
        max_val = -1

        flag = 0
        for num in numbers:
            if not 0 <= num <= 13:
                return False
            if num == 0:
                continue
            # 右移：看看这一位是不是用过了
            if (flag >> num) & 1 == 1:
                return False

            # 左移：表示这一位我现在要占用
            flag = flag | (1 << num)

            min_val = min(min_val, num)
            max_val = max(max_val, num)
            if max_val - min_val >= 5:
                return False
        return True
