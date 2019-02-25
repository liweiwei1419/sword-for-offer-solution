

public class Solution2 {

    TreeNode res;
    private int k;

    // 中序遍历
    TreeNode KthNode(TreeNode pRoot, int k) {
        if (k <= 0 || pRoot == null) {
            return null;
        }
        this.k = k;
        inOrder(pRoot);
        return res;
    }

    void inOrder(TreeNode node) {
        if (node == null) {
            return;
        }
        inOrder(node.left);
        k--;
        if (k == 0) {
            res = node;
            return;
        }
        inOrder(node.right);
    }

}