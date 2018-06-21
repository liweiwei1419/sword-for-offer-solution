public class Solution {

    private static final int ZERO = (int) '0';
    private static final int NINE = (int) '9';

    public int StrToInt(String str) {
        int len = str.length();
        if (len == 0) {
            return 0;
        }
        // 最终结果带的符号
        int symbol = 1;
        int res = 0;
        int start = 0;
        char[] chars = str.toCharArray();

        // 如果字符串的第 0 号索引表示的是"符号"，那么，数值的转换从索引为 1 处开始
        if (chars[0] == '-') {
            symbol = -1;
            start = 1;
        }
        if (chars[0] == '+') {
            start = 1;
        }
        for (int i = start; i < len; i++) {
            // 字符 '0' 的 ASCII 值是 48
            // 字符 '9' 的 ASCII 值是 57
            if (chars[i] < ZERO || chars[i] > NINE) {
                return 0;
            }
            res = res * 10 + chars[i] - ZERO;
        }
        return res * symbol;
    }

    public static void main(String[] args) {
        System.out.println((int) '0');
        System.out.println((int) '9');
    }
}