import java.util.Arrays;

public class TestCase {


    public static void main(String[] args) {
        int[] nums = new int[]{7, 5, 6, 4};
        int[] nums1 = new int[]{7, 5, 6, 4};


        BFSolution bfSolution = new BFSolution();

        Solution2 solution2 = new Solution2();

        System.out.println(bfSolution.inversionPairs(nums));
        System.out.println(solution2.inversionPairs(nums1));

        System.out.println(Arrays.toString(nums1));

    }
}
