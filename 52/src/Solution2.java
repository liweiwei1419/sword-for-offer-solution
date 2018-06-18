import java.util.Stack;

class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }

    ListNode(Integer[] nums) {
        ListNode currNode = this;
        currNode.val = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currNode.next = new ListNode(nums[i]);
            currNode = currNode.next;
        }
    }

    @Override
    public String toString() {
        ListNode currNode = this;
        StringBuilder s = new StringBuilder();
        while (currNode != null) {
            s.append(currNode.val);
            s.append(" -> ");
            currNode = currNode.next;
        }
        // 最后添加一个 NULL 标志表示添加到末尾了
        s.append("NULL");
        return s.toString();
    }
}

public class Solution {

    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if (pHead1 == null || pHead2 == null) {
            return null;
        }
        Stack<ListNode> stack1 = new Stack<>();
        Stack<ListNode> stack2 = new Stack<>();
        ListNode curNode = pHead1;
        while (curNode != null) {
            stack1.add(curNode);
            curNode = curNode.next;
        }
        curNode = pHead2;
        while (curNode != null) {
            stack2.add(curNode);
            curNode = curNode.next;
        }

        ListNode res = null;
        // 因为是公共结点，所以他们的地址一定一样，可以用 ==
        while (!stack1.isEmpty() && !stack2.isEmpty() && stack1.peek() == stack2.peek()) {
            stack1.pop();
            res = stack2.pop();

        }
        return res;
    }

    // 思路：画出图来，我们就知道，链表的后半部分不一样，
    // 那么我们就让他们前半部分一样就得了，遍历完以后，就会遇到公共结点了
    public ListNode FindFirstCommonNode2(ListNode pHead1, ListNode pHead2) {
        if (pHead1 == null || pHead2 == null) {
            return null;
        }
        ListNode p1 = pHead1;
        ListNode p2 = pHead2;

        while (p1 != p2) {
            p1 = p1 == null ? pHead2 : p1.next;
            p2 = p2 == null ? pHead1 : p2.next;
        }
        return p1;
    }

    public ListNode FindFirstCommonNode3(ListNode pHead1, ListNode pHead2) {
        ListNode p1 = pHead1;
        ListNode p2 = pHead2;

        while (p1 != p2) {
            p1 = p1 == null ? pHead2 : p1.next;
            p2 = p2 == null ? pHead1 : p2.next;
        }
        return p1;
    }


    public static void main(String[] args) {
        ListNode phead1 = new ListNode(0);
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);
        ListNode node5 = new ListNode(5);

        phead1.next = node1;
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;

        ListNode phead2 = new ListNode(6);
        ListNode node7 = new ListNode(7);
        phead2.next = node7;
        node7.next = node4;


        Solution solution = new Solution();
        ListNode findFirstCommonNode2 = solution.FindFirstCommonNode2(phead1, phead2);
        System.out.println(findFirstCommonNode2);
    }
}
