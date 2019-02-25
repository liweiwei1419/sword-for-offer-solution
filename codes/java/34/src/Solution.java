import java.util.ArrayList;
import java.util.Stack;

class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }
}

public class Solution {
    // 使用搜索的策略可以完成
    public ArrayList<ArrayList<Integer>> FindPath(TreeNode root, int target) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        Stack<Integer> pre = new Stack<>();
        findPath(root, target, pre, res);
        return res;
    }

    private void findPath(TreeNode root, int target, Stack<Integer> pre, ArrayList<ArrayList<Integer>> res) {
        if (root == null || root.val > target) {
            return;
        }
        // 注意：题目中问的是到叶子结点
        if (root.val == target && root.left == null && root.right == null) {
            pre.add(root.val);
            res.add(new ArrayList<>(pre));
            pre.pop();
            return;
        }
        assert root.val < target && root != null;
        pre.add(root.val);
        findPath(root.left, target - root.val, pre, res);
        findPath(root.right, target - root.val, pre, res);
        pre.pop();
    }

    public static void main(String[] args) {
        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node8 = new TreeNode(8);
        TreeNode node7 = new TreeNode(7);

        node1.left = node2;
        node1.right = node3;

        node2.left = node4;
        node2.right = node8;

        node3.left = node7;

        Solution solution = new Solution();
        ArrayList<ArrayList<Integer>> findPath = solution.FindPath(node1, 11);
        System.out.println(findPath);
    }
}