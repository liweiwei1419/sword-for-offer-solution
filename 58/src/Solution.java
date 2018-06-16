public class Solution {

    /**
     * 辅助函数：翻转字符数组指定区间内的字符
     *
     * @param str
     * @param start
     * @param end
     */
    private void reverseString(char[] str, int start, int end) {
        int l = start;
        int r = end;
        while (l < r) {
            swap(str, l, r);
            l++;
            r--;
        }
    }

    /**
     * 辅助函数：交换字符数组指定索引的字符
     *
     * @param str
     * @param index1
     * @param index2
     */
    private void swap(char[] str, int index1, int index2) {
        if (index1 == index2) {
            return;
        }
        char temp = str[index1];
        str[index1] = str[index2];
        str[index2] = temp;
    }

    public String ReverseSentence(String str) {
        int len = str.length();
        if (len == 0 || len == 1) {
            return str;
        }
        char[] charArr = str.toCharArray();
        reverseString(charArr, 0, len - 1);
        int start = 0;
        for (int i = 0; i < len; i++) {
            if (charArr[i] == ' ') {
                reverseString(charArr, start, i - 1);
                start = i + 1;
            }
        }
        // 最后还要记得反转一下
        reverseString(charArr, start, len - 1);
        return String.valueOf(charArr);
    }

    public static void main(String[] args) {
        String str = "write your code here";
        Solution solution = new Solution();
        String reverseSentence = solution.ReverseSentence(str);
        System.out.println(reverseSentence);
    }
}
