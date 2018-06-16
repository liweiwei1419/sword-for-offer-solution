import java.util.ArrayList;

public class Solution {
    public ArrayList<Integer> GetLeastNumbers_Solution(int[] input, int k) {
        ArrayList<Integer> res = new ArrayList<>();
        int len = input.length;
        if (len == 0 || k < 0 || k > len) {
            return res;
        }
        int l = 0;
        int r = len - 1;
        // 考虑边界条件
        while (l <= r) {
            int partition = partition(input, l, r);
            if (partition < k - 1) {
                l = partition + 1;
            } else if (partition > k - 1) {
                r = partition - 1;
            } else {
                assert partition == k - 1;
                for (int i = 0; i < k; i++) {
                    res.add(input[i]);
                }
                break;
            }
        }
        return res;
    }

    private int partition(int[] nums, int l, int r) {
        // 可以随机选取
        int pivot = nums[l];
        int lt = l;
        for (int i = l + 1; i <= r; i++) {
            if (nums[i] < pivot) {
                lt++;
                swap(nums, lt, i);
            }
        }
        swap(nums, lt, l);
        return lt;
    }

    private void swap(int[] nums, int index1, int index2) {
        if (index1 == index2) {
            return;
        }
        int temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{4, 5, 1, 6, 2, 7, 3, 8};
        int k = 8;
        Solution solution = new Solution();
        ArrayList<Integer> getLeastNumbers_solution = solution.GetLeastNumbers_Solution(nums, k);
        System.out.println(getLeastNumbers_solution);
    }
}