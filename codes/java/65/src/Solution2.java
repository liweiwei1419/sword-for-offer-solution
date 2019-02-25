/**
 * @author liwei
 * @date 18/6/19 下午1:45
 */
public class Solution2 {

    // 书上的写法
    public int Add(int num1, int num2) {
        int sum = 0;
        int carry = 0;
        do {
            sum = num1 ^ num2;
            carry = num1 & num2;

            num1 = sum;
            num2 = carry << 1;
        } while (carry != 0);
        return sum;
    }
}
