class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}

public class Solution {

    TreeNode res;

    // 中序遍历
    TreeNode KthNode(TreeNode pRoot, int k) {
        if (k <= 0 || pRoot == null) {
            return null;
        }
        int[] arr = new int[1];
        arr[0] = k;
        inOrder(pRoot, arr);
        return res;
    }

    void inOrder(TreeNode node, int[] k) {
        if (node == null) {
            return;
        }
        inOrder(node.left, k);
        k[0]--;
        if (k[0] == 0) {
            res = node;
            return;
        }
        inOrder(node.right, k);
    }

}