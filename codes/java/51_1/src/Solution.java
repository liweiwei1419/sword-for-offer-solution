/**
 * 分治法，同归并排序
 *
 * @author liwei
 */
public class Solution {

    private int count = 0;
    private int[] buff;

    public int InversePairs(int[] array) {
        int len = array.length;
        buff = new int[len];
        if (len == 0) {
            return 0;
        }
        sortAndCount(array, 0, len - 1);
        return count;
    }

    private void sortAndCount(int[] array, int l, int r) {
        // 递归终止条件，l == r 的时候
        if (l == r) {
            // 区间缩成一个数，无法计算逆序对
            return;
        }
        int mid = l + (r - l) / 2;
        sortAndCount(array, l, mid);
        sortAndCount(array, mid + 1, r);
        // 这一步别忘了，如果数组有序，就不用归并了
        if (array[mid] > array[mid + 1]) {
            mergeOfTwoSortedArrayAndCount(array, l, mid, r);
        }
    }

    // 4 5 6  1 2 3
    // j 出列的时候，计算逆序对
    // j 出列的时候，i 还剩下的数
    private void mergeOfTwoSortedArrayAndCount(int[] array, int l, int mid, int r) {
        for (int i = l; i <= r; i++) {
            buff[i] = array[i];
        }
        int i = l;
        int j = mid + 1;
        for (int k = l; k <= r; k++) {
            if (i == mid + 1) {
                // i 用完了，使用 j
                array[k] = buff[j];
                j++;
            } else if (j == r + 1) {
                array[k] = buff[i];
                i++;
            } else if (buff[i] <= buff[j]) {
                // i 出列
                array[k] = buff[i];
                i++;
            } else {
                // j 出列
                array[k] = buff[j];
                j++;
                count += (mid - i + 1);
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 3, 4, 5, 6, 7, 0};
        Solution solution = new Solution();
        int inversePairs = solution.InversePairs(nums);
        System.out.println(inversePairs);

        nums = new int[]{7, 5, 6, 4};
        solution = new Solution();
        inversePairs = solution.InversePairs(nums);
        System.out.println(inversePairs);
    }
}
