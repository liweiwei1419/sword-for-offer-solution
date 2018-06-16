import java.util.Arrays;

/**
 * 计算逆序对的同时，把排序也给做了
 * 时间复杂度：时间复杂度只有O(nlogn)
 *
 * @author liwei
 */
public class Solution2 {

    private int[] temp;

    public int inversionPairs(int[] nums) {
        int len = nums.length;
        if (len == 0 || len == 1) {
            return 0;
        }
        temp = new int[len];
        return inversionPairs(nums, 0, len - 1);
    }

    /**
     * 计算在数组 nums 的索引区间 [l,r] 内统计逆序对
     *
     * @param nums 待统计的数组
     * @param l    待统计数组的左边界，可以取到
     * @param r    待统计数组的右边界，可以取到
     * @return
     */
    private int inversionPairs(int[] nums, int l, int r) {
        // 极端情况下，就是只有 1 个元素的时候
        // 这里只要写 == 就可以了，不必写大于
        if (l == r) {
            return 0;
        }
        int mid = l + (r - l) / 2;
        int leftPairs = inversionPairs(nums, l, mid);
        int rightPairs = inversionPairs(nums, mid + 1, r);
        int mergePairs = 0;
        // 在归并的过程中计算逆序对
        if (nums[mid] > nums[mid + 1]) {
            // 这一步同样适用于归并排序的优化
            // 如果数组有序，不存在逆序对，也就没有必要归并统计了
            mergePairs = mergeAndCount(nums, l, mid, r);
        }
        return leftPairs + rightPairs + mergePairs;

    }

    private int mergeAndCount(int[] nums, int l, int mid, int r) {
        // 复制到辅助数组里，帮助我们完成统计
        for (int i = l; i <= r; i++) {
            temp[i] = nums[i];
        }
        int i = l;
        int j = mid + 1;
        int res = 0;
        for (int k = l; k <= r; k++) {
            if (i > mid) {
                // i 用完了，只能用 j
                nums[k] = temp[j];
                j++;
            } else if (j > r) {
                // j 用完了，只能用 i
                nums[k] = temp[i];
                i++;
            } else if (temp[i] <= temp[j]) {
                // 不统计逆序对，只做排序
                nums[k] = temp[i];
                i++;
            } else {
                nums[k] = temp[j];
                j++;
                // 【关键】快就快在这里，一次可以数出一个区间的个数的逆序对
                res += (mid - i + 1);
            }
        }
        return res;
    }


    public static void main(String[] args) {
        int[] nums = new int[]{3, 1, 4, 5, 2};
        Solution2 solution2 = new Solution2();
        int inversionPairs = solution2.inversionPairs(nums);
        System.out.println(Arrays.toString(nums));
        System.out.println(inversionPairs);

        // 完全有序的数组，逆序对为 0
        // 完全逆序的数组，逆序对为 N*（N-1）/2
    }

}
