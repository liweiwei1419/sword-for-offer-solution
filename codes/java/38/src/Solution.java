import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

/**
 * 使用标准的递归回溯的解法
 *
 * @author liwei
 */
public class Solution {

    private boolean[] marked;
    private ArrayList<String> res;

    public ArrayList<String> Permutation(String str) {
        res = new ArrayList<>();
        int len = str.length();
        if (len == 0) {
            return res;
        }
        marked = new boolean[len];
        char[] charArr = str.toCharArray();

        Arrays.sort(charArr);

        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < len; i++) {
            stringBuilder.append(charArr[i]);
        }
        Stack<Character> pre = new Stack<>();
        findPermutation(stringBuilder.toString(), 0, len, pre);
        return res;
    }

    private void findPermutation(String str, int hasUsedCount, int len, Stack<Character> pre) {
        if (hasUsedCount == len) {
            StringBuilder stringBuilder = new StringBuilder();
            for (int i = 0; i < len; i++) {
                stringBuilder.append(pre.get(i));
            }
            res.add(stringBuilder.toString());
            return;
        }
        for (int i = 0; i < len; i++) {
            if (!marked[i]) {
                if (i > 0 && str.charAt(i) == str.charAt(i - 1) && !marked[i - 1]) {
                    continue;
                }
                marked[i] = true;
                pre.add(str.charAt(i));
                findPermutation(str, hasUsedCount + 1, len, pre);
                pre.pop();
                marked[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        ArrayList<String> permutation = solution.Permutation("aba");
        System.out.println(permutation);
    }
}