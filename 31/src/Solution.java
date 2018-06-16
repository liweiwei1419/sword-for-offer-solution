import java.util.LinkedList;
import java.util.Stack;

public class Solution {

    // 这道题花了好长时间，不过终于思路清晰了
    public boolean IsPopOrder(int[] pushA, int[] popA) {
        int lenA = pushA.length;
        int lenB = popA.length;
        if (lenA != lenB) {
            return false;
        }

        // 把两个数组放入一个队列中，是为了方便遍历
        LinkedList<Integer> queue1 = new LinkedList<>();
        for (int i = 0; i < lenA; i++) {
            queue1.addLast(pushA[i]);
        }
        LinkedList<Integer> queue2 = new LinkedList<>();
        for (int i = 0; i < lenA; i++) {
            queue2.addLast(popA[i]);
        }

        Stack<Integer> stack = new Stack<>();
        // 以上的代码虽然长，但也只是做了一些极端测试用例的考虑和变量的初始化工作

        // 步骤1：
        // 把原始数组形成的队列遍历完成，
        // 只要是与栈数组形成的队列的队首元素不等的，都放入一个辅助栈中
        while (!queue1.isEmpty()) {
            int peekFirst1 = queue1.removeFirst();
            int peekFirst2 = queue2.peekFirst();

            if (peekFirst1 != peekFirst2) {
                stack.add(peekFirst1);
            } else {
                queue2.removeFirst();
            }

        }
        // 步骤 2：陆续弹出栈，遍历栈数组形成的队列，只要不等就表示不符合题目要求
        while (!stack.isEmpty()) {
            if (!queue2.removeFirst().equals(stack.pop())) {
                return false;
            }
        }
        // 步骤 3：能走到最后的，说明符合题目要求
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
//        int[] pushA = new int[]{1, 2, 3, 4, 5};
//        int[] popA = new int[]{4, 5, 3, 2, 1};
        int[] pushA = new int[]{1};
        int[] popA = new int[]{1};
        boolean isPopOrder = solution.IsPopOrder(pushA, popA);
        System.out.println(isPopOrder);
    }
}