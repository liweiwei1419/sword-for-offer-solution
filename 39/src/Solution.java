import java.util.Arrays;

public class Solution {
    //
    // {1,2,3,2,2,2,5,4,2} 9 4
    // {1,2,3,2,2,2,5,4} 8 4
    public int MoreThanHalfNum_Solution(int[] array) {
        int len = array.length;
        if (len == 0) {
            return 0;
        }
        Arrays.sort(array);
        int target = array[len / 2];
        int count = 0;
        for (int i = 0; i < len; i++) {
            if (array[i] == target) {
                count++;
            }
        }
        if (count > len / 2) {
            return target;
        }
        return 0;
    }


    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 3, 2, 2, 2, 5, 4, 2};
        // [1,2,3,2,4,2,5,2,3]
        Solution solution = new Solution();
        int moreThanHalfNum_solution = solution.MoreThanHalfNum_Solution(nums);
        System.out.println(moreThanHalfNum_solution);
    }
}