/**
 * @author liwei
 * @date 18/6/16 上午11:07
 */
public class Solution2 {
    /***
     * 可以使用 1001 作为测试用例来理解，a&(a-1) 的结果会将 a 最右边的 1 变为 0 ，直到 a = 0，还可以先将 a&1 != 0,然后右移 1 位，但不能计算负
     * 数的值
     * @param n
     * @return
     */
    public int NumberOf1(int n) {
        int count = 0;
        while (n != 0) {
            count++;
            n = (n - 1) & n;
        }
        return count;
    }
}
