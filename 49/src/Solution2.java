/**
 * 求丑数，讨论去提供的解法，和书上的思路是一样的
 */
public class Solution2 {

    // 1、2、3、4、5、6 都是丑数
    public int GetUglyNumber_Solution(int index) {
        if (index < 7) {
            return index;
        }

        // 状态的定义：第 i 个丑数的最小值，从 0 开始计算
        int[] dp = new int[index];
        dp[0] = 1;

        int t2 = 0;
        int t3 = 0;
        int t5 = 0;

        // 注意： i 从 1 开始
        for (int i = 1; i < index; i++) {
            dp[i] = min3(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5);
            if (dp[i] == dp[t2] * 2) {
                t2++;
            }
            if (dp[i] == dp[t3] * 3) {
                t3++;
            }
            if (dp[i] == dp[t5] * 5) {
                t5++;
            }
        }
        // System.out.println(Arrays.toString(dp));
        return dp[index - 1];
    }

    private int min3(int n1, int n2, int n3) {
        return Integer.min(Integer.min(n1, n2), n3);
    }

    public static void main(String[] args) {
        Solution2 solution2 = new Solution2();
        // 1 2 3 4 5 6 8 9 10 12 15 16 18 20 24
        // [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
        int getUglyNumberSolution = solution2.GetUglyNumber_Solution(15);
    }
}
