import java.math.BigDecimal;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {

    private int count = 0;
    //  6
    // 7 8
    private PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>((a, b) -> a - b);
    //  4
    // 3 2
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>((a, b) -> b - a);

    private final static BigDecimal TWO = new BigDecimal("2");

    public void Insert(Integer num) {
        count++;
        if (count % 2 == 1) {
            // 如果是奇数，插入到最小堆
            if (minHeap.isEmpty()) {
                minHeap.add(num);
                return;
            }
            Integer minEle = minHeap.peek();
            Integer maxEle = maxHeap.peek();
            if (num >= maxEle || num >= minEle) {
                minHeap.add(num);
            } else {
                assert num < minEle;
                // 只有这一种情况
                minHeap.add(maxHeap.poll());
                maxHeap.add(num);
            }
        } else {
            // 如果是偶数，插入到最大堆

            if (maxHeap.isEmpty()) {
                maxHeap.add(num);
                return;
            }

            Integer maxEle = maxHeap.peek();
            Integer minEle = minHeap.peek();

            if (num <= minEle || num <= maxEle) {
                maxHeap.add(num);
            } else {
                assert num > maxEle;
                // 只有这一种情况
                maxHeap.add(minHeap.poll());
                minHeap.add(num);
            }
        }
    }

    public Double GetMedian() {
        if (count == 0) {
            return 0d;
        }
        if (count % 2 == 1) {
            // 如果是奇数
            return Double.valueOf(minHeap.peek());
        } else {
            // 如果是偶数
            BigDecimal a = new BigDecimal(String.valueOf(minHeap.peek()));
            BigDecimal b = new BigDecimal(String.valueOf(maxHeap.peek()));
            BigDecimal sum = a.add(b);
            BigDecimal half = sum.divide(TWO, 3, BigDecimal.ROUND_HALF_UP);
            return half.doubleValue();
        }
    }


}
