/**
 * @author liwei
 * @date 18/6/16 上午11:07
 */
public class Solution2 {
    public int NumberOf1(int n) {
        int count = 0;
        while (n != 0) {
            count++;
            n = (n - 1) & n;
        }
        return count;
    }
}
