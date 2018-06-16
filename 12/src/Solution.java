public class Solution {

    /**
     *       x-1,y
     * x,y-1   x,y    x,y+1
     *       x+1,y
     */
    private int[][] direct = new int[][]{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    public boolean hasPath(char[] matrix, int rows, int cols, char[] str) {
        int len = matrix.length;
        if (len == 0) {
            return false;
        }
        boolean[] marked = new boolean[len];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(matrix, rows, cols, str, str.length, marked, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[] matrix, int rows, int cols, char[] str, int len, boolean[] marked, int i, int j, int start) {
        // 匹配到最后，说明找到一条路径
        int index = getIndex(i, j, cols);
        if (start == len - 1) {
            return matrix[index] == str[start];
        }
        // 要特别小心！
        marked[index] = true;
        if (matrix[index] == str[start]) {
            // 当前匹配了，才开始尝试走后面的路
            for (int k = 0; k < 4; k++) {
                // 特别小心，一定是一个初始化的新的变量
                int newi = i + direct[k][0];
                int newj = j + direct[k][1];
                int nextIndex = getIndex(newi, newj, cols);
                if (inArea(newi, newj, rows, cols) && !marked[nextIndex]) {
                    // marked[nextIndex] = true; 不在这里设置
                    if (dfs(matrix, rows, cols, str, len, marked, newi, newj, start + 1)) {
                        return true;
                    }
                    // marked[nextIndex] = false; 不在这里设置
                }
            }
        }
        // 要特别小心！
        marked[index] = false;
        return false;
    }

    private int getIndex(int x, int y, int cols) {
        return x * cols + y;
    }

    private boolean inArea(int x, int y, int rows, int cols) {
        return x >= 0 && x < rows && y >= 0 && y < cols;
    }

    public static void main(String[] args) {
        char[] matrix = new char[]{'a', 'b', 't', 'g',
                'c', 'f', 'c', 's',
                'j', 'd', 'e', 'h'};
        int rows = 3;
        int cols = 4;
        Solution solution = new Solution();
        char[] str = "hscfdeh".toCharArray();
        boolean hasPath = solution.hasPath(matrix, rows, cols, str);
        System.out.println(hasPath);
    }
}
