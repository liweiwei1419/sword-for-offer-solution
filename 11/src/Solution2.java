/**
 * https://www.nowcoder.com/questionTerminal/9f3231a991af4f55b95579b44b7a01ba
 *
 * @author liwei
 */
public class Solution2 {

    public int minNumberInRotateArray(int[] array) {
        int len = array.length;
        if (len == 0) {
            return 0;
        }
        int first = 0;
        int last = len - 1;
        while (first < last) {
            int mid = first + (last - first) / 2;
            if (array[mid] > array[last]) {
                first = mid + 1;
            } else if (array[mid] == array[last]) {
                last = last - 1;
            } else {
                last = mid;
            }
        }
        return array[first];
    }

    public static void main(String[] args) {
        // int[] nums = new int[]{3};
        // int[] nums = new int[]{3, 4, 5, 6, 7, 8, 9, 1, 2};
        // int[] nums = new int[]{1, 2, 3, 4, 5};
        int[] nums = new int[]{2, 2, 2, 1, 2};
        Solution2 solution2 = new Solution2();
        int minNumberInRotateArray = solution2.minNumberInRotateArray(nums);
        System.out.println(minNumberInRotateArray);
    }
}