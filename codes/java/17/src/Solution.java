import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {

    private List<String> res;

    private void findPermutation(int hasUsedCount, int n, Stack<Integer> pre) {
        if (hasUsedCount == n) {
            // 打印 pre
            String integerStr = listToString(pre);
            if (!"".equals(integerStr)) {
                res.add(integerStr);
            }
            return;
        }
        for (int i = 0; i < 10; i++) {
            pre.add(i);
            findPermutation(hasUsedCount + 1, n, pre);
            // 这一步很关键，下一轮循环，我得换一个数
            pre.pop();
        }
    }

    private String listToString(Stack<Integer> pre) {
        StringBuilder stringBuilder = new StringBuilder();
        // 遇到不为零的数字，就打开字符串拼接的功能
        boolean startPrint = false;
        for (int i = 0; i < pre.size(); i++) {
            // !startPrint 前面加上这个判断，打开输出以后，就不用每次都判断拿出来的数等不等于 0 了
            if (!startPrint && pre.get(i) != 0) {
                startPrint = true;
            }
            if (startPrint) {
                stringBuilder.append(pre.get(i));
            }
        }
        return stringBuilder.toString();
    }

    /**
     * 入口函数
     * @param n
     * @return
     */
    public List<String> print1ToMaxOfNDigits(int n) {
        res = new ArrayList<>();
        if (n <= 0) {
            return res;
        }
        // 转换成排列问题
        Stack<Integer> pre = new Stack<>();
        findPermutation(0, n, pre);
        return res;
    }

    public static void main(String[] args) {
        int n = 3;
        Solution solution = new Solution();
        List<String> print1ToMaxOfNDigits = solution.print1ToMaxOfNDigits(n);
        System.out.println(print1ToMaxOfNDigits);
        System.out.println(n + " 位数有多少个：" + print1ToMaxOfNDigits.size());
    }
}
