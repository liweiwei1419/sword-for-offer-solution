public class Solution {
    // 本质还是斐波拉契数列问题，要注意：
    // （1）首先判断极端情况
    // （2）如何减少空间复杂度
    public int RectCover(int target) {
        int n = target;
        if (n == 0) {
            return 0;
        }
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    // 最佳解法
    public int RectCover1(int target) {
        if (target <= 2) {
            return target;
        }
        int a = 1;
        int b = 2;
        int c = 0;
        for (int i = 3; i <= target; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    // 参考资料：http://cuijiahua.com/blog/2017/11/basis_10.html
    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 10;
        for (int i = 0; i < n; i++) {
            int rectCover = solution.RectCover(i);
            int rectCover1 = solution.RectCover1(i);
            System.out.println(rectCover + "\t" + rectCover1);
            if (rectCover != rectCover1) {
                System.out.println("解法错误！");
            }
        }
    }
}