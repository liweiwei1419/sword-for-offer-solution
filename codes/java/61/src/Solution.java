import java.util.Arrays;

public class Solution {

    public boolean isContinuous(int[] numbers) {
        int len = numbers.length;
        if (len != 5) {
            return false;
        }
        Arrays.sort(numbers);
        // "0" 的个数
        int zeroCount = 0;
        // 当前数与后一个数的距离，距离为 1，表示是顺子
        int diffDistance = 0;
        for (int i = 0; i < 4; i++) {
            if (numbers[i] == 0) {
                zeroCount++;
                continue;
            }
            if (numbers[i] == numbers[i + 1]) {
                return false;
            } else {
                diffDistance += (numbers[i + 1] - numbers[i] - 1);
            }

        }
        return zeroCount >= diffDistance;
    }
}