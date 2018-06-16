class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }
}

public class Solution {
    boolean isSymmetrical(TreeNode pRoot) {
        if (pRoot == null) {
            return true;
        }
        return helper(pRoot.left, pRoot.right);
    }

    private boolean helper(TreeNode pRoot1, TreeNode pRoot2) {
        if (pRoot1 == null && pRoot2 == null) {
            return true;
        }
        if (pRoot1 == null || pRoot2 == null || pRoot1.val != pRoot2.val) {
            return false;
        }
        return helper(pRoot1.left, pRoot2.right) && helper(pRoot1.right, pRoot2.left);
    }
}