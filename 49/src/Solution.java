/**
 * 求丑数
 */
public class Solution {

    private boolean isUgly(int number) {
        while (number % 2 == 0) {
            number /= 2;
        }
        while (number % 3 == 0) {
            number /= 3;
        }
        while (number % 5 == 0) {
            number /= 5;
        }
        return number == 1;
    }

    public int getUglyNumber(int index) {
        if (index <= 0) {
            return 0;
        }
        int count = 0;
        int n = 0;
        while (count < index) {
            n++;
            if (isUgly(n)) {
                count++;
            }
        }
        return n;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        for (int i = 1; i <=15 ; i++) {
            int getUglyNumberSolution = solution.getUglyNumber(i);
            System.out.printf("%s ",getUglyNumberSolution);
        }
    }
}
