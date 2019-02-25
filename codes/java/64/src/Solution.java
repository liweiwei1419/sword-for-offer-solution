public class Solution {

    public int Sum_Solution(int n) {
        if (n <= 0) {
            return 0;
        }
        return n + Sum_Solution(n - 1);
    }

    public int Sum_Solution2(int n) {
        int sum = 0;
        for (int i = 0; i <= n; i++) {
            sum += i;
        }
        return sum;
    }

    public int Sum_Solution3(int n) {
        int sum = n;
        boolean ans = n > 0 && ((sum += Sum_Solution(n - 1)) > 0);
        return sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 100;
        int solution1 = solution.Sum_Solution(n);
        System.out.println(solution1);
        int solution2 = solution.Sum_Solution2(n);
        System.out.println(solution2);
        if (solution1 != solution2) {
            System.out.println("程序错误");
        }
    }
}
