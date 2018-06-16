public class Solution {

    public int FindGreatestSumOfSubArray(int[] array) {
        int n = array.length;
        if (n == 0) {
            return 0;
        }
        int[] dp = new int[n];
        dp[0] = array[0];
        int res = array[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Integer.max(dp[i - 1] + array[i], array[i]);
            res = Integer.max(res, dp[i]);
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{6, -3, -2, 7, -15, 1, 2, 2};
        Solution solution = new Solution();
        int findGreatestSumOfSubArray = solution.FindGreatestSumOfSubArray(nums);
        System.out.println(findGreatestSumOfSubArray);
    }
}
