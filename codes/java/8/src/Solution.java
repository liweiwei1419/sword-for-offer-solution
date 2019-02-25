// 参考资料：https://www.nowcoder.com/questionTerminal/9023a0c988684a53960365b889ceaf5e
class TreeLinkNode {
    int val;
    TreeLinkNode left = null;
    TreeLinkNode right = null;
    TreeLinkNode next = null;

    TreeLinkNode(int val) {
        this.val = val;
    }

    @Override
    public String toString() {
        return "TreeLinkNode{" +
                "val=" + val +
                '}';
    }
}

public class Solution {
    public TreeLinkNode GetNext(TreeLinkNode pNode) {
        if (pNode == null) {
            return null;
        }
        if (pNode.right != null) {
            TreeLinkNode node = pNode.right;
            // 这种情况漏掉了
            while (node.left != null) {
                node = node.left;
            }
            return node;

        } else {
            TreeLinkNode parent = pNode.next;
            TreeLinkNode child = pNode;
            while (parent != null && parent.right == child) {
                child = parent;
                parent = parent.next;
            }
            if (parent == null) {
                return null;
            }
            if (parent.left == child) {
                return parent;
            }

        }
        return null;
    }


    public static void main(String[] args) {
        TreeLinkNode node1 = new TreeLinkNode(1);
        TreeLinkNode node2 = new TreeLinkNode(2);
        TreeLinkNode node3 = new TreeLinkNode(3);
        TreeLinkNode node4 = new TreeLinkNode(4);
        TreeLinkNode node5 = new TreeLinkNode(5);
        TreeLinkNode node6 = new TreeLinkNode(6);
        TreeLinkNode node7 = new TreeLinkNode(7);
        TreeLinkNode node8 = new TreeLinkNode(8);
        TreeLinkNode node9 = new TreeLinkNode(9);

        node1.left = node2;
        node2.next = node1;
        node1.right = node3;
        node3.next = node1;

        node2.left = node4;
        node4.next = node2;
        node2.right = node5;
        node5.next = node2;

        node3.left = node6;
        node6.next = node3;

        node4.left = node7;
        node7.next = node4;

        node5.left = node8;
        node8.next = node5;

        node5.right = node9;
        node9.next = node5;

        Solution solution = new Solution();
        TreeLinkNode getNext = solution.GetNext(node6);
        System.out.println(getNext);

        System.out.println("----- 遍历验证 ------");
        getNext = solution.GetNext(node1);
        System.out.println(getNext);

        getNext = solution.GetNext(node2);
        System.out.println(getNext);

        getNext = solution.GetNext(node3);
        System.out.println(getNext);

        getNext = solution.GetNext(node4);
        System.out.println(getNext);

        getNext = solution.GetNext(node5);
        System.out.println(getNext);

        getNext = solution.GetNext(node6);
        System.out.println(getNext);

        getNext = solution.GetNext(node7);
        System.out.println(getNext);

        getNext = solution.GetNext(node8);
        System.out.println(getNext);
    }
}