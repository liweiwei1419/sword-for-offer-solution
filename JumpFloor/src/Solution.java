public class Solution {

    // 1 2 3 5 8
    // 1 2 3 4 5
    public int JumpFloor(int target) {
        int n = target;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    // i j （i+j）
    // 1 2 3 5
    // 1 2 3 4
    public int JumpFloor1(int target) {
        if (target == 1) {
            return 1;
        }
        int n = target;
        int i = 1;
        int j = 2;
        int temp;
        for (int k = 3; k <= n; k++) {
            temp = j;
            j = i + j;
            i = temp;
        }
        return j;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        for (int i = 1; i < 5; i++) {
            int jumpFloor = solution.JumpFloor1(i);
            System.out.println(jumpFloor);
        }
    }
}
