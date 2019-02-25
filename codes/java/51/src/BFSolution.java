public class BFSolution {

    /**
     * 暴力解法求逆序对，使用两种循环进行枚举，时间复杂度：O(n^2)
     *
     * @param nums
     */
    public int inversionPairs(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] > nums[j]) {
                    System.out.println("找到的逆序对之一：" + nums[i] + " " + nums[j]);
                    count++;
                }
            }
        }
        return count;
    }
}
