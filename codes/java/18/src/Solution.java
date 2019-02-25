class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }

    public ListNode(int[] arr) {
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("arr can not be empty");
        }
        this.val = arr[0];
        ListNode cur = this;
        for (int i = 1; i < arr.length; i++) {
            cur.next = new ListNode(arr[i]);
            cur = cur.next;
        }
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        ListNode cur = this;
        while (cur != null) {
            s.append(cur.val + " -> ");
            cur = cur.next;
        }
        s.append("NULL");
        return s.toString();
    }
}

public class Solution {
    public ListNode deleteDuplication(ListNode pHead) {
        ListNode dummyNode = new ListNode(-1);
        dummyNode.next = pHead;
        ListNode curNode = dummyNode;
        while (curNode.next != null && curNode.next.next != null) {
            ListNode next = curNode.next;
            ListNode nextNext = next.next;
            if (next.val == nextNext.val) {
                while (nextNext.next != null && nextNext.val == nextNext.next.val) {
                    nextNext = nextNext.next;
                }
                ListNode delNode = nextNext;
                curNode.next = delNode.next;
                delNode.next = null;
            } else {
                curNode = curNode.next;
            }
        }
        return dummyNode.next;
    }


    public static void main(String[] args) {
        int[] nums = new int[]{1, 2, 3, 3, 4, 4, 5};
        ListNode head = new ListNode(nums);
        System.out.println(head);

        Solution solution = new Solution();
        ListNode deleteDuplication = solution.deleteDuplication(head);
        System.out.println(deleteDuplication);
    }
}