import java.util.Arrays;

public class Solution {
    // 保证奇数和奇数，偶数和偶数之间的相对位置不变。
    public void reOrderArray(int[] array) {
        int len = array.length;
        if (len == 0) {
            return;
        }
        // 奇数全部挪到缓存数组中
        int[] buff = new int[len];
        int j = -1;
        for (int i = 0; i < len; i++) {
            if (array[i] % 2 == 1) {
                j++;
                buff[j] = array[i];
            }
        }
        // 如果没有奇数，直接返回就可以了
        if (j == -1) {
            return;
        }
        // 从后向前赋值
        int k = len - 1;
        for (int i = len - 1; i >= 0; i--) {
            if (array[i] % 2 == 0) {
                array[k] = array[i];
                k--;
            }
        }
        while (j >= 0) {
            array[j] = buff[j];
            j--;
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        Solution solution = new Solution();
        solution.reOrderArray(arr);
        System.out.println(Arrays.toString(arr));
    }
}