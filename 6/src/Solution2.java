import java.util.ArrayList;

/**
 * 递归写法
 *
 * @author liwei
 */
public class Solution2 {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList<Integer> res = new ArrayList<>();
        if (listNode == null) {
            return res;
        }
        printListFromTailToHead(listNode, res);
        return res;
    }

    private void printListFromTailToHead(ListNode listNode, ArrayList<Integer> res) {
        if (listNode == null) {
            return;
        }
        // 写在这个位置，就是正序
        if (listNode.next != null) {
            printListFromTailToHead(listNode.next, res);
        }
        // 写在这个位置，就是倒序
        res.add(listNode.val);
    }
}