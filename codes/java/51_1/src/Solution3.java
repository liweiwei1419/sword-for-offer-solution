/**
 * 暴力解法
 */
public class Solution3 {

    public int InversePairs(int[] array) {
        int count = 0;
        int len = array.length;
        if (len == 0) {
            return 0;
        }

        for (int i = 0; i < len - 1; i++) {
            for (int j = i + 1; j < len; j++) {
                if (array[i] > array[j]) {
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 3, 4, 5, 6, 7, 0};
        Solution3 solution3 = new Solution3();
        int inversePairs = solution3.InversePairs(nums);
        System.out.println(inversePairs);

        nums = new int[]{7, 5, 6, 4};
        solution3 = new Solution3();
        inversePairs = solution3.InversePairs(nums);
        System.out.println(inversePairs);
    }
}
