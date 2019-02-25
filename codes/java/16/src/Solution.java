public class Solution {

    public double Power(double base, int exponent) {
        if (exponent == 0) {
            return 1;
        }
        if (exponent < 0) {
            return 1 / Power(base, -exponent);
        }
        // 使用位运算的 与 运算符代替了求余数运算，来判断一个数是奇数还是偶数
        if ((exponent & 1) == 0) {
            // 等价于 exponent 是偶数
            double square = Power(base, exponent >> 1);
            return square * square;
        } else {
            // 是奇数的时候
            double square = Power(base, (exponent - 1) >> 1);
            return square * square * base;
        }
    }

    public static void main(String[] args) {
        int base = 3;
        int exponent = -3;
        Solution solution = new Solution();
        double result1 = solution.Power(base, exponent);
        System.out.println(result1);
        exponent = 6;
        double result2 = solution.Power(base, exponent);
        System.out.println(result2);
        // exponent 指数，exponent >> 1 表示将指数除以 2
        System.out.println(exponent >> 1);
    }
}
