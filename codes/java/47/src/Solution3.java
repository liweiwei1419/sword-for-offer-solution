public class Solution3 {

    public int getMaxValue(int[][] matrix) {
        int row = matrix.length;
        if (row == 0) {
            return 0;
        }
        int col = matrix[0].length;
        int[] dp = new int[col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                dp[j] = Integer.max(dp[j], j - 1 < 0 ? 0 : dp[j - 1]) + matrix[i][j];
            }
        }
        return dp[col - 1];
    }

    public static void main(String[] args) {
        int[][] matrix = new int[][]{
                {1, 10, 3, 8},
                {12, 2, 9, 6},
                {5, 7, 4, 11},
                {3, 7, 16, 5}
        };
        Solution3 solution3 = new Solution3();
        int maxValue = solution3.getMaxValue(matrix);
        System.out.println(maxValue);
    }
}
