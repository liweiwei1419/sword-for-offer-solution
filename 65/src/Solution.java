public class Solution {

    public int Add(int num1, int num2) {
        int sum = 0;
        while (true) {
            sum = num1 ^ num2;
            int carry = num1 & num2;
            if (carry == 0) {
                break;
            }
            num1 = sum;
            num2 = carry << 1;

        }
        return sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int add = solution.Add(14, 15);
        System.out.println(add);
    }
}