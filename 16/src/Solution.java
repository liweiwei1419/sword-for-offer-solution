public class Solution {

    public static void main(String[] args) {
        int base = 3;
        int exponent = -3;
        System.out.println(power(base, exponent));
        exponent = 6;
        System.out.println(power(base, exponent));
        // exponent 指数，exponent >> 1 表示将指数除以 2
        System.out.println(exponent >> 1);
    }

    // 没有按照书上写的来实现
    public static double power(double base, int exponent) {
        if (exponent == 0) {
            return 1;
        }
        if (exponent < 0) {
            return 1 / power(base, -exponent);
        }
        // 使用位运算的 与 运算符代替了求余数运算，来判断一个数是奇数还是偶数
        if ((exponent & 1) == 0) {
            double temp = power(base, exponent >> 1);
            return temp * temp;
        } else {
            double temp = power(base, (exponent - 1) >> 1);
            return temp * temp * base;
        }
    }
}
