# 45、把数组排成最小的数
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
# 例如输入数组[3, 32, 321]，则打印出这3个数字能排成的最小数字321323。


class Solution(object):
    def printMinNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        if len(nums) == 0:
            return ''
        # 自定义排序规则
        from functools import cmp_to_key
        key_func = cmp_to_key(lambda a, b: int(a + b) - int(b + a))
        result = sorted(map(str, nums), key=key_func)
        return ''.join(result)


if __name__ == '__main__':
    list1 = [7, -8, 5, 4, 0, -2, -5]
    # 要求：1、正数在前负数在后
    # 2、正数从小到大
    # 3、负数从大到小

    result = sorted(list1, key=lambda x: (x < 0, abs(x)))
    print(result)

    s = 'asdf234GDSdsf23'  # 排序:小写-大写-奇数-偶数

    print(
        "".join(
            sorted(
                s,
                key=lambda x: (
                    x.isdigit(),
                    x.isdigit() and int(x) %
                    2 == 0,
                    x.isupper(),
                    x))))
