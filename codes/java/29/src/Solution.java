import java.util.ArrayList;

// 29 顺时针打印矩阵
// 参考资料：https://www.nowcoder.com/questionTerminal/9b4c81a02cd34f76be2659fa0d54342a
public class Solution {

    private enum State {
        RIGHT, DOWN, LEFT, UP
    }

    public ArrayList<Integer> printMatrix(int[][] matrix) {
        ArrayList<Integer> res = new ArrayList<>();
        int row_max = matrix.length;
        if (row_max == 0) {
            return res;
        }
        int col_max = matrix[0].length;
        row_max--;
        col_max--;
        int row_min = 0;
        int col_min = 0;
        // 上面的代码虽然看起来行数比较多，但是其实只是做了极端情况的考虑和一些变量的初始化工作

        // 下面的代码虽然看起来比较长，但是也只是做了当前状态的判断以及状态转移，代码框架是一模一样的
        // 仔细体会这个过程，其实就是：每次接收一个状态，根据这个状态做出相应的操作，然后变更状态
        State state = State.RIGHT;
        int i = 0;
        int j = 0;
        while (row_min <= row_max && col_min <= col_max) {
            if (state == State.RIGHT) {
                while (j <= col_max) {
                    res.add(matrix[i][j]);
                    j++;
                }
                j--;
                i++;
                state = State.DOWN;
                row_min++;
            } else if (state == State.DOWN) {
                while (i <= row_max) {
                    res.add(matrix[i][j]);
                    i++;
                }
                i--;
                j--;
                state = State.LEFT;
                col_max--;
            } else if (state == State.LEFT) {
                while (j >= col_min) {
                    res.add(matrix[i][j]);
                    j--;
                }
                j++;
                i--;
                state = State.UP;
                row_max--;
            } else {
                assert state == State.UP;
                while (i >= row_min) {
                    res.add(matrix[i][j]);
                    i--;
                }
                i++;
                j++;
                state = State.RIGHT;
                col_min++;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[][] matrix1 = {{1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}};
        int[][] matrix = new int[5][6];
        int count = 1;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(count + "\t");
                matrix[i][j] = count;
                count++;
            }
            System.out.println();
        }
        Solution solution = new Solution();
        ArrayList<Integer> printMatrix = solution.printMatrix(matrix);
        System.out.println(printMatrix);
    }
}
