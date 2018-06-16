public class Solution {

    // 虽然可以通过，但是 O(n) 的复杂度并不理想
    public int minNumberInRotateArray(int[] array) {
        // {3,4,5,1,2}
        // 1 2 3 4 5
        int len = array.length;
        for (int i = 1; i < len - 1; i++) {
            if (array[i] < array[i - 1]) {
                return array[i];
            }
        }
        // 如果走到这里，说明数组是升序的，直接返回第 0 号索引的元素就可以了
        return array[0];
    }

    public static void main(String[] args) {
        // int[] nums = new int[]{3, 4, 5, 1, 2};
        int[] nums = new int[]{1, 2, 3, 4, 5};
        Solution solution = new Solution();
        int minNumberInRotateArray = solution.minNumberInRotateArray(nums);
        System.out.println(minNumberInRotateArray);
    }
}