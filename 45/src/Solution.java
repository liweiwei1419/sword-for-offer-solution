import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    public String PrintMinNumber(int[] numbers) {
        int len = numbers.length;
        if (len == 0) {
            return "";
        }
        if (len == 1) {
            return numbers[0] + "";
        }
        Comparator<String> comparator = new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String a = o1 + o2;
                String b = o2 + o1;
                int len = a.length();
                for (int i = 0; i < len ; i++) {
                    if(a.charAt(i)<b.charAt(i)){
                        return -1;
                    }else if(a.charAt(i)>b.charAt(i)){
                        return 1;
                    }
                }
                return 0;
            }
        };
        String[] numsStr = new String[len];
        for (int i = 0; i < len; i++) {
            numsStr[i] = numbers[i] + "";
        }
        Arrays.sort(numsStr, comparator);
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < len; i++) {
            stringBuilder.append(numsStr[i]);
        }
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        int[] nums = new int[]{3, 32, 321};
        Solution solution = new Solution();
        String printMinNumber = solution.PrintMinNumber(nums);
        System.out.println(printMinNumber);
    }
}