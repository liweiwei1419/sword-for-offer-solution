class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public class Solution {
    public boolean IsBalanced_Solution(TreeNode root) {
        int[] depth = new int[1];
        return isBalanced(root, depth);
    }

    private boolean isBalanced(TreeNode root, int[] depth) {
        if (root == null) {
            depth[0] = 0;
            return true;
        }
        int[] left = new int[1];
        int[] right = new int[1];
        // 满足左子树右子树是平衡二叉树的时候，才去计算它们的高度差
        if (isBalanced(root.left, left) && isBalanced(root.right, right)) {
            if (Math.abs(left[0] - right[0]) <= 1) {
                depth[0] = Integer.max(left[0], right[0]) + 1;
                return true;
            }
        }
        return false;
    }
}