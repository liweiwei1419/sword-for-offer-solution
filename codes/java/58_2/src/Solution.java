/**
 * https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?tpId=13&tqId=11196&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
 * 左旋转字符串
 *
 * @author liwei
 */
public class Solution {

    private void reverseString(char[] charArr, int start, int end) {
        int l = start;
        int r = end;
        while (l < r) {
            swap(charArr, l, r);
            l++;
            r--;
        }
    }

    private void swap(char[] charArr, int index1, int index2) {
        if (index1 == index2) {
            return;
        }
        char temp = charArr[index1];
        charArr[index1] = charArr[index2];
        charArr[index2] = temp;
    }

    public String LeftRotateString(String str, int n) {
        int len = str.length();
        if (len == 0 || n < 0) {
            return "";
        }
        if (len == 1) {
            return str;
        }

        // 这里要注意了
        n = len - n % len;

        char[] charArr = str.toCharArray();
        reverseString(charArr, 0, len - 1);
        reverseString(charArr, 0, n - 1);
        reverseString(charArr, n, len - 1);
        return String.valueOf(charArr);
    }

    public static void main(String[] args) {
        String str = "abcXYZdef";
        Solution solution = new Solution();
        String leftRotateString = solution.LeftRotateString(str, 3);
        System.out.println(leftRotateString);
    }
}