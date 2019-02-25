import java.util.Random;

public class TestCase {

    private static Random random = new Random(System.currentTimeMillis());

    private static int[] generateRandomArray() {
        int len = 10;
        int[] randomArray = new int[len];
        for (int i = 0; i < len; i++) {
            int randomInt = random.nextInt(50);
            randomArray[i] = randomInt;
        }
        return randomArray;
    }

    public static void main(String[] args) {

        for (int i = 0; i < 5; i++) {
            int[] randomArray = generateRandomArray();
            int[] randomArray2 = randomArray.clone();
            int[] randomArray3 = randomArray.clone();
            Solution solution = new Solution();
            Solution2 solution2 = new Solution2();
            Solution3 solution3 = new Solution3();
            int inversePairs1 = solution.InversePairs(randomArray);
            int inversePairs2 = solution2.InversePairs(randomArray2);
            int inversePairs3 = solution3.InversePairs(randomArray3);
            System.out.println(inversePairs1 + "\t" + inversePairs2 + "\t" + inversePairs3);
            if(inversePairs1!=inversePairs2 || inversePairs1!=inversePairs3 || inversePairs2!=inversePairs3){
                System.out.println("算法错误！");
            }
        }


    }
}
