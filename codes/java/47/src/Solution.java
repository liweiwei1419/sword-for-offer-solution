public class Solution {

    public int getMaxValue(int[][] matrix) {
        int row = matrix.length;
        if (row == 0) {
            return 0;
        }
        int col = matrix[0].length;
        int[][] dp = new int[row][col];
        dp[0][0] = matrix[0][0];

        for (int j = 1; j < col; j++) {
            dp[0][j] = dp[0][j - 1] + matrix[0][j];
        }
        for (int i = 1; i < row; i++) {
            dp[i][0] = dp[i - 1][0] + matrix[i][0];
            for (int j = 1; j < col; j++) {
                dp[i][j] = Integer.max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j];
            }
        }
        return dp[row - 1][col - 1];
    }

    public static void main(String[] args) {
        int[][] matrix = new int[][]{
                {1, 10, 3, 8},
                {12, 2, 9, 6},
                {5, 7, 4, 11},
                {3, 7, 16, 5}
        };
        Solution solution = new Solution();
        int maxValue = solution.getMaxValue(matrix);
        System.out.println(maxValue);
    }
}
