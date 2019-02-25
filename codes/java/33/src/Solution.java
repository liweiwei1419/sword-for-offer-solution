public class Solution {
    public boolean VerifySquenceOfBST(int[] sequence) {
        int len = sequence.length;
        if (len == 0) {
            return false;
        }
        if (len == 1) {
            return true;
        }
        int l = 0;
        int r = len - 1;
        while (l <= r) {
            int mid = judgeBST(sequence, l, r);
            if (mid == -1) {
                return false;
            }
            // 注意考虑数组下标越界的问题
            // return (mid > 1 ? judgeBST(sequence, l, mid - 1) != -1 : true) && judgeBST(sequence, mid, r) != -1;
            return (mid <= 1 || judgeBST(sequence, l, mid - 1) != -1) && judgeBST(sequence, mid, r) != -1;
        }
        return true;
    }

    // mid 以及 mid 以后的数子都小于 arr[r]
    private int judgeBST(int[] arr, int l, int r) {
        int p = arr[r];
        int i = l;
        int mid;
        // 5，4，3，2，1
        while (arr[i] < p) {
            i++;
        }
        mid = i;
        while (arr[i] > p && i < r) {
            i++;
        }
        // 如果遍历到末尾了，就说明，在这一层，是可以构成 BST 的
        if (i == r) {
            return mid;
        }
        return -1;
    }

    public static void main(String[] args) {
        // int[] nums1 = {5, 7, 6, 9, 11, 10, 8};
        int[] nums = {5, 4, 3, 2, 1};
        Solution solution = new Solution();
        boolean verifySquenceOfBST = solution.VerifySquenceOfBST(nums);
        System.out.println(verifySquenceOfBST);
    }
}