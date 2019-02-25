public class Solution {
    public int NumberOf1(int n) {
        int count = 0;
        // 负数左移的时候，最高位补 1，因此，为了避免死循环，先要把最高位变成 0
        // 负数左移的时候，最高位补 1，因此，为了避免死循环，先要把最高位变成 0
        // 负数左移的时候，最高位补 1，因此，为了避免死循环，先要把最高位变成 0

        // 为负数的时候，将最高位的 1 变成 0
        // 即由负数变成正数，然后再计算 1 的个数
        if (n < 0) {
            n = n & Integer.MAX_VALUE;
            count++;
        }

        // 当 n 是正数的时候，计算 1 的个数
        while (n != 0) {
            count += n & 1;
            n = n >> 1;
        }
        return count;
    }
}