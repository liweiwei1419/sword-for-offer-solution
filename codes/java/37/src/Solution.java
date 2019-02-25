// 剑指 Offer 第 37 题 P194

import java.util.LinkedList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution {

    /**
     * 序列化一棵二叉树（其实就是前序遍历）
     * @param root
     * @return
     */
    public String serialize(TreeNode root) {
        if (root == null) {
            return "$,";
        }
        StringBuilder sb = new StringBuilder(root.val + ",");
        sb.append(serialize(root.left));
        sb.append(serialize(root.right));
        return sb.toString();
    }

    // 反序列化一棵二叉树
    public TreeNode deserialize(String str) {
        String[] strArr = str.split(",");
        LinkedList<String> queue = new LinkedList<>();
        for (String s : strArr) {
            queue.addLast(s);
        }
        return preOrder(queue);
    }

    // 使用队列就实现了迭代器的功能
    private TreeNode preOrder(LinkedList<String> queue) {
        String s = queue.removeFirst();
        if (!"$".endsWith(s)) {
            TreeNode newNode = new TreeNode(Integer.parseInt(s));
            newNode.left = preOrder(queue);
            newNode.right = preOrder(queue);
            // 理解将新创建的结点返回回去的必要性
            return newNode;
        }
        // 是 "$" 就返回空指针，注意这里的递归方法，会把空指针接在原来的树节点上
        return null;
    }

    public static void main(String[] args) {
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);
        TreeNode node6 = new TreeNode(6);
        node1.left = node2;
        node1.right = node3;
        node2.left = node4;
        node3.left = node5;
        node3.right = node6;

        Solution solution = new Solution();
        String serializeStr = solution.serialize(node1);
        System.out.println(serializeStr);

        String s = "1,2,4,$,$,$,3,5,$,$,6,$,$,";
        TreeNode treeNode = solution.deserialize(s);
        String serializeStr1 = solution.serialize(treeNode);
        System.out.println(serializeStr1);
    }
}
