public class Solution {

    public boolean Find(int target, int[][] array) {
        int row = array.length;
        if (row == 0) {
            return false;
        }
        int col = array[0].length;

        // 从左下角开始查找
        int i = row - 1;

        // 这一行代码还可以位于下面这个注释中，但是在这个位置效率更高，也应该在这个位置，j 没有必要重置
        // 这一行代码还可以位于下面这个注释中，但是在这个位置效率更高，也应该在这个位置，j 没有必要重置
        // 这一行代码还可以位于下面这个注释中，但是在这个位置效率更高，也应该在这个位置，j 没有必要重置
        int j = 0;

        // 从最后一行开始，一点一点去匹配，遇到比
        while (i >= 0) {
            // int j = 0;
            while (j < col && array[i][j] < target) {
                j++;
            }
            if (j < col && array[i][j] == target) {
                return true;
            }
            i--;
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] matrix = new int[][]{
                {1, 2, 8, 9},
                {2, 4, 9, 12},
                {4, 7, 10, 13},
                {6, 8, 11, 15}
        };
        Solution solution = new Solution();
        boolean find = solution.Find(16, matrix);
        System.out.println(find);
    }
}
