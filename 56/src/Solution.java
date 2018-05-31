import java.util.Arrays;

// 第 56 题：数组中数字出现的次数 P275
// 参考资料：
// 1、https://blog.csdn.net/derrantcm/article/details/46771717
public class Solution {

    // 考察位运算：或、与、异或、非，以及无符号左移 >>>
    public int[] findNumbersAppearanceOnce(int[] nums) {
        int len = nums.length;
        int[] res = new int[2];
        assert len >= 2;
        if (len == 2) {
            return nums;
        }
        // 那两个只出现一次的数的异或运算的结果
        int xor = xor(nums);
        // 找到这个 xor 的二进制表示第 1 个是 1 的数位是第几位
        int binaryFirstNotZero = binaryFirstNotZero(xor);
        // 接下来分别对两组进行异或
        for (int i = 0; i < len; i++) {
            // 如果这个数右移这么多位是 1 的分在一组，是 0 的分在另外一组，遍历的时候，就进行异或运算
            if ((nums[i] >>> binaryFirstNotZero & 1) == 1) {
                res[0] ^= nums[i];
            } else {
                res[1] ^= nums[i];
            }
        }
        return res;
    }

    // 得到一个数组经过异或运算的结果 xor
    // 异或 的英文翻译就是 xor
    private int xor(int[] nums) {
        int xor = 0;
        for (int i = 0; i < nums.length; i++) {
            xor ^= nums[i];
        }
        return xor;
    }

    // 得到一个整数的二进制表示从右到左第 1 个非零的位数是第几位
    private int binaryFirstNotZero(int num) {
        int index = 0;
        // 这里的 1 把它看成二进制的 1，即 00000001
        while ((num & 1) == 0 && index < 32) {
            num >>>= 1;
            index++;
        }
        // 走到这里满足 (num & 1) == 1
        return index;
    }

    public static void main(String[] args) {
        int[] nums = {2, 4, 3, 6, 3, 2, 5, 5};
        Solution solution = new Solution();
        int[] res = solution.findNumbersAppearanceOnce(nums);
        System.out.println(Arrays.toString(res));

        int[] nums2 = {2, 4, 3, 6, 3, 2, 5, 5};
        int[] res2 = solution.findNumbersAppearanceOnce(nums2);
        System.out.println(Arrays.toString(res2));

        int[] nums3 = {4, 6};
        int[] res3 = solution.findNumbersAppearanceOnce(nums3);
        System.out.println(Arrays.toString(res3));

        int[] nums4 = {4, 6, 1, 1, 1, 1};
        int[] res4 = solution.findNumbersAppearanceOnce(nums4);
        System.out.println(Arrays.toString(res4));
    }
}
