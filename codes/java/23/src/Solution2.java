class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}


public class Solution {

    public ListNode EntryNodeOfLoop(ListNode pHead) {

        // 先考虑好极端情况
        // 空结点、只有一个结点、两个结点（不互相指向）
        if (pHead == null || pHead.next == null || pHead.next.next == null) {
            return null;
        }

        // 注意：一开始呀先让 slow 和 fast 走一定步数，
        // 否则起点一样，fast != slow 就永远不成立了！！！
        // 解决这道问题要用一些数论的知识
        ListNode slow = pHead.next;
        ListNode fast = pHead.next.next;
//        ListNode slow = pHead;
//        ListNode fast = pHead;
        while (fast.next != null && fast.next.next != null && fast != slow) {
            slow = slow.next;
            fast = fast.next.next;
        }
        if (fast.next == null || fast.next.next == null) {
            return null;
        }
        // 走到这里一定满足 fast == slow
        assert fast == slow;
        // 复位到开头
        fast = pHead;
        while (fast != slow) {
            fast = fast.next;
            slow = slow.next;
        }
        return fast;
    }
}
