import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

/**
 * 树状数组解法
 *
 * @author liwei
 */
public class Solution2 {

    public int InversePairs(int[] array) {
        int len = array.length;
        int count = 0;
        if (len == 0) {
            return 0;
        }
        // 离散化
        // [1, 2, 3, 4, 5, 6, 7, 0]
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 0; i < len; i++) {
            set.add(array[i]);
        }
        FenwickTree fenwickTree = new FenwickTree(set.size());
        Map<Integer, Integer> map = new HashMap<>();
        int index = 1;
        for (Integer num : set) {
            map.put(num, index);
            index++;
        }
        for (int i = len - 1; i >= 0; i--) {
            index = map.get(array[i]);
            // 下面这两步最关键了：从后向前算
            fenwickTree.update(index, 1);
            count += fenwickTree.query(index - 1);
        }
        return count;
    }

    private class FenwickTree {

        /**
         * 预处理数组
         */
        private int[] tree;
        private int len;

        public FenwickTree(int n) {
            this.len = n;
            tree = new int[n + 1];
        }

        /**
         * 单点更新
         *
         * @param i     原始数组索引 i
         * @param delta 变化值 = 更新以后的值 - 原始值
         */
        public void update(int i, int delta) {
            // 从下到上更新，注意，预处理数组，比原始数组的 len 大 1，故 预处理索引的最大值为 len
            while (i <= len) {
                tree[i] += delta;
                i += lowbit(i);
            }
        }

        /**
         * 查询前缀和
         *
         * @param i 前缀的最大索引，即查询区间 [0, i] 的所有元素之和
         */
        public int query(int i) {
            // 从右到左查询
            int sum = 0;
            while (i > 0) {
                sum += tree[i];
                i -= lowbit(i);
            }
            return sum;
        }

        public int lowbit(int x) {
            return x & (-x);
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 3, 4, 5, 6, 7, 0};
        Solution2 solution2 = new Solution2();
        int inversePairs = solution2.InversePairs(nums);
        System.out.println(inversePairs);

        nums = new int[]{7, 5, 6, 4};
        solution2 = new Solution2();
        inversePairs = solution2.InversePairs(nums);
        System.out.println(inversePairs);
    }
}
