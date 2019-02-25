
public class Solution2 {
    public TreeNode convert(TreeNode root) {
        if (root == null) {
            return root;
        }
        TreeNode left = rightMost(root.left);
        TreeNode right = leftMost(root.right);
        convert(root.left);
        convert(root.right);
        if (left != null) {
            left.right = root;
        }
        root.left = left;
        if (right != null) {
            right.left = root;
        }
        root.right = right;
        while (root.left != null) {
            root = root.left;
        }
        return root;
    }

    TreeNode leftMost(TreeNode root) {
        if (root == null) {
            return null;
        }
        while (root.left != null) {
            root = root.left;
        }
        return root;
    }

    TreeNode rightMost(TreeNode root) {
        if (root == null) {
            return null;
        }
        while (root.right != null) {
            root = root.right;
        }
        return root;
    }
}