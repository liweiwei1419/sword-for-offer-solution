/**
 * @author liwei
 * @date 18/6/19 上午9:22
 */
public class Solution2 {

    public double Power(double base, int exponent) {
        // 不能用 == 比较两个浮点数是否相等,因为有误差。
        if (equals(base, 0) && exponent < 0) {
            throw new IllegalArgumentException("当底数为 0 的时候，指数为负数没有意义");
        }
        if (exponent == 0) {
            return 1.0;
        }
        if (exponent > 0) {
            return power(base, exponent);
        } else {
            return power(1 / base, -exponent);
        }
    }

    public double power(double base, int exponent) {
        if (exponent == 0) {
            return 1.0;
        }
        if (exponent % 2 == 0) {
            double square = power(base, exponent / 2);
            return square * square;
        } else {
            double square = power(base, (exponent - 1) / 2);
            return square * square * base;
        }
    }

    private boolean equals(double num1, double num2) {
        return num1 - num2 < 0.000001 && num1 - num2 > -0.000001;
    }
}
