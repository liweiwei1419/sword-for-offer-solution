public class Solution {
    // 1 2 3
    public int JumpFloorII(int target) {
        if (target == 0 || target == 1) {
            return 1;
        }
        int n = target;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            // 起点是 1 这一点要特别小心
            int res = 1;
            for (int j = 1; j < i; j++) {
                res += dp[j];
            }
            dp[i] = res;
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int jumpFloorII = solution.JumpFloorII(3);
        System.out.println(jumpFloorII);
    }
}
