class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}

public class Solution {

    public ListNode FindKthToTail(ListNode head, int k) {
        // 注意点1：极端输入直接输出结果
        if (head == null) {
            return null;
        }
        ListNode dummyNode = new ListNode(-1);
        dummyNode.next = head;
        ListNode fast = dummyNode;
        for (int i = 0; i < k; i++) {
            fast = fast.next;
            // 注意点2：对不符合要求的输入的判断
            if (fast == null) {
                return null;
            }
        }
        ListNode slow = dummyNode;
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
    }
}